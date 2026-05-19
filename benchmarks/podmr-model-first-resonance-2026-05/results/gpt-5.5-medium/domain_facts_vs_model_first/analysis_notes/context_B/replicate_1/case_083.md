<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_083

Sequence interpretation

The provided sequence is Rabimodulated.xml. The active instructions first polarize the NV and acquire a detection readout before any microwave pulse; this is the true m_S = 0 reference. Because full_expt = 0, the optional m_S = 1 reference block is skipped. The only active microwave manipulation before the second detection is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

Thus the two combined readouts are:

- readout 1: polarized m_S = 0 fluorescence reference
- readout 2: fluorescence after the modulated Rabi pulse

The active pulse settings are length_rabi_pulse = 52 ns and mod_depth = 1. With sample_rate = 250 MHz, 52 ns is exactly 13 samples, so rounding leaves it at 52 ns.

Quantitative expected signal model

Given the stated setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant rectangular pulse, the transferred population is

P_transfer = sin^2(pi * f_Rabi * t)

Using f_Rabi = 10 MHz and t = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9)
           = sin^2(1.6336)
           = 0.996

The m_S = 0 to m_S = +1 fluorescence contrast scale is about 22%, so the expected resonant fractional readout drop is

0.22 * 0.996 = 0.219

The measured mean reference readout is 46.686 counts, so a full pODMR resonance under this pulse should produce an approximate drop of

46.686 * 0.219 = 10.23 counts

That means readout 2 should be roughly 36.5 counts at resonance, relative to a 46.7-count reference, ignoring smaller normalization details.

Data comparison

The measured combined readout means are:

- mean readout 1 = 46.686
- mean readout 2 = 46.582
- mean(readout 2 - readout 1) = -0.104 counts
- standard deviation of pointwise differences = 1.385 counts

The largest negative combined difference is -4.288 counts at 3.845 GHz, corresponding to only an 8.9% drop at that point. This is far smaller than the approximately 21.9% / 10.2-count drop expected from the active 52 ns, mod_depth 1 pulse. Neighboring points do not form a convincing full-depth pODMR line, and the overall mean signal is essentially equal to the reference.

Per-average traces also should not be treated as a strong independent repeatability test because stored averages can reflect tracking cadence. Still, they do not rescue the interpretation: the local depressions are only a few counts and sit on comparable point-to-point fluctuations.

Decision

The expected resonant response from the active physical model is a near-pi-pulse contrast-scale drop, but the observed signal does not show such a feature. I therefore classify this case as resonance_absent.
