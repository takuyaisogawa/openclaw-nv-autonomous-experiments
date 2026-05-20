Case: podmr_044_2026-05-16-232730

I used inputs/sequence.xml as the provided sequence XML. The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first call adj_polarize and detection, so readout 1 is the optically prepared m_S = 0 reference. Since full_expt = 0, the optional m_S = +1 reference block is skipped. The later rabi_pulse_mod_wait_time followed by detection makes readout 2 the pODMR signal after the microwave pulse.

The provided XML has sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and mod_depth = 1. Rounding to sample ticks gives 52 ns exactly. Using the stated setup calibration, f_R = 10 MHz * mod_depth = 10 MHz. For a resonant square pulse the transferred population is

P_flip = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, an on-resonance pODMR signal should be lower than the m_S = 0 reference by

C * P_flip = 0.22 * 0.996 = 0.219,

so the modeled signal/reference ratio at resonance is 1 - 0.219 = 0.781. With the measured mean readout-1 level of 48.56 counts, this corresponds to an expected resonant readout-2 value of about 37.92 counts, a drop of about 10.64 counts.

The actual combined readouts give readout-2/readout-1 ratios from 0.952 to 1.044. The largest observed apparent contrast is only 0.0478 at 3.865 GHz, and the residual scatter of the normalized contrast after removing a linear trend is 0.0214. The expected 0.219 contrast is about 10.3 times that scatter and would be obvious in the raw traces. A grid calculation using the Rabi lineshape

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

also predicts a minimum signal/reference ratio of 0.781 whenever the resonance lies on a sampled frequency point, which is not observed anywhere in the scan.

Decision: resonance_absent.
