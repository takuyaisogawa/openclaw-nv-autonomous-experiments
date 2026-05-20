Case podmr_034_2026-05-15-235221

I used the provided sequence XML to identify the active sequence. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. It first polarizes the NV, then performs detection for the true m_S = 0 reference. Since full_expt = 0, the optional m_S = +1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-microwave pODMR signal readout.

Sequence parameters used:
- sample_rate = 250 MHz, so the AWG sample period is 4 ns.
- length_rabi_pulse = 52 ns, and round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- mod_depth = 1.
- Setup contrast scale between m_S = 0 and m_S = +1 = 22%.
- Rabi frequency at mod_depth = 1 = 10 MHz.

Explicit quantitative model:

For a square resonant Rabi pulse starting from m_S = 0, with detuning Delta in Hz,

P_flip(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).

The normalized post-pulse readout model is

R2 / R1 = offset - C * P_flip(Delta),

with C = 0.22, f_R = 10 MHz, and tau = 52 ns. On resonance,

P_flip(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.9961.

Thus the expected on-resonance normalized readout is approximately

1 - 0.22 * 0.9961 = 0.7809.

Observed combined ratios R2/R1 at the strongest dip points:
- 3.870 GHz: 30.827 / 38.192 = 0.8072
- 3.875 GHz: 26.808 / 34.231 = 0.7831
- 3.880 GHz: 26.288 / 34.885 = 0.7536

The mean of these three central ratios is 0.7813, essentially the expected 0.7809 for a near-pi pulse with 22% contrast. Off the dip, excluding these three points, the mean ratio is 0.9748 with standard deviation 0.0362, so the central reduction is about 0.1935 in normalized readout. A fixed-physics detuned Rabi model fit with only center frequency and offset free gives a best center near 3.87575 GHz, offset 0.9865, SSE 0.0273 versus 0.1200 for a constant-ratio null model.

The dip amplitude, width, and location across adjacent frequency points are consistent with the expected pODMR response of the active 52 ns modulated Rabi pulse. The stored averages both contain the central dip, but I treated that only as supporting information because stored averages can reflect tracking cadence rather than independent repeatability.

Decision: resonance_present.
