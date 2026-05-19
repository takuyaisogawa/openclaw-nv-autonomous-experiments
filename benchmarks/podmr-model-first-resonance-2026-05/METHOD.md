# Method

Each run asks GPT-5.5 medium to classify one pODMR measurement as
`resonance_present` or `resonance_absent`.

The three prompt conditions form an ablation:

1. `context_0_xml_only`: NV pODMR context plus XML inspection.
2. `context_A_domain_facts`: XML inspection plus contrast/Rabi/average facts.
3. `context_B_model_first`: same domain facts plus explicit quantitative
   expected-signal modeling before judgment.

Each condition is run for three replicates over the same 96 cases. Scoring is
performed against `labels/gold_labels.csv`.

The `analysis_notes/` folders contain model-generated free-form notes written
for each run before scoring. They are included for auditability and should not
be treated as labels or ground truth.
