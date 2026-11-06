# Local Verification Records — Proposed Feature

**Status:** Proposed; requires product and UX validation before implementation
**Product area:** Evidence and verification
**Scope:** Local, opt-in records for checks performed by a developer

## Problem

Build and test results are often separated from the code revision and context they describe. A later reader may not know which revision was checked, which command was used, what the outcome was, or whether the result was actually observed by the IDE.

## Goal

Let a developer keep a small, inspectable record of a verification result and its provenance without requiring a cloud account, AI provider, or MOONWITNESS XV service.

## Proposed first increment

The first increment records results the developer explicitly enters. It does not silently execute commands, infer a pass from terminal text, or claim that a manually entered result was independently verified by the IDE.

Each record should include:

- Stable record ID and UTC creation time.
- Workspace association and revision identifier when available; clearly show unknown or uncommitted state.
- Check name and command text, both entered or confirmed by the developer.
- Outcome: `passed`, `failed`, `not_run`, or `blocked`.
- Provenance: `user_reported` for the first increment.
- Optional evidence reference, such as a log path or URL. Do not copy log contents by default.
- Optional note, with a warning that command text, paths, and notes may contain secrets or personal data.

The UI must label user-entered outcomes as **reported by you**, not as a CI-verified or IDE-verified result. A later feature that runs commands and captures exit status is a separate, explicitly authorized increment.

## User flow

1. The developer opens the workspace's verification records and chooses **Add record**.
2. The developer supplies or confirms the check name, command, revision, outcome, and optional evidence reference.
3. Before saving, the UI shows the exact information that will be stored and identifies user-reported fields.
4. The record is saved locally and appears in a time-ordered list.
5. The developer can inspect, export, or delete an individual record. Storage errors are visible and do not produce a success-shaped record.

## Data lifecycle recommendation

- Store records under the existing user-local Lapce/MOONWITNESS application data directory, keyed by a stable workspace identifier. Do not write into the repository by default.
- Reuse the existing local JSON persistence conventions only if they can provide safe, atomic writes and bounded record growth; otherwise specify a dedicated versioned format before implementation.
- Keep absolute workspace paths local and out of exported records unless the user explicitly includes them.
- Do not sync, upload, or collect telemetry. Provide explicit export and delete behavior.
- Preserve records if the workspace is moved; show the workspace association as unresolved until the user reconnects it.

This storage recommendation is provisional. The persistence mechanism must be selected after checking migration, corruption recovery, record limits, and compatibility with the current `LapceDb`.

## Security and privacy constraints

- Never execute a command as a side effect of creating or viewing a record.
- Do not capture terminal output automatically in this increment.
- Warn before saving command strings, log paths, or notes that may contain tokens or private filesystem paths.
- Do not treat linked or user-entered evidence as proof that the content is trustworthy.
- Surface serialization, disk-full, and permission errors to the user.

## Acceptance criteria

1. A developer can create, inspect, export, and delete a record without network access.
2. Each outcome is visibly marked as user-reported; unknown revision and environment values are not fabricated.
3. The record identifies the workspace, revision when available, check, command, outcome, timestamp, and optional evidence reference.
4. No command is run and no file in the project workspace is changed by the recording flow.
5. Persistence failures are shown and do not appear as successful saves.
6. Exported data omits absolute paths unless the developer explicitly chooses to include them.
7. Tests cover each outcome, missing revision, moved workspace, malformed stored data, export, delete, and persistence failure.

## Deferred

- Running checks, capturing exit codes or output, and automatic CI integrations.
- Shared/team records, cloud sync, AI summaries, telemetry, and ecosystem services.
- Release certification or a global "verified" status derived from individual records.

## Open decisions

- Where should the entry point live: a dedicated panel, command palette, or both?
- Should records be grouped by revision or simply ordered by time?
- What record retention/size limit is appropriate?
- Which export format is most useful without creating a de facto public schema too early?
- Which privacy warning and path-redaction behavior is understandable without obstructing the workflow?
