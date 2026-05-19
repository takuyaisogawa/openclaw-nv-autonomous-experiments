<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_092

Sequence and readout roles:
- The run export identifies the active sequence as Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The stored sequence instructions first polarize and detect, then conditionally acquire a 1-level reference only when full_expt is nonzero, then apply the Rabi-modulated MW pulse and detect again.
- The actual run variables have full_expt = 0, so the conditional 1-level reference is disabled.
- Therefore readout 1 is the post-polarization reference readout, and readout 2 is the post-MW-pulse readout.
- Actual run pulse parameters: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, switch_delay = 100 ns.

Quantitative physical model:
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth.
- For this run, f_R = 10 MHz and pulse duration t = 52 ns.
- For a rectangular driven two-level pulse, the resonant population transfer is P = sin^2(pi f_R t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of 22%, the expected resonant readout reduction is 0.22 * 0.996 = 0.219, i.e. about 21.9%.
- The mean readout-1 level is 51.83 counts, so a resonant pulse should reduce readout 2 by about 51.83 * 0.219 = 11.36 counts near resonance.

Observed signal:
- I evaluated the normalized contrast as (readout1 - readout2) / readout1 at each frequency.
- The largest observed suppression of readout 2 is at 3.905 GHz: readout1 = 51.48, readout2 = 49.88, difference = 1.60 counts, contrast = 3.10%.
- Other nearby points are similarly small: 3.900 GHz gives 1.53%, 3.910 GHz gives 1.94%, 3.915 GHz gives 2.67%, and 3.920 GHz gives 2.11%.
- Several points away from this region show readout 2 above readout 1, up to -4.05% contrast by this sign convention, so the few-percent variations are on the scale of drift/noise/readout imbalance rather than the expected 21.9% resonant response.
- Stored averages are only two and may reflect tracking cadence, so I did not treat the per-average traces as a strong independent repeatability test.

Decision:
- The expected resonant signal for the active pulse sequence is about 11.4 counts, but the observed maximum suppression is only about 1.6 counts and does not approach the physical contrast expected for a 52 ns, mod_depth = 1 resonant Rabi pulse.
- I therefore decide that a pODMR resonance is absent in this scan.
