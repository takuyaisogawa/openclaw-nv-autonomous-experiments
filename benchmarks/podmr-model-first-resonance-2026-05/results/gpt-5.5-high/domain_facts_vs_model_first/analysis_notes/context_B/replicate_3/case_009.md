Case podmr_016_2026-05-12-120649

Sequence interpretation

The provided XML is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to
3.925 GHz in 5 MHz steps. The active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse,
mod_depth, switch_delay, ch_on)

The configured active pulse duration is length_rabi_pulse = 52 ns. The
configured mod_depth is 1. full_expt = 0, so the optional m_S = +1 reference
block is disabled. Therefore the two stored readouts have these roles:

- readout 1: polarized m_S = 0 fluorescence reference, acquired before the
  microwave pulse.
- readout 2: fluorescence after the 52 ns modulated Rabi pulse, the
  resonance-sensitive readout.

Expected signal model

Using the supplied setup facts, the Rabi frequency is about 10 MHz at
mod_depth = 1. For a square resonant pulse, the transfer probability is

P(delta) = (Omega^2 / (Omega^2 + Delta^2)) *
           sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega / 2pi = 10 MHz and t = 52 ns. At zero detuning,
f_R * t = 0.52 cycles, so P(0) = sin^2(pi * 0.52) = 0.996. With the stated
22% m_S = 0 to m_S = +1 contrast scale, an on-resonance point should suppress
readout 2 relative to the m_S = 0 reference by about
0.22 * 0.996 = 21.9%.

For the measured mean readout 1 level of 25.73 counts, that is an expected
drop of about 5.64 counts, placing the resonant post-pulse readout near
20.1 counts if the baseline reference is otherwise unchanged.

The finite-pulse calculation also predicts a broad enough response that a
5 MHz sampled scan should catch a substantial dip even if the resonance lies
between sample points:

- detuning 0 MHz: transfer 0.996, expected contrast 21.9%
- detuning 2.5 MHz: transfer 0.929, expected contrast 20.4%
- detuning 5 MHz: transfer 0.749, expected contrast 16.5%
- detuning 7.5 MHz: transfer 0.508, expected contrast 11.2%
- detuning 10 MHz: transfer 0.273, expected contrast 6.0%

Data comparison

I compared the resonance-sensitive quantity (readout2 - readout1) / readout1.
The strongest observed suppression is only about -5.3%, occurring at 3.895 GHz
and 3.915 GHz. Several nearby points are positive or near zero rather than
forming the expected detuning-dependent dip. The largest absolute negative
difference is about -1.37 counts, far smaller than the roughly -5.6 count
drop expected for a resonant near-pi pulse.

The per-average traces show large slow baseline changes consistent with
tracking cadence effects, so they should not be treated as a strong
repeatability test. The combined data still lacks the large post-pulse
suppression predicted by the active sequence and pulse settings.

Decision

No pODMR resonance is present in this scan.
