Case: podmr_032_2026-05-16-201700

Sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML has length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, pumping_time = 1 us, and delay_wrt_1mus = 0.2 us.
- Because full_expt = 0, the explicit m_S = 1 reference block is skipped. The first detection after optical polarization is the m_S = 0 reference readout. The second detection follows the modulated Rabi pulse and is the pODMR signal readout.

Quantitative model:
- Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1.
- For a resonant square pulse with duration tau = 52 ns, the expected transfer probability is P = sin^2(pi*f_R*tau).
- With f_R = 10 MHz and tau = 52 ns, P = sin^2(pi*10e6*52e-9) = 0.996.
- With m_S=0 to m_S=+1 contrast about 22%, the expected fractional fluorescence drop at resonance is 0.22*0.996 = 0.219.
- The measured mean first-readout reference is 55.255 counts, so the expected resonant drop in the second readout is about 55.255*0.219 = 12.1 counts. A resonant point should therefore have signal/reference ratio near 0.781, apart from noise and linewidth effects.

Observed data comparison:
- Across the scan, the second-minus-first readout differences have mean +0.006 counts and standard deviation 1.51 counts.
- The most negative second-minus-first point is only -2.35 counts, while the expected resonant suppression is about -12.1 counts.
- The second/first readout ratios range from 0.958 to 1.073 and average 1.000; none approach the modeled resonant ratio near 0.781.
- Near the center point at 3.875 GHz, the second readout is higher than the reference by +3.94 counts, opposite in sign to the expected resonant dip.
- The two stored averages show similar tracking-offset-scale behavior rather than an independent repeatability test; at 3.875 GHz both averages also have positive signal-reference differences.

Decision:
The active pODMR pulse should produce a large negative fluorescence contrast if it is on resonance, but the measured signal channel stays comparable to the m_S=0 reference and never shows a dip remotely close to the expected magnitude. I therefore decide that a pODMR resonance is absent.
