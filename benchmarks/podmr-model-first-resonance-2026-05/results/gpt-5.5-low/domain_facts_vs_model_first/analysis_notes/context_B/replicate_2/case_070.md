Case: podmr_056_2026-05-17-050447

Sequence and readout roles

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first polarizes the NV, then immediately performs a detection. This first detection is the true m_S = 0 / bright reference readout. Because full_expt = 0, the optional m_S = 1 reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and performs the second detection. Thus readout 1 is the pre-microwave bright reference and readout 2 is the post-pulse pODMR signal readout.

Recorded pulse parameters

The recorded scan variables give length_rabi_pulse = 52 ns and mod_depth = 1. The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so the expected resonant Rabi frequency here is 10 MHz.

Explicit signal model calculation

For a resonant rectangular pulse, the transition probability from m_S = 0 to m_S = +1 is

P = sin^2(pi * f_Rabi * tau).

With f_Rabi = 10 MHz and tau = 52 ns:

pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 0.52 pi,
P = sin^2(0.52 pi) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pulse should reduce the post-pulse readout relative to the bright reference by approximately

0.22 * 0.996 = 0.219, or 21.9%.

Using the measured readout 1 mean baseline of 43.77 raw units, the expected resonant decrease in readout 2 relative to readout 1 is about

43.77 * 0.219 = 9.59 raw units,

corresponding to an expected resonant readout2/readout1 ratio near 0.781.

Observed data comparison

The measured combined readouts have mean readout 1 = 43.77 and mean readout 2 = 43.93. The pointwise difference readout2 - readout1 has mean +0.16 raw units and standard deviation 1.42 raw units, with a minimum of -2.60 raw units and maximum of +2.90 raw units. The minimum combined readout2/readout1 ratio is 0.943 at 3.900 GHz. The individual stored averages show similar scale: their minimum ratios are about 0.923 and 0.927, still far above the modeled resonant ratio of about 0.781, and stored averages are not treated as a strong independent repeatability test.

Decision

A real pODMR resonance under this pulse condition should produce a large post-pulse fluorescence dip relative to the bright reference, around 9.6 raw units or 22%. The observed readout separation is centered near zero and never approaches the expected resonant contrast. The visible variations are compatible with drift/noise and tracking cadence rather than a resonant population-transfer signal. I therefore decide that a pODMR resonance is absent.
