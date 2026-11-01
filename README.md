# BinderSeal

**v1.0.0 — production.** Local-first evidence binder sealer for field operators, auditors, and compliance teams.

Offline. Deterministic. Pay once. Compatible with QuantumGuard CONTRACT-v1 and the Operator Pages suite.

## Why BinderSeal?

Auditors, GRC teams, and field operators need tamper-evident packages of evidence: reports, checklists, logs, CSVs, photos, contracts, and close-out documents. Folder dumps are easy to dispute.

BinderSeal walks a directory, computes deterministic SHA-256 hashes for every file, builds a sorted manifest, and seals the binder into a client-verifiable QuantumGuard evidence pack.

- No SaaS. No subscription. Runs offline after key setup.
- Clients and auditors verify with free `qg verify` → PASS / FAIL / INDETERMINATE.
- Source files stay local; only hashes + metadata enter the sealed pack.

## Quick start

```bash
pip install -r requirements.txt
python3 src/binderseal.py --demo
python3 src/binderseal.py --dir ./audit-packet --binder-id AUDIT-2026-042 --recursive --report --out sealed_binder.json
qg verify sealed_binder.json
```

## Commercial SKUs

| SKU | Price | Includes |
|-----|-------|----------|
| Operator | $99 | CLI + key setup + 1-year email support |
| Command | $249 | + recursive/report + reseller rights |
| Agency | $599 | + white-label + design partner onboarding |

Purchase / access: **danpennic@gmail.com**

Source remains free under MIT. See `docs/FULFILLMENT.md` and `docs/PRODUCTION.md`.

## Claims (frozen)

- Ed25519 only. No post-quantum claims.
- Offline after key setup. No network inside the sealer.
- Deterministic hashing of file bytes. CONTRACT-v1 pack shape.

## License

MIT — see `LICENSE-MIT`.
