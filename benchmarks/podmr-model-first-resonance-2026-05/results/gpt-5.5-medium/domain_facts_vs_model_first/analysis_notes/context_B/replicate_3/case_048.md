Case podmr_034_2026-05-16-204545

Active sequence identification:
- Sequence file: Rabimodulated.xml.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active measurement sequence is:
  1. optical polarization,
  2. detection of the polarized m_S = 0 reference,
  3. wait,
  4. one rabi_pulse_mod_wait_time pulse,
  5. detection after the microwave pulse.
- Therefore readout 1 is the polarized m_S = 0 reference and readout 2 is the signal after the Rabi-modulated microwave pulse.
- From the provided sequence XML and variable values, mod_depth = 1 and length_rabi_pulse = 52 ns.

Physical model calculation:
- Setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square resonant pulse, population transfer is P = sin^2(pi * f_R * tau).
- With f_R = 10 MHz and tau = 52 ns, f_R * tau = 0.52, so P = sin^2(pi * 0.52) = 0.996.
- Expected fractional PL drop at resonance is therefore 0.22 * 0.996 = 0.219, about 22%.
- With raw readouts near 50 counts, a resonant point should lower readout 2 relative to readout 1 by about 11 counts, with a localized trough over the pulse bandwidth.

Data comparison:
- Mean readout 1 = 50.016 counts.
- Mean readout 2 = 49.366 counts.
- Mean fractional contrast (readout1 - readout2) / readout1 = 1.28%.
- Largest positive fractional contrast is 5.22%, occurring at scan values 3.830 GHz and 3.850 GHz, far below the expected about 22%.
- The contrast also changes sign at several points, with readout 2 exceeding readout 1 at 3.855, 3.860, 3.875, 3.885, 3.915, and 3.925 GHz.
- Stored averages are only two and may reflect tracking cadence, so I do not treat the per-average overlay as a strong independent repeatability test.

Decision:
The expected resonant signal for the active pulse is a large localized drop in readout 2 relative to the m_S = 0 reference. The measured scan only shows small, sign-changing fluctuations, so a pODMR resonance is absent.
