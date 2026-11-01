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

## Buy (Stripe)

| SKU | Price | Checkout |
|-----|-------|----------|
| Operator | $99 | [Pay $99](https://buy.stripe.com/test_9B68wO3KH58Y0OY0qcew800) |
| Command | $249 | [Pay $249](https://buy.stripe.com/test_fZu6oGbd9bxm8hqb4Qew801) |
| Agency | $599 | [Pay $599](https://buy.stripe.com/test_bJeaEWa95cBqbtCdcYew802) |

**These links are currently TEST mode** (`buy.stripe.com/test_…`). Use card `4242 4242 4242 4242` to exercise checkout. Live links require promoting the same products on the live Stripe account, then swapping these URLs.

Fulfillment remains manual after payment (see `docs/FULFILLMENT.md`). Support: danpennic@gmail.com

## License

MIT — `LICENSE-MIT`.
