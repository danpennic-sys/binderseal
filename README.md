# BinderSeal

Seal a folder of evidence into one verifiable pack. Offline. Pay once.

```bash
pip install cryptography && pip install .
binderseal --dir ./docs --binder-id JOB-42 --out sealed.json
qg verify sealed.json   # PASS
```

## Buy

| | |
|--|--|
| **$99** Operator | [Checkout](https://buy.stripe.com/test_9B68wO3KH58Y0OY0qcew800) |
| **$249** Command | [Checkout](https://buy.stripe.com/test_fZu6oGbd9bxm8hqb4Qew801) |
| **$599** Agency | [Checkout](https://buy.stripe.com/test_bJeaEWa95cBqbtCdcYew802) |

Test card: `4242 4242 4242 4242`. Email after pay: danpennic@gmail.com

## Honest limits

Ed25519 only. No cloud. Same files → same seal. Source is free (MIT); packs are paid.

Details for operators: `docs/PRODUCTION.md` · Fulfillment: `docs/FULFILLMENT.md`
