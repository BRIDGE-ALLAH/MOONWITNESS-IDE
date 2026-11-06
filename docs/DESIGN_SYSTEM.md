# MOONWITNESS XV — RIOT OBSERVATORY DESIGN SYSTEM

**Product:** MOONWITNESS IDE  
**Experience direction:** XV Hybrid / Command Center / Rich visual density  
**Tagline:** Observe the chaos. Decode the system. Engineer the future.

This document is the implementation contract for the MOONWITNESS interface. The product must feel like an engineering observatory with a rebellious industrial identity—not a recolored clone of a conventional code editor.

## 1. Design principles

1. **Editor remains sovereign.** Code editing, LSP, completion, diagnostics, terminal, source control, debugging, keymaps, and workspace behavior must remain intact.
2. **Command-center composition.** The shell prioritizes system awareness and fast access to engineering tools while keeping the editor as the primary work surface.
3. **Controlled grunge.** Distressed textures, poster-like typography, and rough graphic details belong in framing, welcome surfaces, and decorative regions—not behind source text or dense data.
4. **Signal has meaning.** Amber marks primary actions and focus; acid green marks healthy/ready states; riot red marks errors or destructive conditions; teal is reserved for secondary telemetry.
5. **Progressive disclosure.** Rich density must not mean constant visual noise. Secondary telemetry and panels remain collapsible and user-controlled.
6. **Accessible contrast.** Text, syntax, focus indicators, and status signals must remain readable at common Windows scaling settings.

## 2. Color tokens

| Token | Value | Role |
|---|---|---|
| Obsidian | `#111315` | Main canvas |
| Graphite | `#1B1E20` | Panels and raised surfaces |
| Steel | `#282B2D` | Selected/hovered surfaces |
| Signal Amber | `#E8A044` | Primary accent, focus, active state |
| Acid Lime | `#A9CF72` | Healthy/ready state |
| Riot Red | `#D64B37` | Errors and destructive state |
| Nebula Teal | `#78B9B2` | Secondary telemetry |
| Warm Ivory | `#E8E1D3` | Primary text |
| Ash | `#85817A` | Muted metadata |

The default dark theme is **RIOT OBSIDIAN**. The light counterpart is **PAPER SIGNAL** and retains the same warm industrial accent family.

## 3. Command-center information architecture

The target shell is organized into five zones:

- **Command Rail:** compact, persistent navigation for Explorer, Search, Source Control, Run/Debug, Extensions, and Settings. Existing panel commands remain the source of truth; no duplicate feature implementation.
- **Project Observatory:** workspace tree, open editors, project metadata, and repository context.
- **Engineering Deck:** existing editor tabs, split editors, code surface, breadcrumbs, and navigation. It remains the largest region.
- **Intelligence Bay:** contextual diagnostics, symbol outline, call hierarchy, architecture/evidence views, and future AI surfaces. Only implemented data may be presented as live.
- **Signal Console:** existing terminal, problems, build output, debug console, and progress. It remains dockable and resizable.

The existing Floem panel system already supports left, bottom, and right containers, panel pickers, drag-and-drop panel movement, and resize handles. The redesign should extend and restyle these mechanisms rather than replace them.

## 4. Layout behavior

- Default workspace: left project panel visible, editor centered, right intelligence panel available, bottom signal console available.
- Editor receives the majority of horizontal space.
- Left/right panels retain minimum practical widths and resize behavior.
- Bottom console is collapsible and resizable.
- Command rail stays narrow and does not steal focus from the editor.
- All panels remain movable through existing panel drag-and-drop behavior.
- Small windows should hide or collapse secondary regions before shrinking the editor below a usable width.

## 5. Typography and graphic language

- UI headings: condensed, bold display face where a bundled/licensed font is available.
- Metadata and telemetry: monospace, uppercase labels, compact tracking.
- Source code: preserve the editor's configured coding font and line metrics.
- Use numbered section markers such as `01 / PROJECT`, `02 / ENGINEERING DECK`, and `03 / SIGNAL CONSOLE`.
- Use orbit/coordinate motifs sparingly in welcome surfaces, empty states, and decorative chrome.
- Do not add noisy textures to editor text, completion menus, or diagnostic content.

## 6. Motion and interaction

- Short transitions for panel reveal/hide and selection feedback.
- No continuous ambient animation while editing.
- Reduced-motion preference must be respected where supported.
- Every status indicator must be backed by real application state; no fabricated build, network, AI, or diagnostic telemetry.

## 7. Implementation phases

### Phase I — Identity foundation
- Establish the RIOT OBSIDIAN palette and PAPER SIGNAL companion theme.
- Add a product wordmark to the application chrome.
- Document design tokens and visual rules.

### Phase II — Command shell
- Evolve the existing activity/panel pickers into a coherent Command Rail.
- Give the left, center, right, and bottom regions clear hierarchy and branded section headers.
- Preserve panel resizing, drag/drop, focus, and keyboard workflows.

### Phase III — Observatory surfaces
- Add a purposeful workspace/welcome surface.
- Add repository and architecture visualizations only when backed by real workspace data.
- Integrate existing diagnostics, source control, debug, and progress state into the Signal Console.

### Phase IV — Finish and validation
- Review Windows display scaling, keyboard navigation, contrast, and reduced motion.
- Run formatting, Clippy, workspace checks, and Windows build.
- Compare screenshots at common window sizes and verify that core editing workflows remain unchanged.

## 8. Non-goals and safeguards

- Do not replace Floem or rewrite the editor engine for visual reasons.
- Do not remove existing Lapce-derived capabilities or compatibility identifiers.
- Do not imply MOONWITNESS XV ecosystem services are implemented unless their code and tests exist.
- Do not introduce external image/font assets without verifying licenses and packaging behavior.
- Do not claim a phase is complete until its code, tests, and platform evidence are available.

## 9. Current implementation note

The first implementation increment applies the RIOT OBSIDIAN / PAPER SIGNAL theme tokens and product wordmark. The full Command Rail, Intelligence Bay, and Observatory dashboard are subsequent UI engineering work and must be implemented incrementally against the existing Floem panel architecture.
