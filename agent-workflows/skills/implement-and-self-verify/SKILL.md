---
name: implement-and-self-verify
description: Implement an authorized web-app change, run relevant automated checks and the changed browser journey, and hand off a candidate with evidence for review.
---

# Implement and self-verify

Produce a candidate that implements the supplied acceptance specification and has been checked through both relevant automated tests and the running UI. Read the applicable scope in the [runtime contract](../../RUNTIME_CONTRACT.md). V1 uses managed Codex self-validation, ordinary CI, and owner review. You own implementation and self-checks; independent validation is a separate optional mode.

## Establish the task boundary

Read the task's criteria, allowed paths, baseline commit, operating guide, feature map, and budget. Use repository inspection or a small experiment to resolve factual questions. Record reversible implementation assumptions. If an ambiguity changes the required product behavior, identify the decision and continue only independent work; do not silently choose a new acceptance target.

Do not change the authoritative task specification, validator instructions, evidence receipts, or gate configuration to make the candidate pass. Propose necessary changes to these as separate work. Use the specification supplied by the owner/task or pinned by the controller, not an unapproved revision from the candidate branch.

## Implement and test

Choose the simplest coherent implementation within the task. Use one implementation owner by default. Additional workers or competing designs need an actual independent subtask, suitable isolation, and authorization from the task/controller; there is no automatic multi-model design stage.

For a bug, capture the smallest practical failing regression check before changing the implementation. For a feature, add tests of intended behavior at the layer where they provide useful signal. Avoid tests that merely reproduce the implementation or mostly exercise mocks. Do not weaken assertions to accommodate a defect. If failing-before evidence is impractical, record why and retain the closest useful executable reproduction.

Identify which nearby behavior could break because of the change. Test the important assumptions with real code: callers, serialized formats, permission checks, state transitions, or dependency behavior as relevant. Distinguish tested conclusions from unproven risks; a list of speculative possibilities is not validation.

Run the repository's required checks and relevant unit/integration tests. Then drive the changed user journey in the real app. Observe the action and resulting state. Demonstrate persistence through reload or a new session when the criterion requires it. Backend tests remain necessary for properties a browser cannot establish.

Use screenshots for visual state and browser records for behavior. A success toast alone does not prove a write persisted. A build succeeding does not prove the feature works. If the instance behaves unexpectedly, recheck readiness and state before drawing conclusions; retain the original failure while diagnosing whether the app or harness caused it.

## Hand off the candidate

Keep changes in the owned branch/checkout. Record test commands and outcomes, UI evidence, coverage by criterion, changed files, unresolved issues, and the exact candidate commit. Externalize the patch or commit and evidence through the task's verified handoff path before the sandbox expires. Push or open a PR only when that action is authorized.

In v1, hand off the candidate and self-check evidence for CI and owner review; do not wait for a nonexistent validator or claim independent acceptance. If independent-validation mode is selected, the controller builds a fixed candidate from committed content in a fresh environment. Self-check reports are retained for diagnosis but withheld from that validator's initial discovery pass.

If checks fail, repair within the task budget. If the budget, credentials, or environment block progress, return the partial result and evidence with a concrete blocker. An agent's successful process exit is not an acceptance result.
