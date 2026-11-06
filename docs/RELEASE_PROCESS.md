# MOONWITNESS IDE release process

## Candidate pipeline

The `.github/workflows/release-candidate.yml` workflow builds the tagged source on GitHub-hosted Linux, macOS, and Windows runners. It packages the resulting executable with the project README, Apache-2.0 license text, brand guide, and build instructions, then generates SHA-256 checksums.

The workflow accepts either a pushed `v*` tag or a manual dispatch for an existing tag. In both cases, the tag must exactly match the workspace version in `Cargo.toml` (for example, `v0.4.6`). The workflow creates or updates a **draft** GitHub release; it never publishes a release automatically. A published release is not modified by a rerun.

## What these archives are—and are not

The current candidate pipeline produces executable ZIP archives. They are not signed installers, notarized macOS application bundles, Linux distribution packages, or self-updating installations. Runtime dependencies and platform-specific installation behavior must be validated on clean target systems before distribution. The macOS runner architecture follows the current `macos-latest` runner supplied by GitHub and must be recorded with the candidate.

The pipeline does not yet provide code signing, notarization, an SBOM, dependency-vulnerability attestation, or reproducible-build provenance. Those remain release gates in [RELEASE_READINESS.md](RELEASE_READINESS.md).

## Maintainer acceptance sequence

1. Confirm the exact tag points to the reviewed `main` commit and matches `Cargo.toml`.
2. Wait for the release-candidate workflow to complete successfully on every matrix platform.
3. Download the draft archives and `SHA256SUMS`; verify checksums independently.
4. Install and launch each candidate on clean supported operating systems. Exercise workspace opening, editing, LSP, terminal, source control, debug, settings persistence, and upgrade behavior.
5. Review licensing notices, dependency inventory, security scan results, platform metadata, and known limitations.
6. Update release notes with the exact commit, tested platforms, verification scope, and unresolved issues.
7. Obtain maintainer acceptance, then publish the draft manually from GitHub Releases.

Do not publish a candidate solely because its compilation workflow passed. A successful build is not an installer test, a runtime test, or release acceptance.
