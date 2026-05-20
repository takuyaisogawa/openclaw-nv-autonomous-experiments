Case: podmr_047_2026-05-17-001223

Input basis used: only inputs/sequence.xml and inputs/raw_export.json from this isolated workspace.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Active readout 1 is the "true 0 level reference" after laser polarization and detection.
- Active readout 2 is the detection after one rabi_pulse_mod_wait_time pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.

Explicit expected-signal calculation:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, use f_R = 10 MHz.
- For a resonant square pulse, transferred population P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fluorescence change is 0.22 * 0.996 = 21.9% of the bright readout.
- The measured readout 1 mean is 50.38 counts, so the expected resonance drop in readout 2 relative to readout 1 is about 50.38 * 0.219 = 11.04 counts.

Observed data:
- Mean readout 2 - readout 1 = -0.32 counts.
- Standard deviation of pointwise readout 2 - readout 1 = 1.42 counts.
- Most negative point is -2.73 counts at 3.905 GHz, far smaller than the expected approximately -11 count resonant feature.
- The trace also has positive excursions up to +2.54 counts, so the negative excursions are consistent with scan noise/tracking-scale variation rather than a robust Rabi-driven ODMR dip.
- Stored averages are only two and are not treated as a strong independent repeatability test, per the provided domain note.

Decision:
The physically expected resonant signal for the active pulse is large and negative in readout 2 relative to readout 1, but no such feature is present anywhere in the scanned range. The pODMR resonance is therefore absent.
