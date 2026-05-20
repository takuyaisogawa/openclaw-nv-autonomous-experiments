Case: podmr_023_2026-05-16-174219

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, sibling cases, previous outputs, or external context.

Active sequence and readout roles:

The provided sequence is Rabimodulated.xml. The instructions set the microwave and then perform:

1. adj_polarize followed by detection: this is the true m_S = 0 bright reference.
2. The "Acquire 1 level reference" block is skipped because full_expt = 0.
3. rabi_pulse_mod_wait_time followed by detection: this is the pODMR signal readout after the microwave pulse.

Thus readout 1 is the m_S = 0 reference and readout 2 is the microwave-driven signal. The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model:

Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the active 52 ns pulse has on-resonance transition probability

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant point should reduce the signal readout by

0.22 * 0.996 = 0.219, or about 21.9%.

The measured readout 1 mean is 47.55 counts, so the expected on-resonance drop in readout 2 relative to readout 1 is approximately

47.55 * 0.219 = 10.42 counts.

The generalized square-pulse Rabi model

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau)

with Omega = 10 MHz and tau = 52 ns predicts approximate absolute drops of 10.42 counts at zero detuning, 7.83 counts at 5 MHz detuning, and 2.86 counts at 10 MHz detuning. Therefore a real resonance in this scan should be a large, broad depletion of readout 2 relative to readout 1 over at least one to several adjacent scan points.

Observed data comparison:

The measured readout 2 minus readout 1 differences have mean +0.14 counts and standard deviation 1.46 counts, with minimum -2.48 counts and maximum +3.15 counts. The largest observed positive contrast (readout1 - readout2) / readout1 is only 0.0506 at 3.835 GHz, equivalent to a 2.48 count drop. This is far smaller than the approximately 10.4 count drop expected for the active mod_depth = 1, 52 ns pulse. Adjacent points also do not show the expected broad resonant depletion: at 3.830 GHz the drop is 1.48 counts and at 3.840 GHz readout 2 is brighter than readout 1 by 0.46 counts.

Conclusion:

The physically expected pODMR signal for the active pulse would be much larger and more structured than the observed readout differences. The data do not show a pODMR resonance.
