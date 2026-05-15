OpenClaw project wake from cron.

Use the NV project manager skill at <OPENCLAW_WORKSPACE>/skills/nv-project-manager/SKILL.md. Assume the project-execution agent is a Codex API agent with gpt-5.5/xhigh unless configuration says otherwise. Treat the agent as the research planner: Python provides state, queue safety, audit logging, and hard hardware/code safety boundaries, not a full scientific plan. Advance the project autonomously when evidence and policy are sufficient.

Project id: nv23_aligned_nv_t2star_13c_image145844_20260513_1507
Project dir: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507
Shared NV startup memory: <OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md
Detailed NV research knowledge: <OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md
Lab log: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md
Figure root: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures
Human advice: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/human_advice.md
Advice inbox: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/advice/inbox
Research state: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/state.md
Bridge jobs: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/bridge_jobs
Evidence index: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/.manager/evidence.jsonl
Experiment intents: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/experiment_intents
Work notes: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/notes
Agent completion marker: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/.manager/agent_runs/tick_000092_ed793b01dd1a155c_project.done.json
Agent backend: openclaw-hook
Agent id override: nv-researcher
Agent session key: agent:nv-researcher:hook:nv-project-manager:nv23_aligned_nv_t2star_13c_image145844_20260513_1507:wake:ticked-000092-ed793b01dd1a155c
Agent model override: openai-codex/gpt-5.5
Agent thinking override: xhigh
Completion marker contract: when an Agent completion marker path is provided, writing that marker is the required handoff that tells cron this wake is finished. Ledger, backlog, log.md, or work/task updates show progress but do not by themselves release the in-flight wake. Do not rely on manager fallback auto-markers. If you stop for any reason, including no more useful work, bridge running, external blocker, after submitting a long-running execute, after queueing a not-yet-runnable next item, or after completing the current useful work, write the marker as your final action. The marker JSON must include project_id, completed_at, status, summary, touched_bridge_queue, next_action, and updated_backlog_item_ids (use [] when none were updated).
Cron state path: <OPENCLAW_WORKSPACE>/.openclaw/project_cron/nv23_aligned_nv_t2star_13c_image145844_20260513_1507.json
Project lifecycle: active
Operational state: active
Legacy status: active
Wake intent: continue project work
Work pointer JSON:
{
  "kind": "advance_project",
  "reason": "execution queue is empty; wake the agent to synthesize or update the research agenda and advance all currently runnable safe project work from objective, evidence, human advice, and safety policy",
  "research_context": {
    "brief_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/brief.md",
    "research_state_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/state.md",
    "research_agenda_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/state.md",
    "shared_research_memory_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md",
    "shared_research_knowledge_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md",
    "evidence_index_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/.manager/evidence.jsonl",
    "experiment_intents_root": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/experiment_intents",
    "evidence_count": 96,
    "recent_evidence": [
      {
        "actor": "openclaw-project-manager",
        "category": "figure",
        "evidence_id": "figure_20260514_091311_639663_c97b493627",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_autosave_18avg_review_20260514_0908.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {
          "daily_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "ledger_event": "lab_log_note"
        },
        "related_claims": [],
        "schema_version": 1,
        "source": "record-lab-log",
        "summary": "Refreshed-center Ramsey 18-average autosave review: In-progress refreshed-center r03 Ramsey autosave review while nv23_ramsey_20260514_055148_auto_ramsey is running: 18/20 averages, 900000 shots/tau, final-count text Final = 44.555 kcps, monitor last_error empty, stop_requested=false. Raw export axis contract verified; scan-order-aware drift used Scan.ScanOrderEachAvg/snake and flagged no averages. Full-span and skip-first-4-tau ratio LS screens are currently high-edge dominated near 2.25 MHz; programmed-carrier ratio amplitude 0.01520, expected 13C sideband amplitudes 0.00277/0.00960, and old 1.192 MHz artifact-control amplitude 0.00034; per-average tops remain mixed. Nonterminal progress context only; no T2star or 13C claim.",
        "tags": [],
        "timestamp": "2026-05-14T09:13:11"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "analysis",
        "evidence_id": "image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_raw_export_20260514_0938.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_drift_20260514_0938.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/review_refreshed_center_ramsey_terminal_20260514_0930.py",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/synthesize_refreshed_center_ramsey_terminal_20260514_0945.py"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {},
        "related_claims": [
          "pending_T2star",
          "nearby_13C_negative_under_ramsey_conditions"
        ],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Terminal refreshed-center r03 Ramsey review: job nv23_ramsey_20260514_055148_auto_ramsey completed normally with final_counts_kcps=43.433, 20/20 averages, 1.0e6 shots/tau, axis contract verified, scan-order-aware drift source Scan.ScanOrderEachAvg/snake with no flagged averages. Full/skip-transient LS screens are high-edge dominated near 2.266-2.276 MHz; programmed 1.5 MHz carrier-like component is present but modest (ratio amplitude 0.01575 full, 0.01231 skip-first-4; raw signal LS amp 0.705 kcps below median per-point SEM 0.850 kcps). Expected 13C sideband amplitudes at 1.115/1.885 MHz are 0.00278/0.00962 ratio and do not form a coherent symmetric sideband claim. Bootstrap/model comparison prefers a high-edge component over fixed carrier (carrier model delta BIC ~10; carrier+expected-sidebands delta BIC ~28); fixed-carrier T2star candidates are order 1-3 us but model-dependent. No claim-grade numeric T2star; no supported nearby 13C Ramsey sideband/coupling claim under these conditions.",
        "tags": [
          "ramsey",
          "terminal",
          "t2star",
          "13c",
          "r03",
          "model_comparison"
        ],
        "timestamp": "2026-05-14T09:51:18"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "figure",
        "evidence_id": "figure_20260514_095229_772935_7365c0aae9",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {
          "daily_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "ledger_event": "lab_log_note"
        },
        "related_claims": [],
        "schema_version": 1,
        "source": "record-lab-log",
        "summary": "Refreshed-center Ramsey terminal review: Terminal r03 refreshed-center long-span Ramsey completed normally with final_counts_kcps=43.433, 20/20 averages, 1.0e6 shots/tau, and no scan-order-aware drift flags. Review found a modest programmed 1.5 MHz carrier-like component but high-edge-dominated screens near 2.266-2.276 MHz; fixed-carrier T2star candidates are order 1-3 us but model-dependent and not claim-grade. Expected 13C sidebands at 1.115/1.885 MHz are not a coherent pair, so no supported nearby-13C Ramsey claim under current conditions. Do not run another blind long-span repeat.",
        "tags": [],
        "timestamp": "2026-05-14T09:52:29"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "report",
        "evidence_id": "image145844_reimage_r03_branch_closeout_report_20260514_1000",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/reports/20260514_1000_r03_branch_closeout/image145844_reimage_r03_closeout_report_20260514_1000.pdf",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/reports/20260514_1000_r03_branch_closeout/image145844_reimage_r03_closeout_report_20260514_1000.tex",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/notes/20260514_1000_r03_branch_decision_and_closeout.md"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {},
        "related_claims": [
          "aligned_candidate_r03",
          "no_claim_grade_numeric_T2star",
          "nearby_13C_negative_under_ramsey_conditions"
        ],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Closeout/decision report for image145844_reimage_r03 branch. The report records that r03 is the aligned NV candidate; no claim-grade numeric T2star can be quoted from the completed Ramsey branch; and no supported nearby-13C Ramsey sideband/coupling evidence is resolved under current conditions. No further automatic bridge-touching work is justified without a new explicit protocol-development request.",
        "tags": [
          "closeout",
          "report",
          "r03",
          "t2star",
          "13c",
          "decision"
        ],
        "timestamp": "2026-05-14T10:12:18"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "figure",
        "evidence_id": "figure_20260514_101218_829765_72da82fea4",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {
          "daily_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "ledger_event": "closeout_report"
        },
        "related_claims": [],
        "schema_version": 1,
        "source": "record-lab-log",
        "summary": "r03 branch closeout report prepared: Prepared a verified LaTeX/PDF closeout report for image145844_reimage_r03. Final scoped conclusion: r03 is the aligned NV candidate; no claim-grade numeric T2star can be quoted from the completed Ramsey branch; no supported nearby-13C Ramsey sideband/coupling evidence is resolved under current conditions. No further automatic bridge-touching work is justified unless operator requests a new protocol-development branch.",
        "tags": [],
        "timestamp": "2026-05-14T10:12:18"
      }
    ],
    "experiment_intents": {
      "queued": 0,
      "verified": 0,
      "rejected": 0,
      "done": 17
    },
    "backlog_role": "execution_queue_and_audit_not_complete_research_plan",
    "scheduler_role": "event_state_pointer_agent_selects_scientific_next_step"
  },
  "agent_prompt": "Treat this as an event-driven research wake. Read NV_RESEARCH_MEMORY.md startup memory first, then brief.md, human_advice.md, work/state.md, and compact project state. Use the Memory Index to read relevant sections from NV_RESEARCH_KNOWLEDGE.md only as needed. Read .manager/evidence.jsonl, project policy, detailed backlog entries, and directly relevant evidence only as needed, then use the same-wake runnable work loop to complete, update, or queue all currently runnable safe project work until a real stop condition is reached. Python should stay limited to state, queue safety, audit logs, and hard boundaries; the agent should own the scientific plan. Process advice inbox messages with list-advice-inbox/dispose-advice when present, record evidence, update backlog, write work/state.md, log.md, and work/notes files as useful, update NV_RESEARCH_KNOWLEDGE.md for reusable detailed lessons, and write the completion marker."
}

