Case podmr_022_2026-05-16-172725

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Detection/readout roles from the provided XML: readout 1 is the "true 0 level reference" immediately after optical polarization; readout 2 is the signal readout after the Rabi-modulated microwave pulse. The optional 1-level reference block is inactive because full_expt = 0.
- Relevant pulse parameters: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, freqIQ = 50 MHz.

Quantitative expected-signal model:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the pulse has f_R = 10 MHz.
- For a resonant rectangular Rabi pulse, transferred population is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce readout 2 relative to readout 1 by about 0.22 * 0.996 = 21.9% of the readout level.
- The mean readout 1 level is 46.762 raw-count units, so the expected resonant drop is about 10.25 counts.

Data comparison:
- Mean readout 1 = 46.762.
- Mean readout 2 = 46.834.
- Mean readout2/readout1 = 1.002.
- The pointwise readout2 - readout1 differences range from -3.269 to +2.212 counts, with mean +0.072 counts and standard deviation 1.484 counts.
- The largest observed dip, -3.269 counts at 3.890 GHz, is only about 32% of the expected -10.25 count resonant pi-pulse signal and is not accompanied by the expected approximately 22% contrast scale.
- Stored averages show drift/tracking-like offsets in individual averages, so they are not treated as a strong independent repeatability test.

Decision:
The active pulse should produce a large near-pi-pulse pODMR dip if an addressed resonance is present in the scanned range. The combined readouts do not show that physical-scale drop; readout 2 remains comparable to readout 1 across the scan. Therefore the pODMR resonance is absent.
