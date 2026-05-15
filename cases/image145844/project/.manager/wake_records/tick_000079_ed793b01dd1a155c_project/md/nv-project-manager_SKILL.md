---
name: nv-project-manager
description: Manage long-running NV autonomy projects with compact startup guidance, durable project state, evidence ledgers, backlog, bounded code-change requests, physical-action requests, and procurement blockers across many agent invocations.
metadata: {"openclaw":{"requires":{"bins":["python3"]}}}
---

# NV Project Manager

Use this skill when an NV objective should continue across many wakes.

This file is the first-read operating guide. It should be enough to start or
continue project work without carrying the long reference in context. Read the
detailed reference only when the current wake needs a command example,
compatibility-hook behavior, or an unusual edge case:

- `<OPENCLAW_WORKSPACE>/docs/nv_project_manager_full_reference.md`
- `<OPENCLAW_WORKSPACE>/docs/vibe_research_project_structure.md`
- `<MATLAB_23C_ROOT>/docs/autonomous_projects.md`
- `<MATLAB_23C_ROOT>/docs/code_change_protocol.md`
- `<MATLAB_23C_ROOT>/docs/physical_action_protocol.md`

## Role Split

- `nv-researcher` owns research judgment, experiment-design reasoning, evidence
  synthesis, model comparison, finding scope, and agenda/backlog expansion.
- Python owns durable state, queue safety, audit logs, wake pacing, completion
  markers, and hard hardware/code safety boundaries.
- The MATLAB bridge remains the execute safety gate. Do not bypass bridge
  validation, manifest limits, local lab opt-in, queue execute opt-in, or
  hardware safety limits.
- The project manager sits above `nv-batch-run`, `nv-queue-submit`, and
  `nv-sequence-author`; use those tools as needed instead of hand-writing final
  bridge `job.json`.

## Startup

For every `nv-researcher` project wake:

1. Read `<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md`.
2. Read the current project's `brief.md`, `human_advice.md`, and
   `work/state.md`.
3. Use compact wake state, `next_action`, blocker ids, and latest evidence
   pointers from the wake prompt.
4. Use the Memory Index in `NV_RESEARCH_MEMORY.md` to read only relevant
   sections of `<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md`.
5. Treat broad `AGENTS.md` files and detailed docs as on-demand references,
   not routine startup context.

Durable project records should be plain English and preferably ASCII. Japanese
is fine for user-facing chat and notification_service reports.

## New Project

Start projects from the human request without pre-translating it into a detailed
scientific backlog:

```bash
python3 <OPENCLAW_WORKSPACE>/nv_project_manager.py start-project \
  --project-id <id> \
  --objective '<objective>' \
  --human-request '<verbatim human request>' \
  --sample-id NV23
```

`start-project` creates the simple research-state tree: `brief.md`,
`work/state.md`, `work/notes/`, `work/bridge_jobs/`, and `.manager/`. Let
`nv-researcher` author or update the research agenda/backlog after reading the
project context. Operational logs, advice inboxes, and generated artifacts may
exist as support files, but they are not the research-plan surface.

## Continuing Work

The normal scheduler is:

```bash
<OPENCLAW_WORKSPACE>/nv_project_cron_runner.sh --pretty
```

For an immediate project wake:

```bash
<OPENCLAW_WORKSPACE>/nv_project_cron_runner.sh \
  --project-id <id> \
  --force \
  --force-wake \
  --pretty
```

The default project-execution route is the OpenClaw Gateway `/hooks/agent` path
with `agentId=nv-researcher`, `model=openai-codex/gpt-5.5`, and
`thinking=xhigh`, unless the runner or project explicitly overrides it. Use
project-scoped session keys of the form
`agent:nv-researcher:hook:nv-project-manager:<project_id>`.

## Work Loop

Treat `next_action` and backlog items as state pointers, not complete research
plans and not one-item stopping points.

Use a same-wake runnable work loop:

- choose the next safe grounded project task from objective, evidence, human
  advice, policy, and bridge state;
- complete or update it;
- record the evidence/decision;
- continue into the next runnable task while policy, bridge state, evidence,
  and time budget permit.

Stop only at a real stop condition: bridge queued/running blocks the next
bridge-touching item and no useful bridge-free work remains, a bridge
validate/dry_run/execute rejection, an unmaterializable payload, a real external
blocker, exhausted runnable work, or a high-risk change outside policy.

During a running execute, do useful bridge-free project work when grounded:
analysis, model calculations/simulations, literature/PDF review, evidence-gap
closure, notes, figures, tables, or interpretation updates. Do not mutate the
bridge queue or stop/mark terminal a running job without terminal or hard
anomaly evidence.

## Project Memory

- `work/state.md`: compact project state, candidate findings, final claims,
  decisions, and next pointers.
