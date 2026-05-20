Case: podmr_057_2026-05-17-051839

I used the provided sequence XML and the raw exported data only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml / Rabimodulated.
- The active scan variable is mw_freq, from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- Readout 1 is the true mS = 0 fluorescence reference: polarize, then detection.
- Readout 2 is the pODMR signal: a modulated Rabi pulse, then detection.
- mod_depth = 1 from the provided XML variable values.
- length_rabi_pulse = 52 ns, rounded to the 250 MHz sample clock. Since 52 ns * 250 MHz = 13 samples, it remains 52 ns.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1 is about 10 MHz.
- For a resonant rectangular Rabi pulse, population transfer is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the mS = 0 to mS = +1 contrast scale about 22%, the expected resonant fractional fluorescence reduction in readout 2 relative to readout 1 is:
  0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout 1 level is 45.46 counts, so the expected on-resonance readout 2 level is about:
  45.46 * (1 - 0.219) = 35.49 counts.
- The expected resonant drop is therefore about 9.96 counts.
- Even if the true resonance falls midway between 5 MHz scan points, the nearest point is only 2.5 MHz detuned. Using the off-resonant Rabi formula P = (f_Rabi^2 / (f_Rabi^2 + detuning^2)) * sin^2(pi * sqrt(f_Rabi^2 + detuning^2) * t), the transfer at 2.5 MHz detuning is still about 0.93, implying about a 20% fluorescence drop. Thus a real resonance in the scanned interval should still be large compared with the observed fluctuations.

Observed quantitative comparison:
- Mean readout 1 = 45.455 counts.
- Mean readout 2 = 45.420 counts.
- Mean readout2/readout1 ratio = 0.9993.
- The deepest observed readout2/readout1 ratio is 0.955 at 3.925 GHz, a 4.5% drop, corresponding to about 2.08 counts.
- The scan contains no point near the model-predicted ratio of about 0.781 for a resonant pi pulse.
- Stored per-average traces differ at the one-to-two-count scale, consistent with tracking/noise-scale variation rather than the approximately ten-count signal expected from the active pulse sequence.

Decision:
The expected pODMR signal from the active 52 ns, mod_depth 1 pulse is a large negative contrast feature, but the measured readout 2 stays essentially equal to readout 1 across the scan. I therefore decide resonance_absent.
