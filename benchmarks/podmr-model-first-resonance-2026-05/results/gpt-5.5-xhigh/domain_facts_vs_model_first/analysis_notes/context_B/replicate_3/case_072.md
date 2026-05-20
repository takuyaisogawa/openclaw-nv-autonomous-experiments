Case podmr_058_2026-05-17-053345

I used the provided Rabimodulated.xml sequence. The active sequence takes an optical-polarized detection first, then skips the optional +1 reference block because full_expt = 0, then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) and detects again. Therefore readout 1 is the polarized mS = 0 reference and readout 2 is the post-microwave signal readout.

Active pulse parameters from the provided sequence XML / variable values:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s
- sample_rate = 250 MHz, so the rounded pulse remains 13 samples = 52 ns

Physical model calculation:
- Given f_Rabi = 10 MHz at mod_depth = 1.
- For a resonant square Rabi pulse starting in mS = 0, P(+1) = sin^2(pi * f_Rabi * t).
- With t = 52 ns, P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale C = 0.22, the expected resonant fluorescence depletion in readout 2 relative to readout 1 is C * P(+1) = 0.219, so the expected normalized readout-2/readout-1 ratio is about 0.781 at a sampled resonance.
- At the mean reference level of 45.68 counts, that is an expected drop of about 10.0 counts.

Measured readout comparison:
- The largest measured normalized depletion (readout1 - readout2) / readout1 is 0.0688.
- The minimum measured readout2/readout1 ratio is 0.9312.
- The largest measured count drop is 3.23 counts.
- A fixed-contrast Rabi-line model with the resonance center inside the scan expects about 0.20 depletion at the two nearest 3.885/3.890 GHz points if centered between them, but the observed depletion there is only about 0.069.
- With a constant offset allowed, the fixed 22% contrast model centered within the scan fits worse than a constant no-resonance contrast baseline (SSE 0.0667 versus 0.0320 for the measured normalized depletion).

Decision:
The active pulse should generate an almost full-contrast pODMR dip if a resonance is sampled, but the observed readout-2 depletion is small, irregular, and not compatible with the expected Rabi-line amplitude. I therefore decide resonance_absent.
