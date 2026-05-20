Case: podmr_080_2026-05-17-105113

Sequence identification:
- Sequence file: Rabimodulated.xml.
- Active sequence path: polarize, detection, wait, Rabi-modulated microwave pulse, detection, final wait.
- full_expt = 0, so the intermediate "1 level reference" branch is inactive even though do_adiabatic_inversion is set true.
- Readout 1 role: optical detection immediately after polarization, the mS = 0 / bright reference.
- Readout 2 role: optical detection after the microwave Rabi pulse, the pODMR signal readout.
- mod_depth = 1 from the provided XML variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate to 52 ns.

Physical signal model:
The setup contrast between mS = 0 and mS = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the driven population transfer versus detuning is

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),

with Omega = 2*pi*10 MHz, Delta = 2*pi*(f - f0), and tau = 52 ns. On resonance,
P0 = sin^2(pi * 10e6 * 52e-9) = 0.996.

Therefore, a real on-resonance pODMR feature should make the post-pulse readout dimmer than the mS = 0 reference by approximately
0.22 * 0.996 = 0.219, or about 21.9% of the bright readout. The observed bright reference is about 51.67 counts, so the expected on-resonance drop is about 11.32 counts.

Observed data check:
- Mean readout 1 = 51.67 counts.
- Mean readout 2 = 51.70 counts.
- Mean readout2 - readout1 = +0.03 counts.
- Minimum observed readout2 - readout1 = -1.81 counts at 3.895 GHz.
- Maximum observed readout2 - readout1 = +1.52 counts.
- Standard deviation of readout2 - readout1 across the scan = 0.88 counts.

I fit the expected detuned Rabi response shape across possible resonance centers in the scanned frequencies to the observed readout2-readout1 trace. The best unconstrained fit wanted the opposite sign: readout 2 increasing at the modeled resonance rather than decreasing. A fixed-amplitude physical model with the expected 11.3 count negative dip gives much larger residuals than a constant/no-resonance baseline.

Decision:
No pODMR resonance is present. The active pulse should produce a large negative readout-2 feature if it is resonant, but the measured differences are small, sign-inconsistent, and comparable to raw point-to-point noise/tracking variation.
