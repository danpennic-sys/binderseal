# BinderSeal fulfillment

Same pattern as QuantumGuard Operator Pack. Manual fulfillment. No secrets in git.

## SKUs

| SKU | Price | Deliver |
|-----|-------|---------|
| Operator | $99 | CLI + this repo tag + key setup note + 1-year email support |
| Command | $249 | + recursive/report guidance + HTML template + reseller note |
| Agency | $599 | + white-label report + design-partner onboarding call |

Contact: danpennic@gmail.com

## Stripe (operator action)

1. Stripe Dashboard → Payment Links → New product per SKU (or one product, three prices).
2. Collect buyer email.
3. Test with 4242… then switch to live.
4. Put live URLs in README and product page the same hour they work.
5. Do **not** put `sk_live_` or webhooks that auto-mint access until you are ready.

## After payment

1. Email the buyer:
   - Link to public source: https://github.com/danpennic-sys/binderseal
   - Tag/commit of the frozen drop (v1.0.0)
   - Short key setup: `pip install cryptography` then first run creates `~/.binderseal_key.pem`
   - Verify path: install QuantumGuard free CLI, `qg verify sealed.json`
2. For Command/Agency: attach or link the HTML report example and any private notes you keep offline.
3. Log the sale offline (date, email, SKU). Do not store card data.

## What not to do

- Do not put Stripe secrets in this repo.
- Do not claim PQC or continuous monitoring.
- Do not auto-grant GitHub access from an untested webhook.
