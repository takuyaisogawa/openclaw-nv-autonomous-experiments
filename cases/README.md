# Case Studies

Each case directory is centered on a sanitized OpenClaw project-folder copy
for one completed autonomous-agent experiment. Case data, figures, reports,
bridge records, and analysis artifacts are kept inside the sanitized
`project/` tree.

Start with:

- [../docs/case_walkthrough.md](../docs/case_walkthrough.md) for a cross-case
  reader guide.
- [image145844/README.md](image145844/README.md) for the image145844 case
  entry point.
- [image231924/README.md](image231924/README.md) for the image231924 case
  entry point.

Inside each case, the main audit entry point is:

```text
project/work/state.md
```

Useful audit paths repeated across both cases:

| Path | What to inspect |
| --- | --- |
| `project/work/state.md` | Current and final scientific state |
| `project/.manager/evidence.jsonl` | Evidence ledger |
| `project/experiment_intents/` | Agent-authored intent lifecycle |
| `project/work/bridge_jobs/` | Bridge submit/status/result records |
| `project/work/artifacts/analysis/` | Analysis JSON and scripts |
| `project/work/artifacts/figures/` | Generated review figures |
