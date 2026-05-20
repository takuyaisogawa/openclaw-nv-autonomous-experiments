Case: podmr_079_2026-05-17-103702

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, sibling cases, previous outputs, or external context.

Active sequence and readout roles:

- Sequence name in the export: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence XML, the active microwave operation is:
  `PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);`
  followed by detection.
- `full_expt = 0`, so the optional "Acquire 1 level reference" block is inactive.
- The first readout is acquired immediately after optical polarization and is therefore the m_S = 0 reference.
- The second readout is acquired after the Rabi-modulated microwave pulse and is the pODMR signal readout.
- `length_rabi_pulse = 52 ns`; at the 250 MS/s sample rate this is exactly 13 samples, so rounding does not change it.
- The executed variable list and the provided sequence XML give `mod_depth = 1`.

Quantitative signal model:

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a square resonant pulse, the transfer probability is

P_transfer = sin^2(pi * f_R * t).

With f_R = 10 MHz and t = 52 ns:

pi * f_R * t = pi * 0.52 = 1.6336 rad
P_transfer = sin^2(1.6336) = 0.9961.

The supplied contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional drop in the second readout relative to the first is

0.22 * 0.9961 = 0.2191, or 21.9%.

On the observed baseline near 50 raw counts, a resonance should therefore produce a negative paired change of about

50 * 0.2191 = 10.96 raw counts.

I also evaluated the square-pulse frequency response

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

against the measured paired difference readout2 - readout1 across the scan.

Observed data summary:

- Mean readout1: 50.718 counts.
- Mean readout2: 50.782 counts.
- Mean paired difference readout2 - readout1: +0.064 counts.
- Paired difference range: -2.096 to +2.308 counts.
- Relative paired difference range: -3.93% to +4.76%.

The largest observed negative excursion is only about 2.1 counts, far smaller than the approximately 11-count drop predicted for an on-resonance 52 ns pulse at mod_depth = 1. The observed paired differences also alternate in sign and do not form the expected negative pODMR dip. A simple least-squares fit of the expected square-pulse lineshape to the paired differences selected a negative amplitude scale, meaning the best model correlation has the opposite sign from a pODMR fluorescence drop.

Decision:

The sequence and physical model predict a large, easily visible negative second-readout feature if a pODMR resonance is present in the scanned frequency range. The measured signal lacks that feature. I therefore decide that a pODMR resonance is absent.
