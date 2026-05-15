OpenClaw project wake from cron.

Use the NV project manager skill at <OPENCLAW_WORKSPACE>/skills/nv-project-manager/SKILL.md. Assume the project-execution agent is a Codex API agent with gpt-5.5/xhigh unless configuration says otherwise. Treat the agent as the research planner: Python provides state, queue safety, audit logging, and hard hardware/code safety boundaries, not a full scientific plan. Advance the project autonomously when evidence and policy are sufficient.

Project id: nv23_aligned_nv_t2star_13c_image231924_20260511_2319
Project dir: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319
Shared NV startup memory: <OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md
Detailed NV research knowledge: <OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md
Lab log: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/log.md
Figure root: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures
Human advice: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/human_advice.md
Advice inbox: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/advice/inbox
Research state: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/state.md
Bridge jobs: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs
Evidence index: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/.manager/evidence.jsonl
Experiment intents: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/experiment_intents
Work notes: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/notes
Agent completion marker: <OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/.manager/agent_runs/tick_000023_27d74398b60f5cbd_project.done.json
Agent backend: openclaw-hook
Agent id override: nv-researcher
Agent session key: agent:nv-researcher:hook:nv-project-manager:nv23_aligned_nv_t2star_13c_image231924_20260511_2319:wake:ticked-000023-27d74398b60f5cbd
Agent model override: openai-codex/gpt-5.5
Agent thinking override: xhigh
Completion marker contract: when an Agent completion marker path is provided, writing that marker is the required handoff that tells cron this wake is finished. Ledger, backlog, log.md, or work/task updates show progress but do not by themselves release the in-flight wake. Do not rely on manager fallback auto-markers. If you stop for any reason, including no more useful work, bridge running, external blocker, after submitting a long-running execute, after queueing a not-yet-runnable next item, or after completing the current useful work, write the marker as your final action. The marker JSON must include project_id, completed_at, status, summary, touched_bridge_queue, next_action, and updated_backlog_item_ids (use [] when none were updated).
Cron state path: <OPENCLAW_WORKSPACE>/.openclaw/project_cron/nv23_aligned_nv_t2star_13c_image231924_20260511_2319.json
Project lifecycle: active
Operational state: active
Legacy status: active
Wake intent: continue project work
Work pointer JSON:
{
  "kind": "advance_project",
  "reason": "execution queue is empty; wake the agent to synthesize or update the research agenda and advance all currently runnable safe project work from objective, evidence, human advice, and safety policy",
  "research_context": {
    "brief_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/brief.md",
    "research_state_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/state.md",
    "research_agenda_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/state.md",
    "shared_research_memory_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md",
    "shared_research_knowledge_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md",
    "evidence_index_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/.manager/evidence.jsonl",
    "experiment_intents_root": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/experiment_intents",
    "evidence_count": 42,
    "recent_evidence": [
      {
        "actor": "openclaw-project-manager",
        "category": "analysis",
        "evidence_id": "analysis_20260512_031721_840657_19692bf40a",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_raw_export.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_drift.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_raw_readouts.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {},
        "related_claims": [],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Narrow weak-pi pODMR after terminal Ramsey completed and reviewed: raw/fit-reference minimum gives updated center 3.8761166667 GHz (+0.250 MHz from prior weak-pi center; pointwise ratio min +0.500 MHz). This makes the old 1.593 MHz Ramsey peak plausibly residual detuning rather than 13C; T2star remains candidate-only pending corrected-center Ramsey.",
        "tags": [],
        "timestamp": "2026-05-12T03:17:21"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "note",
        "evidence_id": "note_20260512_031810_487387_9705802004",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/notes/image231924_c01_narrow_weak_podmr_after_ramsey_review_20260512_0318.md"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {},
        "related_claims": [],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Note for narrow weak-pi pODMR after Ramsey: updated center 3.8761166667 GHz; old 1.593 MHz Ramsey peak likely residual detuning, 13C downgraded pending corrected-center Ramsey.",
        "tags": [],
        "timestamp": "2026-05-12T03:18:10"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "artifact",
        "evidence_id": "artifact_20260512_032618_651713_de6e78654b",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/experiment_intents/verified/image231924_c01_corrected_center_ramsey_repeat_20260512_0320.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_0320.batch_spec.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_0320.batch_state.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute.job_initial.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute.status_initial.json"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {},
        "related_claims": [],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Submitted and started corrected-center Ramsey/T2star repeat: bridge job nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute; pre-enqueue advisory had no blockers, estimated runtime 4479 s and per-average tracking window 742 s under the 900 s night cap; auto-align selected 23.416 kcps and the experiment has started.",
        "tags": [],
        "timestamp": "2026-05-12T03:26:18"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "analysis",
        "evidence_id": "analysis_20260512_040239_706388_8f15704429",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_raw_export.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/analyze_corrected_center_ramsey_autosave_avg2.py",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_per_average.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_raw_readouts.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/notes/image231924_c01_corrected_center_ramsey_autosave_avg2_review_20260512_0359.md"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {},
        "related_claims": [],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "In-progress corrected-center Ramsey autosave after 2/6 averages raw-exported and reviewed: bridge still running with healthy counts (Final = 25.898 kcps), no terminal/anomaly evidence; carrier-nearest FFT bin ranks 3rd while expected lower/upper 13C bins rank 6/23, so this is only progress evidence and T2star/13C remain no-conclusion until terminal review.",
        "tags": [],
        "timestamp": "2026-05-12T04:02:39"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "figure",
        "evidence_id": "figure_20260512_040302_647471_cffab9dc03",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {
          "daily_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/log.md",
          "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/log.md",
          "ledger_event": "lab_log_note"
        },
        "related_claims": [],
        "schema_version": 1,
        "source": "record-lab-log",
        "summary": "Corrected-center Ramsey autosave 2/6 review: At 03:59 EDT the corrected-center Ramsey repeat remained running with 2/6 averages completed and healthy counts (Final = 25.898 kcps). Autosave raw export/review found the carrier-nearest FFT bin ranked 3rd and expected lower/upper 13C bins ranked 6/23; this is progress evidence only, with no T2star or 13C conclusion until terminal review.",
        "tags": [],
        "timestamp": "2026-05-12T04:03:02"
      }
    ],
    "experiment_intents": {
      "queued": 2,
      "verified": 1,
      "rejected": 0,
      "done": 7
    },
    "backlog_role": "execution_queue_and_audit_not_complete_research_plan",
    "scheduler_role": "event_state_pointer_agent_selects_scientific_next_step"
  },
  "agent_prompt": "Treat this as an event-driven research wake. Read NV_RESEARCH_MEMORY.md startup memory first, then brief.md, human_advice.md, work/state.md, and compact project state. Use the Memory Index to read relevant sections from NV_RESEARCH_KNOWLEDGE.md only as needed. Read .manager/evidence.jsonl, project policy, detailed backlog entries, and directly relevant evidence only as needed, then use the same-wake runnable work loop to complete, update, or queue all currently runnable safe project work until a real stop condition is reached. Python should stay limited to state, queue safety, audit logs, and hard boundaries; the agent should own the scientific plan. Process advice inbox messages with list-advice-inbox/dispose-advice when present, record evidence, update backlog, write work/state.md, log.md, and work/notes files as useful, update NV_RESEARCH_KNOWLEDGE.md for reusable detailed lessons, and write the completion marker."
}

