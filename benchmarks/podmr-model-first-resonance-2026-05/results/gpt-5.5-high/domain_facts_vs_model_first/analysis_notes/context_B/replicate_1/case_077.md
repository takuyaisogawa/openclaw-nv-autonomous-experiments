Case: podmr_063_2026-05-17-064555

I used the provided sequence XML, not labels or sibling cases. The active sequence is Rabimodulated.xml. The sequence first performs adjacent polarization and detection, so readout 1 is the true m_S = 0 reference. Because full_expt = 0, the conditional m_S = +1 reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and performs the final detection, so readout 2 is the pODMR signal after the microwave pulse.

Relevant XML parameters:

- length_rabi_pulse = 52 ns, rounded on a 250 MHz sample clock; 52 ns is already 13 samples.
- mod_depth = 1 in the provided XML and exported variable values.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active pulse is a rectangular modulated Rabi pulse, not the adiabatic inversion block.

Explicit model calculation:

Use the driven two-level transition probability for a square pulse,

P_transfer(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * tau),

with f_R = 10 MHz at mod_depth = 1 and tau = 52 ns. The current setup contrast scale is about C = 0.22, so the expected fractional readout depression of readout 2 relative to the m_S = 0 reference is C * P_transfer.

The calculated profile is:

- 0 MHz detuning: P_transfer = 0.996, expected fractional dip = 0.219, or about 11.4 counts for a 52-count reference.
- 5 MHz detuning: P_transfer = 0.749, expected fractional dip = 0.165, or about 8.6 counts.
- 10 MHz detuning: P_transfer = 0.273, expected fractional dip = 0.060, or about 3.1 counts.
- 15 MHz detuning: P_transfer = 0.012, expected fractional dip = 0.003, or about 0.1 counts.

Thus, if the swept microwave frequency crosses resonance on this 5 MHz grid, the provided XML predicts a very large, localized depression in readout 2: nearly a full-contrast pi-pulse response at the center and still a large response one scan step away.

Observed data:

- readout 1 mean = 51.821 counts, standard deviation = 1.494 counts.
- readout 2 mean = 51.403 counts, standard deviation = 1.526 counts.
- readout1 - readout2 mean = 0.418 counts, standard deviation = 1.360 counts.
- readout1 - readout2 range = -1.692 to +2.731 counts.
- readout2/readout1 mean = 0.9922, standard deviation = 0.0261.
- readout2/readout1 minimum = 0.9496, maximum = 1.0329.

The largest observed readout-2 depression relative to readout 1 is about 2.73 counts, or 5.0%, and it is not accompanied by the multi-point 10 to 20% dip expected from the 52 ns, mod_depth 1 pulse. Several neighboring points instead have readout 2 equal to or higher than readout 1.

I also compared ratio models after allowing a linear baseline drift in readout2/readout1. The null drift-only fit has SSE = 0.013421 and RMSE = 0.0253. A resonance model with the physically fixed 22% contrast and the square-pulse transition profile, scanning the unknown resonance center over the measured frequency range, gives best SSE = 0.036796 and RMSE = 0.0419, which is worse than the null. If the resonance amplitude is allowed to float freely, the best fit amplitude is only 0.0519 fractional contrast, far below the expected 0.22 for the provided mod_depth and pulse duration; this is consistent with noise and tracking drift rather than the expected physical pODMR response.

The stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence. They also do not show a stable expected full-contrast resonance response.

Decision: resonance absent. The physically expected pODMR signal for the active sequence should be much larger than the observed readout-to-readout deviations, and the fixed physical model is not supported by the data.
