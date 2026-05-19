<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_062

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence file/name: Rabimodulated.xml / Rabimodulated.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is the true m_S = 0 optical reference after adj_polarize and detection before the microwave test pulse.
- Readout 2 is the post-microwave detection after rabi_pulse_mod_wait_time.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this remains 52 ns after rounding.

Physical expected-signal model:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a rectangular resonant Rabi pulse, the transferred population is
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  where delta is microwave detuning in cycles/s and t = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected on-resonance fractional fluorescence drop is C * P(0) = 0.219, about 21.9%.
- With observed raw readouts around 50 counts, an on-resonance point should therefore be lower by about 10.96 counts in readout 2 relative to readout 1.

Observed quantitative checks:
- Mean readout 1 = 50.482 counts, standard deviation across scan points = 0.948.
- Mean readout 2 = 49.790 counts, standard deviation across scan points = 1.026.
- Pointwise normalized contrast (readout1 - readout2) / readout1 has mean 0.0134 and standard deviation 0.0272.
- The largest observed positive pointwise contrast is 0.0735 at 3.850 GHz, still about one third of the expected 0.219 resonant contrast and not accompanied by the broad dip shape expected for a 10 MHz Rabi rate sampled every 5 MHz.
- A fixed-contrast Rabi lineshape search using C = 0.22 does not improve the fit meaningfully over a constant baseline unless the resonance center is pushed outside the scanned band; the data are dominated by percent-level fluctuations rather than an approximately 22% microwave-induced dip.

Decision:
No pODMR resonance is present in this scan. The active pulse would be close to a pi pulse at the stated setup calibration, so a real resonance in the scanned range should produce a large, obvious drop in the second readout; the measured readouts show only small unstructured fluctuations.
