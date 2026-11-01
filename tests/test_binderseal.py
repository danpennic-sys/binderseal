#!/usr/bin/env python3
"""Tests for BinderSeal v1.0.1 — fail-closed crypto, content-addressed determinism."""
import base64
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import binderseal as bs  # noqa: E402


class TestBinderSeal(unittest.TestCase):
    def test_version(self):
        self.assertEqual(bs.__version__, "1.0.1")

    def test_sha256_hex_stable(self):
        self.assertEqual(
            bs.sha256_hex(b"hello"),
            "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        )

    def test_content_addressed_determinism(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "a.txt").write_text("alpha\n", encoding="utf-8")
            (d / "b.txt").write_text("beta\n", encoding="utf-8")
            files = bs.collect_files(d, recursive=False)
            self.assertEqual(len(files), 2)
            self.assertTrue(all("sha256" in f for f in files))
            self.assertTrue(all("mtime_iso" not in f for f in files))

            priv, pub = bs.load_or_create_key(d / "test_key.pem")
            pack1 = bs.build_evidence_pack("T-1", files, "note", priv, pub, "tester")
            pack2 = bs.build_evidence_pack("T-1", files, "note", priv, pub, "tester")

            self.assertEqual(pack1["payload_hash"], pack2["payload_hash"])
            self.assertEqual(pack1["signature"], pack2["signature"])
            self.assertEqual(pack1["payload"], pack2["payload"])
            # sealed_at is advisory outer field and may differ
            self.assertIn("sealed_at", pack1)

            payload = json.loads(base64.b64decode(pack1["payload"]))
            self.assertNotIn("sealed_at", payload)
            self.assertEqual(payload["type"], "evidence_binder")
            self.assertEqual(payload["binder_id"], "T-1")
            self.assertEqual(payload["file_count"], 2)

    def test_excludes_dotfiles(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "keep.txt").write_text("x", encoding="utf-8")
            (d / ".hidden").write_text("y", encoding="utf-8")
            files = bs.collect_files(d)
            names = {f["name"] for f in files}
            self.assertIn("keep.txt", names)
            self.assertNotIn(".hidden", names)

    def test_html_escape(self):
        from binderseal.core import write_html_report

        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            (d / "a.txt").write_text("x", encoding="utf-8")
            files = bs.collect_files(d)
            # Inject XSS-like binder id via path name is hard; use binder_id
            priv, pub = bs.load_or_create_key(d / "k.pem")
            pack = bs.build_evidence_pack(
                '<script>alert(1)</script>', files, "", priv, pub
            )
            report = d / "r.html"
            write_html_report(pack, report, '<script>alert(1)</script>')
            text = report.read_text(encoding="utf-8")
            self.assertNotIn("<script>alert(1)</script>", text)
            self.assertIn("&lt;script&gt;", text)


if __name__ == "__main__":
    unittest.main()
