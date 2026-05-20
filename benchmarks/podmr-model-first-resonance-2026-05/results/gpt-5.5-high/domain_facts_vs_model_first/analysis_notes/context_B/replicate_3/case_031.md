Case: podmr_016_2026-05-16-131456

Sequence and readout roles:
- The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the active instructions, full_expt = 0, so the optional "1 level reference" block is not executed.
- Readout 1 is the detection immediately after optical polarization, before the microwave pulse. It is the bright m_S = 0 reference/tracking readout.
- Readout 2 is the detection after a single rabi_pulse_mod_wait_time pulse and is the pODMR signal channel.
- The active pulse has length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding leaves 52 ns unchanged at 250 MS/s.

Physical model calculation:
- Given the setup facts, the on-resonance Rabi frequency at mod_depth = 1 is about f_R = 10 MHz.
- For a square microwave pulse, the excited-state transfer probability versus detuning d is:
  P(d) = f_R^2/(f_R^2+d^2) * sin^2(pi * t * sqrt(f_R^2+d^2)),
  using frequencies in cycles/s and pulse duration t = 52 ns.
- On resonance, P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- With an m_S = 0 to m_S = +1 contrast scale of about 22%, the expected full-resonance fluorescence drop is about 0.22 * 0.996 = 21.9% of the bright readout. For a 47-count bright level this is about 10.3 counts. A smaller observed drop is plausible from finite linewidth, imperfect calibration, and the scan grid not necessarily landing exactly at the resonance center.

Explicit fit/model check:
- I fit readout 2 to an affine baseline minus A * P(d), allowing only the resonance center, baseline, slope, and amplitude to float while keeping f_R = 10 MHz and t = 52 ns fixed.
- The best center is about 3.87744 GHz with fitted amplitude A = 8.49 counts on a 47.0-count baseline, or about 18.1% raw contrast.
- A baseline-only affine fit has SSE = 132.46, while the physical Rabi response fit has SSE = 13.98, leaving only 10.6% of the baseline-only residual.
- Normalizing readout 2 by readout 1 gives a best center about 3.87727 GHz and fitted contrast 20.5%; the physical model SSE is 14.5% of the normalized baseline-only SSE.
- Off-resonance readout-2 residual scatter is about 0.79 counts, while the central depression reaches about 5.9 counts below a simple global affine baseline and about 7.4 counts below the local off-resonant level near 47 counts.
- The dip shape spans roughly 3.865-3.885 GHz, consistent with the expected bandwidth of a 52 ns square pulse and the 10 MHz Rabi frequency.

Decision:
The post-pulse readout has a quantitatively strong, model-shaped depression at the expected scale, while the pre-pulse reference does not show the same resonance feature. This is a pODMR resonance.
