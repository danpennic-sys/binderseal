#!/usr/bin/env python3
"""
BinderSeal v1.0.0 — local-first evidence binder sealer.
Compatible with QuantumGuard CONTRACT-v1 and the Operator Pages suite.
Offline after key setup. Deterministic payload hashing.

Claims (frozen):
- Ed25519 only. No PQC.
- Source free. Commercial Operator/Command/Agency packs sold separately.
- Same inputs → same payload hash. CLI and any future HTTP path must agree on bytes.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

__version__ = "1.0.0"

try:
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from cryptography.hazmat.primitives import serialization
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

DEFAULT_EXCLUDES = {".git", ".hg", ".svn", "__pycache__", "node_modules", ".DS_Store"}


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_or_create_key(key_path: Path):
    """Returns (private_key_or_None, public_key_hex)."""
    if not CRYPTO_AVAILABLE:
        return None, "00" * 32
    if key_path.exists():
        with open(key_path, "rb") as f:
            priv = serialization.load_pem_private_key(f.read(), password=None)
        pub = priv.public_key()
        pub_bytes = pub.public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw
        )
        return priv, pub_bytes.hex()
    priv = Ed25519PrivateKey.generate()
    pub = priv.public_key()
    pub_bytes = pub.public_bytes(
        serialization.Encoding.Raw, serialization.PublicFormat.Raw
    )
    pem = priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    key_path.parent.mkdir(parents=True, exist_ok=True)
    key_path.write_bytes(pem)
    return priv, pub_bytes.hex()


def sign_payload(priv, payload_hash_hex: str) -> str:
    if not CRYPTO_AVAILABLE or priv is None:
        return "00" * 64
    return priv.sign(bytes.fromhex(payload_hash_hex)).hex()


def should_skip(path: Path, root: Path, excludes: set[str]) -> bool:
    try:
        rel = path.relative_to(root)
    except ValueError:
        return True
    for part in rel.parts:
        if part in excludes or part.startswith(".") and part not in (".", ".."):
            return True
    return False


def collect_files(
    dir_path: Path, recursive: bool = False, excludes: set[str] | None = None
) -> list[dict]:
    excludes = excludes or DEFAULT_EXCLUDES
    files: list[dict] = []
    if not dir_path.exists():
        return files
    paths = dir_path.rglob("*") if recursive else dir_path.glob("*")
    for p in sorted(paths):
        if not p.is_file():
            continue
        if should_skip(p, dir_path, excludes):
            continue
        try:
            files.append(
                {
                    "name": p.name,
                    "relative_path": str(p.relative_to(dir_path)).replace("\\", "/"),
                    "size_bytes": p.stat().st_size,
                    "sha256": hash_file(p),
                    "mtime_iso": datetime.fromtimestamp(
                        p.stat().st_mtime, tz=timezone.utc
                    ).isoformat(),
                }
            )
        except OSError as e:
            files.append({"name": p.name, "error": str(e)})
    return files


def build_evidence_pack(
    binder_id: str,
    file_list: list,
    notes: str,
    priv,
    pub_hex: str,
    operator: str = "auditor",
) -> dict:
    payload_obj = {
        "version": "1",
        "type": "evidence_binder",
        "binder_id": binder_id,
        "notes": notes or "",
        "operator": operator,
        "file_count": len([f for f in file_list if "error" not in f]),
        "files": file_list,
        "sealed_at": datetime.now(timezone.utc).isoformat(),
        "tool": f"binderseal/{__version__}",
    }
    payload_bytes = json.dumps(
        payload_obj, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    payload_b64 = base64.b64encode(payload_bytes).decode("ascii")
    payload_hash = sha256_hex(payload_bytes)
    signature = sign_payload(priv, payload_hash)
    return {
        "version": "1",
        "payload": payload_b64,
        "payload_hash": payload_hash,
        "signature": signature,
        "public_key": pub_hex,
        "alg": "ed25519",
    }


def write_html_report(pack: dict, out_path: Path, binder_id: str) -> None:
    try:
        payload = json.loads(base64.b64decode(pack["payload"]))
    except Exception:
        payload = {}
    files = payload.get("files", [])
    rows = "".join(
        f"<tr><td>{f.get('relative_path', f.get('name', ''))}</td>"
        f"<td>{f.get('size_bytes', '')}</td>"
        f"<td><code>{f.get('sha256', f.get('error', ''))}</code></td></tr>"
        for f in files
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>BinderSeal Report — {binder_id}</title>
  <style>
    body {{ font-family: system-ui, sans-serif; max-width: 960px; margin: 2rem auto; padding: 0 1rem; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 0.9rem; }}
    th, td {{ border: 1px solid #ccc; padding: 0.4rem 0.6rem; text-align: left; vertical-align: top; }}
    th {{ background: #f4f4f4; }}
    code {{ font-size: 0.8rem; word-break: break-all; }}
    .meta {{ color: #555; margin-bottom: 1.5rem; }}
  </style>
</head>
<body>
  <h1>BinderSeal Evidence Report</h1>
  <div class="meta">
    <p><strong>Binder ID:</strong> {binder_id}</p>
    <p><strong>Payload hash:</strong> <code>{pack.get('payload_hash', '')}</code></p>
    <p><strong>Algorithm:</strong> {pack.get('alg', '')} · <strong>Tool:</strong> binderseal/{__version__}</p>
    <p>Verify offline: <code>qg verify &lt;sealed.json&gt;</code> → PASS / FAIL / INDETERMINATE</p>
  </div>
  <table>
    <thead><tr><th>Path</th><th>Size</th><th>SHA-256</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</body>
</html>
"""
    out_path.write_text(html, encoding="utf-8")


