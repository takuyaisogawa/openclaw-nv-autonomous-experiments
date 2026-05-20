Case: podmr_033_2026-05-15-233800

Sequence and readout interpretation:

- The sequence file is Rabimodulated.xml and the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz, mod_depth = 1, and length_rabi_pulse = 5.2e-08 s. The instruction rounds this to the sample clock, giving 13 samples / 250 MHz = 52 ns.
- The first active acquisition block is "Acquiring true 0 level reference": adj_polarize followed by detection. This is the bright m_S = 0 reference readout.
- full_expt = 0, so the separate "Acquire 1 level reference" block is skipped.
- The second active acquisition is after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This readout is the pODMR signal after the scanned microwave/Rabi pulse.

Quantitative expected-signal model:

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is about f_R = 10 MHz. For a two-level transition driven with detuning d, the excited-state population after a rectangular pulse of duration t is

P_1(d) = f_R^2 / (f_R^2 + d^2) * sin^2(pi * t * sqrt(f_R^2 + d^2)).

With t = 52 ns and f_R = 10 MHz, the on-resonance transfer is

P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance readout ratio is

R_signal / R_bright = 1 - 0.22 * 0.996 = 0.781.

For a resonance centered at the observed dip near 3.875 GHz, the same model gives normalized ratios on the scan grid approximately:

0.993, 0.991, 0.998, 0.998, 0.982, 0.973, 0.989, 0.997, 0.940, 0.835, 0.781, 0.835, 0.940, 0.997, 0.989, 0.973, 0.982, 0.998, 0.998, 0.991, 0.993.

Observed data comparison:

- Combined readout 1 is relatively flat: mean 38.460, population standard deviation 0.768.
- Combined readout 2 has a pronounced minimum: mean 36.634, population standard deviation 2.644, minimum 28.827 at scan value 3.875 GHz.
- The bright-normalized ratio readout2/readout1 reaches a minimum of 28.827 / 38.500 = 0.749 at 3.875 GHz.
- Off the central dip region, the mean ratio is about 0.980 with population standard deviation 0.035. Scaling the model by this off-resonance ratio predicts an on-resonance ratio of about 0.980 * 0.781 = 0.765, close to the observed 0.749.
- The adjacent points are also consistent with a finite-width Rabi response: observed ratios around the minimum are 0.943 at 3.865 GHz, 0.897 at 3.870 GHz, 0.749 at 3.875 GHz, 0.820 at 3.880 GHz, and 0.911 at 3.885 GHz.

Stored per-average traces show cadence/drift effects and are not treated as a strong independent repeatability test, but both stored averages still place their strongest normalized dip in the same central region, at 3.875 to 3.880 GHz.

Decision:

The active pulse is essentially a pi pulse at mod_depth = 1, so a true pODMR resonance should produce a roughly 22% darkening of the second readout relative to the m_S = 0 reference. The observed central dip is about 23.1% below the local off-resonance ratio and about 25.1% below the simultaneous bright readout at the minimum. This matches the explicit Rabi-transfer expectation in amplitude and scan shape. I decide that a pODMR resonance is present.
