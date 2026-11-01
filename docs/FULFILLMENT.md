# BinderSeal fulfillment (v1.0.1)

Manual fulfillment. No secrets in git.

## SKUs + test checkout

| SKU | Price | Product | Price ID | Payment link (TEST) |
|-----|-------|---------|----------|---------------------|
| Operator | $99 | `prod_VYC4c7RPP8r4mY` | `price_1UX5gjAAQSB4Mr7sZ2nZsAEw` | https://buy.stripe.com/test_9B68wO3KH58Y0OY0qcew800 |
| Command | $249 | `prod_VYC4HDvVqTuSKm` | `price_1UX5gnAAQSB4Mr7sBio4d3bC` | https://buy.stripe.com/test_fZu6oGbd9bxm8hqb4Qew801 |
| Agency | $599 | `prod_VYC41CPTy60XsI` | `price_1UX5gpAAQSB4Mr7sUto3UJia` | https://buy.stripe.com/test_bJeaEWa95cBqbtCdcYew802 |

Account: `acct_1SnzzgAAQSB4Mr7s` (test mode only in this session).

Test card: `4242 4242 4242 4242`.

## Live promotion (remaining)

1. Connect/authorize the **live** Stripe account in this session (or Dashboard).
2. Recreate the same three products + prices + Payment Links in livemode.
3. Replace test URLs in README and `products/binderseal.html` the same hour.
4. Do not put `sk_live_` or webhook secrets in git.

## After payment

1. Buyer email is on the Stripe Customer / payment.
2. Point buyer at https://github.com/danpennic-sys/binderseal (tag `v1.0.1` when published).
3. `pip install cryptography` then `pip install .` or wheel from release.
4. Verify path: free QuantumGuard CLI `qg verify sealed.json`.
5. Log sale offline. Support: danpennic@gmail.com
