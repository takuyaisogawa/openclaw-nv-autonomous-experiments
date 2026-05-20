Case: podmr_042_2026-05-16-225623

Sequence and readout roles:
- The active sequence is Rabimodulated.xml.
- The provided sequence.xml sets length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz, and scans mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The first detection follows adj_polarize and is the polarized m_S = 0 reference readout.
- The explicit m_S = 1 reference block is disabled by full_expt = 0.
- The second detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and is the microwave-pulse signal readout.
- The raw export also contains an embedded sequence text with mod_depth = 0.3, but the provided sequence.xml and exported Variable_values give mod_depth = 1. I used mod_depth = 1 per the provided XML and active variable values.

Physical model calculation:
Use a two-level driven transition model for the pulse response,

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

Given the setup facts, f_R = 10 MHz * mod_depth = 10 MHz and t = 52 ns. On resonance:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected resonant post-pulse fluorescence ratio is approximately

readout2 / readout1 = 1 - 0.22 * 0.996 = 0.781.

Equivalently, for raw readouts near 46 to 49 counts, an on-resonance pi-like pulse should lower readout 2 by roughly 10 counts relative to readout 1.

Data calculation:
- Mean readout2/readout1 = 1.0035.
- Standard deviation of readout2/readout1 = 0.0294.
- Minimum observed readout2/readout1 = 0.9479, corresponding to only a 5.2% drop.
- Mean readout2 - readout1 = +0.14 counts.
- Most negative readout2 - readout1 = -2.54 counts.

Model comparison:
- A linear baseline fit to readout2/readout1 has RMSE = 0.0293.
- For a fixed physical mod_depth = 1 resonance centered on a sampled scan point, the best Rabi-line model has expected sampled fractional dip = 0.219 and RMSE = 0.0482, worse than the baseline-only fit.
- Allowing the resonance center outside the scan avoids the large dip and only produces a small edge correction, which is not evidence for an in-scan resonance.
- A free-amplitude line-shape fit prefers the opposite sign near the low-frequency edge, not the expected fluorescence dip.

Decision:
The expected pODMR signal for the active 52 ns, mod_depth = 1 pulse is a large, coherent resonant dip in the post-pulse readout relative to the m_S = 0 reference. The measured normalized readout stays near unity with only small scatter-scale excursions and no line-shaped dip of the required magnitude. A pODMR resonance is absent.
