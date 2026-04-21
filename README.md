# Axiom Labs — `.github`

Meta-repo for the [Axiom Labs](https://github.com/axiom-labs-os) organization.
Hosts the org profile, community health files, reusable CI/CD workflows,
and the brand system.

## Layout

```
.
├── .github/workflows/        Reusable GitHub Actions workflows (workflow_call).
│   ├── python-ci.yml           Lint + matrix test + coverage + pre-commit.
│   ├── python-release.yml      Build + Sigstore-sign + Trusted-Publish + smoke.
│   ├── python-docs.yml         MkDocs Material build + Pages deploy.
│   └── security-scan.yml       grype + REUSE + gitleaks.
├── brand/                    Logo, palette, typography, templates.
│   ├── logo/                   SVG masters + PNG exports + favicon bundle.
│   ├── palette.md              Color tokens with contrast-ratio reference.
│   ├── typography.md           Space Grotesk + system-stack body + scale.
│   ├── usage.md                Clear space, minimums, mark-vs-wordmark rules.
│   └── templates/
│       ├── axiom-labs.mplstyle         matplotlib style for paper figures.
│       └── axiom-labs-preamble.tex     LaTeX preamble for paper submissions.
├── profile/README.md         Org landing page, rendered at github.com/axiom-labs-os.
├── CODE_OF_CONDUCT.md        Contributor Covenant v2.1.
├── SECURITY.md               Vulnerability disclosure policy.
└── README.md                 This file.
```

## Using the reusable workflows

Each workflow is a `workflow_call` target. Consumer repos add a short caller
stub. Example — `.github/workflows/ci.yml` in a product repo:

```yaml
name: CI
on:
  push: { branches: [main] }
  pull_request: { branches: [main] }
jobs:
  ci:
    uses: axiom-labs-os/.github/.github/workflows/python-ci.yml@v1
    with:
      package-name: dendra
      python-versions: '["3.10","3.11","3.12","3.13"]'
      extras: 'dev,train,viz'
      provenance-forbidden-patterns: 'utexas|UT Austin|bbooth@'
```

Pin to a tag (`@v1`) in production; pin to a SHA for highest supply-chain
assurance.

## Regenerating brand PNGs

The PNG exports in `brand/logo/` are generated from SVG masters. To rebuild:

```bash
cd brand/logo
python _export.py
```

Requires `cairosvg`.

## License

Code: Apache-2.0. Brand and documentation: CC-BY-4.0 (unless a specific
file states otherwise in its SPDX header).

Copyright © 2026 B-Tree Ventures, LLC. DBA Axiom Labs.
