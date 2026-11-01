# BinderSeal production readiness (v1.0.0)

**Status: FROZEN for commercial use — 2026-11-01**

## Claims card

| Claim | Status |
|-------|--------|
| Ed25519 only | Yes |
| Offline after key setup | Yes |
| Deterministic SHA-256 of file bytes | Yes |
| CONTRACT-v1 pack shape | Yes |
| PQC / network trust / wall-clock in verifier | No — never claimed |
| Source free (MIT) | Yes |
| Commercial SKUs sold separately | Yes |

## Production checklist

- [x] Version pinned `__version__ = "1.0.0"`
- [x] Unit tests (`tests/test_binderseal.py`)
- [x] CI on push/PR (Python 3.10 + 3.12)
- [x] HTML report via `--report`
- [x] Exclude patterns for `.git`, caches, hidden files
- [x] Fulfillment runbook (`docs/FULFILLMENT.md`)
- [x] Marketing positioning (`MARKETING.md`)
- [ ] Stripe Payment Link live for Operator / Command / Agency (operator action)
- [ ] Product page live on operatorpages.com (landing update)
- [ ] Design-partner sealed packet sent

## How operators run it in the field

```bash
pip install -r requirements.txt
python3 src/binderseal.py --dir ./evidence --binder-id AUDIT-042 --recursive --report --out sealed.json
qg verify sealed.json
```

Key file defaults to `~/.binderseal_key.pem`. Protect it. Do not commit keys.

## Non-goals (v1)

- Built-in payment or license enforcement in the CLI
- Second verifier implementation
- Network calls inside the sealer
- Post-quantum signatures
