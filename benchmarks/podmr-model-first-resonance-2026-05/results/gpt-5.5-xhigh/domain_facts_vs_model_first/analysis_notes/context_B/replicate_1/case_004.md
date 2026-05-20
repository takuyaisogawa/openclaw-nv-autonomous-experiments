Case podmr_007_2026-05-11-064944.

I used the provided sequence XML and the raw export values for the scan data. The active sequence is Rabimodulated.xml / Rabimodulated. The instructions first polarize and detect immediately; the comment identifies this as the true m_S=0 reference, so readout 1 is the bright reference. The branch that would acquire a m_S=1 reference is gated by full_expt, and full_expt is 0, so that branch is inactive. The only swept microwave-dependent detection is after PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on); therefore readout 2 is the pODMR signal after the modulated Rabi pulse.

Sequence parameters used before deciding:
- sample_rate = 250 MHz, so length_rabi_pulse = 52 ns is exactly 13 samples after rounding.
- mod_depth = 1.
- mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- detuning = 0.
- full_expt = 0, so there is no active m_S=1 reference readout.

Physical model calculation:
The provided setup scale gives Rabi frequency f_R = 10 MHz at mod_depth = 1. For a square pulse starting in m_S=0, the driven transition probability at detuning Delta is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With t = 52 ns and Delta = 0,
P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current contrast scale between m_S=0 and m_S=+1 is about 22%, so the expected on-resonance readout-2 fractional dip relative to readout 1 is
0.22 * 0.996 = 0.219.

The mean combined readout 1 level is 31.72 counts, so the expected resonant dip is about
31.72 * 0.219 = 6.95 counts,
giving an expected on-resonance readout-2/readout-1 ratio near 0.781. Because the scan step is 5 MHz and the Rabi frequency is 10 MHz, the response should also remain large at nearby grid points if the resonance falls between sampled frequencies.

Observed paired readout calculation from the combined data:
- Mean paired contrast (readout1 - readout2) / readout1 = 0.0045.
- Standard deviation of paired contrast across the scan = 0.0515.
- Maximum positive paired contrast = 0.1128 at 3.855 GHz, corresponding to a 3.81 count dip.
- Several points have negative contrast, including 3.915 GHz with readout 2 higher than readout 1 by 2.73 counts.

I also fit the explicit Rabi line-shape template across the scanned frequency range. With a free nonnegative amplitude and baseline, the best amplitude was 0.0715, far below the physically expected 0.22. With the physical 0.22 amplitude fixed, the line-shape model had larger RMS residual than the no-resonance constant-contrast model. The stored two averages show fluctuations of comparable size, but I did not treat them as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The active sequence would produce a large, broad readout-2 dip for a pODMR resonance under the stated mod_depth and pulse duration. The measured data do not show the expected magnitude or line shape. I therefore decide that a pODMR resonance is absent.
