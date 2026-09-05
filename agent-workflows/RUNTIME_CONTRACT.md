# Runtime contract

This is the shared contract for the six skills in this package. It specifies the responsibilities of the future GitHub Actions/E2B runner. These are design requirements, not claims that cloud orchestration, browser tools, artifact storage, or an acceptance gate have already been implemented.

## Components and ownership

| Component | Responsibility | Does not own |
| --- | --- | --- |
| Task owner | Intended behavior, required criteria, authorized scope and exceptions | Fabricating evidence |
| Controller | Pin inputs, provision resources, enforce budgets, capture receipts, evaluate reports, publish authorized outputs | Inventing product requirements |
| Codex implementer | Product changes, useful tests, UI self-checks, repair | Independent acceptance or validator policy |
| Grok validator | Independent browser journeys, observed outcomes, criterion report | Product edits or changes to expected results |
| Maintenance worker | Operating guide and harness corrections | Product fixes or retrospective acceptance |
| Improvement worker | Evaluated proposals for later skill/tool versions | Hot-editing the rules of an active run |

The initial configuration has one implementer and one independent validator. Provider/model identifiers are explicit configuration inputs. An optional second validator uses the same spec and fixed candidate, isolated fixtures, and fresh context. A model change is recorded and evaluated; unavailable models cause a visible configuration failure rather than a silent substitution.

## Task brief

The controller supplies each phase a self-contained brief. Required fields:

| Field | Meaning |
| --- | --- |
| `task_id` | Stable identifier across implementation and repair attempts |
| `phase`, `attempt_id`, `role` | What this invocation owns and how it is identified |
| `goal` | Requested observable outcome |
| `spec_path`, `spec_sha256` | Immutable acceptance input and hash of its exact bytes |
| `baseline_sha` | Repository commit from which implementation starts |
| `candidate_sha`, `build_id` | Required for validation/repair; controller-assigned identity of tested content |
| `skill_revision`, `harness_revision` | Versions actually used in this attempt |
| `operating_guide` | Environment procedure, fixture roles, readiness, browser tools, evidence export |
| `allowed_paths`, `allowed_tools` | Scope that the environment also enforces |
| `fixture_namespace` | Dedicated server-side test data, not just fresh cookies |
| `evidence_sink` | Durable run-specific artifact destination and submission interface |
| `budget` | Wall time, model/tool usage limits, and any remaining retry/repair allowance |
| `publication_policy` | Which branch/PR/report actions are already authorized |

Credentials are injected by the runtime, not written into briefs, specs, artifacts, or skills. Missing capabilities are reported as missing; skill text cannot make a browser or provider integration exist.

## Acceptance specification

Each criterion has a stable unique ID, required outcome, preconditions, and necessary observation boundary. For example, saving a record requires a later read if persistence is part of the outcome. The specification states required roles/viewports/entry points where relevant and names allowed external test doubles and their coverage limitations.

All entries in `criteria` are required. Optional product ideas live separately in `suggestions`; they cannot be used to fail required acceptance. A human-authorized requirement change creates new spec bytes/hash and a new attempt.

The source-informed feature map is historical and operational context for implementation/maintenance. It is not the source of truth for a new task's expected behavior. The validator's initial brief excludes source code, feature recipes, implementation conversation, self-check results, and other validators' findings.

The [notes specification](examples/notes-acceptance.json) is an illustrative task input. It is not an observed app, live test result, or generated project verification package.

## Candidate and data lifecycle

1. The implementer externalizes a commit or patch through the authorized handoff path.
2. The controller records an immutable commit, creates a clean candidate environment, builds it with pinned dependencies, and binds a build ID to the artifact and configuration. Build identity must not rely only on a version string controlled by the app.
3. The candidate has isolated disposable data and no model-provider or repository-write credentials. Validators receive their own data namespace and browser context. A shared database must enforce fixture isolation, or the controller provisions separate databases/app instances.
4. The controller gives the validator access to the fixed candidate. The implementer cannot mutate that instance during validation.
5. Evidence is exported outside the sandbox before cleanup. Cleanup targets only resources identified as belonging to this attempt. Retries use unique attempt IDs and never overwrite old reports.

E2B lifecycle calls, browser services, provider authentication/refresh, and artifact uploads are adapter work still to implement. Pin their versions during that integration. Install neither an agent credential nor a shared account auth cache in a reusable public sandbox image.

## Browser capability contract

