Analysis note for podmr_037_2026-05-16-213011

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence/readout roles

The provided sequence is Rabimodulated.xml. In the active instruction path, full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The executed detections are therefore:

1. adj_polarize, then detection: true m_S = 0 polarized fluorescence reference. This is readout 1.
2. rabi_pulse_mod_wait_time, then detection: post-microwave Rabi-pulse signal. This is readout 2.

The relevant pulse is:

- length_rabi_pulse = 5.2e-08 s = 52 ns
- mod_depth = 1
- mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns

Physical expected-signal model

Given the stated setup, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For the active mod_depth = 1, f_R = 10 MHz.

For a resonant square pulse starting from m_S = 0, the transfer probability to m_S = +1 is:

P_transfer = sin^2(pi * f_R * tau)

With tau = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected resonant fractional fluorescence change in the post-pulse readout relative to the polarized reference is:

expected_drop_fraction = 0.22 * 0.996 = 0.219

The median readout-1 level is about 47.5 raw-count units, so an on-resonance pi-pulse response should produce an absolute readout-2 drop of:

0.219 * 47.5 = 10.4 raw-count units

This is the expected scale for a true resonance under the active pulse sequence.

Observed data comparison

I compared readout 2 to readout 1 point-by-point using (readout2 - readout1) / readout1. A resonance should appear as a negative dip in this quantity, with expected depth about -0.219 near resonance.

Observed extrema:

- minimum normalized difference: -0.0437 at 3.825 GHz, corresponding to only -2.12 raw-count units
- maximum normalized difference: +0.0619 at 3.900 GHz
- median normalized difference: +0.0098
- standard deviation across scan points: 0.0280
- robust MAD-based scatter estimate: 0.0306

The most negative observed point is about five times smaller than the expected resonant contrast, is at the scan edge, and is not accompanied by the broad negative feature expected for a 52 ns near-pi pulse. The post-pulse readout is often above the reference rather than below it. The per-average traces also show point-to-point scatter at a few percent level and do not provide independent repeatability evidence for a resonant dip.

Decision

The active sequence should have produced a large, easily visible approximately 22% negative readout-2/readout-1 feature on resonance. The observed trace shows only small scatter-level fluctuations and no physically consistent negative pODMR resonance. I decide resonance_absent.
