Case podmr_014_2026-05-12-081841

Sequence identification

The provided sequence is Rabimodulated.xml. The active experiment varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true m_S = 0 bright reference. Because full_expt = 0, the explicit m_S = +1 reference block is skipped. The second acquired readout is therefore the signal after one rabi_pulse_mod_wait_time pulse, followed by detection.

Relevant pulse parameters from the active sequence values are:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s but unchanged because 52 ns is 13 samples.
- mod_depth = 1.
- do_adiabatic_inversion = true is not active for the acquired readouts because the only adiabatic-inversion code is inside the skipped full_expt block and is commented there.
- readout 1 role: bright m_S = 0 reference.
- readout 2 role: post-Rabi-pulse signal.

Physical model calculation

Using the supplied setup facts, the Rabi frequency at mod_depth = 1 is approximately 10 MHz. For a square pulse, the transition probability at detuning Delta is

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * t * sqrt(Omega^2 + Delta^2)),

where Omega = 2*pi*10 MHz and t = 52 ns. On resonance, Omega*t = 3.267 rad = 1.04*pi, giving P(0) = 0.996. With the stated 22% contrast scale, the expected signal/reference ratio on resonance is approximately 1 - 0.22*0.996 = 0.781, i.e. about a 10 count drop from a 46 count bright reference.

Because the scan step is 5 MHz, a resonance anywhere within the scanned range is at most 2.5 MHz from a sampled point. At 2.5 MHz detuning the same model gives P = 0.929 and expected signal/reference ratio 0.796, still about a 9.4 count drop. At 5 MHz detuning the expected ratio is 0.835, still a large drop.

Data comparison

The combined readout means are:

- readout 1 mean = 46.624 counts, standard deviation across scan = 1.138 counts.
- readout 2 mean = 46.315 counts, standard deviation across scan = 1.078 counts.
- readout2/readout1 mean = 0.9938, standard deviation = 0.0283.
- minimum observed readout2/readout1 ratio = 0.9370 at 3.865 GHz.
- minimum observed readout2 - readout1 difference = -3.13 counts.

The deepest observed normalized dip is therefore only about 6.3%, much smaller than the approximately 20-22% dip expected at a sampled resonance. A fixed-contrast resonance model with the above Rabi parameters was also scanned over possible resonance centers in the measured frequency interval while allowing only a multiplicative baseline scale. Its best chi-square using the observed ratio scatter was 93.3, compared with 20.0 for a flat-ratio model. Thus the expected pODMR resonance model fits substantially worse than no resonance.

Decision

No pODMR resonance is present in this scan. The pulse should have been close to a pi pulse and the expected resonant contrast would be large compared with the observed fluctuations, but no such dip appears in the post-pulse signal relative to the bright reference.
