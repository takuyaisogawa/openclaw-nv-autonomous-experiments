Case: podmr_008_2026-05-11-131831

Inputs used: inputs/sequence.xml and inputs/raw_export.json.

Sequence identification:
- Active sequence file: Rabimodulated.xml.
- Scanned variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion = 1.
- The executed readouts are therefore:
  1. Readout 1: polarized true m_S = 0 level reference, before the microwave pulse.
  2. Readout 2: readout after the microwave Rabi pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.
- sample_rate = 250 MHz, so 52 ns is exactly 13 samples after rounding.

Physical model calculation:
The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, and the sequence uses mod_depth = 1. For a square resonant pulse, the transfer probability is

P1(delta) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * t * sqrt(fR^2 + delta^2))

using fR = 10 MHz and t = 52 ns. On resonance:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the given 22% contrast scale, the expected fractional PL loss in the post-pulse readout at resonance is:

0.22 * 0.996 = 0.219, or about 22%.

At the mean polarized readout level of 20.08 counts, the expected resonant loss is about 4.40 counts. The expected ratio readout2/readout1 is about 0.781 at exact resonance. If the resonance lies on a scan point, adjacent +/-5 MHz points should still be strongly suppressed, with model ratio about 0.835; +/-10 MHz points should show about a 6% dip.

Data comparison:
- Mean readout 1 = 20.079 counts.
- Mean readout 2 = 19.791 counts.
- Mean readout2/readout1 ratio = 0.988, with standard deviation 0.057.
- The lowest ratio occurs at 3.840 GHz: readout1 = 21.096, readout2 = 18.596, ratio = 0.881, fractional loss = 11.9%.
- This deepest single point is only about half of the expected resonant loss. Using its local reference, the expected resonant readout2 would be 21.096 * 0.781 = 16.48 counts, not 18.60 counts.
- The neighboring points also do not follow the expected pulse spectrum: at 3.835 and 3.845 GHz the observed ratios are 1.059 and 1.017, while a resonance near 3.840 GHz would predict ratios around 0.835.

I also fit the readout2/readout1 ratios with the above pulse line shape plus a linear baseline while scanning possible resonance centers. A linear baseline alone gave RSS = 0.05498. The best unrestricted line-shape fit found a fractional amplitude of only about 0.071 near 3.840 GHz, far below the expected 0.219. Forcing the expected 0.22 amplitude made the fit worse, with best RSS about 0.07348.

The per-average traces show large monotonic tracking-like changes in opposite directions between the two stored averages, so I do not treat the stored averages as strong independent repeatability evidence. The paired combined readout ratio is the relevant comparison, and it lacks the expected 22% resonance response and expected neighboring-point structure.

Decision: resonance_absent.
