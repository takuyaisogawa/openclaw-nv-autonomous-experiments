Analysis note for podmr_004_2026-05-10-171142

Sequence and readout roles

The XML sequence is Rabimodulated.xml. The exported scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps, with 21 points, 2 stored averages, and
50000 repetitions.

The active instruction path first performs adj_polarize followed by detection,
then wait_for_awg. This is the true m_S = 0 reference readout. The "Acquire 1
level reference" block is conditional on full_expt, and full_expt is 0, so that
block is skipped. The active experiment readout is then produced after
rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by
detection. Therefore readout 1 is the m_S = 0 reference and readout 2 is the
post-Rabi-pulse signal readout.

Pulse parameters from the XML/export:
- sample_rate = 250 MHz, so 52 ns is exactly 13 samples after rounding.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- current setup Rabi frequency estimate = 10 MHz at mod_depth 1.

Quantitative model

Use a rectangular-pulse two-level Rabi response with detuning delta in Hz:

P(delta) = (f_R^2 / (f_R^2 + delta^2)) *
           sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz and t = 52 ns. The optical contrast scale between m_S = 0
and m_S = +1 is 22%, so the expected pulsed/readout reference ratio is

readout_2 / readout_1 = 1 - 0.22 * P(delta).

On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961. The expected ratio is
0.7809, a 21.9% dip. With the observed mean reference readout of 43.68 counts,
this corresponds to a drop of about 9.57 counts.

The scan step is 5 MHz, so if a resonance center lies inside the scan window,
at least one sampled point is within 2.5 MHz of the center. The model gives
P(2.5 MHz) = 0.9292, so even in the worst center-between-points case the
expected captured dip is 0.22 * 0.9292 = 20.4%, or about 8.93 counts.

Observed data

The combined readouts give:
- mean readout 1 = 43.6795 counts
- mean readout 2 = 44.2491 counts
- minimum observed readout_2/readout_1 ratio = 0.9428 at 3.855 GHz
- largest observed negative difference readout_2 - readout_1 = -2.4615 counts
  at 3.855 GHz
- observed difference standard deviation across the scan = 1.7381 counts

Thus the deepest observed dip is only 5.7%, far smaller than the expected
20-22% sampled dip for the active 52 ns, mod_depth 1 pulse. The readout 2 trace
also has positive excursions above the reference, including ratios above 1.09,
which is not the expected sign or line shape for a pODMR resonance.

Model comparison using the fixed physical contrast supports the same
conclusion. A no-resonance constant-offset model for readout_2 - readout_1 has
SSE = 60.4 counts^2. A fixed-contrast resonance model with center constrained
inside the scan has best SSE = 139.9 counts^2, substantially worse. Allowing
the resonance contrast amplitude to float positive gives a best fitted contrast
of only 0.0418, not the expected 0.22 for this near-pi pulse.

Decision

No pODMR resonance is present in this scan. The active pulse should have
produced a large, sampled, negative dip in readout 2 relative to the m_S = 0
reference if the resonance were present, and the observed fluctuations do not
match the required amplitude or physical line shape.