Project context JSON:
{
  "objective": "Find a magnetic-field-aligned NV from image145844, then obtain a well-supported T2star and 13C conclusion.",
  "sample_id": "NV23",
  "planning_horizon": {},
  "success_metrics": [],
  "shared_research_memory": {
    "path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md",
    "startup_memory_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md",
    "detailed_knowledge_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md",
    "read_required": true,
    "read_required_for": [
      "nv-researcher",
      "nv_project_work",
      "nv-project-manager"
    ],
    "read_policy": "read_startup_memory_every_wake; read_detailed_knowledge_sections_on_demand_by_memory_index",
    "scope": "compact_startup_contract_and_detailed_nv_knowledge_router",
    "source": "NV_RESEARCH_MEMORY.md",
    "detailed_source": "NV_RESEARCH_KNOWLEDGE.md",
    "exists": true,
    "updated_epoch": 1778696197.4189858,
    "size_bytes": 16328,
    "snapshot_char_limit": 16000,
    "snapshot_truncated": true,
    "snapshot": "# NV Research Memory\n\nCompact every-wake contract for NV project-execution agents.\n\nThis file is separate from `MEMORY.md`. Direct-chat sessions may use\n`MEMORY.md`; `nv-researcher` project wakes use this file as startup policy and\nrouter. Detailed NV practice lives in\n`<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md` and should be read\nby relevant section only.\n\n## Core Wake Contract\n\nOn every NV project wake, read:\n\n- This file.\n- The current project's `brief.md`, `human_advice.md`, and `work/state.md`.\n- Compact state, wake reason, `next_action`, blocker ids, and latest evidence\n  pointers supplied by the scheduler.\n\nDo not routinely read broad `AGENTS.md` files. Consult them only for visible\ncode/policy conflicts, explicit wake instructions, or hardware/protocol/code\nquestions.\n\nConflict priority:\n\n1. Explicit human `STOP`, pause, cancel, do-not-continue, or must-first\n   instructions.\n2. Hard bridge queue, hardware, code-safety, manifest, execute, and local lab\n   opt-in gates.\n3. Current project `human_advice.md`.\n4. Current project brief, state, compact state, and latest evidence.\n5. This file.\n6. Historical examples and optional references.\n\nRule strengths:\n\n- `HARD`: fail-closed. Includes STOP/pause/cancel orders, queue mutation rules,\n  hardware/code/manifest/execute uncertainty, local lab opt-in, and completion\n  markers.\n- `DEFAULT`: normal lab practice. Follow unless current evidence or human advice\n  justifies a safer, more specific choice.\n- `SOFT`: scientific interpretation guidance. Use for caveats, provenance,\n  finding scope, and follow-up design; do not make it an external blocker by\n  itself.\n- `PROVENANCE`: evidence used for reasoning. Not a hard gate by itself.\n- `HISTORICAL`: old context. Do not revive as current policy without a specific\n  reason.\n\n## Hard Safety Baseline\n\n- Do not submit, mutate, stop, or mark terminal any bridge job unless the bridge\n  queue/running state and requested action satisfy the bridge policy.\n- Bridge occupancy blocks new bridge-touching submission or queue mutation.\n  Bridge-free analysis, notes, planning, and evidence cleanup may continue.\n- Hardware/safety uncertainty, non-trackable manual apparatus uncertainty,\n  code-safety uncertainty, manifest-limit uncertainty, missing local lab opt-in,\n  or execute-gate failure blocks the affected action.\n- Before materializing a new bridge-touching experiment, prefer an\n  agent-authored experiment intent and parse the verifier JSON verdict. A zero\n  process return code is not enough if the JSON verdict is blocked.\n- Preserve the MATLAB bridge safety model. Do not widen hardware limits,\n  manifest limits, execute gates, or instrument-driver behavior from an NV\n  project wake.\n- Before ending any cron-triggered project-execution wake, write the required\n  JSON completion marker at the exact path from the wake prompt.\n\n## Working Defaults\n\n- Treat prior conclusions as hypotheses, not facts; re-check primary evidence\n  before building further decisions on them.\n- `next_action` is a state pointer, not the full research plan. Python owns\n  durable state, queue safety, audit logs, wake pacing, and hard safety gates.\n  The agent owns research judgment, chunk planning, evidence synthesis,\n  literature/prior-result comparison, pulse-sequence protocol inspection, and\n  experiment design.\n- Use a same-wake runnable work loop. Continue safe grounded project work until\n  bridge state, hard gates, real external blockers, exhausted runnable work, or\n  the required handoff stops the wake.\n- From current experiment data, calculation/analysis results, and literature\n  findings, form scientific hypotheses and then perform or plan experiments,\n  calculations/analysis, and literature review to test them.\n- For signals observed in experiment results, evaluate whether they plausibly\n  arise from a physical phenomenon or from apparatus artifacts, analysis\n  artifacts, or noise.\n- The 23-C quick starter PDF is available to OpenClaw agents at\n  `<OPENCLAW_WORKSPACE>/docs/Quick_Starter_Guide.pdf`.\n- Current 23-C setup context: the Tektronix AWG5014B has been replaced by two\n  Siglent SDG6032X units; experiments use the `ms = +1` transition; the DC\n  magnetic field corresponds to resonance near 3.875 GHz.\n- Current setup contrast reference: photoluminescence contrast between\n  `m_S = 0` and `m_S = +1` is about 22%; use measurement-specific expected\n  contrast when deciding signal presence.\n- When judging a candidate signal, compare the observed effect size with the\n  measurement-specific expected contrast; features far below the expected\n  contrast need stronger supporting evidence before being promoted.\n- Also compare the observed effect size with its noise/uncertainty; low-SNR\n  features need stronger supporting evidence before being promoted.\n- Readout roles are sequence-dependent; inspect the actual XML before\n  interpreting reference/signal channels. Signal contrast can be evaluated from\n  the signal readout alone, relative to its own off-resonant or fitted baseline;\n  reference normalization is not required to obtain signal contrast. Use\n  reference-based normalization mainly for drift correction and plotting.\n  Normalization amplifies noise and denominator artifacts. When using\n  normalization, evaluate and record both required views: point-wise\n  normalization and normalization against a fitted line or curve to the\n  reference readout. Compare both with raw readouts to capture slow\n  reference/baseline variation from drift without adding more noise.\n- Do not use point-wise normalization values as the signal-presence criterion.\n  Do not treat normalization-only features as candidate physical signals.\n- Keep candidate signal presence, physical interpretation, and derived\n  parameter claims separate.\n- Calibration/scout are usually fine at `2e5-3e5` total shots. Use at least\n  `2e5` total shots to secure minimum SNR. Cleaner\n  quantitative data can require more than `2e5-3e5` total shots, and\n  publication-quality data generally requires at least `1e6` total shots,\n  because this setup has error sources beyond shot noise, including drift and\n  laser-power fluctuations.\n- The experiment code has also been substantially revised for the two-Siglent\n  route; do not assume old Tektronix AWG5014B code paths or timing behavior are\n  protocol-equivalent to the current setup without inspecting the active code\n  and sequence XML/manifest.\n- For this setup, use the working approximation that Rabi frequency is about\n  10 MHz at `mod_depth = 1` and scales approximately linearly with `mod_depth`.\n- External blocking is only for cases where progress requires a human, robot, or\n  other physical-world action, or where hardware/safety/queue/code uncertainty\n  makes an action unsafe. Scientific uncertainty should be handled by the agent.\n- After meaningful evidence review, terminal results, model comparison, or\n  bridge-free synthesis, update Current Findings with what is supported, useful\n  for the next decision, downgraded, unresolved, and what evidence would change\n  the finding.\n- Always establish the expected signal from the relevant physical model before\n  planning or interpreting measurements; always perform a simulation or explicit\n  model calculation. When experiment results disagree with the current model,\n  consider revising the model or explicitly record why it is being kept.\n- Always assess whether the expected signal from the relevant physical model\n  should be distinguishable from noise/uncertainty.\n- First decide whether a signal is present from raw/readout-aware evidence; fit\n  only after signal presence is supported, using an appropriate physical or\n  empirical function for that measurement type. Use the fit-derived value\n  downstream only if the fit remains consistent with the data shape and baseline\n  behavior.\n- Stored averages are often primarily a tracking cadence, not a strong\n  independent-repeatability test; do not overweight average-to-average agreement\n  unless repetitions per average are large enough for that comparison.\n- Recent-average drift under snake scan order is advisory provenance. Do not\n  stop, wake, or block solely for drift flags. Stop only for hard anomalies such\n  as tracking loss, count collapse, hardware/safety uncertainty, explicit STOP,\n  or monitor errors that make continuing unsafe.\n- On drift, count collapse, TrackCenter failure, imaging-frame shift, or\n  resonance shift, check TSP01 logs and record temp/RH deltas as provenance.\n- For snake-ordered scans with stored averages, use an even number of averages\n  by default so forward and reverse acquisition directions are balanced. If an\n  odd average count is intentionally used, record the explicit exception reason.\n- Use recent drift-score evidence, including usable measurement-derived drift\n  scores from the last 1 hour when available, and the MATLAB/OpenClaw advisory\n  when choosing repetitions, averages, and scan points. Cite the last-hour drift\n  evidence in the plan when it affects the choice. Good drift can justify a\n  longer per-average window only within the active advisory cap. If the advisory\n  estimated per-average/tracking window exceeds the cap, revise before execute:\n  reduce repetitions per average and/or scan points first, raise averages only\n  when doing so preserves useful total shots without violating the cap, and\n  reduce total shots when the task is a screening/triage measurement that does\n  not require precision. Drift conditions continuously change; do not blindly\n  reuse averages/repetitions from past data without reassessing current drift\n  evidence and advisory caps.\n- Consider drift before relying on saved Imaging positions. If the sample or\n  focus may have moved enough that the saved image no longer points to the\n  current target locations, repeat Imaging or run an expanded re-image before\n  using those positions.\n- If TrackCenter fails repeatedly from saved or image-derived seeds, suspect\n  that drift has shifted the Imaging frame relative to the current target\n  locations. Re-image before treating the candidate as absent or non-trackable.\n- Quantitative follow-up guidance applies only after prerequisite\n  signal/resonance evidence is established. Do not use it to rescue failed\n  signal-presence.\n- For substantive scientific decisions and experiment-result interpretation,\n  compare current evidence with relevant literature and this lab's past data\n  before finalizing the next scientific decision or interpretation. Use a\n  targeted web literature search when needed to keep the\n  comparison current and well sourced. Prefer primary sources and record the\n  search queries, sources, and decision-relevant takeaway used.\n- For pulse-sequence-dependent plans or scientific statements, inspect the\n  actual sequence XML/manifest, active instruction path, timing definitions,\n  typed/boolean variables, comments/disabled blocks, saved metadata, and\n  readout roles before relying on shortcut names or stating protocol parity.\n- Use targeted evidence access. Start from compact state and latest pointers;\n  read large logs by tail or id/keyword search.\n- Durable project notes, advice records, backlog text, completion markers, and\n  other machine-consumed records should be plain English and preferably ASCII.\n  User-facing chat and notification_service reports may be Japanese.\n\n## Memory Index\n\nUse this router for `NV_RESEARCH_KNOWLEDGE.md`:\n\n- `Shared Literature`: web literature search, papers, DOI/arXiv/publisher\n  pages, local paper library, prior-result comparison, Hamiltonian/model\n  interpretation, coupling extraction, old hardware assumptions.\n- `Experiment Defaults`: sequence defaults, strong-pi pulsed ODMR, resonance\n  validity, Rabi/weak-pi, CPMG/Hahn/XY8/DDRF, XML/protocol\n  inspection, weak signal follow-up.\n- `Drift, Tracking, And Environment`: Imaging, TrackCenter, usual NV/NV23\n  identity, nearby-NV recovery, position freshness, TSP01/environment drift,\n  count/tracking interpretation.\n- `Shot Budget And Data Quality`: shot credit, SEM scaling, stored averages,\n  visual review, fit validity, snake scan, recent-average drift.\n- `OpenClaw Project Operation`: route policy, same-wake work, running-execute\n  bridge-free work, project layout, advice inbox, verifier verdicts, WSL\n  canonical state, Imaging/TrackCenter helpers, queue staging, completion\n  markers, code auto-resume, notification_service reports/media.\n- `Research Practice And Closeout`: literature/prior-result comparison,\n  non-experiment findings that affect design, LaTeX closeout reports, manual\n  experiment evidence.\n\n## Wake Digest\n\n- `HARD`: Human STOP/pause/cancel/must-first instructions and bridge/hardware/\n  code/manifest/execute failures override autonomy.\n- `HARD`: Parse verifier JSON before enqueue; return code alone is insufficient.\n- `HARD`: Every cron-triggered wake must write the completion marker.\n- `HARD`: Before planning or interpreting any measurement, establish the\n  expected signal from the relevant physical model and always perform a\n  simulation or explicit quantitative model calculation. Qualitative\n  expected-signal prose is not a model calculation. If this is missing, do not\n  enqueue the measurement or promote the interpretation.\n- `HARD`: Design each measurement from a simulation or explicit quantitative\n  model so the target effect should be distinguishable from noise/uncertainty.\n  Before enqueue, record the expected effect size/scale, the chosen scan range,\n  spacing, repetitions/averages, and why those settings should make the effect\n  visible. If the target effect is not expected to be resolvable, redesign the\n  measurement before enqueue.\n- `DEFAULT`: Do not put automatic fit requests such as `analysis.fit_kind` into\n  ordinary bridge jobs. Use terminal savedexperiment raw export plus plots\n  first.\n- `DEFAULT`: For substantive scientific decisions and experiment-result\n  interpretation, compare current evidence with relevant literature and this\n  lab's past data before finalizing the next scientific decision or\n  interpretation. Web-search the literature as needed to make that comparison\n  current and well sourced.\n- `DEFAULT`: Inspect actual sequence XML/manifest content before protocol-based\n  plans or scientific statements.\n- `SOFT`: Use SEM/SEM-scaling only when planning or reviewing long acquisitions\n  intended to improve statistics by accumulating more shots.\n- `HARD`: Under snake scan order, use even average counts by default and\n  record any odd-count exception. Tune repetitions, averages, and scan points\n  from recent drift scores, including last-hour measurement-derived drift scores\n  when available, plus advisory drift risk. Good drift can justify a longer\n  per-average window only within the active advisory cap; if the advisory\n  exceeds that cap, revise before execute by reducing repetitions per average\n  and/or scan points before considering a capped, shot-preserving average split.\n  Drift conditions continuously change; do not blindly reuse averages/\n  repetitions from past data without reassessing current drift evidence and\n  advisory caps.\n- `HARD`: Consider drift before relying on saved Imaging positions. If the\n  sample or focus may have moved enough that the saved image no longer points to\n  the current target locations, repeat Imaging or run an expanded re-image\n  before using those positions.\n- `HARD`: If TrackCenter fails repeatedly from saved or image-derived seeds,\n  suspect Imaging-frame drift and re-image before treating the candidate as\n  absent or non-trackable.\n- `HARD`: Do not infer or transpose SavedImages axes from array shape. Python\n  image analysis must use an explicit `ImageData_YXZ`/`axis_order` contract\n  before candidate coordinates are used for TrackCenter.\n- `PROVENANCE`: Usual-NV/NV23 labeled imaging/tracking data informs identity and\n  seed choice, but TrackCenter counts alone do not prove identity.\n- `DEFAULT`: WSL project state is canonical. New projects use the simple\n  research-s",
    "detailed_knowledge_exists": true,
    "detailed_knowledge_updated_epoch": 1778696274.0995097,
    "detailed_knowledge_size_bytes": 29942
  },
  "autonomy": {},
  "research_context": {
    "brief_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/brief.md",
    "research_state_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/state.md",
    "research_agenda_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/state.md",
    "shared_research_memory_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md",
    "shared_research_knowledge_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md",
    "evidence_index_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/.manager/evidence.jsonl",
    "experiment_intents_root": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/experiment_intents",
    "evidence_count": 96,
    "recent_evidence": [
      {
        "actor": "openclaw-project-manager",
        "category": "figure",
        "evidence_id": "figure_20260514_091311_639663_c97b493627",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_autosave_18avg_review_20260514_0908.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {
          "daily_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "ledger_event": "lab_log_note"
        },
        "related_claims": [],
        "schema_version": 1,
        "source": "record-lab-log",
        "summary": "Refreshed-center Ramsey 18-average autosave review: In-progress refreshed-center r03 Ramsey autosave review while nv23_ramsey_20260514_055148_auto_ramsey is running: 18/20 averages, 900000 shots/tau, final-count text Final = 44.555 kcps, monitor last_error empty, stop_requested=false. Raw export axis contract verified; scan-order-aware drift used Scan.ScanOrderEachAvg/snake and flagged no averages. Full-span and skip-first-4-tau ratio LS screens are currently high-edge dominated near 2.25 MHz; programmed-carrier ratio amplitude 0.01520, expected 13C sideband amplitudes 0.00277/0.00960, and old 1.192 MHz artifact-control amplitude 0.00034; per-average tops remain mixed. Nonterminal progress context only; no T2star or 13C claim.",
        "tags": [],
        "timestamp": "2026-05-14T09:13:11"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "analysis",
        "evidence_id": "image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_raw_export_20260514_0938.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_drift_20260514_0938.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/review_refreshed_center_ramsey_terminal_20260514_0930.py",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/synthesize_refreshed_center_ramsey_terminal_20260514_0945.py"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {},
        "related_claims": [
          "pending_T2star",
          "nearby_13C_negative_under_ramsey_conditions"
        ],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Terminal refreshed-center r03 Ramsey review: job nv23_ramsey_20260514_055148_auto_ramsey completed normally with final_counts_kcps=43.433, 20/20 averages, 1.0e6 shots/tau, axis contract verified, scan-order-aware drift source Scan.ScanOrderEachAvg/snake with no flagged averages. Full/skip-transient LS screens are high-edge dominated near 2.266-2.276 MHz; programmed 1.5 MHz carrier-like component is present but modest (ratio amplitude 0.01575 full, 0.01231 skip-first-4; raw signal LS amp 0.705 kcps below median per-point SEM 0.850 kcps). Expected 13C sideband amplitudes at 1.115/1.885 MHz are 0.00278/0.00962 ratio and do not form a coherent symmetric sideband claim. Bootstrap/model comparison prefers a high-edge component over fixed carrier (carrier model delta BIC ~10; carrier+expected-sidebands delta BIC ~28); fixed-carrier T2star candidates are order 1-3 us but model-dependent. No claim-grade numeric T2star; no supported nearby 13C Ramsey sideband/coupling claim under these conditions.",
        "tags": [
          "ramsey",
          "terminal",
          "t2star",
          "13c",
          "r03",
          "model_comparison"
        ],
        "timestamp": "2026-05-14T09:51:18"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "figure",
        "evidence_id": "figure_20260514_095229_772935_7365c0aae9",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {
          "daily_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "ledger_event": "lab_log_note"
        },
        "related_claims": [],
        "schema_version": 1,
        "source": "record-lab-log",
        "summary": "Refreshed-center Ramsey terminal review: Terminal r03 refreshed-center long-span Ramsey completed normally with final_counts_kcps=43.433, 20/20 averages, 1.0e6 shots/tau, and no scan-order-aware drift flags. Review found a modest programmed 1.5 MHz carrier-like component but high-edge-dominated screens near 2.266-2.276 MHz; fixed-carrier T2star candidates are order 1-3 us but model-dependent and not claim-grade. Expected 13C sidebands at 1.115/1.885 MHz are not a coherent pair, so no supported nearby-13C Ramsey claim under current conditions. Do not run another blind long-span repeat.",
        "tags": [],
        "timestamp": "2026-05-14T09:52:29"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "report",
        "evidence_id": "image145844_reimage_r03_branch_closeout_report_20260514_1000",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/reports/20260514_1000_r03_branch_closeout/image145844_reimage_r03_closeout_report_20260514_1000.pdf",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/reports/20260514_1000_r03_branch_closeout/image145844_reimage_r03_closeout_report_20260514_1000.tex",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/notes/20260514_1000_r03_branch_decision_and_closeout.md"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {},
        "related_claims": [
          "aligned_candidate_r03",
          "no_claim_grade_numeric_T2star",
          "nearby_13C_negative_under_ramsey_conditions"
        ],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Closeout/decision report for image145844_reimage_r03 branch. The report records that r03 is the aligned NV candidate; no claim-grade numeric T2star can be quoted from the completed Ramsey branch; and no supported nearby-13C Ramsey sideband/coupling evidence is resolved under current conditions. No further automatic bridge-touching work is justified without a new explicit protocol-development request.",
        "tags": [
          "closeout",
          "report",
          "r03",
          "t2star",
          "13c",
          "decision"
        ],
        "timestamp": "2026-05-14T10:12:18"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "figure",
        "evidence_id": "figure_20260514_101218_829765_72da82fea4",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_ramsey_refreshed_center_terminal_model_comparison_20260514_0948.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image145844_20260513_1507",
        "provenance": {
          "daily_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/log.md",
          "ledger_event": "closeout_report"
        },
        "related_claims": [],
        "schema_version": 1,
        "source": "record-lab-log",
        "summary": "r03 branch closeout report prepared: Prepared a verified LaTeX/PDF closeout report for image145844_reimage_r03. Final scoped conclusion: r03 is the aligned NV candidate; no claim-grade numeric T2star can be quoted from the completed Ramsey branch; no supported nearby-13C Ramsey sideband/coupling evidence is resolved under current conditions. No further automatic bridge-touching work is justified unless operator requests a new protocol-development branch.",
        "tags": [],
        "timestamp": "2026-05-14T10:12:18"
      }
    ],
    "experiment_intents": {
      "queued": 0,
      "verified": 0,
      "rejected": 0,
      "done": 17
    },
    "backlog_role": "execution_queue_and_audit_not_complete_research_plan",
    "scheduler_role": "event_state_pointer_agent_selects_scientific_next_step"
  },
  "budgets": {},
  "stop_conditions": []
}

