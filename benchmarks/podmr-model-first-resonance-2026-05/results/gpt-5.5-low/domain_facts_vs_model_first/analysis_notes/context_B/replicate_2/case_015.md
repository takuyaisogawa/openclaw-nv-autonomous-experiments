Case podmr_034_2026-05-15-235221

Input sequence identification:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML has full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 role: first detection after optical polarization, before the microwave pulse; this is the bright m_S = 0 reference.
- Readout 2 role: detection after the modulated Rabi microwave pulse; this is the resonance-sensitive signal.
- mod_depth from the provided sequence XML variable values: 1.
- Active pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s still 52 ns.

Expected signal model:
The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1, and the active pulse length is 52 ns. Using a two-level square-pulse model,

P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

with f_R = 10 MHz and t = 52 ns. On resonance this gives sin^2(pi * 10e6 * 52e-9) = 0.996. Therefore the expected normalized post-pulse fluorescence on resonance is approximately

1 - 0.22 * 0.996 = 0.781

relative to the pre-pulse bright reference. The model gives a broad pODMR dip: expected ratios are about 0.835 at +/-5 MHz and about 0.940 at +/-10 MHz from resonance.

Data comparison:
The combined readout ratios readout2/readout1 near the feature are:
- 3.870 GHz: 30.827 / 38.192 = 0.807, a 19.3% dip.
- 3.875 GHz: 26.808 / 34.231 = 0.783, a 21.7% dip.
- 3.880 GHz: 26.288 / 34.885 = 0.754, a 24.6% dip.

Away from the central feature, excluding 3.860 to 3.890 GHz, the mean ratio is 0.984 with standard deviation 0.035. The central ratios are far below this off-feature level and have the size expected from the physical model. Stored averages both show a central depression in readout 2, but I do not treat the two averages as a strong independent repeatability test because stored averages may mostly reflect tracking cadence.

Decision:
The pulse duration and mod_depth predict an on-resonance pODMR dip of roughly the observed magnitude. The raw data contain a clear post-pulse fluorescence dip centered near 3.875-3.880 GHz while the pre-pulse reference does not show a matching drop. A pODMR resonance is present.
