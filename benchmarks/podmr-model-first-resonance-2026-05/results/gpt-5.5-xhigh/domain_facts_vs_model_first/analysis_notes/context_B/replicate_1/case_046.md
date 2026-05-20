Case: podmr_032_2026-05-16-201700

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the active instruction path, full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- Readout 1 is the detection immediately after adj_polarize, before the microwave Rabi pulse. It is the bright m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(... length_rabi_pulse, mod_depth ...). It is the pODMR signal readout after the driven pulse.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, this is exactly 13 samples, so rounding leaves 52 ns.
- mod_depth = 1 in the provided sequence XML and in the exported runtime Variable_values. The embedded raw_export Sequence text contains an older default of 0.3, but the active value used here is the provided/runtime value of 1.
- do_adiabatic_inversion is not used in the active pulse path; the adiabatic call is commented and the full_expt block is disabled.

Quantitative model:
The setup contrast between m_S = 0 and m_S = +1 is C = 0.22. The given Rabi frequency is about 10 MHz at mod_depth = 1, so f_R = 10 MHz. For a rectangular resonant drive, I used the two-level Rabi response

P1(d) = f_R^2 / (f_R^2 + d^2) * sin^2(pi * t * sqrt(f_R^2 + d^2))

where d is detuning in Hz and t = 52 ns. The expected normalized readout depression is C * P1(d), so signal/readout reference should be 1 - C * P1(d).

On resonance:
P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
Expected contrast depression = 0.22 * 0.996 = 0.219, or 21.9%.
The mean readout 1 level is 55.26 raw units, so the expected on-resonance readout-2 loss is about 12.1 raw units.

Because the scan step is 5 MHz, even a resonance halfway between sampled points would have d = 2.5 MHz at the nearest point:
P1(2.5 MHz) = 0.929, expected depression = 20.4%, about 11.3 raw units.
At d = 5 MHz, expected depression is still 16.5%, about 9.1 raw units.

Measured contrast calculation:
I computed observed contrast as (readout1 - readout2) / readout1 for the combined readouts.
- Mean observed contrast: -0.043%.
- Standard deviation across scan points: 2.75%.
- Maximum positive depression: 4.18% at 3.830 GHz, equal to 2.35 raw units.
- At 3.875 GHz the signal is higher than the reference by 3.94 raw units, giving -7.29% contrast, opposite the expected resonance sign.
- No scan point has a depression close to the 9-12 raw units expected for the active pulse model.

Model comparison:
Using the fixed physical contrast C = 0.22 and allowing the resonance center to vary inside the scanned band, the best rectangular-pulse model fit is at the high-frequency edge and has normalized SSE 0.0773. A flat no-resonance model has normalized SSE 0.0151, so the physically expected resonance model is much worse than no resonance.

If the Rabi model shape is allowed to fit an arbitrary positive contrast amplitude, the best amplitude is only 2.77%, about 8 times smaller than the expected 21.9% on-resonance contrast for mod_depth = 1. That small fitted amplitude is comparable to the point-to-point readout scatter and does not match the active pulse expectation.

The two stored averages mainly show a brightness offset between tracking intervals, so I did not treat them as a strong independent repeatability test. The combined readout comparison is still decisive because the expected active-pulse signal is much larger than the observed depressions.

Decision: resonance_absent.
