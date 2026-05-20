Case: podmr_024_2026-05-16-175646

Sequence interpretation

The provided XML is Rabimodulated.xml. The active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on);

The variables used for this case are sample_rate = 250 MHz, mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps, freqIQ = 50 MHz, length_rabi_pulse = 52 ns, length_last_wait = 1 us, mod_depth = 1, delay_wrt_1mus = 0.2 us, switch_delay = 100 ns, and pumping_time = 1 us. The pulse length is already an integer number of 4 ns samples, so the rounded active pulse duration remains 52 ns.

Readout roles

full_expt = 0, so the conditional block that would acquire an mS = +1 reference is inactive. Each scan point has two detections:

1. After adj_polarize and before the Rabi pulse: the polarized mS = 0 reference readout.
2. After the 52 ns modulated Rabi pulse: the signal readout used to test for resonant transfer out of mS = 0.

The stored per-average traces differ mainly by an offset consistent with tracking cadence, so I treat them as diagnostic overlays rather than an independent repeatability test.

Expected quantitative signal model

Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the resonant transfer probability is:

P = sin^2(pi * f_Rabi * tau)

With f_Rabi = 10 MHz and tau = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast between mS = 0 and mS = +1 is about 22%, so a resonant pulse should reduce the post-pulse readout relative to the mS = 0 reference by:

0.22 * 0.996 = 0.219

Thus the expected signal/reference ratio at resonance is about:

1 - 0.219 = 0.781

The measured reference readout mean is 53.855 counts, so the expected resonant post-pulse readout is about 42.054 counts, a drop of about 11.801 counts from the reference. A square-pulse detuning model,

P(df) = (f_Rabi^2 / (f_Rabi^2 + df^2)) * sin^2(pi * tau * sqrt(f_Rabi^2 + df^2)),

would still create a prominent dip over this 5 MHz stepped scan if the transition lay in the scanned band.

Observed data comparison

Combined readout statistics:

- Reference readout mean = 53.855, standard deviation = 0.717, range = 52.596 to 55.885.
- Post-pulse signal mean = 54.175, standard deviation = 0.848, range = 52.154 to 55.385.
- Signal/reference ratio mean = 1.006, standard deviation = 0.0206, range = 0.969 to 1.050.
- Signal-reference difference mean = +0.320 counts, standard deviation = 1.102 counts.

The deepest observed ratio is 0.969 at 3.895 GHz, only a 3.1% drop, and it is isolated rather than a resonance-shaped feature. This is far smaller than the approximately 21.9% drop expected from a near-pi pulse on resonance. The observed maximum signal-reference excursions are about 1 to 3 counts, while the expected resonant contrast is about 11.8 counts.

Decision

No pODMR resonance is present in this scan. The active sequence and pulse parameters predict a large negative post-pulse contrast at resonance, but the data show no quantitatively compatible dip in the post-pulse readout relative to the mS = 0 reference.
