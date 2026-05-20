Case podmr_003_2026-05-16-003531

I used only the supplied sequence and raw export for this case.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first performs adj_polarize followed by detection under the comment "Acquiring true 0 level reference"; this is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. There is no separate m_S = +1 reference readout in this data.
- The active signal readout is after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on) followed by detection; this is readout 2.
- From the provided sequence XML and exported variable values: mod_depth = 1, length_rabi_pulse = 52 ns, sample_rate = 250 MHz. The pulse length is already an integer 13 samples, so rounding leaves it at 52 ns.

Physical model calculation:
The relevant two-level square-pulse model for the microwave pulse is

P_transfer(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * tau * sqrt(Omega^2 + Delta^2)),

using frequencies in cycles/s. With the given setup fact Omega = 10 MHz * mod_depth and mod_depth = 1, Omega = 10 MHz. For tau = 52 ns:

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected fractional fluorescence loss on resonance is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean bright reference readout is 37.42 counts, so the expected resonant count loss is about 8.20 counts, giving an expected resonant signal level near 29.22 counts. The observed readout 2 values near the dip are 33.38, 29.35, 28.06, and 32.94 counts at 3.870, 3.875, 3.880, and 3.885 GHz, while the corresponding reference readouts are 38.21, 35.94, 39.98, and 36.63 counts. The normalized losses at those points are 12.6%, 18.4%, 29.8%, and 10.1%. These are the right order and frequency width for the expected near-pi pODMR dip; the largest single point is deeper than the nominal 22% contrast but is plausible given the raw count scatter and tracking cadence.

I also fit the normalized ratio readout2/readout1 to y = b - A * P_transfer(f - f0). The best fit gives f0 = 3.87767 GHz, b = 0.9999, A = 0.251, and SSE = 0.0443 versus a constant-ratio SSE = 0.1485. Holding A fixed to the expected contrast 0.22 gives f0 = 3.87768 GHz, b = 0.9943, and SSE = 0.0459. Thus the explicit physical line-shape model explains most of the structured variation in the normalized readouts. The isolated low point at 3.925 GHz does not match the modeled resonance shape and I treat it as scatter/tracking rather than the primary feature.

Decision: resonance_present. The active pulse should produce an approximately 22% fluorescence dip on resonance, and the data show a localized dip centered near 3.878 GHz with magnitude and width consistent with that model.
