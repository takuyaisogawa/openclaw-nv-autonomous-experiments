<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_071

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize then detect, giving the true m_S = 0 reference readout.
- full_expt = 0, so the optional separate m_S = 1 reference block is skipped.
- The sequence then applies one rabi_pulse_mod_wait_time pulse and detects again, giving the post-pulse pODMR signal readout.
- Thus readout 1 is the m_S = 0 reference and readout 2 is the post-Rabi-pulse signal, not an independent 0/1 calibration pair.

Pulse parameters:
- length_rabi_pulse = 52 ns.
- mod_depth = 1 from inputs/sequence.xml and exported Variable_values. The embedded sequence text in raw_export.json has a default mod_depth of 0.3, but the active exported value and provided XML both indicate 1.
- Setup Rabi frequency at mod_depth = 1 is about 10 MHz.

Quantitative expected-signal model:
- Use a square-pulse two-level model with Rabi frequency f_R = 10 MHz and detuning delta in cycles/s:
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).
- At resonance with tau = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of about 22%, the expected on-resonance fluorescence change is:
  0.22 * 0.996 = 0.219, or about a 21.9% drop from the off-resonant signal.
- The observed post-pulse readout baseline is about 45.42 raw units, so the expected resonant dip is about:
  45.42 * 0.219 = 9.95 raw units.

Observed data check:
- readout 1 mean = 45.46, standard deviation = 0.97, range = 43.65 to 46.92.
- readout 2 mean = 45.42, standard deviation = 1.28, range = 43.83 to 47.75.
- readout 2 - readout 1 mean = -0.035, standard deviation = 0.985, range = -2.08 to +1.79.
- No point or multi-point feature approaches the expected roughly 10 raw-unit resonant drop.
- A grid search fitting the square-pulse pODMR template plus constant offset gives positive best-fit amplitudes for both readouts, meaning the strongest template-like structure is a peak rather than the expected fluorescence dip.

Decision:
The physically expected pODMR resonance for this pulse should be a large, broad fluorescence dip if an addressed NV transition lies in the scan range. The measured signal lacks that dip and is consistent with tracking/noise-scale variation, so the resonance is absent.
