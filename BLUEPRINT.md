# MOONWITNESS IDE — Product & Engineering Blueprint

**Document type:** Product vision, brand system, and implementation blueprint  
**Product:** MOONWITNESS IDE  
**Positioning:** The Engineering Observatory  
**Status:** Strategic blueprint; roadmap items are proposals until implemented and verified  
**Ecosystem:** MOONWITNESS XV

---

## 1. Executive definition

MOONWITNESS IDE is an evidence-driven engineering workspace. It begins with a native code editor and evolves toward a development environment that helps people understand repositories, make deliberate changes, verify outcomes, and preserve project knowledge.

It is not positioned as an autonomous software engineer or merely another editor with an AI chat panel. Its differentiator is the combination of a productive code-editing environment, repository and architecture understanding, evidence-linked engineering workflows, durable project knowledge, bounded AI assistance, and explicit human control.

**Core promise:** Help developers understand the system, trace the evidence, and build with intention.

This blueprint defines product intent. It does not certify that roadmap capabilities are implemented.

## 2. Brand platform

### 2.1 Name
**MOONWITNESS IDE**

Use the full name on first reference. Use **MOONWITNESS** only when context is unambiguous. Keep spelling consistent across documentation, UI, website, releases, and package metadata as the rebrand progresses.

### 2.2 Primary descriptor
**The Engineering Observatory**

The observatory metaphor expresses careful observation, clear instruments, traceable findings, and a long view of system health. It should guide product language and visual design—not become an excuse for vague or mystical claims.

### 2.3 Tagline
**Understand the system. Trace the evidence. Build with intention.**

Supporting brand line:

**The Moon Watches. The Record Remembers. The Evidence Remains Inspectable.**

Use the primary tagline in developer-facing product communication because it states the practical value directly. Use the supporting line to connect the IDE to the wider MOONWITNESS XV philosophy.

### 2.4 Brand promise
MOONWITNESS IDE makes complex software work more understandable and accountable without taking authority away from developers.

### 2.5 Brand character
- **Observant:** inspect before acting.
- **Precise:** distinguish facts, hypotheses, and unknowns.
- **Calm:** reduce cognitive noise rather than add spectacle.
- **Trustworthy:** show evidence and limitations.
- **Capable:** support serious engineering workflows.
- **Human-directed:** keep people in control of consequential actions.

### 2.6 Voice and vocabulary

Prefer clear, concrete engineering language.

| Prefer | Avoid |
|---|---|
| evidence, source, trace, verify | magic, omniscient, guaranteed |
| proposal, review, accept | AI decided, AI approved |
| planned, experimental, available | shipped without release evidence |
| repository map, dependency, interface | total understanding |
| human approval, bounded action | fully autonomous unless demonstrably true |

Brand copy must never imply that AI can know the entire repository, guarantee correctness, or replace engineering review.

## 3. Product thesis

Software projects accumulate complexity faster than individual developers can hold in working memory. The cost is not only writing code: it is reconstructing context, discovering hidden dependencies, understanding old decisions, validating changes, and transferring knowledge.

MOONWITNESS IDE addresses this by treating **understanding and verification as first-class engineering activities**, alongside editing and execution.

The product should answer five recurring questions:
1. What is in this workspace?
2. How do its important parts relate?
3. What evidence supports this explanation or proposed change?
4. What changed, and how was it verified?
5. What knowledge should the next contributor be able to recover?

## 4. Target users and jobs to be done

### Primary: software developers
Need a fast, dependable editor and a clearer understanding of unfamiliar or growing codebases.

### Secondary: technical leads and architects
Need to inspect boundaries, dependencies, decisions, risks, and the impact of proposed changes.

### Secondary: maintainers of long-lived projects
Need project context and decisions to remain recoverable across contributors and time.

### Secondary: AI-assisted developers
Need contextual help that is inspectable, permission-aware, and subject to human review.

