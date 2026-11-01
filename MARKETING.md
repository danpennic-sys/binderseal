# BinderSeal Marketing

## Positioning

**Evidence Binder that actually seals.**

Stop shipping folder dumps that auditors cannot trust. BinderSeal turns any directory of reports, checklists, logs, and documents into a single QuantumGuard CONTRACT-v1 pack. Same content → same signed payload hash. Offline. Pay once.

Fits Operator Pages: we don't promise anything we prove it.

## Checkout (test mode)

| SKU | Price | Link |
|-----|-------|------|
| Operator | $99 | https://buy.stripe.com/test_9B68wO3KH58Y0OY0qcew800 |
| Command | $249 | https://buy.stripe.com/test_fZu6oGbd9bxm8hqb4Qew801 |
| Agency | $599 | https://buy.stripe.com/test_bJeaEWa95cBqbtCdcYew802 |

Test card: `4242 4242 4242 4242`. Promote to live when livemode account is authorized.

## Target buyers

- Field operators closing jobs (pair with CloseSeal / LifecycleSeal)
- Internal auditors and GRC teams building evidence packets
- ICS/OT integrators who need least-privilege evidence of access
- Design partners who already buy Operator Pack

## Claims (honest)

- Ed25519 only (v1). No PQC.
- Fail-closed without cryptography.
- Content-addressed determinism; `sealed_at` not signed.
- PASS / FAIL / INDETERMINATE only via QuantumGuard verifier.
- Source free; commercial packs sold separately.

## Remaining GTM

1. Tag `v1.0.1` + GitHub Release (`docs/RELEASE.md`)
2. Live Stripe links
3. One design-partner packet: real sealed binder + `qg verify` demo
4. Announce with frozen claims only

Proof sells. Marketing lags product.
