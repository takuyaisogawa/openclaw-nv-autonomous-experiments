Case: podmr_009_2026-05-16-113112

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- The sequence is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The first detection occurs immediately after adj_polarize and is the true m_S = 0 optical reference.
- full_expt = 0, so the optional m_S = 1 reference block is inactive.
- The active microwave operation is a single rabi_pulse_mod_wait_time before the second detection.
- Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-microwave signal readout.

Pulse parameters from the provided XML:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1.
- setup Rabi frequency estimate at mod_depth = 1 is 10 MHz.

Expected signal calculation:
For a resonant Rabi pulse, I model the transferred population as
P_transfer = sin^2(pi * f_Rabi * t).
With f_Rabi = 10 MHz and t = 52 ns:
P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected
fractional reduction in the post-pulse readout on resonance is
0.22 * 0.996 = 0.219.

Thus the expected on-resonance readout2/readout1 ratio is approximately
1 - 0.219 = 0.781.

Measured data check:
- Minimum readout2/readout1 ratio is 0.773 at 3.875 GHz.
- The corresponding absolute difference is readout1 - readout2 = 7.135 counts.
- Nearby ratios remain suppressed at 3.880 GHz and 3.885 GHz: 0.804 and 0.813.
- Edge/off-feature ratios average about 0.986 using the first 8 and last 6 scan points.

Decision:
The observed dip in readout 2 relative to the m_S = 0 reference has the correct
sign, frequency-localized shape, and magnitude for a near-pi pODMR resonance:
the measured minimum ratio 0.773 is very close to the model expectation 0.781.
Stored per-average traces are not treated as an independent repeatability test
because they can reflect tracking cadence. The combined readouts are sufficient
for a resonance-present decision.