- `work/bridge_jobs/`: bridge-execution contract JSON only.
- `work/notes/`: one small note per meaningful analysis, calculation,
  experiment decision, check, review, or failed idea.
- `.manager/evidence.jsonl`: append-only evidence/artifact registry.
- `log.md`: human research notebook, not just a machine audit log.

Register important artifacts when useful:

```bash
python3 <OPENCLAW_WORKSPACE>/nv_project_manager.py record-evidence \
  --project-id <id> \
  --category <category> \
  --summary '<summary>' \
  --path <artifact>
```

If a reusable detailed NV lesson is learned, update
`<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md` in the relevant
section with a concise dated note and provenance pointer. Update
`NV_RESEARCH_MEMORY.md` only for every-wake priority, hard safety, routing, or
digest changes.

## Bridge And Safety

For new bridge-touching experiments, write scientific intent first, then verify
hard safety/queue gates:

```bash
python3 <OPENCLAW_WORKSPACE>/nv_project_manager.py queue-experiment-intent \
  --project-id <id> \
  --intent-json '<json object>'

python3 <OPENCLAW_WORKSPACE>/nv_project_manager.py verify-experiment-intent \
  --project-id <id> \
  --intent-id <intent_id>
```

The verifier is not a scientific planner, and a verified intent is not itself a
bridge job. It checks hard constraints such as queue state and safety policy.

Pulsed ODMR refresh work should not put `analysis.fit_kind` into ordinary
bridge/batch jobs. Use the terminal savedexperiment raw export plus plot as the
first evidence handoff. If a downstream center is needed, require
raw/readout-aware review plus a transparent task-specific analysis or model
comparison with recorded assumptions, artifacts, and provenance.

Standalone Imaging and TrackCenter use the dedicated direct helper rather than
manifest-backed sequence submission:

```bash
python3 <OPENCLAW_WORKSPACE>/enqueue_nv_imaging_direct.py scan ...
python3 <OPENCLAW_WORKSPACE>/enqueue_nv_imaging_direct.py track ...
```

## Requests And Blockers

- Code changes: queue a structured `queue-code-change-request`; stay within
  `allowed_write_scopes`; complete with `complete-code-change-request`.
- Physical actions: queue a structured `queue-physical-request`; complete with
  `complete-physical-request`.
- Procurement gaps: write a proposal under the project `procurement/` tree.
- If `next_action.kind` is `blocked`, `blocked_external`, or `blocked_code`, do
  not run experiments until the relevant blocker is resolved.

Instrument drivers, legacy GUI, safety-policy edits, execute-gate changes, and
manifest safety-limit changes require explicit human review. Low-risk WSL-side
analysis/orchestration edits may resume after allowed-scope and passed
verification evidence when project policy permits.

## Literature

Use the local paper library first when relevant:

- `<OPENCLAW_WORKSPACE>/literature/`
- `<OPENCLAW_WORKSPACE>/literature/INDEX.md`

If the local library is not enough for a specific research question, model
choice, interpretation, or experiment-design decision, perform a targeted web
literature search when web/search tools are available. Prefer primary sources:
papers, arXiv records, publisher pages, DOI records, and official datasets. If
a useful paper is accessible, save the PDF or bibliographic metadata under
`literature/` when permitted, update `literature/INDEX.md` when practical, and
record the query/source plus decision-relevant takeaway in project notes or
reusable knowledge.

## Completion

Before ending every cron-triggered project-execution wake:

1. Update durable project state that changed.
2. Keep `work/state.md` current when interpretation, candidate findings, final
   claims, decisions, open questions, or next-experiment implications changed.
3. Write a concise human-facing lab log entry when useful:
   `python3 <OPENCLAW_WORKSPACE>/nv_project_manager.py record-lab-log --project-id <id> --title '<title>' --summary '<summary>'`.
4. Write the JSON completion marker at the exact `Agent completion marker` path
   from the wake prompt as the final handoff.

Ledger, backlog, lab log, and task notes show progress, but they do not replace
the required completion marker.

## On-Demand Reference

Read `<OPENCLAW_WORKSPACE>/docs/nv_project_manager_full_reference.md`
when you need:

- full command examples;
- compatibility hook details for `nv-result`, `nv-recovery`,
  `nv-direct-recovery`, `nv-request-resolve`, or `nv-measurement-plan`;
- detailed route policy examples;
- LaTeX closeout/report details;
- unusual legacy behavior.

## Output

When reporting project-manager work, include only the useful essentials:

- `project_id`
- `project_dir`
- `next_action.kind`
- blocker or code-change request id, if any
- evidence, queue action, lab log, figure, or completion marker written

Keep final messages concise. The durable state lives in the project files.
