Case podmr_017_2026-05-12-134151

Sequence/readout identification:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional "1 level reference" block is inactive.
- readout 1 is therefore the detection immediately after adj_polarize, a true m_S = 0 reference.
- readout 2 is the detection after the scanned rabi_pulse_mod_wait_time pulse.
- mod_depth = 1 from the provided sequence/variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.

Quantitative expected signal model:
- Use a driven two-level Rabi model for m_S = 0 to m_S = +1.
- Given setup calibration: f_Rabi(mod_depth=1) ~= 10 MHz, scaling linearly with mod_depth.
- For a square pulse of duration t = 52 ns, the on-resonance transfer probability is
  P = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional fluorescence drop in readout 2 relative to readout 1 is
  0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout 1 value is 22.70, so an on-resonance readout 2 point should be near
  22.70 * (1 - 0.219) = 17.73, an absolute drop of about 4.97 counts.

Observed data check:
- Combined readout 1 mean = 22.70, combined readout 2 mean = 22.77.
- The pointwise difference readout2 - readout1 has mean +0.07 counts, standard deviation 1.12 counts, minimum -2.10 counts.
- The minimum observed ratio readout2/readout1 is 0.913, corresponding to only an 8.7% drop, far smaller than the expected 21.9% resonant drop.
- No scan point approaches the expected post-pulse level of about 17.7 counts.
- The two stored averages show strong opposing slow trends, consistent with tracking/cadence effects rather than independent confirmation of a resonance.

Decision:
The physically expected pODMR signal for this pulse would be a large post-pulse fluorescence dip relative to the preceding m_S = 0 reference. The measured readout 2 values remain roughly equal to readout 1 across the scan and do not show the expected 22% contrast-scale dip. I therefore decide that no pODMR resonance is present.
