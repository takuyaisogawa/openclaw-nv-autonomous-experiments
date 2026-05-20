Case: podmr_010_2026-05-16-114624

I used only the provided sequence and raw export for this decision.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The active readout flow is: polarize, detection, wait, microwave Rabi-modulated pulse, detection, wait.
- full_expt is 0, so the optional mS=+1 reference block is disabled. Therefore readout 1 is the post-polarization mS=0 optical reference, and readout 2 is the signal after the scanned microwave pulse.
- Pulse duration: length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already an integer 13 samples, so rounding does not change it.
- mod_depth: inputs/sequence.xml and the exported Variable_values report mod_depth = 1. The embedded Sequence text in raw_export.json contains an inconsistent stale-looking mod_depth = 0.3 string, but the explicit XML file requested for the decision and the numeric exported variable values both give 1.

Quantitative expected-signal model:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. The resonant transition probability for a rectangular pulse is

P1(delta=0) = sin^2(pi * f_Rabi * tau).

Using f_Rabi = 10 MHz and tau = 52 ns:

P1 = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated mS=0 to mS=+1 contrast scale of about 22%, a resonant pulse should reduce the signal readout by about

0.996 * 22% = 21.9%

relative to the bright mS=0 reference scale. In counts, using the combined readout-1 mean of 38.74, the expected resonant drop is about 8.49 counts.

I also checked the finite-detuning rectangular-pulse response:

P1(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * tau * sqrt(f_Rabi^2 + delta^2)).

For 5 MHz scan spacing around a resonance center, the model gives expected contrast drops:
- delta = -10 MHz: 6.0%
- delta = -5 MHz: 16.5%
- delta = 0 MHz: 21.9%
- delta = +5 MHz: 16.5%
- delta = +10 MHz: 6.0%

Observed combined data:
- Baseline normalized readout-2/readout-1 ratio away from the central feature is 0.9827.
- The minimum normalized ratio occurs at scan value 3.875 GHz: readout 1 = 40.904, readout 2 = 31.192, ratio = 0.7626.
- This is a 23.7% drop relative to the same-point readout-1 reference, or a 22.4% extra drop relative to the off-resonance normalized baseline.
- Neighboring normalized extra drops around 3.875 GHz are approximately 16.2% at -5 MHz, 22.4% at center, 14.2% at +5 MHz, and 5.3% at +10 MHz, closely matching the rectangular-pulse model values above.

The stored averages show drift/tracking changes and are not a strong independent repeatability test, as expected from the domain note. The combined normalized signal nevertheless has the expected amplitude and line shape for a pODMR resonance under the active 52 ns, mod_depth 1 pulse.

Decision: resonance_present.
