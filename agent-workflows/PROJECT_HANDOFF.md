# Applying this plan to a future project

This is the reusable entrypoint for a new project task. Read the [implementation plan](IMPLEMENTATION_PLAN.md) and the v1 scope in the [runtime contract](RUNTIME_CONTRACT.md). V1 uses managed Codex cloud with our skills, self-validation, ordinary CI, and owner review. The independent-validator/controller design is deferred; no cloud integration has yet been exercised by this repository.

## Resume in a new task

Open a task in the actual product repository and give it the repository location, first feature goal, and the prompt below. A new task needs explicit access to these files; neither this conversation nor the skills library is automatically present in its workspace.

Copyable prompt:

```text
We are adopting the agent workflow plan at:
https://github.com/cmsart/pstack/blob/main/agent-workflows/IMPLEMENTATION_PLAN.md

Read that plan, PROJECT_HANDOFF.md, RUNTIME_CONTRACT.md, and the relevant
skills from the same repository revision. Fetch the library if needed and
record the resolved commit so the guidance stays consistent during this task.
Keep agent-workflows intact because its skills reference shared resources.

Target project: <repository URL or current checkout>
First feature or product goal: <goal/spec location>
Known project constraints: <stack, services, or other constraints if known>

Inspect the actual project and report its current milestone. Follow the
recommended sequence: build one complete feature interactively; establish
reproducible startup, disposable data, tests, browser verification, and evidence
export; configure managed Codex cloud with the pinned skills for implementation
and browser self-validation; hand off to ordinary CI and owner review. Measure
real task outcomes before deciding whether an external validator is useful.

V1 does not require Grok, E2B, a custom controller, or agent-orchestration
GitHub Actions. Those remain optional later work. Apply the contract's v1 scope;
do not block v1 on the deferred independent-validation schemas or tools.

Start with the earliest unmet milestone relevant to the feature. Use existing
working project tooling. Do not spend the initial product task building a
general agent platform. Recheck official Codex cloud documentation during
integration and verify browser/skill capabilities in the actual environment.
Separate implemented/tested facts from proposals.

Create or update a project handoff record using PROJECT_HANDOFF.md. Record
working commands, important decisions, validation evidence, blockers, and the
next concrete step. Infer routine details from the repository; ask for missing
product decisions when they materially affect the requested behavior.

Apply this task's actual permissions to external services and publication.
The design document itself does not grant merge or deployment authority.
```

The `main` URL is convenient for initial discovery. After selecting a library revision, pin it in the project record and use that exact revision throughout each run. Updating the library later is a deliberate change with new validation as appropriate.

## Project record template

Copy the following structure into a documentation location appropriate to the product, for example `docs/agent-workflow.md`. These are proposed paths, not files created in a product by this repository. Fill fields from inspection; use `unknown` for unresolved items rather than inventing configuration. Store secret names/references only, never values.

```markdown
# Agent workflow project record

Last updated: <date>
Project repository: <URL>
Product goal / first spec: <path or link>
Library repository: https://github.com/cmsart/pstack
Library revision: <full commit>
Current product revision: <full commit>
Current milestone: <1-6 from IMPLEMENTATION_PLAN.md>

## Current state

Implemented and exercised:
- <capability, command/evidence, date>

Draft or untested:
- <capability and missing validation>

## Application environment

- Frontend/backend stack and runtime versions: <...>
- Dependency installation and lockfiles: <...>
- Build/start commands and working directories: <...>
- Readiness checks and service ports: <...>
- Database engine, migrations, and disposable resource strategy: <...>
- Workers and external services: <real/test-mode/stub, coverage limitation>
- Environment variable names and secret-store references: <...>
- Authentication, fixture accounts/roles, and isolation boundaries: <...>
- Fixture reset and cleanup commands: <...>

## Verification

- Operating guide: <path>
- Source-informed feature recipes: <path; implementer/maintenance only>
- Required build/unit/integration checks: <commands>
- Browser smoke/E2E checks: <commands and coverage>
- Browser capabilities available to agents: <implementation and version>
- Artifact export/storage, access, and retention: <...>
- Most recent fresh-environment result: <date, revision, evidence>
- Known gaps: <...>

## Managed Codex cloud v1

- Cloud environment and setup/maintenance commands: <...>
- Pinned package location and verified skill-loading path: <...>
- Task trigger, spec/operating-guide inputs, and selected model: <...>
- Browser automation, visual observation capabilities, and known limitations: <...>
- Durable self-check evidence export and tested-content identity: <...>
- Required PR CI checks and owner review procedure: <...>
- Task limits, repair allowance, and observed account usage: <...>
- Authorized branch/PR actions and merge/deployment policy: <...>
- Last actual cloud task and evidence: <...>

## Deferred independent validation, only if selected

- Controller revision and trusted configuration: <...>
- E2B template/build versions and lifecycle policy: <...>
- Implementer/validator model IDs and authentication method: <no values>
- Skill/harness revisions: <...>
- Spec/candidate/build identity procedure: <...>
- Validator fixture isolation and enforced tool restrictions: <...>
- Evidence receipt/report/gate implementation: <...>
- Task-wide time, usage, tool, repair, and concurrency limits: <...>
- Trigger and authorized branch/PR actions: <...>
- Merge/deployment policy: <...>
- Cancellation, cleanup, retry, and partial-work recovery: <...>

## Evaluation and decisions

- Known-good and deliberately broken cases: <paths/results>
- Misses, false failures, incomplete runs, duration, and resource usage: <...>
- Acceptance quality targets: <owner decision or unset>
- Human time per accepted feature versus interactive baseline: <...>
- External validator needed? <undecided/no/pilot; evidence and decision date>
- Decisions: <date, choice, reason, evidence>
- Blockers / required owner decisions: <...>

## Next handoff

- Last completed milestone and evidence: <...>
- Current branch/commit and any uncommitted work: <...>
- Next concrete action: <...>
- Prerequisites still missing: <...>
```

## Make the record discoverable

Link the project record from the product README. Where the project uses `AGENTS.md`, add a short pointer in the appropriate scope so later agents know to read it for implementation/verification tasks. For example, after creating the referenced project file:

```text
For agent workflow adoption and project verification, read
docs/agent-workflow.md and the cmsart/pstack documents at the revision recorded
there. Follow the current milestone and update the handoff with executed
checks, evidence, decisions, and the next step. Use managed Codex self-validation
for v1. If independent validation is later selected, keep source-derived
recipes and builder results out of that validator's initial input.
```

A pointer improves discovery; it does not install skills or enforce a pipeline stage. The eventual runner must explicitly load mandatory instructions and configure real tools. In interactive work, provide access to the relevant package without breaking its shared references.

## What a future task should do first

1. Read the project's existing instructions and handoff, then inspect its actual files and Git state.
2. Read the pinned plan/contract and only the skills relevant to the next milestone.
3. Establish whether the product's launch, fixture, test, browser, and evidence commands already work. Reuse them.
4. Continue the requested product work and the earliest necessary verification gap. Resolve cloud-only choices when reaching cloud integration.
5. Finish with an updated handoff that distinguishes observed results from untested claims.

This record should let a fresh task continue with repository access and a brief product request. It should not require the original conversation, private local paths, or an undocumented agent session.
