case_id: podmr_033_2026-05-16-203113
timestamp: 2026-05-16-203113

Sequence identification

The active sequence is Rabimodulated.xml. With full_expt = 0, only two detections are active:

1. readout 1: after adj_polarize and before the microwave pulse, so this is the bright m_S = 0 reference.
2. readout 2: after rabi_pulse_mod_wait_time, so this is the frequency-dependent post-pulse pODMR signal.

The skipped full_expt block means there is no active m_S = +1 reference acquisition. The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected-signal model

Using the stated setup scale, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square pulse of duration t = 52 ns, I used the two-level driven-transition model

P_transfer(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),

where Omega and delta are in cycles per second. On resonance this gives

P_transfer(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected normalized fluorescence depletion at resonance is about

0.22 * 0.996 = 0.219,

so readout 2 should be roughly 22% below readout 1 at resonance. With the observed readout 1 level near 54 counts, this corresponds to an expected on-resonance drop of about 12 counts. Even at 5 MHz detuning the same model predicts P_transfer = 0.749 and a depletion of about 16.5%, still far larger than the observed point-to-point fluctuations.

Observed data check

For the combined readouts:

- mean readout 1 = 53.899, standard deviation across scan = 1.033
- mean readout 2 = 54.309, standard deviation across scan = 1.372
- mean readout2/readout1 = 1.0076
- standard deviation of readout2/readout1 across scan = 0.0191
- minimum readout2/readout1 = 0.9728, corresponding to only 2.7% depletion
- maximum apparent brightening = 4.6%

The largest apparent depletion is about 2.7%, not about 22%, and it is not a clear contiguous resonance feature. Stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence; however, the combined trace itself does not show the physically expected post-pulse dip.

I also compared simple fits to the normalized signal. A linear baseline alone had RSS = 0.00719. Adding a free-amplitude Rabi-response dip found only a small best amplitude near 4%, much smaller than the expected 22%. Forcing the expected 22% depletion shape increased the RSS to 0.03719, making the physically expected resonance model a poor description of the data.

Decision

A pODMR resonance is absent. The active pulse should nearly invert the spin on resonance and produce a large negative contrast in readout 2 relative to readout 1, but the measured signal shows no such depletion anywhere in the scanned range.
