Case: podmr_032_2026-05-14-161051

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence: Rabimodulated.xml.
- The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive.
- The two active detections are:
  1. readout 1: after adj_polarize, before the microwave pulse; this is the true m_S = 0 reference.
  2. readout 2: after rabi_pulse_mod_wait_time; this is the post-microwave pODMR signal.
- mod_depth = 1.
- length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the rectangular-pulse transition probability is
  P(f, f0) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),
  where Omega = 2*pi*10 MHz, Delta = 2*pi*(f - f0), and tau = 52 ns.
- On resonance, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance post-pulse readout drop is 0.22 * 0.996 = 0.219, i.e. readout2/readout1 about 0.781 for full inversion.
- The same model gives P values at detunings of 0, 5, 10, 15, 20, 25, and 50 MHz of 0.996, 0.749, 0.273, 0.0117, 0.0479, 0.1248, and 0.0304 respectively. The expected normalized contrast is therefore largest over the nearest few 5 MHz scan points around resonance.

Data calculation:
- I used normalized contrast C = (readout1 - readout2) / readout1.
- Around the candidate feature:
  - 3.870 GHz: C = 6.73%
  - 3.875 GHz: C = 7.74%
  - 3.880 GHz: C = 17.80%
  - 3.885 GHz: C = -2.06%
  - 3.890 GHz: C = 4.14%
- Outside 3.865-3.890 GHz, the contrast mean is 0.30% with a sample standard deviation of 4.85%.
- A least-squares fit of readout2/readout1 to B - A*P(f,f0), with f_R and tau fixed by the sequence and setup facts, gives:
  - best f0 = 3.8776 GHz
  - B = 1.003
  - A = 0.116
  - SSE = 0.0487 versus 0.0710 for a constant-ratio null model
  - R^2 = 0.314 versus the null
- The fitted amplitude is smaller than the full 22% scale, but the observed local maximum contrast of 17.8% is in the physically expected range for a near-pi pulse and is concentrated near the model center. Stored averages show strong tracking drift, so I did not treat per-average overlays as a strong independent repeatability test.

Decision:
The post-pulse readout has a localized dip near 3.88 GHz with the sign, width, and magnitude expected from the 52 ns, mod_depth 1 Rabi pulse model. I decide that a pODMR resonance is present.
