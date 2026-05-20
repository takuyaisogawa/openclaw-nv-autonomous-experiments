Case podmr_033_2026-05-15-233800

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The instruction flow first polarizes the NV and performs detection before the microwave pulse. This is the true m_S = 0 fluorescence reference, corresponding to readout 1.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies one rabi_pulse_mod_wait_time pulse and performs detection. This post-pulse fluorescence is readout 2.

Pulse settings:
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, round(length_rabi_pulse * sample_rate) gives 13 samples, so the active pulse duration remains 52 ns.
- mod_depth = 1 from the provided sequence XML and exported variable values.
- Given the setup fact that Rabi frequency is about 10 MHz at mod_depth = 1, the on-resonance Rabi frequency used for the model is Omega = 10 MHz.

Quantitative model:
- For a square pulse, the driven population transfer versus detuning is modeled as
  P(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau),
  using Omega and Delta in cycles per second.
- On resonance with tau = 52 ns and Omega = 10 MHz, Omega * tau = 0.52 cycles and P(0) = sin^2(pi * 0.52) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fluorescence reduction in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, about a 22% dip.
- At the strongest observed dip, 3.875 GHz, readout 1 = 38.5 and readout 2 = 28.8269. The observed fractional dip is 1 - 28.8269 / 38.5 = 0.251, close to the expected near-pi-pulse contrast scale.
- Using a resonance center of 3.875 GHz, the same detuned Rabi model predicts fractional transfer values of about 0.749 at +/-5 MHz and 0.273 at +/-10 MHz. The observed readout-2 dips around the center are 10.3% at 3.870 GHz, 25.1% at 3.875 GHz, 18.0% at 3.880 GHz, and 8.9% at 3.885 GHz. This is the expected localized dip shape for the given pulse duration and Rabi rate, with modest scatter.
- Across the scan, the correlation between observed fractional dip and this fixed-parameter detuned Rabi response is about 0.85 when centered at 3.875 GHz.

Decision:
The observed readout-2 suppression is localized, has the expected magnitude for a 52 ns near-pi pulse at mod_depth = 1, and follows the detuned Rabi response better than the off-resonant baseline scatter. A pODMR resonance is present.
