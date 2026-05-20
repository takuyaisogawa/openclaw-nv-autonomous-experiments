Case podmr_011_2026-05-16-120107

Sequence/readout identification:
- Provided sequence XML is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active readout structure is: polarize, detect, wait; optional m_S=1 reference block; Rabi-modulated microwave pulse, detect, wait.
- full_expt = 0, so the optional m_S=1 reference block is disabled even though do_adiabatic_inversion is true. The stored two readouts are therefore:
  - readout 1: true m_S=0 reference after optical polarization.
  - readout 2: signal after the Rabi-modulated microwave pulse.
- Active microwave pulse for the pODMR test is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative expected-signal model:
- Given setup contrast between m_S=0 and m_S=+1 is about 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, the active Rabi frequency is 10 MHz.
- For a square pulse, the resonant transfer probability is P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The median readout-1 level is 42.29 counts, so a full resonant transfer should reduce readout 2 by about 42.29 * 0.22 * 0.996 = 9.27 counts, giving an expected resonant readout-2 value near 33.02 counts.

Data comparison:
- The measured readout-2 minimum is 33.10 counts at 3.880 GHz.
- The simultaneous readout-1 value at that point is 41.40 counts, so the local observed drop is 8.31 counts, or 20.1%.
- This is within the expected contrast scale for a near-pi pulse, and readout 1 does not show a matching dip.
- A two-level detuned Rabi lineshape model, fitting readout2 = baseline - amplitude * P_transfer(freq), gives a best center near 3.87825 GHz, baseline 41.72 counts, and dip amplitude 8.62 counts. The fitted amplitude is consistent with the 22% contrast expectation after allowing for count noise and baseline drift.
- Stored averages are only two averages and can reflect tracking cadence, so I did not treat per-average agreement as a strong independent repeatability test.

Decision:
The readout-2 dip has the expected amplitude, location, and approximate width for the active 52 ns, mod_depth 1 Rabimodulated pODMR pulse, while readout 1 remains a reference trace. A pODMR resonance is present.
