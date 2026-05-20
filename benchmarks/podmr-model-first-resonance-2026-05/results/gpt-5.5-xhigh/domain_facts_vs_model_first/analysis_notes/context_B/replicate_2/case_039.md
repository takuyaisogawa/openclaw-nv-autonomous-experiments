Case: podmr_024_2026-05-16-175646

Files used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The sequence first performs adj_polarize, then detection. This is the polarized m_S = 0 reference readout.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive despite do_adiabatic_inversion being true.
- The active microwave operation is one rabi_pulse_mod_wait_time call followed by detection. This second detection is the pODMR signal readout after the MW pulse.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the MW-pulsed signal.
- Provided sequence.xml and exported Variable_values give length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1. The saved sequence text embedded in raw_export.json contains an older-looking default line with mod_depth = 0.3, but the exported run variables and provided XML both record mod_depth = 1, so I used mod_depth = 1 for the active run.

Quantitative expected signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the 52 ns pulse has f_R * t = 10e6 * 52e-9 = 0.52 Rabi cycles.
- For a rectangular resonant pulse starting from m_S = 0, the transferred population is P_1 = sin^2(pi * f_R * t) = sin^2(pi * 0.52) = 0.996.
- With the stated contrast scale C = 0.22 between m_S = 0 and m_S = +1, the expected fractional PL drop at exact resonance is C * P_1 = 0.219.
- The mean readout-1 level is 53.855, so the expected resonant drop is about 53.855 * 0.219 = 11.8 raw-readout units. The expected signal readout at a grid-centered resonance would be about 42.1.
- Including detuning for the rectangular pulse, P_1(delta) = Omega^2/(Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t), with Omega = 2*pi*10 MHz. The expected contrast drops are:
  - 0 MHz detuning: 21.9%
  - 2.5 MHz detuning: 20.4%
  - 5 MHz detuning: 16.5%
  - 10 MHz detuning: 6.0%
- Since the scan step is 5 MHz, any resonance inside the swept range should place at least one sampled point within 2.5 MHz of the resonance and should therefore show roughly a 20% drop in readout 2 relative to readout 1.

Observed data:
- Combined paired normalized contrast, computed as (readout1 - readout2) / readout1, has mean -0.0061 and standard deviation 0.0211.
- The largest positive value is only 0.0307 at 3.895 GHz, corresponding to a 1.65 raw-unit signal drop. This is about 14% of the expected 11.8 raw-unit drop for the active mod_depth = 1 pulse.
- The neighboring points do not show the expected broad pulse-response shape: at 3.890 GHz the contrast is -0.0054 and at 3.900 GHz it is -0.0103, both opposite in sign to a resonance dip.
- A linear-baseline plus expected line-shape fit over possible centers gives the best center near 3.891 GHz but with amplitude scale only about 0.18 of the expected active-pulse response, and the residual scatter remains about 0.017 normalized units. This is consistent with readout noise/tracking variation rather than the predicted pODMR response.
- The two stored averages have large baseline offsets, consistent with tracking cadence, so I did not treat them as a strong independent repeatability test.

Decision:
The active 52 ns, mod_depth = 1 pulse should create a large near-pi-pulse ODMR dip if the transition is within the scan. The observed paired readout changes are much smaller than the physical expectation and lack the expected detuning profile. I therefore decide that a pODMR resonance is absent.
