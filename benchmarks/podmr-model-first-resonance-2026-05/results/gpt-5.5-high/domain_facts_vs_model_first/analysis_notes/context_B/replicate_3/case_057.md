Case: podmr_043_2026-05-16-231159

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The provided sequence is Rabimodulated.xml. The active experiment has full_expt = 0, so the optional +1 reference block is skipped. The executed detections are:

1. adj_polarize, then detection: this is the polarized m_S = 0 reference readout.
2. rabi_pulse_mod_wait_time, then detection: this is the post-microwave-pulse pODMR signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The relevant active values are:

- length_rabi_pulse = 52 ns
- mod_depth = 1
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns
- mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps
- freqIQ = 50 MHz

Physical model calculation

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the resonant transfer probability is

P_1(Delta = 0) = sin^2(pi * f_R * t)

with f_R = 10 MHz and t = 52 ns:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

Thus this pulse is effectively a pi pulse on resonance. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pODMR point should make the post-pulse signal readout about

1 - 0.22 * 0.996 = 0.7809

of the m_S = 0 reference readout. The observed mean reference readout is 47.11 raw units, so the expected resonant post-pulse value is about 36.79 raw units, a drop of about 10.32 raw units relative to the local reference.

Allowing for frequency sampling does not remove this expectation. Using the detuned square-pulse model

P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),

even a point 2.5 MHz from resonance would still give P_1 approximately 0.93 and an expected contrast of about 20.5%, far larger than the observed deviations.

Data comparison

The combined readouts have:

- mean readout 1 = 47.11
- mean readout 2 = 47.55
- mean ratio readout2/readout1 = 1.009
- smallest ratio readout2/readout1 = 0.9757 at 3.885 GHz
- ratio standard deviation across the scan = 0.0200
- largest downward deviation of readout 2 from its median = about 4.0%

The post-pulse readout is not lower than the reference by the expected 20-22%. Instead, it is on average slightly higher than the reference, and the largest local negative contrast relative to the reference is only about 2.4%. The expected resonant post-pulse values, based on the local reference readout, would lie around 35.8 to 38.4 raw units; the observed post-pulse readouts lie around 45.75 to 49.44 raw units.

Decision

The active pulse should produce a large pODMR dip if a resonance were present in the scanned range. No such dip appears in the signal readout or in the readout2/readout1 ratio. The measurement is therefore classified as resonance_absent.
