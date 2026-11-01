# BinderSeal

**v1.0.1** — production acceptance build. Local-first evidence binder sealer.

Offline. Content-addressed deterministic seals. Fail-closed crypto. Pay once.
Compatible with QuantumGuard CONTRACT-v1.

## Quick start

```bash
pip install cryptography
pip install .
binderseal --demo
binderseal --dir ./audit-packet --binder-id AUDIT-2026-042 --recursive --report --out sealed_binder.json
qg verify sealed_binder.json
```

Or without install:

```bash
pip install -r requirements.txt
python -m binderseal --dir ./audit-packet --binder-id AUDIT-042 --out sealed.json
```

## Claims (v1.0.1)

- **Ed25519 only.** No PQC.
- **Fail-closed:** without `cryptography`, the tool exits; it does not emit stub signatures.
- **Determinism:** same paths + sizes + file SHA-256 → same signed `payload_hash`. `sealed_at` is advisory and outside the signed body.
- Source free (MIT). Commercial SKUs sold separately.

## Commercial SKUs

| SKU | Price | Includes |
|-----|-------|----------|
| Operator | $99 | CLI + key setup + 1-year email support |
| Command | $249 | + recursive/report + reseller rights |
| Agency | $599 | + white-label + design partner onboarding |

Purchase: **danpennic@gmail.com** (Stripe links to be added when live)

See `docs/PRODUCTION.md` and `docs/FULFILLMENT.md`.

## License

MIT — `LICENSE-MIT`.
