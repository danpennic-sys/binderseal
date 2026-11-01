# BinderSeal production readiness (v1.0.1)

**Status: PRODUCTION ACCEPTANCE candidate — 2026-11-01**

## Claims card (corrected)

| Claim | Status |
|-------|--------|
| Ed25519 only | Yes |
| Offline after key setup | Yes |
| Fail-closed without cryptography | Yes (v1.0.1) |
| Content-addressed determinism (paths + size + file SHA-256) | Yes (v1.0.1) |
| sealed_at outside signed payload | Yes (v1.0.1) |
| HTML report escaped | Yes (v1.0.1) |
| Installable console script | Yes (v1.0.1) |
| CONTRACT-v1 pack shape | Yes |
| PQC / network trust | No — never claimed |
| Source free (MIT) | Yes |

## Determinism (precise)

Same binder_id, notes, operator, and set of files (relative_path, size_bytes, sha256 of file bytes) → **identical** `payload`, `payload_hash`, and `signature`.

`sealed_at` is an **advisory outer field** on the pack JSON for humans/logs. It is **not** part of the signed payload.

File mtimes are **not** included in the manifest (v1.0.1).

## Crypto policy

Missing `cryptography` → process exits with error. No zero-byte keys or signatures.

## Checklist

- [x] Fail-closed crypto
- [x] Content-addressed deterministic payload
- [x] HTML escape
- [x] Package layout + console entry point
- [x] CI: unit tests + wheel install + CLI smoke
- [ ] CI green recorded on main (after push)
- [ ] Formal git tag `v1.0.1`
- [ ] QuantumGuard interop verified on a real sealed pack
- [ ] Stripe Payment Links live (Operator / Command / Agency)

## Field command

```bash
pip install cryptography
pip install .   # or: pip install dist/binderseal-1.0.1-*.whl
binderseal --dir ./evidence --binder-id AUDIT-042 --recursive --report --out sealed.json
qg verify sealed.json
```
