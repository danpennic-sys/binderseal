# Changelog

## [1.0.1] — 2026-11-01

Production acceptance (no feature expansion).

### Fixed
- **Fail-closed crypto:** refuse to seal without `cryptography`; no zero-byte keys/signatures
- **Determinism:** signed payload is content-addressed only (paths, sizes, file SHA-256); `sealed_at` is outer/advisory; mtimes removed from manifest
- **HTML injection:** report fields escaped via `html.escape`
- **Packaging:** proper `src/binderseal` package + console script; legacy single-file shim removed

### Verified
- Unit tests (5) pass
- CI on main: success (Python 3.10 + 3.12, wheel install, CLI smoke)
- `qg verify` on sealed packs → PASS

### Commerce
- Stripe **test** Payment Links for Operator ($99), Command ($249), Agency ($599)
- Live links require livemode account promotion (see `docs/FULFILLMENT.md`)

## [1.0.0] — 2026-11-01

Initial production-shaped CLI, tests, CI, docs, and landing product page.
