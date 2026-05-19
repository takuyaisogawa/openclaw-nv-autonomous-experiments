<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_051

I used the provided sequence.xml and the raw numeric export, without labels or external cases.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml / Rabimodulated.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- The active cycle is: polarize, detect, wait, apply rabi_pulse_mod_wait_time, detect, wait.
- readout 1 is the polarized no-microwave reference, corresponding to the m_S = 0 bright reference.
- readout 2 is the signal readout after the microwave Rabi pulse.
- mod_depth = 1 in the provided sequence.xml.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.

Explicit expected-signal model:
- Given Rabi frequency about 10 MHz at mod_depth = 1, and approximately linear scaling, f_R = 10 MHz.
- For a resonant rectangular Rabi pulse, transferred population is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected fractional signal reduction in readout 2 at resonance is 0.22 * 0.996 = 0.219.
- Around a baseline raw readout of about 48 counts, the expected resonant drop is about 10.4 counts.

Observed data comparison:
- The combined readout differences readout1 - readout2 have mean -0.30 counts, standard deviation 1.32 counts across scan points, minimum -2.81 counts, and maximum +2.12 counts.
- The largest observed positive drop is at 3.825 GHz: readout1 = 48.37, readout2 = 46.25, drop = 2.12 counts. The expected resonant drop there is about 10.6 counts.
- Several points have readout2 brighter than readout1, including 3.900 GHz with drop = -2.81 counts.
- The stored averages mainly show tracking drift/cadence: per-average paired-difference standard deviation is about 1.96 counts, giving an approximate two-average SEM near 1.39 counts, still far below the approximately 10 count expected resonant contrast.

Decision:
Under the active physical model from the provided XML, a real pODMR resonance would produce a large negative contrast in readout 2 relative to readout 1. No scan point shows anything close to the predicted 22% / approximately 10 count drop. I therefore decide that a pODMR resonance is absent.
