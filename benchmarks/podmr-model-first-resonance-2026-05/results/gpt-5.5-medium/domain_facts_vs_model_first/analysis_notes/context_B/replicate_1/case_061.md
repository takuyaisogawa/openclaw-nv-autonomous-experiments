<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_061

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The sequence is Rabimodulated.xml.
- The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, after rounding to the 250 MHz sample clock. This is 13 samples, still 52 ns.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion = 1 being defined.
- Readout 1 is the detection immediately after optical polarization, so it is the m_S = 0 fluorescence reference.
- Readout 2 is the detection after the Rabi pulse, so it is the pODMR signal readout.

Quantitative model:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: t = 52 ns.
- On resonance, transition probability for a square Rabi pulse is P = sin^2(pi f_R t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional fluorescence reduction in readout 2 relative to readout 1 on resonance is C * P = 0.219.
- With observed readout-1 level near 50 counts, the expected resonant dip is about 0.219 * 50 = 11.0 counts. Equivalently, the expected resonant readout2/readout1 ratio is about 0.781.

Observed data comparison:
- The measured readout2 - readout1 differences have mean -0.32 counts, minimum -2.73 counts, maximum +2.54 counts, and standard deviation about 1.42 counts.
- The deepest observed ratio readout2/readout1 is 0.947 at 3.905 GHz, corresponding to only a 5.3% reduction.
- No scan point approaches the expected resonant ratio of 0.781 or the expected roughly 11-count dip.
- The stored two averages show changes consistent with tracking cadence/drift and scatter, not a strong independent repeatability test.

Decision:
The expected pODMR signal for the provided active pulse should be large and unmistakable. The raw readouts do not show a drop with the required magnitude, so I decide that a pODMR resonance is absent.
