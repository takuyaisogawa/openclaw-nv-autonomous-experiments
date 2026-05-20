Case: podmr_017_2026-05-16-132945

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml / provided sequence is Rabimodulated.
- The instructions first run adj_polarize followed by detection, giving readout 1 as the optically pumped true m_S = 0 reference.
- full_expt = 0, so the optional 1-level reference block is inactive. There is no separate inverted-state reference in the active experiment.
- The active signal readout is after one rabi_pulse_mod_wait_time pulse, so readout 2 is the post-microwave-pulse readout.
- Active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Pulse parameters from the provided sequence/raw saved values:
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the rounded pulse remains 52 ns.
- Current setup Rabi frequency is about 10 MHz at mod_depth = 1, so the expected resonant rotation angle is theta = 2*pi*10e6*52e-9 = 3.267 rad.

Explicit physical model calculation:
- For a resonant two-level Rabi pulse, the transfer probability from m_S = 0 to m_S = +1 is P = sin^2(theta/2).
- With theta = 3.267 rad, P = sin^2(1.6336) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce the signal readout by about 0.22 * P = 21.9% relative to off-resonant signal readout.
- The readout 2 off-resonant baseline, excluding +/-10 MHz around the minimum, is 43.656 counts. The expected resonant minimum is 43.656 * (1 - 0.22 * 0.996) = 34.090 counts.

Observed data calculation:
- Readout 2 minimum is 34.173 counts at 3.875 GHz.
- Observed drop from the off-resonant readout 2 baseline is 43.656 - 34.173 = 9.483 counts.
- Expected drop from the pulse model is 9.567 counts, essentially the same size.
- Non-dip readout 2 standard deviation is about 1.049 counts, making the dip about 9.0 sigma relative to off-dip scatter.
- Normalizing readout 2 by readout 1 gives a baseline ratio of 0.986 excluding the dip region and a minimum ratio of 0.753 at 3.875 GHz. This is a 23.6% fractional ratio drop, close to the expected 21.9% contrast for a near-pi pulse.
- Both stored averages show the same central depression near 3.875 GHz, but I do not treat the two averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The active sequence should produce a near-full m_S = 0 to m_S = +1 transfer on resonance, yielding about a 22% fluorescence drop in the post-pulse readout. The observed post-pulse readout has a centered dip whose size and normalized contrast match that quantitative expectation. A pODMR resonance is present.
