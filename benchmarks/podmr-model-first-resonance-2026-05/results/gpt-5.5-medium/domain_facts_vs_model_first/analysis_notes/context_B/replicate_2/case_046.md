Case: podmr_032_2026-05-16-201700

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The instructions first perform optical polarization, then a detection labeled "Acquiring true 0 level reference", then wait. The "Acquire 1 level reference" block is conditional on full_expt, but full_expt is 0, so that block is inactive. Afterward the sequence applies one rabi_pulse_mod_wait_time pulse and performs a second detection.

Thus the two active readouts are:
- readout 1: bright m_S = 0 reference, before the microwave Rabi pulse.
- readout 2: post-Rabi-pulse signal.

Relevant sequence values from the provided XML:
- active sequence: Rabimodulated.xml
- scanned variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- mod_depth: 1
- length_rabi_pulse: 52 ns, rounded at 250 MS/s remains 52 ns
- full_expt: 0, so there is no active m_S = +1 reference readout

Quantitative expected signal model

Given the supplied domain facts, the setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Here mod_depth = 1, so f_Rabi = 10 MHz.

For a resonant square pulse, the transferred population is modeled as:

P_transfer = sin^2(pi * f_Rabi * t)

With t = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.9961.

The expected fluorescence reduction of the post-pulse signal on resonance is therefore:

expected fractional drop = 0.22 * 0.9961 = 0.2191, or about 21.9%.

The mean bright reference readout is 55.255 counts, so the expected on-resonance signal would be:

55.255 * (1 - 0.2191) = 43.15 counts.

Equivalently, an on-resonance point should show about a 12.11 count drop from the bright reference under this model.

Observed data comparison

Combined readouts from raw_export.json:
- readout 1 mean: 55.255
- readout 2 mean: 55.262
- readout 2 - readout 1 mean: 0.006
- minimum readout2/readout1 ratio: 0.958 at 3.830 GHz
- maximum readout2/readout1 ratio: 1.073 at 3.875 GHz

The deepest observed negative signal relative to the reference is -2.35 counts, far smaller than the modeled on-resonance drop of about -12.11 counts. The expected normalized signal/reference ratio on resonance is about 0.781, but the minimum observed ratio is about 0.958. The trace also does not show a clear localized dip in the post-pulse readout at the expected scale; the largest feature near 3.875 GHz is an increase in readout 2, opposite the expected fluorescence decrease.

Stored per-average traces differ substantially in offset, consistent with the provided caution that stored averages often reflect tracking cadence rather than a strong independent repeatability test. They do not rescue a resonance-scale dip in the combined signal.

Decision

Under the active Rabimodulated sequence and the quantitative Rabi/contrast model, a true pODMR resonance should be a large post-pulse fluorescence dip of roughly 22%. The measured data show only small reference-relative fluctuations of a few percent and no resonance-scale dip. Therefore, I classify this case as resonance_absent.
