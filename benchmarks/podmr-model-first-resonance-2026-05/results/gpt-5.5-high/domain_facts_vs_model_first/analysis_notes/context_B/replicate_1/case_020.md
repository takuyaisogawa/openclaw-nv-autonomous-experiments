Active sequence and readout roles

I used inputs/sequence.xml for the active pulse program. The sequence is Rabimodulated.xml. It first polarizes and detects a true m_S = 0 reference, then waits. The "Acquire 1 level reference" block is skipped because full_expt = 0, so there is no active m_S = 1 reference in this run. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Therefore readout 1 is the m_S = 0 bright reference and readout 2 is the pODMR signal after the microwave pulse.

Physical model calculation

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1. With pulse duration t = 52 ns, the resonant transition probability for a square pulse is

P(0) = sin^2(pi * f_Rabi * t)
     = sin^2(pi * 10e6 * 52e-9)
     = 0.996.

Using the stated contrast scale C = 0.22 between m_S = 0 and m_S = +1, a resonant pi pulse should reduce the signal readout by

C * P(0) = 0.22 * 0.996 = 0.219,

or about 21.9 percent relative to off-resonance fluorescence. With an off-resonance readout-2 level estimated robustly as 37.70 counts, the expected resonant minimum is

37.70 * (1 - 0.219) = 29.44 counts.

Observed data check

Readout 2 has a minimum of 30.33 counts at 3.880 GHz, with the adjacent point at 3.875 GHz equal to 30.63 counts. Relative to the 37.70 count off-resonance level, the observed drop is 19.6 percent, close to the expected 21.9 percent. The readout-2/readout-1 ratio gives a similar resonant dip, with an approximately 23.0 percent drop at 3.875 GHz. Readout 1 does not show the same dip; it remains near the bright reference level through the feature.

I also evaluated the detuned square-pulse model

P(Delta) = f_Rabi^2 / (f_Rabi^2 + Delta^2) * sin^2(pi * t * sqrt(f_Rabi^2 + Delta^2))

over the scan points with C = 0.22. A grid search over center frequency gave a best center near 3.8786 GHz. The model reduced the readout-2 squared error to about 20 percent of a flat no-resonance model, and its predicted minimum is at the observed dip.

Decision

The observed feature has the expected readout role, sign, size, and frequency-localized shape for pODMR under the active sequence. I decide that a pODMR resonance is present.
