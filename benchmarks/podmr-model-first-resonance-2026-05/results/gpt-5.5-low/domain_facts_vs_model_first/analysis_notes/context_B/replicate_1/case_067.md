Case podmr_053_2026-05-17-042031

Sequence identification:
- Active sequence: Rabimodulated.xml.
- Swept variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Pulse sequence roles: first polarization plus detection is the bright m_S=0 reference readout. The "Acquire 1 level reference" block is inactive because full_expt = 0, so there is no independent dark-state reference readout. The final readout after rabi_pulse_mod_wait_time is the pODMR signal readout.
- Relevant pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1 in the provided sequence XML.

Expected signal model:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the resonant transition probability for a square Rabi pulse is
  P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10e6 Hz and t = 52e-9 s:
  P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- With the setup contrast scale of about 22% between m_S=0 and m_S=+1, the expected resonant fluorescence drop in the signal readout relative to the bright reference is about
  0.22 * 0.996 = 0.219, or 21.9%.

Observed data:
- The two combined readouts are close in scale: mean readout 1 = 45.20 and mean readout 2 = 45.02.
- Pointwise contrast (readout1 - readout2) / readout1 ranges from about -8.4% to +7.2%.
- The largest apparent signal dip is at 3.880 GHz, where readout 1 = 45.885 and readout 2 = 42.596, giving 7.2% contrast. A second dip-like point appears at 3.890 GHz with 7.0% contrast.
- These dips are roughly one third of the expected near-pi-pulse contrast and occur in data with substantial drift/average-to-average variation. Stored averages likely reflect tracking cadence, so they are not strong independent repeatability evidence.

Decision:
The expected pODMR resonance for the active 52 ns, mod_depth 1 Rabi pulse should be a near-full contrast response of about 22%. The observed readout-2 suppression is much smaller, irregular, and not compelling against the drift/noise scale. I therefore decide that a pODMR resonance is absent.
