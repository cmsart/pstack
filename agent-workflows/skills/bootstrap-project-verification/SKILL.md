---
name: bootstrap-project-verification
description: Create and exercise a project-specific operating guide and verification harness for a web app before agents implement or independently validate changes.
---

# Bootstrap project verification

Give the next agent a tested way to start, identify, drive, observe, and clean up this app. Scope this skill to web applications. Produce a project package in the location supplied by the task; do not install global skills or configure cloud accounts as a side effect.

Read the [runtime contract](../../RUNTIME_CONTRACT.md) for ownership and evidence rules. This skill has source access. Its observations describe the current application; they do not authorize acceptance requirements.

## Discover the real operating path

Read the repository's startup documentation, package commands, existing browser tests, routes, authentication, and fixture setup. Reuse working tools before building replacements. Establish:

- The build/start commands, required environment variable names, readiness condition, and shutdown mechanism.
- How to identify the candidate commit and build using controller-owned metadata; the app's own version label is only supplementary evidence.
- How to create disposable users and isolated server-side data, reset them, and open clean browser contexts. Browser context isolation alone does not isolate a database.
- Which external services are real, test-mode, or stubbed; what behavior each substitute cannot establish.
- The actual browser capability available to the agent, including screenshots and action/assertion records. Do not invent a tool name because an upstream skill used it.
- How the controller retains artifacts outside an ephemeral sandbox before teardown.

If the base app does not start, diagnose and report the concrete cause. Fix a product defect only if the task authorizes that scope. Setup scaffolding must be labeled and isolated; it must not replace the feature under test or falsify readiness.

## Produce two distinct guides

Create an `OPERATING_GUIDE.md` for any agent using the app. Include launch, readiness/doctor, test-account roles, fixture lifecycle, supported browser operations, evidence export, and cleanup. Describe environment mechanics without prescribing the new feature's acceptance journey or exposing source internals. List prerequisites and limitations explicitly; never include credential values.

Create a source-informed `features/` index and a small initial set of feature recipes for implementer self-checks and later maintenance. Each recipe records:

1. Feature ID and known entry points.
2. Preconditions and starting data.
3. User actions and observable results, using real accessible names or other observed handles.
4. Persistence or other side effects that require a second observation.
5. Known gaps and whether each expectation comes from an approved requirement, existing test, or current behavior.

Keep this feature map out of the independent validator's initial brief. An observed behavior is not an acceptance requirement. Mark untested recipes as untested instead of presenting the entire map as verified.

Add a project `SKILL.md` entrypoint with valid name/description that routes to these guides, and only the executable helpers they need. Document helper invocations. The controller supplies this package explicitly; this skill does not assume `.cursor`, a particular provider, or an installed plugin.

## Exercise the package

Follow the generated instructions from a fresh state: launch, doctor, drive one representative feature through the UI, inspect its observable outcome, export evidence, and clean up only the resources this run owns. Check that exported artifacts still resolve after cleanup. Clean up failed attempts too.

A smoke test proves the operating recipe for the exercised feature. It does not establish acceptance of the app or coverage of every feature in the map. If browser access or export is unavailable, return a draft package with `BLOCKED` and the missing capability; do not claim the package was exercised.

## Return

Report the package path, app/build identity, feature actually exercised, executed commands, evidence references, cleanup result, untested recipes, and remaining prerequisites. Suggest maintenance when the guide drifts; do not create a schedule unless requested.
