---
name: repair-confirmed-failure
description: Reproduce a validator-reported web-app failure, make an evidence-backed correction with regression coverage, and request independent validation of a new candidate.
---

# Repair a confirmed failure

Fix the demonstrated behavior within the existing task specification. Read the [runtime contract](../../RUNTIME_CONTRACT.md). A repair assignment includes the original report, reproduction evidence, failing candidate identity, relevant criteria, allowed paths, and remaining repair budget.

## Reproduce before diagnosing

Check out the reported candidate or confirm why the current candidate differs. Recreate the reported preconditions and UI actions. Preserve the failing result. If the failure cannot be reproduced, inspect the run identity, fixtures, observation method, and available logs before changing code.

Do not label the report wrong because your first replay passed. Retain intermittent evidence and return `INCONCLUSIVE` when the behavior cannot be resolved within budget. If the report tests behavior the spec does not require, document the mismatch for the decision owner; you do not have unilateral authority to dismiss a required failure.

## Establish the cause and regression check

Form hypotheses and use runtime evidence or focused instrumentation to distinguish them. Remove changes justified only by a refuted hypothesis. Establish the smallest regression check that would catch the defect: unit, component, integration, or browser-level, according to the actual failure.

Run the check against the failing candidate before the fix and confirm the failure is for the intended reason. A browser reproduction is a valid regression check when a unit test would require misleading mocks or unrelated scaffolding. State any missing failing-before evidence explicitly.

## Correct and verify

Change the smallest coherent product surface that resolves the cause and preserves adjacent contracts. Do not edit the acceptance criteria, expected results, validator skill, or gate. A harness correction belongs in a separate maintenance change and cannot make this acceptance run retrospectively pass.

Run the regression check and the original UI reproduction after the fix, then relevant neighboring tests. Check other instances of the same failure mechanism where evidence indicates shared exposure. Avoid speculative scope expansion.

Commit or export the candidate through the authorized handoff path. Preserve both failing and passing artifacts with their respective commit/build identities. The controller creates a fresh candidate and reruns the failing journey plus the required acceptance coverage; old passes do not transfer automatically to new code.

## Return

Report the cause, correction, failing-before and passing-after evidence, regression coverage, unresolved findings, candidate identity, and whether another repair round is needed. Only the controller counts rounds and grants remaining budget. When exhausted, return a durable handoff instead of starting another loop.

Your passing self-check requests independent revalidation. It does not overwrite the validator's original verdict or authorize merge/deployment.
