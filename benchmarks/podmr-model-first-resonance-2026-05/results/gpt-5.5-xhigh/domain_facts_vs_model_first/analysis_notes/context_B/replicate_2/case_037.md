Case podmr_022_2026-05-16-172725

Sequence and readout roles

The sequence XML is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables relevant to the pulse are:

- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) / 250 MHz = 52 ns, so the requested duration is preserved.
- mod_depth = 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. The do_adiabatic_inversion boolean is therefore not used by the executed sequence.

The executed detections are:

1. adj_polarize followed by detection: this is the true m_S = 0 reference, corresponding to readout 1.
2. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) followed by detection: this is the pODMR signal after the MW pulse, corresponding to readout 2.

Physical model calculation

Use the two-level driven transition model for population transferred from m_S = 0 to m_S = +1 by a rectangular MW pulse:

P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

where delta is detuning in Hz, t = 52 ns, and f_R is the Rabi frequency in cycles/s. The setup facts give f_R approximately 10 MHz at mod_depth = 1. The fluorescence model is:

normalized_signal(delta) = 1 - C * P1(delta)

with C = 0.22 for the m_S = 0 to m_S = +1 contrast scale.

On resonance:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961
expected normalized signal = 1 - 0.22 * 0.9961 = 0.7809

The mean m_S = 0 reference readout is 46.762 counts, so a resonance sampled on-center should give an expected post-pulse readout of about 36.515 counts, a dip of about 10.25 counts.

Sampling check

The frequency step is 5 MHz. If a resonance lies anywhere inside the scan range, at least one sampled point is within 2.5 MHz of it. The model gives max sampled P1 >= 0.9292 in that worst case, so the expected minimum sampled normalized signal is <= 1 - 0.22 * 0.9292 = 0.7956. At exact 5 MHz detuning the model still gives normalized signal 0.8353.

Data comparison

Measured combined values:

- readout 1 mean = 46.762
- readout 2 mean = 46.834
- readout2/readout1 mean = 1.0020
- readout2/readout1 minimum = 0.9312 at 3.890 GHz
- readout2/readout1 maximum = 1.0497

The largest observed normalized depression is therefore only about 6.9%, far smaller than the expected roughly 20-22% depression for a resonance in this scan. If the point at 3.890 GHz were an on-resonance point, its readout 1 value of 47.519 would imply expected readout 2 about 37.106, but the observed readout 2 is 44.250, higher by 7.144 counts.

I also compared line-shape fits. With the readout 1 values used as the local baseline, the best free-amplitude fit to the Rabi line shape gives an effective contrast amplitude of only 0.0245, about 11% of the expected 0.22. Forcing the expected 0.22 contrast gives a sum of squared residuals about 4.1 times worse than a constant-offset no-resonance model. The two stored averages mainly show slow baseline/tracking changes, so I do not treat them as independent repeatability evidence for a weak resonance.

Decision

The active pulse should produce an easily visible post-pulse PL dip if a pODMR resonance is present within the scanned range. The measured readout 2 does not show the expected magnitude or line shape relative to the m_S = 0 reference. I decide resonance_absent.
