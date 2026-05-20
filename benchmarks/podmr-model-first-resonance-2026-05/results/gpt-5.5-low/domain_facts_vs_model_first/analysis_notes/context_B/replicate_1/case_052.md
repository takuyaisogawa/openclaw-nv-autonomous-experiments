Case: podmr_038_2026-05-16-214551

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave preparation before the signal readout is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- full_expt = 0, so the conditional "+1 level reference" block is skipped.
- Readout 1 is the first detection after optical polarization, before the microwave pulse. It is the bright m_S = 0 reference for each frequency point.
- Readout 2 is the detection after the 52 ns Rabi-modulated microwave pulse. This is the pODMR signal readout.

Quantitative model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the expected resonant Rabi frequency here is 10 MHz.
- For a resonant square pulse, the population transfer probability is P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns and f_Rabi = 10 MHz, P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219, or 21.9% of the bright reference.
- The mean readout 1 level is 46.568 raw units, so the expected resonant drop is about 46.568 * 0.219 = 10.20 raw units. A resonant readout 2 near the line center would therefore be expected near 36.36 raw units before allowing for linewidth and detuning.

Observed data check:
- Mean readout 1 = 46.568.
- Mean readout 2 = 46.231.
- Mean readout2 - readout1 = -0.337 raw units.
- Standard deviation of pointwise readout2 - readout1 across the scan = 1.168 raw units.
- Largest observed fractional drop of readout 2 relative to readout 1 is at 3.845 GHz: readout 1 = 46.519, readout 2 = 43.731, drop = 2.788 raw units = 5.99%.
- No scan point approaches the expected 10.20 raw-unit, 21.9% drop for a resonant near-pi pulse.
- The stored two averages show tracking-level drift and scatter, not a repeated localized dip consistent with the physical contrast model.

Decision:
The active sequence should produce a large localized drop in readout 2 relative to readout 1 if a pODMR resonance is present. The observed scan has only small fluctuations and no model-sized depletion, so I classify this case as resonance_absent.
