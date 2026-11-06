# MOONWITNESS IDE Release Readiness

This checklist defines the evidence required before calling a revision release-ready. It is intentionally conservative. A checked box must be supported by a result for the exact commit being released.

## 1. Repository identity and documentation

- [x] Public product name, brand artwork, default themes, and application-facing labels updated.
- [x] Upstream Lapce relationship and compatibility-retained identifiers documented.
- [x] Build instructions point to the MOONWITNESS IDE repository.
- [x] Contribution, pull request, issue-form, and security-reporting guidance added.
- [x] GitHub repository description and homepage updated to MOONWITNESS IDE.
- [x] Relevant repository topics added (`rust`, `ide`, `code-editor`, `developer-tools`, `moonwitness`).
- [x] Issues feature enabled so issue forms and the documented issue workflow are usable.
- [x] Default branch reviewed and intentionally selected (`main`).

## 2. Source and build verification

- [x] CI workflow defines formatting, spelling, Clippy, cross-platform build, and documentation-test jobs.
- [x] A dedicated Cargo `ci` profile exists for the workflow.
- [x] GitHub Actions is enabled and workflow results are visible for the current branch.
- [ ] The MOONWITNESS draft release workflow has completed a successful end-to-end tagged run and has been audited; the inherited Lapce release workflow is intentionally disabled.
- [ ] Formatting and spellcheck pass on the remote candidate revision.
- [ ] Clippy passes on all configured platforms.
- [ ] Linux, macOS, and Windows builds pass.
- [ ] Workspace documentation tests pass.
- [ ] Portable Windows build passes.
- [ ] A maintainer independently reproduces the documented local build.

## 3. Platform and packaging validation

- [ ] Install, launch, update, and uninstall tested on supported Linux distributions.
- [ ] macOS application bundle, signing/notarization requirements, launch, and update tested.
- [ ] Windows installer, signing requirements, launch, update, and uninstall tested.
- [ ] App icon, file associations, desktop integration, menus, and About dialog inspected on each platform.
- [ ] Data directories, settings migration, and existing Lapce-derived user data compatibility verified.
- [ ] Accessibility, display scaling, localization, and high-contrast behavior reviewed.

## 4. Security, licensing, and supply chain

- [ ] Dependency and license inventory reviewed, including transitive dependencies and bundled assets.
- [ ] Upstream notices and third-party license obligations verified for distributed packages.
- [ ] Secret scanning and dependency vulnerability checks completed.
- [ ] Threat model and permissions for plugins, remote development, terminals, and future AI integrations reviewed.
- [ ] Reproducible build or provenance approach documented.
- [ ] SBOM generated and archived for the release candidate.

## 5. Product acceptance

- [ ] Implemented capabilities are separated from roadmap statements in release notes.
- [ ] AI and automation remain opt-in, bounded, reviewable, and human-directed where implemented.
- [ ] No feature is described as integrated, deployed, or verified without evidence.
- [ ] Known limitations and upstream divergences documented.
- [ ] Release notes identify the exact commit, platforms, checks, and known issues.

## 6. Release authorization

- [ ] All required checks above are complete or explicitly waived with an owner and rationale.
- [ ] Release artifacts and checksums are published.
- [ ] Upgrade and rollback guidance is available.
- [ ] A maintainer has completed release acceptance.

## Release candidate workflow\n\nThe repository now includes a tagged, three-platform draft-release workflow. It packages executable ZIP archives and SHA-256 checksums, validates the tag against the Cargo workspace version, and intentionally creates only a draft release. The workflow has not yet been exercised against a release tag. Its archives are not signed installers, notarized bundles, or distribution packages. See [RELEASE_PROCESS.md](RELEASE_PROCESS.md).\n\n## Current evidence snapshot

Snapshot recorded on 2026-11-06 for repository [BRIDGE-ALLAH/MW-IDE](https://github.com/BRIDGE-ALLAH/MW-IDE), default/development branch `main`.

- The public repository name is `MW-IDE`; the product identity remains **MOONWITNESS IDE — The Engineering Observatory**.
- The primary README, About dialog project link, Cargo homepage metadata, Linux AppStream URLs, build guide, and contributor guidance point to the renamed repository.
- The dark/light application tiles, primary symbol, and default Observatory themes are present in the repository. The About dialog displays the product name and descriptor.
- The latest inspected CI run before the current changes, [42137472459](https://github.com/BRIDGE-ALLAH/MW-IDE/actions/runs/42137472459), failed at `cargo fmt --all --check` on About-menu formatting in `lapce-app/src/title.rs`. The focused formatting correction passes locally and is included in the pending push for a fresh CI run.
- Local checks on the current working tree: `cargo fmt --all --check` passed; `cargo clippy --profile ci` completed with 129 warnings; `cargo check -p lapce-app -p lapce-proxy`, `cargo build --bin lapce`, `cargo test --profile ci --doc --workspace`, and `cargo build --profile ci --frozen` passed. The doc-test run passed 1 test and ignored 1. These local results do not establish cross-platform CI success.
- Windows runtime smoke test on an NVIDIA GeForce GT 610: `cargo dev` opened a visible `MW-IDE - Lapce` window using the user-local OpenGL override. The initial missing-instance socket and stale PATH entry were logged at debug level; no app/proxy startup error was observed. This does not verify other GPUs or operating systems.
- The default branch is `main`. Issues is enabled; no open issues were listed when checked.
- Repository metadata now identifies MOONWITNESS IDE. Description is “MOONWITNESS IDE is an open-source Rust code editor evolving into an evidence-driven engineering workspace.” Homepage is the canonical repository URL; topics are `rust`, `ide`, `code-editor`, `developer-tools`, and `moonwitness`.
- No successful cross-platform CI, installer test, signing/notarization test, or release acceptance has been verified for the current working tree.
- The current local changes are being prepared for a commit and push to `main` so CI can validate that exact revision. Local build/startup observations are not cross-platform release evidence.
- MOONWITNESS XV, ARSY, LUMEN, and other ecosystem integrations remain architecture/roadmap context unless separately implemented and verified.

**Current release status: NOT RELEASE-READY — the current CI run is pending, the draft-release workflow has not yet been exercised with a version tag, and platform runtime, installer/signing, security, and maintainer acceptance evidence remain incomplete.**
