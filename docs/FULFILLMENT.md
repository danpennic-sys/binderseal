# BinderSeal fulfillment (v1.0.1)

Manual fulfillment. No secrets in git.

## SKUs

| SKU | Price | Deliver |
|-----|-------|---------|
| Operator | $99 | CLI (tagged release) + key setup + 1-year email support |
| Command | $249 | + recursive/report guidance + reseller note |
| Agency | $599 | + white-label report + design-partner onboarding |

Contact: danpennic@gmail.com

## Stripe (operator action — still outstanding)

1. Stripe Dashboard → Payment Links for $99 / $249 / $599.
2. Collect buyer email.
3. Test then live. Put live URLs in README and product page the same hour.
4. Do not put `sk_live_` in git.

## After payment

1. Point buyer at https://github.com/danpennic-sys/binderseal tag `v1.0.1`
2. `pip install cryptography` then `pip install .` or wheel from release
3. Verify path: free QuantumGuard CLI `qg verify sealed.json`
4. Log sale offline.
