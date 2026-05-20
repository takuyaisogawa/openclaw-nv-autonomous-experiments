Case: podmr_082_2026-05-17-111957

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence file: Rabimodulated.xml.
- The active scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is not active.
- The active readouts are therefore:
  1. readout 1: after adj_polarize, before the Rabi pulse; this is the bright m_S = 0 reference.
  2. readout 2: after one rabi_pulse_mod_wait_time pulse and then detection; this is the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s remains 52 ns.

Expected physical signal calculation:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square resonant pulse, transition probability P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10e6 Hz and tau = 52e-9 s:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant pulse should make readout 2 darker than readout 1 by about:
  mean(readout 1) * 0.22 * 0.996 = 50.375 * 0.22 * 0.996 = 11.04 counts.
- Therefore, if a resonance lies in the swept range and the active pulse addresses it, readout 2 should show a localized dip toward roughly 39.34 counts at resonance, not merely a 1-3 count fluctuation.

Observed quantitative checks:
- mean(readout 1) = 50.375.
- mean(readout 2) = 50.028.
- mean(readout 2 - readout 1) = -0.347 counts.
- standard deviation of readout 2 - readout 1 over scan points = 1.529 counts.
- strongest observed deficit readout 1 - readout 2 = 3.462 counts, at 3.850 GHz.
- This strongest deficit is only about 31% of the expected full resonant drop and is comparable to point scatter, while other points show readout 2 above readout 1.
- A forced square-pulse dip fit over candidate resonance centers gives best amplitude about 2.91 counts, far below the expected about 11.04 counts.
- Stored averages are only two averages and may reflect tracking cadence, so I do not treat per-average similarity as a strong independent repeatability test.

Decision:
The active sequence should produce a large dark pODMR dip if resonance is present in the scanned band. The observed second readout has no quantitatively compatible resonance-depth feature, and the possible dip-like fluctuations are much smaller than the expected signal. I therefore decide resonance_absent.
