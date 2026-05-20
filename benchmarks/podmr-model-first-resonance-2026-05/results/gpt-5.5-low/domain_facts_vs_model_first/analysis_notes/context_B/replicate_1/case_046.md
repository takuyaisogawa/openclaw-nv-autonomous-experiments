Case: podmr_032_2026-05-16-201700

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence: Rabimodulated, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect before any microwave pulse. Therefore readout 1 is the true m_S = 0 reference.
- full_expt = 0 disables the separate m_S = 1 reference block.
- The active pODMR signal is readout 2, acquired after the single rabi_pulse_mod_wait_time pulse.
- Pulse duration: length_rabi_pulse = 52 ns. At the 250 MHz sample rate this is exactly 13 samples, so rounding does not materially change it.
- The provided sequence.xml lists mod_depth = 1. The embedded sequence text in raw_export.json contains mod_depth = 0.3, while Variable_values reports mod_depth = 1; I therefore calculated the expected signal for both, using the provided XML value as primary.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency scaling: f_R = 10 MHz * mod_depth.
- For a resonant square pulse of duration t, transferred population P = sin^2(pi * f_R * t).
- Expected fractional fluorescence dip on resonance is C * P.

For mod_depth = 1:
- f_R = 10 MHz.
- t = 52 ns.
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional dip = 0.22 * 0.996 = 0.219.
- With a reference level near 55.26 counts, expected on-resonance dip is about 12.1 raw-count units.

For mod_depth = 0.3:
- f_R = 3 MHz.
- P = sin^2(pi * 3e6 * 52e-9) = 0.222.
- Expected fractional dip = 0.0487.
- With a reference level near 55.26 counts, expected on-resonance dip is about 2.69 raw-count units.

Observed data check:
- Mean readout 1 = 55.255 counts.
- Mean readout 2 = 55.262 counts.
- Mean signal/reference ratio = 1.0004.
- The post-pulse signal readout does not show a negative dip of either expected scale.
- Around the nominal middle of the scan, 3.875 GHz, readout 2 is 58.06 counts and signal/reference is 1.073, which is a positive excursion, not the expected pODMR fluorescence loss.
- A linear-baseline residual check on readout 2 gives the largest positive residual at 3.875 GHz (+2.80 counts), while the deepest negative residual occurs at 3.920 GHz (-1.99 counts), below even the conservative 2.69-count expectation and not forming a convincing resonance feature.
- Stored averages differ substantially in offset and appear consistent with tracking cadence effects, so I did not treat per-average repetition as strong independent confirmation.

Decision:
The relevant model predicts a negative fluorescence dip in the post-pulse signal at resonance. The measured post-pulse signal and signal/reference ratio show no such dip, and the central feature has the opposite sign. I decide resonance_absent.