Expose navigation, click, fill, keypress, scroll, screenshots, accessible/visible state, and bounded waits. Record action results and browser observations automatically. The actual tool names come from the adapter; these are capabilities, not invented callable APIs.

Restrict validation tools outside the model's control. No general shell or arbitrary page evaluation should enable source inspection, internal state setters, direct business-API shortcuts, or evidence fabrication. Network/console diagnostics may help explain a failure but do not substitute for exercising the required UI action.

The controller can reset fixtures and provision accounts. Pre-authentication is allowed only when login is not the behavior under test. Testing through a stubbed integration does not prove the production service. DOM-based interaction and screenshots are complementary; screenshot inspection alone cannot prove persistence or authorization.

## Evidence and report contract

The trusted browser/runner records artifacts. Each receipt includes an artifact ID, attempt ID, candidate/build identity, timestamp, content hash, and durable location. Record the actual model requested/resolved and tool versions in the run manifest. Artifacts may include Playwright traces, screenshots, console/network records, assertion results, or executed-test logs.

The agent reports concise conclusions and references these receipts. It cannot mint authoritative receipts or modify stored evidence. Before accepting a report, the controller verifies referenced artifacts exist and match the attempt; artifact existence alone does not prove the semantic conclusion.

An acceptance report contains:

| Field | Meaning |
| --- | --- |
| `task_id`, `attempt_id`, `validator_id` | Reporter and run identity |
| `spec_sha256`, `candidate_sha`, `build_id` | Exact inputs tested |
| `skill_revision`, `harness_revision`, `model` | Recorded configuration |
| `criteria` | Exactly one result per required ID: status, observed outcome, evidence IDs, finding IDs |
| `findings` | Criterion ID, preconditions, ordered actions, expected/observed results, evidence, replay count/results |
| `blockers` | Missing prerequisites and the attempted checks |
| `suggestions` | Non-blocking ideas outside required acceptance |
| `usage`, `cleanup` | Budget consumption and resource/export outcome |

Criterion status is `PASS`, `FAIL`, `BLOCKED`, or `INCONCLUSIVE`. Keep agent claims and controller acceptance decisions separate. Missing/duplicate criteria, malformed reports, mismatched identities, missing receipts, or a crashed agent produce an invalid or incomplete run, never a pass.

See [scenario expectations](examples/acceptance-scenarios.md) for edge cases that the eventual gate and agents must handle. Those are authored evaluation cases, not test results.

## Decision and repair rules

The controller applies rules to the complete set of required reports for the current identity:

- **Accept:** every required criterion is `PASS` with valid evidence in every required validator report, and all required automated checks pass. No unresolved failure for this candidate may remain. This makes the candidate ready for the authorized publication step; acceptance alone does not grant deployment or merge authority.
- **Repair:** a required behavior has a confirmed, reproducible failure. A single validator's counterexample is enough. Do not vote it away or silently reduce the required validator count after a dropout.
- **Replay/diagnose:** a failure is disputed, intermittent, or might reflect a harness problem. Replay in a fresh attempt against the same identity. Preserve both reports. The controller may assign this evidence to a validator after the independent discovery pass is complete.
- **Block/escalate:** required coverage is unavailable, evidence is inconclusive, a product decision is needed, or the budget is exhausted. A decision owner must explicitly revise requirements or authorize additional work; elapsed time is not approval.

Default policy for the first integration: at most two product repair rounds per task and one infrastructure replay per failed attempt, also bounded by a task-wide deadline and spend/tool-call limits supplied in the brief. These are starting defaults the task owner may override. Only the controller counts attempts and grants budget. Retrying until a failure happens to pass is not a recovery policy.

A new candidate SHA, build/configuration, spec, skill, or harness revision requires a new acceptance attempt. After a product repair, recheck the reported failure and all required criteria on the new identity. Later optimization may reduce redundant work only with an explicit validated policy.

Harness fixes and skill improvements are separate versioned changes. They do not retroactively change historical verdicts or hot-patch an active validator.

## Portability and package use

Keep the `agent-workflows/` directory intact: the six entrypoints link to this shared contract. A runner should mount it read-only and provide the selected skill and contract explicitly. Copying a single skill directory requires vendoring its linked contract/resources and adjusting relative paths.

The new frontmatter uses portable `name` and `description` fields and leaves normal skill discovery enabled. Mandatory pipeline stages are selected by the controller, not by hoping a model implicitly invokes a skill. Cursor-specific `Task` calls, `.cursor` directories, model aliases, transcript formats, and automatic model fallbacks are absent from this contract.