The product should not initially optimize for every persona. Core editor stability and developer trust come first.

## 5. Product pillars

### Pillar A — Workspace
A responsive native editing environment for navigation, editing, terminal use, language tooling, and extensibility.

**Success criteria:** startup and interaction performance, reliable editing, platform stability, and compatibility with the inherited editor foundation.

### Pillar B — Repository understanding
Tools that help users inspect project structure, locate key files, discover references, and understand relationships between modules.

**Success criteria:** explanations link to real repository artifacts; maps can be inspected; uncertainty and incomplete coverage are visible.

### Pillar C — Evidence and verification
A workflow that ties changes to tests, diagnostics, logs, review notes, revision identifiers, and their outcomes.

**Success criteria:** users can tell what was checked, against which revision, in what environment, and what remains unknown.

### Pillar D — Knowledge continuity
A place for approved project decisions, constraints, operational knowledge, and technical notes, with provenance and ownership.

**Success criteria:** every stored item has a source or author, a timestamp or revision context where relevant, and a clear distinction between approved knowledge and generated suggestions.

### Pillar E — Bounded AI assistance
Optional AI support for explanation, navigation, drafting, test suggestions, and review preparation.

**Success criteria:** context is visible; actions are scoped; consequential changes require approval; outputs are traceable; users can decline or correct suggestions.

## 6. Technical foundation and upstream relationship

