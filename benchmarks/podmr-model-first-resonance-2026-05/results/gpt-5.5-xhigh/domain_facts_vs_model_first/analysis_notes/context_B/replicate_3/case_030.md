Case: podmr_015_2026-05-16-130043

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence/readout identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions set full_expt = 0, so the optional "1 level reference" block is skipped.
- Readout 1 is the detection immediately after optical polarization, so it is the bright m_S = 0 reference for each scan point.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so it is the pODMR signal readout after the microwave pulse.
- Active pulse duration: length_rabi_pulse = 52 ns. At 250 MS/s this is exactly 13 samples, so the rounded pulse remains 52 ns.
- Active mod_depth: 1.

Quantitative signal model:
For a square microwave pulse, I model the driven two-level population transfer as

P1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)),

where f_R is the on-resonance Rabi frequency in cycles/s, Delta is frequency detuning in cycles/s, and tau is the pulse duration. The given setup has f_R = 10 MHz * mod_depth = 10 MHz. With tau = 52 ns,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale C = 0.22, the expected readout ratio on resonance is

readout2 / readout1 = 1 - C * P1(0) = 1 - 0.22 * 0.996 = 0.781.

Observed data:
- The strongest drop is at 3.875 GHz.
- readout1 = 46.2115, readout2 = 35.8654.
- Observed ratio = 35.8654 / 46.2115 = 0.776.
- Observed fractional drop = 22.39%.
- Far from the feature, the readout2/readout1 ratio averages about 0.970 with a standard deviation about 0.024, so the central point is well below the off-feature behavior.
- The expected model ratio at exact resonance is 0.781, matching the observed 0.776 within the scale of the raw readout noise and tracking drift.
- The two stored averages both show their largest local drop near the same frequency region, but I treat that only as consistency with the feature because stored averages can reflect tracking cadence rather than a strong independent repeatability test.

Decision:
The active pulse is essentially a pi pulse at mod_depth 1, so a true resonance should produce a readout-2 dip of about 22% relative to readout 1. The measured central dip is about 22.4% and occurs as a localized trough in the microwave-frequency scan. This is consistent with a pODMR resonance being present.
