Case: podmr_029_2026-05-16-193002

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual cross-check of the raw arrays

Active sequence and readout roles:
- SequenceName in the export is Rabimodulated.xml; the provided XML scans mw_freq.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The first detection after adj_polarize is the polarized m_S = 0 reference readout.
- The second detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...) and is the pODMR signal readout.
- sample_rate = 250 MHz. The pulse duration is round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- The active variable list and provided XML give mod_depth = 1. I treated the serialized Sequence text in raw_export.json that shows mod_depth = 0.3 as stale/inconsistent with those active values.

Physical signal model:
- Current contrast scale between m_S = 0 and m_S = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a square pulse of length tau = 52 ns, the transfer probability versus detuning d is:
  P1(d) = f_R^2 / (f_R^2 + d^2) * sin(pi * tau * sqrt(f_R^2 + d^2))^2.
- On resonance, P1(0) = sin(pi * 52 ns * 10 MHz)^2 = 0.996.
- Expected normalized fluorescence drop on resonance is C * P1(0) = 0.219.
- Because the scan step is 5 MHz, any resonance inside the scanned range has a sampled point within 2.5 MHz. At 2.5 MHz detuning, P1 = 0.929, so the expected sampled drop is still 0.204.
- With a baseline readout near 45 counts, this corresponds to about 9.9 counts on exact resonance and at least about 9.2 counts at the nearest sampled point.

Data calculation:
- Scan range: 3.825 to 3.925 GHz in 5 MHz steps, 21 points.
- Combined readout 1 mean = 44.93, readout 2 mean = 44.91.
- Signal/reference ratio r2/r1 has mean = 0.9999, standard deviation = 0.0281, and minimum = 0.9440 at 3.855 GHz.
- The largest combined negative signal-reference difference is -2.56 counts, far below the roughly 9 count dip expected from the active-pulse model.
- A no-resonance linear baseline fit to r2/r1 gives SSE = 0.01652.
- Forcing the active mod_depth = 1 square-pulse ODMR model with fixed contrast C = 0.22 and allowing a linear baseline gives best SSE = 0.04943, worse than the no-resonance fit.
- Letting the dip amplitude float positive gives a best normalized amplitude of only 0.059, far below the expected 0.22 and driven by a narrow irregular low point rather than the expected broad square-pulse response.
- As a robustness check only, if mod_depth were 0.3, the exact-resonance expected drop would be 0.0487; the active files do not support that setting, and the two stored averages are not a strong independent repeatability test. The required active mod_depth = 1 calculation is decisive.

Decision:
The active sequence should produce a large, sampled pODMR dip if a resonance is present in this frequency span. The measured signal/reference trace stays near unity and is better explained by baseline/tracking fluctuations than by the expected square-pulse resonance response. Prediction: resonance_absent.
