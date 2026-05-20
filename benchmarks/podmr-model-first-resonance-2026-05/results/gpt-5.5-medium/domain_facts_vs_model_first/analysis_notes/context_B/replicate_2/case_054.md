Case podmr_040_2026-05-16-222642

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped.
- Readout 1 is the initial bright reference after adj_polarize and detection, before the Rabi pulse.
- Readout 2 is the detection after the microwave Rabi pulse.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- From the provided sequence XML, mod_depth = 1.

Quantitative expected-signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling, f_R = 10 MHz here.
- For a rectangular resonant pulse, transferred population P(detuning=0) = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given the setup contrast scale of 22%, the expected on-resonance fluorescence ratio for the post-pulse readout is approximately 1 - 0.22 * 0.996 = 0.781 relative to the bright reference.
- The mean readout-1 reference is 47.188 counts, so the expected on-resonance drop is about 47.188 * 0.22 * 0.996 = 10.34 counts.

Observed data:
- Mean readout 1 = 47.188 counts; mean readout 2 = 46.660 counts.
- The post-minus-reference difference has mean -0.527 counts and standard deviation 1.345 counts.
- The largest observed post-pulse suppression is at 3.885 GHz: readout 1 = 48.365, readout 2 = 44.673, difference = -3.692 counts, ratio = 0.924.
- No point approaches the expected ratio of about 0.781 or the expected drop of about 10.34 counts for a resonant 52 ns pi pulse at mod_depth = 1.

Model comparison:
- I used the detuned rectangular-pulse model
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))
  and converted it to counts with -reference_mean * 0.22 * P(delta).
- Allowing the resonance center to vary across the scanned frequency range and allowing a constant offset, the best resonance-model SSE was 139.97.
- A flat no-resonance model using only the mean post-minus-reference difference had SSE 36.17.
- Thus the expected physical resonance signature is not present in the readout differences; the variations are much smaller and are better described as drift/noise than as the expected pODMR response.

Decision: resonance_absent.
