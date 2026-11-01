# BinderSeal release procedure

MCP cannot create git tags or GitHub Releases from this session. Run locally (or in GitHub UI) after main is green.

## Tag v1.0.1

```bash
git clone https://github.com/danpennic-sys/binderseal.git
cd binderseal
git checkout main
git pull
git tag -a v1.0.1 -m "BinderSeal v1.0.1 production acceptance

- Fail-closed Ed25519 (no stub signatures)
- Content-addressed deterministic payload
- HTML-escaped reports
- Installable package + CI wheel smoke
- QuantumGuard CONTRACT-v1 interop PASS
- Stripe test Payment Links wired"
git push origin v1.0.1
```

## GitHub Release

1. https://github.com/danpennic-sys/binderseal/releases/new?tag=v1.0.1
2. Title: `v1.0.1`
3. Paste the notes from `CHANGELOG.md`
4. Publish

## After tag

Point paid customers at the tag. Optional: attach a built wheel from CI artifacts if you export one.
