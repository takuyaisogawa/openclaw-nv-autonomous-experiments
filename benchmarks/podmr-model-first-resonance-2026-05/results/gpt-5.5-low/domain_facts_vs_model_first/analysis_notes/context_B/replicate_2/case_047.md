Case: podmr_033_2026-05-16-203113

Sequence/readout identification

The saved experiment is SequenceName Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active sequence polarizes the NV, performs a detection readout for the true m_S = 0 reference, waits, skips the optional m_S = 1 reference because full_expt = 0, applies one rabi_pulse_mod_wait_time pulse, then performs the second detection readout. Thus readout 1 is the 0-state/reference readout and readout 2 is the post-microwave-pulse signal readout.

The relevant saved variable values are:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so 52 ns rounds to 52 ns
- mw_freq is the scanned parameter
- do_adiabatic_inversion is true, but the adiabatic inversion block is not active because full_expt = 0

Physical model calculation

Given the provided setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square pulse of duration t = 52 ns, the on-resonance transition probability is

P = sin^2(pi f_R t / 2)
  = sin^2(pi * 10e6 * 52e-9 / 2)
  = 0.531.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence change in the post-pulse readout is approximately

0.22 * 0.531 = 0.117,

or an 11.7% drop relative to the 0-reference fluorescence. The mean reference readout is 53.90 counts, so the expected on-resonance drop is about 6.3 counts.

I also compared the measured readout difference d = readout2 - readout1 against the detuned square-pulse model

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t / 2).

The measured difference has mean 0.41 counts and RMS scatter about 1.00 count, with minimum -1.44 counts and maximum +2.52 counts. A resonance should produce a negative feature of roughly -6.3 counts in readout2 relative to readout1, much larger than the observed excursions.

A drift-only linear baseline for d gives SSE = 20.65. Fitting the physical square-pulse line shape with nonnegative dip amplitude gives best center near 3.886 GHz, fitted full contrast scale A = 1.18 counts, and SSE = 19.69. This corresponds to an on-grid dip of only about 0.62 counts, far below the expected 6.3 count resonant drop and only a marginal improvement over no resonance. The fitted amplitude is therefore consistent with noise/tracking variation rather than the expected pODMR signal.

Decision

No pODMR resonance is present. The active pulse should have produced a clearly resolvable negative post-pulse feature if the scanned range crossed the resonance, but the data show only small, irregular readout differences and no physically sized square-pulse resonance.
