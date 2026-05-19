# pODMR Model-First Resonance Benchmark

This benchmark evaluates whether model-first prompting reduces false-positive
pODMR resonance calls for single NV center data.

The dataset contains 96 strong-pi pODMR measurements:

- 24 resonance-present cases
- 72 resonance-absent cases

Each prompt condition was evaluated with GPT-5.5 medium for three replicates.

## Main Results

| Condition | TP | TN | FP | FN | Accuracy | False-positive rate | False-negative rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XML only | 72 | 145 | 71 | 0 | 75.3% | 32.9% | 0.0% |
| Domain facts | 72 | 196 | 20 | 0 | 93.1% | 9.3% | 0.0% |
| Model-first | 72 | 215 | 1 | 0 | 99.7% | 0.46% | 0.0% |

The model-first condition differs from the domain-facts condition by adding a
requirement to establish the expected physical signal with a simulation or
explicit quantitative model calculation before deciding whether a resonance is
present.

## Contents

- `inputs/`: agent-visible raw export JSON files and raw-readout figures.
- `labels/`: human resonance labels used for scoring.
- `prompts/`: exact prompt condition text.
- `results/`: GPT-5.5 medium predictions, summaries, and per-run analysis notes.
- `scripts/`: scoring and package verification helpers.
