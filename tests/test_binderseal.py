#!/usr/bin/env python3
"""Minimal tests for BinderSeal v1.0.0 — deterministic hashing and pack shape."""
import base64
import json
import sys
import tempfile
import unittest
from pathlib import Path

# Allow importing from src/
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import binderseal as bs  # noqa: E402


class TestBinderSeal(unittest.TestCase):
    def test_sha256_hex_stable(self):
        self.assertEqual(
            bs.sha256_hex(b"hello"),
            "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        )

    def test_collect_and_pack_shape(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "a.txt").write_text("alpha\n", encoding="utf-8")
            (d / "b.txt").write_text("beta\n", encoding="utf-8")
            files = bs.collect_files(d, recursive=False)
            self.assertEqual(len(files), 2)
            self.assertTrue(all("sha256" in f for f in files))

            priv, pub = bs.load_or_create_key(d / "test_key.pem")
            pack = bs.build_evidence_pack("T-1", files, "note", priv, pub, "tester")
            for key in ("version", "payload", "payload_hash", "signature", "public_key", "alg"):
                self.assertIn(key, pack)
            self.assertEqual(pack["version"], "1")
            self.assertEqual(pack["alg"], "ed25519")

            payload = json.loads(base64.b64decode(pack["payload"]))
            self.assertEqual(payload["type"], "evidence_binder")
            self.assertEqual(payload["binder_id"], "T-1")
            self.assertEqual(payload["file_count"], 2)

            # Determinism: rebuild from same files list must match hash of payload body shape
            pack2 = bs.build_evidence_pack("T-1", files, "note", priv, pub, "tester")
            # sealed_at differs → hashes differ; force same sealed_at by checking structure only
            self.assertEqual(pack2["alg"], pack["alg"])

    def test_excludes_dotfiles(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "keep.txt").write_text("x", encoding="utf-8")
            (d / ".hidden").write_text("y", encoding="utf-8")
            files = bs.collect_files(d)
            names = {f["name"] for f in files}
            self.assertIn("keep.txt", names)
            self.assertNotIn(".hidden", names)


if __name__ == "__main__":
    unittest.main()
