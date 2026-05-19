<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence and readout roles

The provided sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. With full_expt = 0, the sequence does not acquire the optional m_S = +1 reference. The two active detections are:

1. readout 1: after adj_polarize, a true m_S = 0 bright reference.
2. readout 2: after rabi_pulse_mod_wait_time, the driven pODMR/Rabi readout.

The active pulse parameters from the provided sequence/variable values are mod_depth = 1 and length_rabi_pulse = 52 ns. The pulse is rounded to the 250 MHz sample clock; 52 ns is already exactly 13 samples.

Physical model calculation

For a rectangular driven pulse, the resonant population transferred out of m_S = 0 is

P_1 = sin^2(theta/2), theta = 2*pi*f_R*t_pulse.

The setup fact gives f_R ~= 10 MHz * mod_depth. With mod_depth = 1 and t_pulse = 52 ns:

theta = 2*pi*(10 MHz)*(52 ns) = 3.267 rad
P_1 = sin^2(1.6336) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional dip in the driven readout is

0.22 * 0.996 = 0.219, or about 21.9%.

The observed readout 1 mean is 53.794 counts, so a resonant 52 ns pulse at mod_depth = 1 should produce an on-resonance decrease of about

53.794 * 0.219 = 11.79 counts

in readout 2 relative to the m_S = 0 reference, ignoring smaller linewidth and contrast-loss effects.

Observed data check

The combined data have:

readout 1 mean = 53.794 counts, standard deviation across scan = 1.018 counts
readout 2 mean = 52.947 counts, standard deviation across scan = 1.067 counts
readout 1 - readout 2 mean = 0.847 counts
maximum readout 1 - readout 2 = 3.462 counts
minimum readout 2/readout 1 = 0.9368, i.e. a 6.3% local deficit

The largest local deficit is far below the approximately 11.8 count / 21.9% expected resonant signal for the active pulse. A simple scan over Lorentzian dip models in the normalized ratio gives a best dip amplitude of about 5.4% with broad width near 29.5 MHz, improving the unweighted ratio SSE only from 0.01464 to 0.01186. That amplitude is about one quarter of the expected resonant contrast.

The two stored averages are also not a strong independent repeatability test because averages can reflect tracking cadence. Still, they do not support a robust resonance: the average-wise difference traces have different maxima and different mean offsets. Average 0 has its largest difference at 3.900 GHz, while average 1 has its largest difference at 3.825 GHz.

Decision

Given the active Rabimodulated sequence, readout 2 should show a large, localized dip relative to readout 1 if a pODMR resonance is present. The measured fluctuations are much smaller than the explicit model expectation and are not repeatably centered. I therefore classify this case as resonance_absent.
