Case: podmr_006_2026-05-11-020739

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The instruction block first performs adj_polarize followed by detection, so readout 1 is the bright m_S = 0 reference.
- full_expt = 0, so the optional separate m_S = +1 reference block is inactive.
- The active swept measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection, so readout 2 is the microwave-pulse signal readout.
- Provided sequence XML / Variable_values give length_rabi_pulse = 52 ns, sample_rate = 250 MHz, mod_depth = 1, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical expectation:
- Setup Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square pulse from |0>, the transition probability at detuning df is
  P1(df) = (fR^2 / (fR^2 + df^2)) * sin^2(pi * t * sqrt(fR^2 + df^2)),
  using fR and df in cycles/s.
- With fR = 10 MHz and t = 52 ns, on resonance P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected fluorescence drop for full available contrast is therefore about 0.22 * 0.996 = 21.9%.
- At detunings of +/-5 MHz, P1 = 0.749, giving about 16.5% expected contrast; at +/-10 MHz, P1 = 0.273, giving about 6.0%; at +/-15 MHz the expected contrast is near zero. Thus the expected resonance should be a narrow dip spanning a few 5 MHz scan points.

Quantitative data check:
- Combined readout 2 has its minimum at 3.875 GHz: 40.46 counts, with 40.54 counts at 3.880 GHz and 41.88 counts at 3.885 GHz.
- Neighboring off-resonance readout 2 values recover to about 46-48 counts, for an observed local dip of about 5-7 counts, roughly 11-15% of the local signal level.
- The readout-2/readout-1 ratio reaches 0.846 at 3.880 GHz, while nearby off-resonance ratios are mostly about 0.94-1.01.
- A least-squares fit of readout 2 to a linear baseline minus the above Rabi lineshape, with fR fixed at 10 MHz and t fixed at 52 ns, gives best center 3.8783 GHz and fitted maximum drop about 6.0 counts. The residual sum of squares improves from 94.93 for a linear baseline to 31.45 with the resonance model.
- The normalized ratio fit gives best center 3.8799 GHz and fitted maximum fractional dip about 12.6%, below the nominal 21.9% maximum but within a plausible reduced-contrast/normalization range for a real single-NV measurement.
- Stored averages should not be treated as a strong independent repeatability test, but both averages show suppressed readout 2 around the same 3.875-3.885 GHz region.

Decision:
The active measurement contains a signal-readout dip at the frequency, width, and approximate scale expected from the 52 ns, mod_depth 1 Rabi pulse model. I therefore classify this case as resonance_present.
