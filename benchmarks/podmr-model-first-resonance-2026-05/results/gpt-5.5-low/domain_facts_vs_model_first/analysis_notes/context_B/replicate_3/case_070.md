Active sequence and readout roles

I used the sequence embedded in inputs/raw_export.json as the active run record. It identifies SequenceName = Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables for the run were length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, and do_adiabatic_inversion = 1. Because full_expt = 0, the conditional "Acquire 1 level reference" block is skipped. The two stored readouts are therefore:

- readout 1: initial polarized m_S = 0 reference detection after adj_polarize
- readout 2: detection after one modulated Rabi pulse of duration 52 ns

Physical model calculation

The relevant pODMR signal for this sequence is the fluorescence decrease after the Rabi pulse when the microwave frequency is resonant with the addressed NV transition. The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so here f_Rabi = 10 MHz.

For a rectangular resonant pulse, the population transfer probability is:

P_transfer = sin^2(pi * f_Rabi * pulse_duration)

With f_Rabi = 10e6 Hz and pulse_duration = 52e-9 s:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996

Expected resonant fluorescence change is therefore:

fractional drop = contrast * P_transfer = 0.22 * 0.996 = 0.219

At a typical 0-reference readout near 45 counts, this predicts a resonant post-pulse readout drop of:

45 * 0.219 = 9.86 counts

Data comparison

The combined readout 1 mean is 43.77 counts and readout 2 mean is 43.93 counts. The pointwise readout2 - readout1 differences range from -2.60 to +2.90 counts, with mean +0.16 counts. The smallest readout2/readout1 ratio is 0.943, a 5.7% drop, far below the approximately 21.9% drop expected for an on-resonance 52 ns pulse at mod_depth = 1.

The per-average traces also show large tracking/baseline variation between the two averages, so the stored averages are not treated as a strong independent repeatability test. Even allowing for that, there is no scan point with the expected roughly 10-count resonant depletion of readout 2 relative to the m_S = 0 reference readout 1.

Decision

No pODMR resonance is present in this scan.