Blocking ids:
- none

Operating rules:
- Read NV_RESEARCH_MEMORY.md first. It is the every-wake startup memory; its `Core Wake Contract` is the canonical startup, priority, safety, and context-routing policy for nv-researcher.
- Use its Memory Index to decide which relevant sections, if any, to read from NV_RESEARCH_KNOWLEDGE.md. Do not read the detailed knowledge file in full by default.
- Routine startup context is intentionally compact: NV_RESEARCH_MEMORY.md, brief.md, human_advice.md, work/state.md, the Work pointer JSON, Project context JSON, blocker ids, and latest evidence pointers in this prompt.
- Do not routinely read <MATLAB_23C_ROOT>/AGENTS.md or the OpenClaw workspace AGENTS.md for project wakes. Consult AGENTS/protocol docs only for visible code/policy conflicts, code or hardware/protocol editing, explicit wake instructions, or specific compact-state pointers.
- Treat `next_action` as a state pointer or blocker, not a complete scientific plan and not a one-item stopping point. Use the same-wake runnable work loop: pick the next safe grounded project task from the required project context, read relevant NV_RESEARCH_KNOWLEDGE.md sections/evidence only as needed, complete or update the task, then continue to the next runnable task until a real stop condition is reached.
- Python owns durable state, queue safety, audit logs, wake pacing, and hard hardware/code safety boundaries. The agent owns research judgment, evidence synthesis, chunk planning, and experiment-design reasoning.
- For bridge-touching work, obey the Core Wake Contract: write/verify an experiment intent when appropriate, require queue idle before submission or mutation, preserve MATLAB bridge safety gates, and never widen hardware or manifest safety limits.
- During running executes, first check terminal/anomaly evidence, then do useful bridge-free project work when grounded. Do not mutate the bridge queue or stop/mark terminal without terminal or hard-anomaly evidence.
- Keep work/state.md current when interpretation, candidate findings, final claims, decisions, open questions, or next-experiment implications change. Register important artifacts and write focused work/notes or lab-log entries when useful.
- If this wake produces a reusable detailed NV lesson, update NV_RESEARCH_KNOWLEDGE.md in the relevant section with a concise dated note and source/provenance pointer. Keep transient project state in the project work tree; update NV_RESEARCH_MEMORY.md only for every-wake priority, hard safety, routing, or digest changes.
- Process advice inbox only to find unprocessed advice; `human_advice.md` is the effective human guidance after interpretation/disposal.
- Use the same-wake runnable work loop to make as much grounded project progress as safely possible: complete/update the current item, queue the next safe runnable item when needed, and continue immediately while policy, bridge state, evidence, and time budget permit.
- Always write the required JSON completion marker at the Agent completion marker path before ending a cron-triggered wake. Include project_id, completed_at, status, summary, touched_bridge_queue, next_action, and updated_backlog_item_ids (use [] when none were updated). Ledger, backlog, log, or notes updates are not a substitute.
