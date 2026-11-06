# Contributing to MOONWITNESS IDE

Thank you for considering a contribution to MOONWITNESS IDE. The project is an evolving, Lapce-based engineering workspace. Contributions are welcome when they improve developer experience, reliability, clarity, accessibility, or the project's evidence-driven direction.

## Before you start

- Read the [README](README.md), [product blueprint](BLUEPRINT.md), and [brand system](BRAND.md).
- Review the repository's [issues](https://github.com/BRIDGE-ALLAH/MOONWITNESS-IDE/issues) before starting substantial work.
- Keep the distinction between inherited Lapce code, MOONWITNESS modifications, original work, and planned features clear.
- Preserve upstream license notices and attribution. Do not remove or rewrite copyright history.

## Ways to contribute

- Report reproducible bugs with platform, steps, expected behavior, and actual behavior.
- Propose improvements with a clear user problem and acceptance criteria.
- Improve documentation, accessibility, tests, and build reliability.
- Submit focused code changes with an explanation of architectural impact.
- Help validate builds and workflows on supported platforms.

## Pull request expectations

A useful pull request should:

1. Explain the problem and the intended user benefit.
2. Keep changes focused and identify affected components.
3. Describe compatibility, security, and migration risks where relevant.
4. Include tests or a concrete verification plan.
5. Update documentation when user-visible behavior changes.
6. Distinguish implemented behavior from future product direction.

Do not claim a build, test, deployment, or release is verified unless the relevant check was run against the exact revision and its result is available.

## AI-assisted contributions

AI tools may help explore, explain, or draft changes. Contributors remain responsible for reviewing generated code, checking licenses, protecting secrets, validating behavior, and explaining the final changes. Generated text or code is not authoritative merely because an AI system produced it.

## Development and validation

Follow the existing build instructions in [docs/building-from-source.md](docs/building-from-source.md). Run the checks relevant to the files you changed and report any checks you could not run. Keep changes compatible with the current Rust workspace unless a separately reviewed migration is intended.

## Upstream relationship

MOONWITNESS IDE is based on [Lapce](https://github.com/lapce/lapce). Preserve upstream attribution and comply with the repository's Apache-2.0 license and all applicable third-party licenses. Internal crate, binary, and directory names may remain Lapce-derived for compatibility; do not rename them casually.

## Questions and discussion

For questions, feature proposals, or bug reports, use the repository's Issues tab once the maintainer enables Issues. Until then, use a focused pull request for proposed documentation changes or contact the maintainer through the GitHub profile linked from this repository. Please do not assume upstream Lapce community channels are MOONWITNESS IDE support channels.

---

**Observe clearly. Trace honestly. Build deliberately. Verify openly. Preserve knowledge.**
