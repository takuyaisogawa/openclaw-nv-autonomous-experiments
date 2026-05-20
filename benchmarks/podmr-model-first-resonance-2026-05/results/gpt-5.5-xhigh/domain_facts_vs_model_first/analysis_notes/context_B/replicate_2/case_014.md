Case: podmr_033_2026-05-15-233800

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first run adj_polarize followed by detection. This is the true m_S = 0 reference readout, corresponding to raw readout 1.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- The active measurement block is one rabi_pulse_mod_wait_time followed by detection. This post-pulse detection is raw readout 2.
- From the provided sequence XML, length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1.

Quantitative model:
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for this sequence.
- For a rectangular driven two-level pulse with detuning df in Hz, the transition probability is:
  P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * tau * sqrt(f_R^2 + df^2)).
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The mean raw readout 1 level is 38.46 counts. With the stated 22% m_S = 0 to m_S = +1 contrast, the expected full transition loss is 0.22 * 38.46 = 8.46 counts.
- Expected on-resonance loss for this pulse is therefore 8.46 * 0.996 = 8.43 counts.

Observed signal:
- The largest measured loss readout1 - readout2 occurs at 3.875 GHz: 38.50 - 28.83 = 9.67 counts, or 25.1% of readout 1.
- Off the central feature, the median loss excluding 3.865 to 3.885 GHz is about 0.60 counts, with standard deviation about 1.40 counts; the central loss is about 6.35 off-region standard deviations above that level.
- The neighboring losses are also in the expected sign and width range for a 52 ns, 10 MHz pulse: 4.08 counts at 3.870 GHz, 6.83 counts at 3.880 GHz, and 3.40 counts at 3.885 GHz.

Model fit check:
- I fit d(f) = readout1 - readout2 to b + A * P(f - f0), using the pulse model above and scanning f0.
- Best fit center: f0 = 3.8769 GHz.
- Best fit offset: b = 0.37 counts.
- Best fit amplitude: A = 8.14 counts, which is 21.2% of the mean readout 1 level and close to the expected 22% contrast.
- Model RSS is 32.73, versus 142.00 for a constant no-resonance difference model.

Stored averages:
- There are two stored averages, and these can reflect tracking cadence rather than independent repeatability. I therefore use them only as a sanity check.
- Both stored averages show the central deficit in the measurement readout: average 1 has its largest loss at 3.880 GHz and average 2 at 3.875 GHz.

Decision:
The measured readout-2 loss has the correct readout role, size, sign, and frequency-localized shape for the expected 52 ns resonant Rabi pulse. A pODMR resonance is present.
