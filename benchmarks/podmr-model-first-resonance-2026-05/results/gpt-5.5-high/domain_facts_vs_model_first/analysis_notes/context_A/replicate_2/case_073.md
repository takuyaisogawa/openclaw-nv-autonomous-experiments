Active sequence and roles:

- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS = +1 reference block is inactive even though do_adiabatic_inversion is true.
- readout 1 is the "true 0 level" bright reference immediately after polarization.
- readout 2 is the detection after the modulated Rabi pulse.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is 13 samples, so it remains 52 ns after rounding.
- mod_depth = 1. Using the supplied setup fact, the Rabi frequency is about 10 MHz, so a 52 ns pulse is essentially a pi pulse.

Expected signal:

At mod_depth = 1 and 52 ns, a real on-resonance drive should produce close to the full bright-to-dark contrast scale, roughly 22% between the bright reference and the post-pulse readout, allowing for some imperfection.

Observed signal:

The combined readouts show only small differences between readout 1 and readout 2. The largest reference-normalized separation is around 3.880 GHz, about 6.4%, with other isolated few-percent separations elsewhere. The post-pulse readout itself is noisy and does not show a clean, robust resonance-shaped dip. The per-average traces mostly reflect a large tracking offset between stored averages, so they are not a strong independent repeatability check.

Decision:

Given the near-pi pulse condition and the expected 22% contrast scale, the observed few-percent, irregular readout separation is too weak and unstable to call a pODMR resonance. I classify this case as resonance_absent.
