Active sequence and readout roles

The provided sequence is Rabimodulated.xml. The stored export and the XML variables give full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The executed readouts are therefore:

1. adj_polarize followed by detection: a true m_s = 0 optical reference, corresponding to readout 1.
2. rabi_pulse_mod_wait_time followed by detection: the pulsed ODMR signal after the microwave pulse, corresponding to readout 2.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative model

Given the setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz and scales linearly with mod_depth. For a square pulse, the transition probability versus detuning can be estimated as

P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * t),

using f_R = 10 MHz and t = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_s = 0 to m_s = +1 contrast scale of about 22%, the expected fractional optical drop in readout 2 at resonance is about 0.22 * 0.996 = 0.219, or about a 21.9% drop relative to the m_s = 0 reference. The mean readout-1 level is 45.20 counts, so the expected resonant dip is about 9.90 counts. Even if the resonance sits halfway between 5 MHz scan points, df <= 2.5 MHz gives P = 0.929, still implying about a 9.24 count dip. At df = 5 MHz the expected dip is still about 7.45 counts.

Observed data check

The combined readouts have mean readout 1 = 45.20 and mean readout 2 = 45.02. The pointwise difference readout2 - readout1 has mean -0.18 counts, standard deviation 1.53 counts, minimum -3.29 counts, and maximum +3.65 counts. The largest deficit occurs at 3.880 GHz, where readout 1 = 45.88 and readout 2 = 42.60, a ratio of 0.928 and a drop of 7.2%. Another similar-sized low point appears at 3.890 GHz, but neither approaches the expected 16-22% resonance-scale reduction for the active pulse model. The per-average traces also show broad baseline and tracking-scale drift, so the stored averages are not a strong independent repeatability test.

Decision

The active pulse should generate a near-full contrast pODMR dip if a resonance is sampled in this frequency window. The observed readout-2 suppression is much smaller than the model prediction and comparable to scan/noise/drift structure, so I decide that a pODMR resonance is absent.
