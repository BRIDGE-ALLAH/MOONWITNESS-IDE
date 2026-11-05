# MOONWITNESS IDE — Brand System

**Descriptor:** The Engineering Observatory  
**Primary tagline:** Understand the system. Trace the evidence. Build with intention.  
**Supporting line:** The Moon Watches. The Record Remembers. The Evidence Remains Inspectable.

## Brand idea

MOONWITNESS IDE is an engineering observatory: a calm, precise workspace for observing software systems, tracing evidence, and making deliberate changes. The identity combines a crescent moon, an orbital path, and a vertical evidence marker. The moon represents sustained attention; the orbit represents relationships across a system; the marker represents a traceable observation.

The symbol is not a claim of omniscience. It stands for disciplined observation and transparent investigation.

## Logo assets

- `extra/images/logo.svg` — primary scalable symbol for documentation and UI.
- `extra/images/logo_color.svg` — color symbol variant.
- `extra/images/logo_app.svg` — dark application tile.
- `extra/images/logo_app_light.svg` — light application tile.
- `icons/lapce/lapce_logo.svg` — editor UI logo asset retained at its upstream-compatible path.

Use SVG assets where supported. Do not stretch, recolor arbitrarily, add effects, or place the mark on low-contrast backgrounds. Keep clear space around the mark approximately equal to the diameter of its small orbit node. For very small sizes, prioritize the crescent and orbit; omit decorative details if a simplified mark is prepared.

## Color palette

| Token | Hex | Role |
|---|---|---|
| Observatory Midnight | `#0B1020` | Primary dark canvas |
| Deep Space | `#151E36` | Elevated dark surfaces |
| Moon Gold | `#F6D99A` | Primary brand accent |
| Aged Brass | `#D9A95B` | Secondary warm accent |
| Signal Cyan | `#66E0DF` | Evidence, focus, active signal |
| Orbit Indigo | `#7B91F5` | Secondary navigation and structure |
| Paper | `#F8FAFF` | Light surfaces |
| Ink | `#172033` | Light-mode text |

Use gold sparingly for identity and key emphasis, cyan for active or inspectable signals, and indigo for supporting structure. Do not use color alone to communicate status; pair it with text or an icon.

## Typography

Use the platform UI sans-serif stack for application chrome and a readable monospace font for code and technical identifiers. Prefer restrained weights and clear hierarchy. Avoid decorative display fonts in engineering workflows. The product name may use a bold geometric sans-serif in marketing material, but body copy must remain highly legible.

## Voice

The brand is observant, precise, calm, trustworthy, capable, and human-directed.

Prefer: observe, trace, evidence, inspect, verify, proposal, review, accept, source, revision, and known limitation.

Avoid: magic, omniscient, guaranteed, autonomous truth, zero-risk, and claims of perfect understanding.

Always distinguish current functionality from planned capability. AI output is a proposal until a human reviews and accepts it.

## Product language

- Product name: **MOONWITNESS IDE**
- Descriptor: **The Engineering Observatory**
- Primary tagline: **Understand the system. Trace the evidence. Build with intention.**
- Supporting line: **The Moon Watches. The Record Remembers. The Evidence Remains Inspectable.**

Use the full product name on first mention. Keep internal crate names and compatibility identifiers unchanged until a separate migration plan is tested.

## Accessibility and implementation

Maintain WCAG-conscious contrast for interface text and controls. Accent colors should not replace semantic state labels. Test the symbol against light, dark, monochrome, and small-size backgrounds before producing additional platform-specific raster assets.

## Upstream attribution

MOONWITNESS IDE is currently based on the Lapce codebase. Keep the upstream license, notices, and attribution. Internal identifiers such as crate names, bundle IDs, executable names, and data directories may remain Lapce-derived for compatibility; that does not change the public product identity.
