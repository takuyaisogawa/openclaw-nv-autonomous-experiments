Case: podmr_074_2026-05-17-092418

Sequence/readout identification from inputs/sequence.xml:

- Active sequence: Rabimodulated microwave-frequency scan, with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped. do_adiabatic_inversion is therefore not active for this measurement.
- Readout 1 is the detection immediately after adj_polarize, so it is the bright mS = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so it is the microwave-pulse pODMR readout.
- mod_depth = 1.
- sample_rate = 250 MHz and length_rabi_pulse = 52 ns. The sequence rounds this to 13 samples, still 52 ns.

Quantitative model:

For the provided setup, f_R = 10 MHz at mod_depth = 1. For a square pulse of duration t = 52 ns, the driven population transfer at detuning delta is

P_plus1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

The fluorescence model is S_pulse / S_0 = 1 - C * P_plus1, with C = 0.22 for the mS = 0 to mS = +1 contrast scale.

Numerical values:

- At delta = 0 MHz: P_plus1 = 0.996, expected contrast = 0.219, so a 49.08-count reference should drop by about 10.75 counts to about 38.33.
- At delta = 2.5 MHz, the largest possible offset between a true in-range resonance and the nearest 5 MHz scan point: P_plus1 = 0.929, expected contrast = 0.204, so the expected sampled drop is still about 10.0 counts.
- At delta = 5 MHz: P_plus1 = 0.749, expected contrast = 0.165, still about 8.1 counts for a 49-count reference.

Data comparison:

- Combined readout 1 mean = 49.077.
- Combined readout 2 mean = 48.785.
- Overall readout2/readout1 ratio = 0.994, only 0.6% lower.
- The largest normalized combined dip is at 3.900 GHz: readout 1 = 50.981, readout 2 = 47.058, ratio = 0.923, contrast = 7.70%, dip = 3.923 counts.
- Several scan points have readout 2 above readout 1, which is inconsistent with a strong pi-pulse resonance line.
- A fixed 22% contrast, 10 MHz Rabi model gives a worse ratio fit than a constant no-resonance baseline (RSS 0.069 versus 0.024). A constrained line-shape fit allows only about 4.9% contrast, far below the expected 20-22% sampled contrast for the XML pulse settings.

Decision:

With the XML pulse duration and mod_depth, an in-range pODMR resonance should produce a large, unmistakable post-pulse fluorescence drop. The observed readout differences are small relative to that model and do not support a resonance.
