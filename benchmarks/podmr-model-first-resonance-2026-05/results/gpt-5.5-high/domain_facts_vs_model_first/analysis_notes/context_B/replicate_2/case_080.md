Case podmr_066_2026-05-17-072831

I used the provided sequence XML and the raw export only for the current case. The active sequence is Rabimodulated.xml with a swept mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The active instructions acquire the polarized reference detection first, then skip the optional +1 reference because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and acquire the second detection. Therefore readout 1 is the m_S = 0 fluorescence reference and readout 2 is the signal after the microwave pulse.

Relevant active pulse parameters from the provided XML:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1.
- The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).

Quantitative model:

Using the stated setup calibration, f_R = 10 MHz at mod_depth = 1. For a rectangular resonant pulse, with f_R and detuning Delta in cycles/s,

P_transfer(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).

With tau = 52 ns and f_R = 10 MHz, the on-resonance transfer probability is sin^2(pi * 10e6 * 52e-9) = 0.996. With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance readout-2/readout-1 ratio is about 1 - 0.22 * 0.996 = 0.781, a 21.9% drop. At the observed mean readout-1 level of 45.90 counts, that is an expected drop of about 10.06 counts. Even if the resonance lay halfway between adjacent 5 MHz scan points, the nearest-point transfer probability would be about 0.929, giving an expected ratio about 0.796.

Data comparison:

- Mean readout 1 = 45.900 counts.
- Mean readout 2 = 45.369 counts.
- Mean difference readout2 - readout1 = -0.531 counts.
- Minimum observed readout2/readout1 ratio = 0.9358 at 3.890 GHz, a 6.4% drop.
- Largest observed count drop = 3.06 counts.

A fixed-amplitude resonance model using the 22% contrast and the 10 MHz, 52 ns pulse predicts a much deeper dip than the data. Fitting that fixed-amplitude model over resonance center gives SSE 0.0577 on the normalized ratios, worse than a flat-ratio model SSE 0.0244. A free-amplitude fit finds only a 6.5% apparent dip amplitude, far below the expected 22% physical contrast for the active pulse. The stored per-average traces mainly show a common tracking offset between averages rather than an independent repeatability check.

Decision: resonance_absent. The measured fluctuations do not contain the deep, physically expected pODMR dip from a 52 ns, mod_depth 1 near-pi pulse.
