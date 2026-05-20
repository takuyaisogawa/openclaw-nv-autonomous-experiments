Case podmr_030_2026-05-13-160024

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml / Rabimodulated.
- The XML sets full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active instructions are:
  1. adj_polarize
  2. detection: true mS = 0 / bright reference readout
  3. wait
  4. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth)
  5. detection: post-Rabi signal readout
- Therefore readout 1 is the bright pre-pulse reference and readout 2 is the post-pulse signal, not an independently acquired mS = +1 reference.

Sequence parameters relevant to the physical model:
- length_rabi_pulse = 52 ns
- mod_depth = 1 in the provided XML and variable values
- scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- averages = 2, repetitions = 40000

Explicit expected-signal calculation:
- Given f_Rabi(mod_depth=1) = 10 MHz and linear scaling with mod_depth, f_Rabi = 10 MHz.
- For a resonant square pulse, population transfer to mS = +1 is approximated by
  P1 = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns:
  P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between mS = 0 and mS = +1 is about 22%, so the expected fractional fluorescence loss at resonance is
  0.22 * 0.996 = 0.219, or about 21.9%.
- The measured readout-1 mean is 27.37 raw-count units, so an on-resonance post-pulse readout should be lower than the reference by about
  27.37 * 0.219 = 6.00 raw-count units.
- Equivalently the expected normalized post/reference ratio at resonance is about 0.781.

Observed quantitative comparison:
- Combined readout-1 mean = 27.37, SD across scan points = 1.23.
- Combined readout-2 mean = 27.73, SD across scan points = 1.35.
- Difference readout2 - readout1 has mean +0.36, SD = 1.57, minimum = -2.26, maximum = +3.27.
- Ratio readout2/readout1 has mean 1.015, SD = 0.058, minimum = 0.918.
- The most negative point is only a 2.26-count drop, far smaller than the expected 6.00-count drop for the active pulse. The lowest normalized ratio, 0.918, is also far above the expected resonant ratio of about 0.781.
- The per-average traces show substantial drift and inconsistent point-to-point changes, so the two stored averages do not provide a strong repeatability test and are consistent with tracking cadence effects.

Decision:
The physically expected resonant pODMR feature for the active sequence should be a large post-Rabi readout decrease relative to the bright reference. The observed scan does not show such a feature; readout 2 is on average slightly higher than readout 1 and the largest observed deficits are much smaller than the expected resonant contrast. I therefore decide that a pODMR resonance is absent.
