# BinderSeal production readiness (v1.0.1)

**Status: PRODUCTION ACCEPTANCE (test commerce) — 2026-11-01**

Live Stripe commerce remains one operator step (promote test products to livemode). Software, CI, interop, and test checkout are complete.

## Claims card

| Claim | Status |
|-------|--------|
| Ed25519 only | Yes |
| Offline after key setup | Yes |
| Fail-closed without cryptography | Yes |
| Content-addressed determinism (paths + size + file SHA-256) | Yes |
| sealed_at outside signed payload | Yes |
| HTML report escaped | Yes |
| Installable console script | Yes |
| CONTRACT-v1 pack shape | Yes |
| QuantumGuard `qg verify` interop | Yes (PASS) |
| CI green on main | Yes |
| Stripe Payment Links (test) | Yes |
| Stripe Payment Links (live) | Outstanding |
| Formal git tag `v1.0.1` | Operator: run commands in `docs/RELEASE.md` |
| PQC / network trust | No — never claimed |
| Source free (MIT) | Yes |

## Determinism (precise)

Same binder_id, notes, operator, and set of files (relative_path, size_bytes, sha256 of file bytes) → **identical** `payload`, `payload_hash`, and `signature`.

`sealed_at` is an **advisory outer field** on the pack JSON. It is **not** part of the signed payload. File mtimes are not in the manifest.

## Crypto policy

Missing `cryptography` → process exits with error. No zero-byte keys or signatures.

## Checklist

- [x] Fail-closed crypto
- [x] Content-addressed deterministic payload
- [x] HTML escape
- [x] Package layout + console entry point
- [x] CI: unit tests + wheel install + CLI smoke
- [x] CI green on main (runs 1–5 success, e.g. https://github.com/danpennic-sys/binderseal/actions/runs/41348913546)
- [x] QuantumGuard interop verified (`qg verify` → PASS)
- [x] Stripe test Payment Links (Operator / Command / Agency)
- [ ] Formal git tag `v1.0.1` (see `docs/RELEASE.md`)
- [ ] Stripe **live** Payment Links (recreate or promote in livemode account)

## Field command

```bash
pip install cryptography
pip install .
binderseal --dir ./evidence --binder-id AUDIT-042 --recursive --report --out sealed.json
qg verify sealed.json
```