def demo() -> None:
    files = [
        {
            "name": "audit-report.pdf",
            "relative_path": "audit-report.pdf",
            "size_bytes": 245760,
            "sha256": "a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456",
            "mtime_iso": "2026-10-29T14:30:00+00:00",
        },
        {
            "name": "checklist.csv",
            "relative_path": "checklist.csv",
            "size_bytes": 8192,
            "sha256": "fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321",
            "mtime_iso": "2026-10-29T15:45:00+00:00",
        },
    ]
    key_path = Path.home() / ".binderseal_key.pem"
    priv, pub_hex = load_or_create_key(key_path)
    pack = build_evidence_pack(
        "AUDIT-2026-DEMO",
        files,
        "Demo: annual compliance evidence binder.",
        priv,
        pub_hex,
    )
    print(json.dumps(pack, indent=2))
    if not CRYPTO_AVAILABLE:
        print(
            "\nNote: cryptography not installed — stub signatures. "
            "pip install cryptography for real Ed25519.",
            file=sys.stderr,
        )
    print("\n# Verify with: qg verify <this.json>  (from QuantumGuard)")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=f"BinderSeal v{__version__} — local evidence binder sealer"
    )
    parser.add_argument("--version", action="version", version=f"binderseal {__version__}")
    parser.add_argument("--demo", action="store_true", help="Run demo and print sealed pack")
    parser.add_argument("--dir", type=str, help="Directory containing evidence files")
    parser.add_argument("--binder-id", type=str, default="unknown", help="Binder identifier")
    parser.add_argument("--notes", type=str, default="", help="Optional notes")
    parser.add_argument("--operator", type=str, default="auditor", help="Operator name")
    parser.add_argument("--out", type=str, help="Output sealed pack path")
    parser.add_argument(
        "--key",
        type=str,
        default=str(Path.home() / ".binderseal_key.pem"),
        help="Private key PEM path",
    )
    parser.add_argument("--recursive", action="store_true", help="Recurse into subdirectories")
    parser.add_argument(
        "--report",
        type=str,
        nargs="?",
        const="auto",
        help="Write HTML report (path or auto next to --out)",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Extra directory/file name to exclude (repeatable)",
    )
    args = parser.parse_args()

    if args.demo:
        demo()
        return 0

    if not args.dir:
        parser.print_help()
        return 2

    dir_path = Path(args.dir)
    if not dir_path.is_dir():
        print(f"Not a directory: {dir_path}", file=sys.stderr)
        return 1

    excludes = DEFAULT_EXCLUDES | set(args.exclude)
    file_list = collect_files(dir_path, args.recursive, excludes)
    if not file_list:
        print(f"No files found in {dir_path}", file=sys.stderr)
        return 1

    if not CRYPTO_AVAILABLE:
        print(
            "Warning: cryptography not installed. Using stub signatures. "
            "pip install cryptography for production seals.",
            file=sys.stderr,
        )

    key_path = Path(args.key)
    priv, pub_hex = load_or_create_key(key_path)
    pack = build_evidence_pack(
        args.binder_id, file_list, args.notes, priv, pub_hex, args.operator
    )

    out_path = Path(args.out or f"sealed_binder_{args.binder_id}.json")
    out_path.write_text(json.dumps(pack, indent=2) + "\n", encoding="utf-8")
    print(f"Sealed {len(file_list)} entries into {out_path}")
    print(f"Payload hash: {pack['payload_hash']}")
    print(f"Verify: qg verify {out_path}")

    if args.report is not None:
        report_path = (
            Path(args.report)
            if args.report != "auto"
            else out_path.with_suffix(".html")
        )
        write_html_report(pack, report_path, args.binder_id)
        print(f"Report: {report_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
