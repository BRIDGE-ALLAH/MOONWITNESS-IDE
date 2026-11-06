# MOONWITNESS IDE Release Readiness

This checklist defines the evidence required before calling a revision release-ready. It is intentionally conservative. A checked box must be supported by a result for the exact commit being released.

## 1. Repository identity and documentation

- [x] Public product name, brand artwork, default themes, and application-facing labels updated.
- [x] Upstream Lapce relationship and compatibility-retained identifiers documented.
- [x] Build instructions point to the MOONWITNESS IDE repository.
- [x] Contribution, pull request, issue-form, and security-reporting guidance added.
- [ ] GitHub repository description and homepage updated to MOONWITNESS IDE.
- [ ] Relevant repository topics added.
- [ ] Issues feature enabled so issue forms and the documented issue workflow are usable.
- [ ] Default branch reviewed and intentionally selected.

## 2. Source and build verification

- [x] CI workflow defines formatting, spelling, Clippy, cross-platform build, and documentation-test jobs.
- [x] A dedicated Cargo `ci` profile exists for the workflow.
- [x] GitHub Actions is enabled and a workflow run is visible for the current candidate commit (queued; completion not yet verified).
- [ ] A MOONWITNESS-specific release workflow has been rebuilt and audited; the inherited Lapce release workflow is intentionally disabled.
- [ ] Formatting and spellcheck pass.
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

## Current evidence snapshot

Snapshot recorded on 2026-11-06 for repository [BRIDGE-ALLAH/MW-IDE](https://github.com/BRIDGE-ALLAH/MW-IDE), development branch `main`.

- The public repository name is `MW-IDE`; the product identity remains **MOONWITNESS IDE — The Engineering Observatory**.
- The primary README, About dialog project link, Cargo homepage metadata, Linux AppStream URLs, build guide, and contributor guidance point to the renamed repository.
- The dark/light application tiles, primary symbol, and default Observatory themes are present in the repository. The About dialog displays the product name and descriptor.
- CI run [#11](https://github.com/BRIDGE-ALLAH/MW-IDE/actions/runs/42136934858) is attached to current `main` head `0779219bfe00eaa092eb65a37dba71b302fb72c2`. At the latest inspection it was **queued**, with formatting/spellchecking and Linux, Windows, and macOS Clippy jobs waiting. No passing result is claimed.
- GitHub still designates `master` as the default branch. `main` remains the requested development branch.
- Repository description is still the inherited generic text (“Lightning-fast and Powerful Code Editor written in Rust”); homepage and topics have not been verified as updated, and Issues remains disabled. The connected GitHub operations available here expose repository reads and source commits, but no repository-settings write action. The maintainer must update Description, Homepage, Topics, Issues, and the default branch in GitHub Settings.
- No successful cross-platform build, installer test, signing/notarization test, or release acceptance has been verified in this session.
- MOONWITNESS XV, ARSY, LUMEN, and other ecosystem integrations remain architecture/roadmap context unless separately implemented and verified.

**Current release status: NOT RELEASE-READY — CI and platform packaging/acceptance evidence remain incomplete, and repository settings are outstanding.**
