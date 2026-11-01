# BinderSeal

**Local-first evidence binder sealer for field operators, auditors, and compliance teams.**

Offline. Deterministic. Pay once. Compatible with QuantumGuard CONTRACT-v1 and the Operator Pages suite.

## Why BinderSeal?

Auditors, GRC teams, and field operators need tamper-evident packages of evidence: reports, checklists, logs, CSVs, photos, contracts, and close-out documents. Folder dumps are easy to dispute ("that file was added later", "the hash doesn't match").

BinderSeal walks a directory, computes deterministic SHA-256 hashes for every file, builds a sorted manifest with relative paths, sizes, and timestamps, and seals the entire binder into a client-verifiable QuantumGuard evidence pack.

- No SaaS. No subscription. Runs completely offline after key setup.
- Clients, auditors, or regulators verify the pack with the free QuantumGuard verifier (`qg verify`).
- Source files stay local; only the cryptographic hashes + manifest go into the sealed pack.
- Pairs with MediaSeal, FieldSeal, JobSeal, CloseSeal, and LifecycleSeal for full job or audit context.

## Quick Start

```bash
# Optional but recommended for real Ed25519 signatures
pip install cryptography

python3 src/binderseal.py --demo
python3 src/binderseal.py --dir ./audit-packet --binder-id AUDIT-2026-042 --out sealed_binder.json
```

Verify the output with the QuantumGuard CLI (from the quantumguard repo):

```bash
qg verify sealed_binder.json
```

Expected verdict: PASS (when using real cryptography).

## What you can sell

| SKU       | Price | Includes                                      |
|-----------|-------|-----------------------------------------------|
| Operator  | $99   | CLI + key setup guide + 1-year email support |
| Command   | $249  | + recursive mode + HTML report + reseller rights for client packs |
| Agency    | $599  | + white-label HTML + design partner onboarding |

Purchase / access: danpennic@gmail.com

Source remains free under Apache-2.0 OR MIT. Commercial Operator Pack sold separately.

## Stack Fit

- Python CLI (same family as MediaSeal, VeriQuote, FieldSeal, JobSeal, CloseSeal, LifecycleSeal)
- Emits QuantumGuard CONTRACT-v1 bundles (Ed25519, deterministic hashing)
- Local key storage (PEM)
- Pure standard library + optional cryptography — no heavy deps

## License

Apache-2.0 OR MIT
