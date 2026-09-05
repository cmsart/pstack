---
name: improve-agent-workflow
description: Turn demonstrated failures or repeated corrections into a narrowly scoped skill or tooling improvement, evaluated between runs before promotion to future agents.
---

# Improve the agent workflow

Use evidence from completed runs to improve the system without changing the rules of an active acceptance attempt. Read the [runtime contract](../../RUNTIME_CONTRACT.md). Inputs are the selected run records, artifacts, task specs, skill versions, and an authorized improvement scope.

## Select a demonstrated lesson

Read only the supplied runs and their evidence. Do not search unrelated conversations or assume a local transcript directory. Identify the observed failure, its consequence, and the mechanism that allowed it. A single clear systemic defect can justify a change; a one-off preference does not automatically become a universal instruction.

Distinguish product defects from agent, harness, and orchestration defects. Prefer a test or structural check when it can enforce the invariant more reliably than prose. Examples:

- Evidence disappears at teardown: fix artifact export/retention.
- A stale candidate passes: enforce build/spec identity comparison in the controller.
- A validator skips an awkward criterion: enforce complete criterion coverage.
- An agent repeatedly misinterprets a product concept: clarify the relevant skill with a concrete counterexample if the approved spec already settles the meaning.

## Propose the smallest change

Route to an existing skill or tool before creating a new one. Record the triggering evidence, proposed edit, expected benefit, and potential tradeoff. Avoid importing an entire transcript, adding broad mandatory review stages, or hardcoding the current provider/model into procedural instructions.

Keep `accepted for evaluation`, `rejected`, and `backlog` items separate. Only file external tickets or edit shared installations when authorized. Drafting and testing within the assigned improvement workspace may proceed under the task's existing authorization.

## Evaluate before promotion

Hold the app/spec/candidate fixtures constant while comparing the old and proposed skill or harness. Use cases that expose the original failure and known-good cases that could be falsely rejected. Add an unseen variant when feasible so the change is not merely memorizing one example.

Measure observable results: missed defects, false failures, required-criterion coverage, unresolved runs, action count, latency, and cost. For the acceptance gate, include stale identity, missing evidence, skipped criteria, and disagreeing validators. A correct result obtained by bypassing the browser or weakening requirements is not a win.

Use an independent evaluator when the available runtime and task authorize it and the uncertainty warrants it. Otherwise label the evaluation as author-run. Do not present static checks or hypothetical scenario reviews as a live model evaluation.

## Return a versioned proposal

Provide the edit/diff, supporting runs, evaluation method and results, known limitations, and rollback target. If live evaluation cannot run, return a draft proposal with that gap. Apply a new version to future tasks only through the designated promotion mechanism or explicit authorization; never hot-edit an active validator's instructions.

Persist actionable lessons in their owning files or mechanisms. Do not claim a lesson was learned merely because it appeared in a final message.
