Case podmr_011_2026-05-16-120107.

I used inputs/sequence.xml as the sequence definition. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The instructions first acquire the true mS = 0 reference after optical polarization, then because full_expt = 0 they skip the mS = +1 reference block, then apply one modulated Rabi microwave pulse and acquire the signal readout. Thus readout 1 is the polarized mS = 0 reference and readout 2 is the post-microwave pODMR signal. The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At 250 MS/s this pulse is exactly 13 samples after rounding.

Quantitative model calculation:

Given the setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square resonant pulse of duration t = 52 ns, the rotation angle is

theta = 2 pi f_R t = 2 pi * 10e6 * 52e-9 = 3.267 rad = 187.2 degrees.

The resonant transferred population is

P(+1) = sin^2(theta / 2) = sin^2(1.6336) = 0.996.

Using the stated mS = 0 to mS = +1 contrast scale of 22%, and the measured readout 1 mean of 42.198 counts, the expected resonant drop in readout 2 relative to readout 1 is

drop_expected = 42.198 * 0.22 * 0.996 = 9.25 counts,

so the expected resonant readout 2 level is about 32.95 counts.

I also compared the measured trace to the standard driven two-level response versus detuning,

P(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2 pi * 10 MHz, Delta = 2 pi * frequency detuning, t = 52 ns, and a 22% optical contrast. Scanning the unknown center frequency on a 0.25 MHz grid gives the best center near 3.87725 GHz. This model predicts readout 2 minima near 33.6 counts at 3.875 GHz and 33.1 counts at 3.880 GHz, matching the observed 34.75 and 33.10 counts. The model RMSE is about 1.19 counts across the full scan.

Observed data:

The largest suppression occurs at 3.880 GHz: readout 1 = 41.404, readout 2 = 33.096, drop = 8.308 counts, fractional drop = 20.1%. At 3.875 GHz the drop is 7.577 counts, fractional drop = 17.9%. These are close to the physically expected 22% maximum contrast for a near-pi pulse. Away from the dip, readout 2 is usually close to readout 1 with an outside-region mean ratio about 0.977, while the minimum ratio in the resonance region is about 0.799. The per-average traces both show the same central suppression, but I treat that only as a consistency check because stored averages may reflect tracking cadence.

Decision:

A pODMR resonance is present. The amplitude, width, and center of the readout 2 dip are quantitatively consistent with the expected response of a 52 ns, mod_depth 1 near-pi pulse, while readout 1 remains a reference rather than showing the same resonance-shaped dip.