Project context JSON:
{
  "objective": "Find a magnetic-field-aligned NV from image231924, then obtain a well-supported T2star and 13C conclusion.",
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
    "updated_epoch": 1778555184.2027516,
    "size_bytes": 15633,
    "snapshot_char_limit": 16000,
    "snapshot_truncated": false,
    "snapshot": "# NV Research Memory\n\nCompact every-wake contract for NV project-execution agents.\n\nThis file is separate from `MEMORY.md`. Direct-chat sessions may use\n`MEMORY.md`; `nv-researcher` project wakes use this file as startup policy and\nrouter. Detailed NV practice lives in\n`<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md` and should be read\nby relevant section only.\n\n## Core Wake Contract\n\nOn every NV project wake, read:\n\n- This file.\n- The current project's `brief.md`, `human_advice.md`, and `work/state.md`.\n- Compact state, wake reason, `next_action`, blocker ids, and latest evidence\n  pointers supplied by the scheduler.\n\nDo not routinely read broad `AGENTS.md` files. Consult them only for visible\ncode/policy conflicts, explicit wake instructions, or hardware/protocol/code\nquestions.\n\nConflict priority:\n\n1. Explicit human `STOP`, pause, cancel, do-not-continue, or must-first\n   instructions.\n2. Hard bridge queue, hardware, code-safety, manifest, execute, and local lab\n   opt-in gates.\n3. Current project `human_advice.md`.\n4. Current project brief, state, compact state, and latest evidence.\n5. This file.\n6. Historical examples and optional references.\n\nRule strengths:\n\n- `HARD`: fail-closed. Includes STOP/pause/cancel orders, queue mutation rules,\n  hardware/code/manifest/execute uncertainty, local lab opt-in, and completion\n  markers.\n- `DEFAULT`: normal lab practice. Follow unless current evidence or human advice\n  justifies a safer, more specific choice.\n- `SOFT`: scientific interpretation guidance. Use for caveats, provenance,\n  finding scope, and follow-up design; do not make it an external blocker by\n  itself.\n- `PROVENANCE`: evidence used for reasoning. Not a hard gate by itself.\n- `HISTORICAL`: old context. Do not revive as current policy without a specific\n  reason.\n\n## Hard Safety Baseline\n\n- Do not submit, mutate, stop, or mark terminal any bridge job unless the bridge\n  queue/running state and requested action satisfy the bridge policy.\n- Bridge occupancy blocks new bridge-touching submission or queue mutation.\n  Bridge-free analysis, notes, planning, and evidence cleanup may continue.\n- Hardware/safety uncertainty, non-trackable manual apparatus uncertainty,\n  code-safety uncertainty, manifest-limit uncertainty, missing local lab opt-in,\n  or execute-gate failure blocks the affected action.\n- Before materializing a new bridge-touching experiment, prefer an\n  agent-authored experiment intent and parse the verifier JSON verdict. A zero\n  process return code is not enough if the JSON verdict is blocked.\n- Preserve the MATLAB bridge safety model. Do not widen hardware limits,\n  manifest limits, execute gates, or instrument-driver behavior from an NV\n  project wake.\n- Before ending any cron-triggered project-execution wake, write the required\n  JSON completion marker at the exact path from the wake prompt.\n\n## Working Defaults\n\n- Treat prior conclusions as hypotheses, not facts; re-check primary evidence\n  before building further decisions on them.\n- `next_action` is a state pointer, not the full research plan. Python owns\n  durable state, queue safety, audit logs, wake pacing, and hard safety gates.\n  The agent owns research judgment, chunk planning, evidence synthesis,\n  literature/prior-result comparison, pulse-sequence protocol inspection, and\n  experiment design.\n- Use a same-wake runnable work loop. Continue safe grounded project work until\n  bridge state, hard gates, real external blockers, exhausted runnable work, or\n  the required handoff stops the wake.\n- From current experiment data, calculation/analysis results, and literature\n  findings, form scientific hypotheses and then perform or plan experiments,\n  calculations/analysis, and literature review to test them.\n- For signals observed in experiment results, evaluate whether they plausibly\n  arise from a physical phenomenon or from apparatus artifacts, analysis\n  artifacts, or noise.\n- The 23-C quick starter PDF is available to OpenClaw agents at\n  `<OPENCLAW_WORKSPACE>/docs/Quick_Starter_Guide.pdf`.\n- Current 23-C setup context: the Tektronix AWG5014B has been replaced by two\n  Siglent SDG6032X units; experiments use the `ms = +1` transition; the DC\n  magnetic field corresponds to resonance near 3.875 GHz.\n- Current setup contrast reference: photoluminescence contrast between\n  `m_S = 0` and `m_S = +1` is about 20%; use measurement-specific expected\n  contrast when deciding signal presence.\n- When judging a candidate signal, compare the observed effect size with the\n  measurement-specific expected contrast; features far below the expected\n  contrast need stronger supporting evidence before being promoted.\n- Also compare the observed effect size with its noise/uncertainty; low-SNR\n  features need stronger supporting evidence before being promoted.\n- Readout roles are sequence-dependent; inspect the actual XML before\n  interpreting reference/signal channels. Use reference-based normalization\n  mainly for drift correction and plotting. Normalization\n  amplifies noise and denominator artifacts. When using normalization, evaluate\n  and record both required views: point-wise normalization and normalization\n  against a fitted line or curve to the reference readout. Compare both with raw\n  readouts to capture slow reference/baseline variation from drift without\n  adding more noise.\n- Do not treat normalization-only features as candidate physical signals.\n- Keep candidate signal presence, physical interpretation, and derived\n  parameter claims separate.\n- Calibration/scout are usually fine at `2e5-3e5` total shots. Use at least\n  `2e5` total shots to secure minimum SNR. Cleaner\n  quantitative data can require more than `2e5-3e5` total shots, and\n  publication-quality data generally requires at least `1e6` total shots,\n  because this setup has error sources beyond shot noise, including drift and\n  laser-power fluctuations.\n- The experiment code has also been substantially revised for the two-Siglent\n  route; do not assume old Tektronix AWG5014B code paths or timing behavior are\n  protocol-equivalent to the current setup without inspecting the active code\n  and sequence XML/manifest.\n- For this setup, use the working approximation that Rabi frequency is about\n  10 MHz at `mod_depth = 1` and scales approximately linearly with `mod_depth`.\n- Scientific uncertainty is agent work, not an external blocker. Ambiguous data,\n  low TrackCenter counts, invalid resonance, candidate-only status, no robust\n  physical conclusion, or strategy choice should normally be handled by\n  bridge-free synthesis, notes, backlog cleanup, and the next safe\n  `research_task`.\n- Reserve external blocking for physical/manual apparatus checks, non-trackable\n  hardware or GUI uncertainty, hardware safety, code/safety/approval work, hard\n  bridge failures that cannot be recovered agent-side, or explicit human\n  do-not-continue orders.\n- After meaningful evidence review, terminal results, model comparison, or\n  bridge-free synthesis, update Current Findings with what is supported, useful\n  for the next decision, downgraded, unresolved, and what evidence would change\n  the finding.\n- Always establish the expected signal from the relevant physical model before\n  planning or interpreting measurements; prefer simulation when useful.\n- Always assess whether the expected signal from the relevant physical model\n  should be distinguishable from noise/uncertainty.\n- First decide whether a signal is present from raw/readout-aware evidence; fit\n  only after signal presence is supported, using an appropriate physical or\n  empirical function for that measurement type. Use the fit-derived value\n  downstream only if the fit remains consistent with the data shape and baseline\n  behavior.\n- Stored averages are often primarily a tracking cadence, not a strong\n  independent-repeatability test; do not overweight average-to-average agreement\n  unless repetitions per average are large enough for that comparison.\n- Recent-average drift under snake scan order is advisory provenance. Do not\n  stop, wake, or block solely for drift flags. Stop only for hard anomalies such\n  as tracking loss, count collapse, hardware/safety uncertainty, explicit STOP,\n  or monitor errors that make continuing unsafe.\n- For snake-ordered scans with stored averages, use an even number of averages\n  by default so forward and reverse acquisition directions are balanced. If an\n  odd average count is intentionally used, record the explicit exception reason.\n- Use recent drift-score evidence, including usable measurement-derived drift\n  scores from the last 1 hour when available, and the MATLAB/OpenClaw advisory\n  when choosing repetitions, averages, and scan points. Cite the last-hour drift\n  evidence in the plan when it affects the choice. Good drift can justify a\n  longer per-average window only within the active advisory cap. If the advisory\n  estimated per-average/tracking window exceeds the cap, revise before execute:\n  reduce repetitions per average and/or scan points first, raise averages only\n  when doing so preserves useful total shots without violating the cap, and\n  reduce total shots when the task is a screening/triage measurement that does\n  not require precision. Drift conditions continuously change; do not blindly\n  reuse averages/repetitions from past data without reassessing current drift\n  evidence and advisory caps.\n- Consider drift before relying on saved Imaging positions. If the sample or\n  focus may have moved enough that the saved image no longer points to the\n  current target locations, repeat Imaging or run an expanded re-image before\n  using those positions.\n- If TrackCenter fails repeatedly from saved or image-derived seeds, suspect\n  that drift has shifted the Imaging frame relative to the current target\n  locations. Re-image before treating the candidate as absent or non-trackable.\n- When a quantitative measurement cannot yield a reliable fitted value despite\n  valid prerequisite evidence, assess whether better measurement conditions or\n  higher data quality could make the result usable. If so, prefer a redesigned\n  repeat with increased averages and/or scan points before abandoning the\n  result.\n- For substantive scientific decisions and experiment-result interpretation,\n  compare current evidence with relevant literature and this lab's past data\n  before finalizing the next scientific decision or interpretation. Use a\n  targeted web literature search when needed to keep the\n  comparison current and well sourced. Prefer primary sources and record the\n  search queries, sources, and decision-relevant takeaway used.\n- For pulse-sequence-dependent plans or scientific statements, inspect the\n  actual sequence XML/manifest, active instruction path, timing definitions,\n  typed/boolean variables, comments/disabled blocks, saved metadata, and\n  readout roles before relying on shortcut names or stating protocol parity.\n- Use targeted evidence access. Start from compact state and latest pointers;\n  read large logs by tail or id/keyword search.\n- Durable project notes, advice records, backlog text, completion markers, and\n  other machine-consumed records should be plain English and preferably ASCII.\n  User-facing chat and notification_service reports may be Japanese.\n\n## Memory Index\n\nUse this router for `NV_RESEARCH_KNOWLEDGE.md`:\n\n- `Shared Literature`: web literature search, papers, DOI/arXiv/publisher\n  pages, local paper library, prior-result comparison, Hamiltonian/model\n  interpretation, coupling extraction, old hardware assumptions.\n- `Experiment Defaults`: sequence defaults, strong-pi pulsed ODMR, resonance\n  validity, Rabi/weak-pi, CPMG/Hahn/XY8/DDRF, XML/protocol\n  inspection, weak signal follow-up.\n- `Drift, Tracking, And Environment`: Imaging, TrackCenter, usual NV/NV23\n  identity, nearby-NV recovery, position freshness, TSP01/environment drift,\n  count/tracking interpretation.\n- `Shot Budget And Data Quality`: shot credit, SEM scaling, stored averages,\n  visual review, fit validity, snake scan, recent-average drift.\n- `OpenClaw Project Operation`: route policy, same-wake work, running-execute\n  bridge-free work, project layout, advice inbox, verifier verdicts, WSL\n  canonical state, Imaging/TrackCenter helpers, queue staging, completion\n  markers, code auto-resume, notification_service reports/media.\n- `Research Practice And Closeout`: literature/prior-result comparison,\n  non-experiment findings that affect design, LaTeX closeout reports, manual\n  experiment evidence.\n\n## Wake Digest\n\n- `HARD`: Human STOP/pause/cancel/must-first instructions and bridge/hardware/\n  code/manifest/execute failures override autonomy.\n- `HARD`: Parse verifier JSON before enqueue; return code alone is insufficient.\n- `HARD`: Every cron-triggered wake must write the completion marker.\n- `DEFAULT`: Use execute-backed strong-pi pulsed ODMR as the default\n  resonance-presence screen. Determination of `mw_freq_hz` requires weak-pi\n  pulsed ODMR.\n- `DEFAULT`: Do not put automatic fit requests such as `analysis.fit_kind` into\n  ordinary bridge jobs. Use terminal savedexperiment raw export plus plots\n  first.\n- `DEFAULT`: For substantive scientific decisions and experiment-result\n  interpretation, compare current evidence with relevant literature and this\n  lab's past data before finalizing the next scientific decision or\n  interpretation. Web-search the literature as needed to make that comparison\n  current and well sourced.\n- `DEFAULT`: Inspect actual sequence XML/manifest content before protocol-based\n  plans or scientific statements.\n- `SOFT`: Use SEM/SEM-scaling only when planning or reviewing long acquisitions\n  intended to improve statistics by accumulating more shots.\n- `HARD`: Under snake scan order, use even average counts by default and\n  record any odd-count exception. Tune repetitions, averages, and scan points\n  from recent drift scores, including last-hour measurement-derived drift scores\n  when available, plus advisory drift risk. Good drift can justify a longer\n  per-average window only within the active advisory cap; if the advisory\n  exceeds that cap, revise before execute by reducing repetitions per average\n  and/or scan points before considering a capped, shot-preserving average split.\n  Drift conditions continuously change; do not blindly reuse averages/\n  repetitions from past data without reassessing current drift evidence and\n  advisory caps.\n- `HARD`: Consider drift before relying on saved Imaging positions. If the\n  sample or focus may have moved enough that the saved image no longer points to\n  the current target locations, repeat Imaging or run an expanded re-image\n  before using those positions.\n- `HARD`: If TrackCenter fails repeatedly from saved or image-derived seeds,\n  suspect Imaging-frame drift and re-image before treating the candidate as\n  absent or non-trackable.\n- `HARD`: Do not infer or transpose SavedImages axes from array shape. Python\n  image analysis must use an explicit `ImageData_YXZ`/`axis_order` contract\n  before candidate coordinates are used for TrackCenter.\n- `PROVENANCE`: Usual-NV/NV23 labeled imaging/tracking data informs identity and\n  seed choice, but TrackCenter counts alone do not prove identity.\n- `DEFAULT`: WSL project state is canonical. New projects use the simple\n  research-state layout: `brief.md`, `work/state.md`, `work/notes/`,\n  `work/bridge_jobs/`, and `.manager/`. Keep bridge-execution contracts in\n  JSON and scientific interpretation in Markdown state/notes. Operational logs,\n  advice inboxes, and generated artifacts may exist as support files, but they\n  are not the research-plan surface.\n",
    "detailed_knowledge_exists": true,
    "detailed_knowledge_updated_epoch": 1778551344.1415162,
    "detailed_knowledge_size_bytes": 27550
  },
  "autonomy": {
    "agent_capability_assumption": {
      "project_execution_agent": "codex_api_gpt_5_5_xhigh",
      "project_execution_agent_id": "nv-researcher",
      "research_judgment_owner": "agent",
      "python_role": "state_queue_safety_audit_and_hard_boundaries",
      "avoid_over_specifying_scientific_steps": true
    },
    "max_autonomy_within_safety": true,
    "allow_agent_backlog_expansion": true,
    "continue_when_backlog_empty": true,
    "allow_autonomous_next_action_selection": true,
    "allow_project_state_updates": true,
    "allow_analysis": true,
    "allow_staging_sequence_authoring": true,
    "allow_analysis_code_changes": true,
    "allow_bridge_wrapper_code_changes": true,
    "allow_instrument_driver_code_changes": false,
    "allow_legacy_gui_code_changes": false,
    "allow_validate": true,
    "allow_dry_run": true,
    "allow_execute_existing_validated": true,
    "allow_physical_action_requests": true,
    "allow_procurement_proposals": true,
    "require_approval_for_execute": false,
    "require_approval_for_high_risk_changes": true,
    "require_code_change_review_before_execute": false,
    "require_physical_result_before_resume": true,
    "phase_execution": {
      "enabled": true,
      "preferred_unit": "same_wake_runnable_work_loop",
      "allow_pre_execute_chain_in_one_wake": true,
      "allow_execute_in_same_wake_when_ready": true,
      "execute_requires_separate_wake": false,
      "execute_can_follow_pre_execute_chain": true,
      "route_policy": {
        "staging_new_or_changed": [
          "validate",
          "dry_run",
          "execute"
        ],
        "validated_manifest_recent_same_route_success_bounded": [
          "execute"
        ],
        "validated_manifest_optional_extra_confidence": [
          "validate",
          "execute"
        ]
      },
      "pre_execute_chain": [
        "build_or_adjust",
        "validate_if_route_unknown_or_extra_confidence_needed",
        "read_validate_terminal_evidence_if_invoked",
        "dry_run_only_for_staging_new_changed_or_route_unknown",
        "read_dry_run_terminal_evidence_if_invoked",
        "prepare_execute_candidate",
        "bridge_execute_submission"
      ],
      "coarse_task_contract": {
        "next_action_kinds": [
          "advance_project",
          "blocked_external",
          "blocked_code",
          "blocked",
          "idle"
        ],
        "backlog_kinds": [
          "research_task",
          "external_request",
          "blocker"
        ],
        "fine_grained_work_classes_disabled": true,
        "stale_fine_grained_labels_are_normalized": true
      },
      "experiment_intent_contract": {
        "enabled": true,
        "agent_writes_scientific_intent": true,
        "python_verifies_safety_and_queue_state": true,
        "verified_intent_is_not_a_bridge_job": true,
        "bridge_job_materialization_remains_with_existing_nv_batch_and_queue_tools": true
      },
      "event_driven_research_agenda": {
        "enabled": true,
        "research_agenda_path": "work/state.md",
        "bridge_jobs_dir": "work/bridge_jobs",
        "events": [
          "terminal_bridge_result",
          "bridge_idle",
          "new_human_advice",
          "new_evidence",
          "runtime_anomaly_or_drift_alert",
          "scheduled_review"
        ],
        "backlog_priority_is_advisory": true
      },
      "validated_manifest_bounded_execute_fast_path": true,
      "execute_reachability_priority": true,
      "same_wake_runnable_work_loop": true,
      "same_wake_runnable_work_loop_applies_to_all_task_types": true,
      "single_phase_stop_contract_disabled": true,
      "continue_after_queuing_next_runnable_item": true,
      "openclaw_freshness_and_provenance_checks_are_advisory": true,
      "dry_run_default_for_validated_manifest_fast_path": false,
      "short_validate_or_dry_run_should_not_wait_for_next_cron": true,
      "completion_marker_releases_inflight": true,
      "allow_parallel_project_work_during_bridge_running": true,
      "parallel_project_work_contract": {
        "first_class_project_component": true,
        "not_secondary_to_experiment": true,
        "prefer_one_meaningful_non_monitoring_contribution": true,
        "mid_run_monitoring_alone_is_not_default_endpoint": true,
        "record_reason_when_skipping_non_monitoring_work": true,
        "eligible_backlog_item_kind": "research_task",
        "compatibility_item_field": "run_while_bridge_running",
        "proactively_consider_when_waiting": [
          "science_objective_analysis_of_completed_or_autosaved_data",
          "science_objective_model_calculations_or_simulations",
          "science_objective_literature_or_paper_pdf_review",
          "figure_table_or_note_updates",
          "evidence_gap_closure",
          "backlog_cleanup_after_science_objective_options"
        ],
        "parallel_work_opportunity_review_enabled": true,
        "parallel_work_opportunity_review_min_tick_interval_seconds": 1800,
        "forbidden_during_running": [
          "submit_bridge_job",
          "mutate_bridge_queue",
          "stop_running_job",
          "mark_running_job_terminal_without_terminal_evidence"
        ],
        "bridge_queue_items_must_set": "requires_bridge_idle or touches_bridge_queue"
      },
      "stop_before_execute_unless_explicit_phase": false,
      "stop_when_bridge_running": false,
      "stop_bridge_touching_work_when_bridge_running": true,
      "bridge_running_does_not_stop_bridge_free_research": true,
      "wake_stop_conditions": [
        "bridge_queued_or_running_blocks_next_bridge_touching_item_and_no_useful_bridge_free_project_work_remains",
        "legacy_bridge_rejection_of_invoked_validate_dry_run_or_execute",
        "missing_or_unmaterializable_payload",
        "real_external_blocker",
        "project_objective_for_this_wake_genuinely_exhausted",
        "high_risk_change_outside_policy"
      ],
      "stop_on_validate_or_dry_run_failure": true,
      "stop_on_openclaw_safety_or_provenance_blocker": false,
      "stop_on_legacy_bridge_rejection": true,
      "stop_before_execute_only_for": [
        "bridge_queued_or_running",
        "missing_or_unmaterializable_payload",
        "missing_manifest",
        "legacy_bridge_rejection_of_invoked_validate_dry_run_or_execute",
        "project_policy_explicitly_disallows_execute"
      ]
    }
  },
  "research_context": {
    "brief_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/brief.md",
    "research_state_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/state.md",
    "research_agenda_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/state.md",
    "shared_research_memory_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_MEMORY.md",
    "shared_research_knowledge_path": "<OPENCLAW_WORKSPACE>/NV_RESEARCH_KNOWLEDGE.md",
    "evidence_index_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/.manager/evidence.jsonl",
    "experiment_intents_root": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/experiment_intents",
    "evidence_count": 42,
    "recent_evidence": [
      {
        "actor": "openclaw-project-manager",
        "category": "analysis",
        "evidence_id": "analysis_20260512_031721_840657_19692bf40a",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_raw_export.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_drift.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_review.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_narrow_weak_podmr_after_ramsey_20260512_025521_raw_readouts.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {},
        "related_claims": [],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Narrow weak-pi pODMR after terminal Ramsey completed and reviewed: raw/fit-reference minimum gives updated center 3.8761166667 GHz (+0.250 MHz from prior weak-pi center; pointwise ratio min +0.500 MHz). This makes the old 1.593 MHz Ramsey peak plausibly residual detuning rather than 13C; T2star remains candidate-only pending corrected-center Ramsey.",
        "tags": [],
        "timestamp": "2026-05-12T03:17:21"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "note",
        "evidence_id": "note_20260512_031810_487387_9705802004",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/notes/image231924_c01_narrow_weak_podmr_after_ramsey_review_20260512_0318.md"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {},
        "related_claims": [],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Note for narrow weak-pi pODMR after Ramsey: updated center 3.8761166667 GHz; old 1.593 MHz Ramsey peak likely residual detuning, 13C downgraded pending corrected-center Ramsey.",
        "tags": [],
        "timestamp": "2026-05-12T03:18:10"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "artifact",
        "evidence_id": "artifact_20260512_032618_651713_de6e78654b",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/experiment_intents/verified/image231924_c01_corrected_center_ramsey_repeat_20260512_0320.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_0320.batch_spec.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_0320.batch_state.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute.job_initial.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/bridge_jobs/nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute.status_initial.json"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {},
        "related_claims": [],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "Submitted and started corrected-center Ramsey/T2star repeat: bridge job nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute; pre-enqueue advisory had no blockers, estimated runtime 4479 s and per-average tracking window 742 s under the 900 s night cap; auto-align selected 23.416 kcps and the experiment has started.",
        "tags": [],
        "timestamp": "2026-05-12T03:26:18"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "analysis",
        "evidence_id": "analysis_20260512_040239_706388_8f15704429",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_raw_export.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.json",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/analysis/analyze_corrected_center_ramsey_autosave_avg2.py",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_per_average.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_raw_readouts.png",
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/notes/image231924_c01_corrected_center_ramsey_autosave_avg2_review_20260512_0359.md"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {},
        "related_claims": [],
        "schema_version": 1,
        "source": "record-evidence",
        "summary": "In-progress corrected-center Ramsey autosave after 2/6 averages raw-exported and reviewed: bridge still running with healthy counts (Final = 25.898 kcps), no terminal/anomaly evidence; carrier-nearest FFT bin ranks 3rd while expected lower/upper 13C bins rank 6/23, so this is only progress evidence and T2star/13C remain no-conclusion until terminal review.",
        "tags": [],
        "timestamp": "2026-05-12T04:02:39"
      },
      {
        "actor": "openclaw-project-manager",
        "category": "figure",
        "evidence_id": "figure_20260512_040302_647471_cffab9dc03",
        "paths": [
          "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/work/artifacts/figures/image231924_c01_corrected_center_ramsey_repeat_autosave_avg2_review.png"
        ],
        "project_id": "nv23_aligned_nv_t2star_13c_image231924_20260511_2319",
        "provenance": {
          "daily_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/log.md",
          "lab_log_path": "<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image231924_20260511_2319/log.md",
          "ledger_event": "lab_log_note"
        },
        "related_claims": [],
        "schema_version": 1,
        "source": "record-lab-log",
        "summary": "Corrected-center Ramsey autosave 2/6 review: At 03:59 EDT the corrected-center Ramsey repeat remained running with 2/6 averages completed and healthy counts (Final = 25.898 kcps). Autosave raw export/review found the carrier-nearest FFT bin ranked 3rd and expected lower/upper 13C bins ranked 6/23; this is progress evidence only, with no T2star or 13C conclusion until terminal review.",
        "tags": [],
        "timestamp": "2026-05-12T04:03:02"
      }
    ],
    "experiment_intents": {
      "queued": 2,
      "verified": 1,
      "rejected": 0,
      "done": 7
    },
    "backlog_role": "execution_queue_and_audit_not_complete_research_plan",
    "scheduler_role": "event_state_pointer_agent_selects_scientific_next_step"
  },
  "budgets": {
    "max_single_job_duration_seconds": 7200,
    "default_max_untracked_window_seconds": 600
  },
  "stop_conditions": [
    "the request would require editing or widening legacy bridge/MATLAB hardware safety limits",
    "bridge queued/running is not clear for bridge-touching queue submission or queue mutation",
    "the execute payload cannot be materialized from an available manifest and sequence",
    "legacy bridge validate, dry_run, or execute gate rejects the job",
    "high-risk code-change result is missing required review or verification evidence; low-risk auto-approved code changes require allowed-scope and passed-verification evidence"
  ]
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