The current repository is a fork of [Lapce](https://github.com/lapce/lapce). The documented upstream foundation includes Rust, Floem, wgpu, rope-based editing, LSP, Vim-like modal editing, remote development, an integrated terminal, and WASI-oriented plugin support.

Keep a clear distinction between:
1. **Inherited capability** — functionality originating in the current Lapce codebase.
2. **MOONWITNESS modification** — code or behavior changed in this fork.
3. **MOONWITNESS original capability** — functionality newly designed and implemented by this project.
4. **Planned capability** — product direction not yet implemented.
5. **Verified capability** — functionality tested against a named revision and environment.

Do not present inherited features as original inventions. Keep upstream copyright and license notices. Review the applicable license and contribution history before redistributing modified binaries or changing package identity.

### Rebrand sequencing

A visual/product rebrand can precede a complete internal rename, but the difference must be transparent. Do not change crate names, binary names, update channels, application identifiers, or data directories casually: these can affect builds, user settings, migrations, and compatibility.

Recommended sequence:
1. Document the fork and product identity.
2. Establish UI and documentation branding.
3. Audit application metadata and user-data paths.
4. Plan package, binary, and crate renaming as a separate compatibility change.
5. Validate clean builds, upgrades, settings migration, and platform packaging.

## 7. Relationship to MOONWITNESS XV

MOONWITNESS IDE is the engineering workspace in the wider MOONWITNESS XV ecosystem.

| Component | Intended boundary |
|---|---|
| MOONWITNESS XV | Shared ecosystem vision and product family |
| MOONWITNESS IDE | Developer-facing engineering workspace |
| ARSY | Central backend hub |
| LUMEN | Planned AI framework / worker capability behind explicit contracts |
| HEADQUARTERS / 100CENTER | Human governance and coordination |
| ORBIT | Planned spatial or immersive interface |

These names describe the wider ecosystem's intended architecture, not proof of deployed services. The IDE must not duplicate the backend's authority or become a governance layer. Integration should happen through documented, versioned APIs and explicit permissions.

## 8. AI and automation governance

AI is an assistant, not an authority.

### Allowed design direction
- Explain code with links to relevant files and symbols.
- Suggest navigation paths and repository summaries.
- Draft implementation options and test plans.
- Identify possible risks for human review.
- Prepare documentation from inspectable source material.
- Propose bounded actions after showing scope and expected effects.

### Required safeguards
1. **Visible context:** show which files, symbols, documentation, or tool outputs informed a result.
2. **Uncertainty:** distinguish observed facts from inference and speculation.
3. **No silent acceptance:** generated code and knowledge remain proposals until accepted.
4. **Permission boundaries:** read, write, execute, network, and external-service permissions must be distinct.
5. **Confirmation:** ask before destructive, external, costly, security-sensitive, or release-related actions.
6. **Auditability:** record meaningful actions and outcomes where appropriate.
7. **Data minimization:** avoid sending secrets, credentials, or unrelated workspace content to external services.
8. **Human accountability:** the user or maintainer owns accepted changes and releases.

No AI-generated proposal should automatically become approved project truth or be auto-published as authoritative documentation.

## 9. Evidence model

The product should make the provenance of engineering statements inspectable.

### Evidence classes
- **Source evidence:** code, configuration, documentation, issue, or commit.
- **Execution evidence:** command output, logs, or runtime observation.
- **Test evidence:** test name, command, environment, revision, and result.
- **Review evidence:** human review, decision, or acceptance record.
- **External evidence:** a linked service or artifact with source and retrieval context.
- **Generated interpretation:** AI or tool-produced explanation that must remain distinguishable from source evidence.

### Verification states

| State | Required meaning |
|---|---|
| CI_VERIFIED | CI checks passed for a specific revision and workflow |
| BUILD_VERIFIED | A build succeeded for a specific revision and environment |
| DEPLOYMENT_READY | Deployment prerequisites were checked; no deployment is implied |
| DEPLOYED_VERIFIED | The deployed instance was inspected and tied to a revision |
| RELEASE_ACCEPTED | Defined release acceptance criteria were met and recorded |

Every verification record should identify the revision, scope, environment, timestamp, commands or workflow, result, and relevant artifact links. A label without supporting evidence is not verification.

## 10. Experience principles

- Keep the editor fast; repository intelligence must not block basic editing.
- Make advanced features discoverable but optional.
- Prefer progressive disclosure over crowded panels.
- Keep AI context and proposed actions inspectable.
- Make it easy to return from an insight to the exact source file.
- Preserve familiar editor workflows where possible.
- Provide graceful behavior when network services or AI providers are unavailable.
- Never make a network connection or AI feature mandatory for core editing.

## 11. Proposed architecture direction

This is a conceptual direction, not a description of implemented modules.

### Local workspace layer
Owns editing, local project access, navigation, terminal interaction, and user-facing state.

### Repository intelligence layer
Analyzes repository artifacts. It should support incremental updates, explicit scope, cancellation, and inspectable source references.

### Evidence and knowledge layer
Stores verification records and approved project knowledge with provenance, revision context, and ownership. Generated suggestions remain separate from accepted records.

### Integration boundary
Connects to optional external services—including MOONWITNESS XV services—through versioned contracts, scoped credentials, and explicit permissions.

### AI provider boundary
Allows optional AI providers or local models without coupling core editor operation to a single provider. Provider access must be visible and configurable.

Architectural decisions should be recorded as implementation evolves. Avoid premature microservices or duplicated sources of truth.

## 12. Delivery roadmap

The sequence below is a proposed order of work. Adjust it based on repository health, maintainer capacity, and user feedback.

### Phase 0 — Identity and baseline
- Establish this README and blueprint as the product narrative.
- Record upstream provenance and license obligations.
- Audit current build, test, packaging, and platform status.
- Identify inherited versus modified components.

**Exit evidence:** baseline build/test report tied to a commit; documented upstream and license review.

### Phase 1 — Product coherence
- Apply product naming and visual identity to selected UI surfaces.
- Audit application metadata, package names, binary names, and data directories.
- Document migration and compatibility risks before internal renaming.

**Exit evidence:** screenshots, metadata audit, platform build checks, migration test plan.

### Phase 2 — Repository understanding
- Prototype repository maps, symbol navigation, and architecture notes.
- Link every generated explanation to relevant source artifacts.
- Make indexing scope, freshness, and limitations visible.

**Exit evidence:** accuracy evaluation on representative repositories; performance and cancellation tests.

### Phase 3 — Evidence workflows
- Associate change sets with tests, diagnostics, and verification records.
- Add revision-aware summaries.
- Distinguish successful checks from incomplete or unrun checks.

**Exit evidence:** reproducible verification records with revision and environment context.

### Phase 4 — Bounded AI assistance
- Add opt-in explanation and proposal workflows.
- Expose context, permissions, and expected side effects.
- Require approval for writes and other consequential actions.

**Exit evidence:** permission tests, context transparency, audit review, and failure handling.

### Phase 5 — Knowledge continuity
- Introduce approved decision records and project notes.
- Preserve provenance, ownership, and revision context.
- Support correction, supersession, and archival without erasing history.

**Exit evidence:** data model, migration plan, provenance tests, and retention policy.

### Phase 6 — MOONWITNESS XV integration
- Integrate only services that have stable contracts and verified availability.
- Keep ARSY, LUMEN, HEADQUARTERS / 100CENTER, and ORBIT responsibilities separate.
- Make offline behavior and integration failures understandable.

**Exit evidence:** contract tests, permission review, integration test report, and service/version compatibility record.

### Phase 7 — Hardening and release
- Security and dependency review.
- Performance and resource profiling.
- Cross-platform build and packaging checks.
- Release acceptance and rollback documentation.

**Exit evidence:** release checklist completed for the exact candidate revision.

## 13. Metrics

Measure real developer value rather than feature count.

| Area | Example measure |
|---|---|
| Editor quality | startup time, input latency, crash rate |
| Repository understanding | time to locate a module or explain a dependency |
| Evidence quality | proportion of claims linked to inspectable artifacts |
| Verification | reproducibility and completeness of recorded checks |
| AI trust | proposal acceptance, correction, and rejection rates; permission violations |
| Continuity | time required for a new contributor to recover project context |
| Reliability | regression rate, failed upgrades, and recovery success |

Metrics should be collected transparently and without exposing private source code or secrets.

## 14. Definition of done

A feature is not complete merely because its UI exists.

For a meaningful feature, completion should include:
- a clear user problem and acceptance criteria;
- documented scope and architectural ownership;
- implementation and relevant automated tests;
- failure, cancellation, and offline behavior;
- accessibility and usability review where applicable;
- security and permission review when data or actions are involved;
- documentation that accurately describes current behavior;
- evidence tied to the revision being evaluated.

## 15. Non-goals and guardrails

MOONWITNESS IDE is not intended to:
- claim complete or perfect understanding of arbitrary repositories;
- autonomously approve its own code or releases;
- silently modify files or execute high-impact actions;
- turn generated interpretation into authoritative project truth;
- replace human governance in MOONWITNESS XV;
- duplicate ARSY's central backend responsibility;
- require cloud AI for basic editor functionality;
- promise deployment, security, or correctness without evidence.

## 16. Immediate priorities

1. Establish a reproducible baseline for the current Lapce-derived application.
2. Decide which visible product surfaces can be branded safely without breaking upstream behavior.
3. Audit the internal Lapce package and binary naming before renaming.
4. Define one small repository-understanding prototype with measurable accuracy.
5. Define a minimal evidence record for a test run tied to a commit.
6. Keep AI and MOONWITNESS XV integrations behind explicit interfaces until their contracts are ready.

## 17. Closing statement

MOONWITNESS IDE exists to make software engineering more understandable, traceable, and sustainable.

It should help developers see the system before changing it, understand the evidence behind a decision, verify what actually happened, and preserve knowledge for the people who continue the work.

**Observe clearly. Trace honestly. Build deliberately. Verify openly. Preserve knowledge.**

---

*MOONWITNESS IDE — The Engineering Observatory.*  
*Understand the system. Trace the evidence. Build with intention.*
