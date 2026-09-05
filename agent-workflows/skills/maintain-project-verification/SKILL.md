---
name: maintain-project-verification
description: Audit and repair an existing web-app operating guide, feature map, or verification harness against source and live behavior without changing product code or acceptance requirements.
---

# Maintain project verification

Keep an existing project verification package usable as the app evolves. Read the [runtime contract](../../RUNTIME_CONTRACT.md). This is a maintenance run with source access, separate from independent acceptance.

## Scope the audit

Locate the operating guide, project skill, feature index, helpers, approved requirement references, and package revision. If no package exists, return the missing prerequisite and route to bootstrap. If several packages could apply, resolve the target from the task before editing.

For a full audit, account for every mapped feature and known entry point. For a targeted drift repair, name the subset and report omitted coverage. Source inspection identifies likely drift; it does not substitute for live execution.

Only edit the verification package's own documentation and helpers. Product code, authoritative criteria, validator policy, and acceptance gate are outside this skill's scope. Additional source-reading workers are optional when useful and authorized; the default is one maintenance owner.

## Inspect and drive

Check index consistency and inspect changed routes, controls, fixture setup, and startup commands. Mark each expectation by its authority: approved requirement, regression test, or historical observation. Do not rewrite a required behavior to match a regression.

Start or obtain an owned test instance; check readiness and build identity. Drive each feature/entry point in the audit scope, resetting fixtures where state could contaminate a later check. Give concurrent drivers separate browser contexts and server-side data; otherwise use one owner sequentially.

Preserve evidence after surprises, then doctor/reset before retrying. Recheck that evidence survives cleanup. Clean up only owned resources and failed-attempt residue. Never kill processes by a broad name or delete retained proof as part of fixture reset.

Classify discrepancies:

- **Documentation drift:** the guide inaccurately describes behavior whose intended change is supported by requirements or other authoritative evidence.
- **Harness gap:** the expected behavior works, but the tooling or recipe cannot drive/observe it correctly.
- **Product regression:** the app violates an existing required behavior; report it for product repair without altering the expectation.
- **Unresolved:** evidence cannot establish which category applies; report the competing explanations and needed check.

## Prove corrections and hand off

Execute every changed helper or recipe against a fresh applicable state. A harness correction must be re-driven through the live UI. If a single allowed environment recovery fails, retain a blocker instead of repeatedly retrying.

Return `CLEAN`, `CHANGED`, or `BLOCKED`, with scope coverage, discrepancy classifications, corrections, evidence, and unreachable prerequisites. `CHANGED` means proposed corrections were exercised; it does not mean they were deployed. Publish only through the task's authorized path.

For partial coverage, report `BLOCKED` with any useful draft corrections. An unreachable feature is blocked coverage, never accepted coverage. The controller versions accepted package changes and applies them to a new validation attempt; current or historical acceptance reports remain bound to their original package version.
