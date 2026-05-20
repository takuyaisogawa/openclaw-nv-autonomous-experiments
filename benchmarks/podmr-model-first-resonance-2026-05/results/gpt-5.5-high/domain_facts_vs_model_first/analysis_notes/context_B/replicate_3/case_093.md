Case podmr_079_2026-05-17-103702

Input basis:
- Used the provided sequence XML and raw export numeric data only.
- Active sequence is Rabimodulated.xml / Rabimodulated behavior: polarize, detect, wait, modulated Rabi pulse, detect, wait.
- The first detection occurs immediately after optical polarization and is the true mS = 0 reference readout.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped; do_adiabatic_inversion is not active for the acquired readouts.
- The second detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so readout 2 is the pODMR-sensitive signal readout.
- Active pulse duration: length_rabi_pulse = 52 ns after sample-rate rounding.
- Active mod_depth: 1.

Physical model calculation:
For this setup the on-resonance Rabi frequency is about 10 MHz at mod_depth = 1. With a rectangular resonant pulse, the transition probability is

P(delta = 0) = sin^2(pi * f_Rabi * tau)

where f_Rabi = 10 MHz and tau = 52 ns. Numerically,

pi * 10e6 * 52e-9 = 1.6336 rad
P(delta = 0) = sin^2(1.6336) = 0.996

The setup contrast between mS = 0 and mS = +1 is about 22%, so an on-resonance pi-like pulse should reduce readout 2 by

0.22 * 0.996 = 0.219

or about 21.9% of the mS = 0 fluorescence. On the observed approximately 51 count raw-readout scale, this is about 11.2 counts. This is the expected signature if the scan crosses the addressed transition: readout 2 should show a strong dip relative to readout 1 near resonance. The detuned rectangular-pulse model used for comparison was

P(delta f) = (f_Rabi^2 / (f_Rabi^2 + delta f^2)) * sin^2(pi * tau * sqrt(f_Rabi^2 + delta f^2))

with the fluorescence model ratio = baseline - 0.22 * P(delta f).

Observed data:
- Readout 1 mean = 50.718, standard deviation = 1.141, range = 48.500 to 53.404.
- Readout 2 mean = 50.782, standard deviation = 0.859, range = 49.558 to 52.788.
- Normalized readout 2 / readout 1 mean = 1.0017, standard deviation = 0.0253, range = 0.9607 to 1.0476.
- The lowest readout 2 point is at 3.860 GHz, but readout 1 is also low there and the normalized ratio is 1.013, not a dip.
- The lowest normalized ratio is about 0.961, only a 3.9% reduction relative to the local reference, far below the modeled 21.9% resonant reduction.
- A least-squares fit allowing the rectangular-pulse feature center to float does not find a physical dip. The best free-amplitude fit wants a positive feature coefficient, while imposing the physical 22% dip gives a much worse residual than a nearly flat normalized trace.

Decision:
The active pulse should produce a near full-contrast pODMR dip if a resonance is present in the scanned frequency window. The measured pODMR-sensitive readout lacks a dip of the expected sign and magnitude after reference normalization. The stored averages do not provide a strong independent repeatability test, but the expected effect is large enough that it should dominate the observed few-percent fluctuations. I therefore classify this case as resonance_absent.
