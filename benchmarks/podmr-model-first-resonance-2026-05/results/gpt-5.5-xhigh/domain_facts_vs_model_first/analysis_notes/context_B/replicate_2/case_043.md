Case: podmr_029_2026-05-16-193002

Sequence and readout roles:

- The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. do_adiabatic_inversion is set, but the adiabatic calls are commented out and not active in this branch.
- The executed detections are:
  1. adj_polarize followed by detection: true m_S = 0 fluorescence reference, corresponding to readout 1.
  2. rabi_pulse_mod_wait_time followed by detection: post-microwave pODMR signal, corresponding to readout 2.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MS/s this is exactly 13 samples, so rounding leaves it at 52 ns.

Physical model calculation:

The supplied setup gives a Rabi frequency of about 10 MHz at mod_depth = 1. I used the driven two-level population transfer model

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz and t = 52 ns. The expected normalized signal readout is

readout2/readout1 = 1 - C * P(delta)

with C = 0.22 for the m_S = 0 to m_S = +1 fluorescence contrast.

Calculated transfer and fluorescence signal:

- delta = 0 MHz: P = 0.9961, expected readout2/readout1 = 0.7809, about 9.86 counts drop on a 45 count baseline.
- delta = 2.5 MHz: P = 0.9292, expected readout2/readout1 = 0.7956, about 9.20 counts drop.
- delta = 5 MHz: P = 0.7488, expected readout2/readout1 = 0.8353, about 7.41 counts drop.
- delta = 10 MHz: P = 0.2729, expected readout2/readout1 = 0.9400, about 2.70 counts drop.

Since the scan step is 5 MHz, a resonance inside the scan range should have a sampled point within 2.5 MHz of resonance and should therefore produce about a 20% to 22% normalized dip, roughly 9 to 10 counts at the observed baseline.

Observed data comparison:

- The combined normalized readout2/readout1 mean is 0.9999.
- The minimum combined normalized ratio is 0.9440 at 3.855 GHz, only a 5.6% decrease.
- The largest absolute combined drop is -2.56 counts at 3.855 GHz.
- Interpreted through the 22% contrast model, the largest observed drop corresponds to only P = 0.255, far below the P >= 0.929 expected for the nearest sampled point to an in-window resonance.

I also compared the full scan shape against the model over possible resonance centers within the scanned frequency range. A fixed 22% contrast resonance model, allowing only a baseline scale factor, gives best RMSE = 0.0557 in normalized ratio, worse than a flat no-resonance model with RMSE = 0.0281. Allowing the dip contrast itself to float gives a best positive-dip contrast of about 5.0%, not the expected 22%.

The stored averages are not treated as strong independent repeatability evidence because they can reflect tracking cadence. They also do not rescue the resonance interpretation: same-average normalized minima are about 5.0% and 8.6%, still far below the expected near-pi-pulse contrast.

Decision:

The active pulse should be a near-pi pulse on resonance and should create a large negative pODMR dip in readout 2 relative to the m_S = 0 reference. The data show only small fluctuations and no physically sized dip. I therefore decide that a pODMR resonance is absent in this scan.
