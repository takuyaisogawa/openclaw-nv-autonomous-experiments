Case: podmr_057_2026-05-17-051839

Input files used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual check of the same raw readouts

Sequence identification from the provided XML:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz, so the requested 52 ns pulse is rounded to 52 ns exactly because 52 ns * 250 MHz = 13 samples.
- mod_depth = 1 in the provided sequence XML and in raw_export Variable_values.
- length_rabi_pulse = 52 ns.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- Readout 1 role: true mS = 0 reference after optical polarization and before the Rabi pulse.
- Readout 2 role: signal readout after the 52 ns modulated Rabi pulse.

Physical model calculation:
Use the driven two-level pulse model for the mS = 0 to mS = +1 transition:

P1(delta) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * t * sqrt(fR^2 + delta^2))

where fR is the on-resonance Rabi frequency in cycles/s, delta is detuning in Hz, and t is the pulse duration. The setup facts give fR = 10 MHz * mod_depth, so with mod_depth = 1, fR = 10 MHz. With t = 52 ns:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between mS = 0 and mS = +1 is about 22%, so the expected resonant normalized pODMR dip is:

0.22 * 0.996 = 0.219, or 21.9%.

The mean readout-1 level is 45.46 counts, so an on-resonance point should drop by about:

45.46 * 0.219 = 9.96 counts.

Data comparison:
- Mean readout 1 = 45.46 counts.
- Mean readout 2 = 45.42 counts.
- Mean normalized contrast 1 - readout2/readout1 = 0.07%.
- Standard deviation of pointwise normalized contrast = 2.16%.
- Largest measured reduction is 4.50% at 3.925 GHz, corresponding to a 2.08 count drop.

This largest measured reduction is only about one fifth of the 21.9% reduction expected for a resonant 52 ns pi pulse at mod_depth = 1, and it occurs at the scan edge rather than as a clear resonance profile. A fixed-amplitude two-level model constrained to have the resonance center inside the scanned frequency range fits much worse than a flat no-resonance model because it requires a roughly 22% dip at or near the resonance. Allowing a resonance center outside the scan can mimic a small edge shoulder, but that is not evidence for a pODMR resonance being present in the measured window.

Decision: resonance_absent.
