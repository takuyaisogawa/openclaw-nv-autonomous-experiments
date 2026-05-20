Case podmr_015_2026-05-16-130043

Sequence and readout roles

The active sequence is Rabimodulated.xml. The instructions first polarize the NV, then acquire a detection window before any microwave pulse. Because full_expt = 0, the conditional "Acquire 1 level reference" block is inactive. Therefore readout 1 is the polarized m_S = 0 bright reference, and readout 2 is the signal after the active Rabi-modulated microwave pulse followed by detection.

Relevant pulse settings from the provided XML/raw export are:
- varied parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- mod_depth: 1
- length_rabi_pulse: 52 ns, rounded at 250 MS/s to 52 ns
- active pulse before readout 2: rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)
- no active acquired m_S = +1 reference, because full_expt = 0

Expected physical signal calculation

Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the spin-transfer probability is

P_transfer = sin^2(pi * f_Rabi * t)

With f_Rabi = 10 MHz and t = 52 ns:

pi * f_Rabi * t = pi * 10e6 * 52e-9 = 0.52 pi
P_transfer = sin^2(0.52 pi) = 0.996

The expected optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance readout-2/readout-1 ratio is

1 - 0.22 * 0.996 = 0.781

Thus a true resonance should appear as an approximately 22% dip in readout 2 relative to readout 1, centered where the microwave frequency reaches the NV transition.

Observed quantitative comparison

The combined readouts show the minimum normalized ratio at scan index 10, mw_freq = 3.875 GHz:

readout 1 = 46.2115
readout 2 = 35.8654
readout2/readout1 = 0.776

Using the median normalized ratio away from the three points around the minimum as a local baseline gives baseline ratio 0.968. The observed ratio dip is

0.968 - 0.776 = 0.192, or 19.9% of the baseline ratio.

This is very close to the calculated 21.9% expected dip for a near-pi pulse at mod_depth = 1. The neighboring points also show recovery away from the minimum, and both stored averages show a corresponding readout-2 depression in the same central region, though the stored averages are treated mainly as tracking-cadence information rather than a strong independent repeatability test.

Decision

The measured central dip has the right sign, frequency-localized shape, and quantitative amplitude for the expected pODMR response from the active pulse sequence. A pODMR resonance is present.
