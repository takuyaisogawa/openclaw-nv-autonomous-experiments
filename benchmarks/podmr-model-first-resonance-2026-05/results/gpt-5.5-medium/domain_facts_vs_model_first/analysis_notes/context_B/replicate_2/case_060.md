Case: podmr_046_2026-05-16-235726

Sequence/readout identification:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions polarize, then detect immediately: readout 1 is the true m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection: readout 2 is the post-microwave signal readout.
- From the provided XML and variable values: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The pulse is already on the 4 ns sample grid.

Quantitative physical model:
- Setup Rabi frequency at mod_depth = 1 is approximately 10 MHz.
- For a resonant square pulse, transition probability P = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns, f_R * t = 0.52 cycles and P = sin^2(pi * 0.52) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant signal ratio is 1 - 0.22 * 0.996 = 0.7809.
- The mean m_S = 0 reference readout is 52.1566, so an on-resonance point should be near 40.73 counts, a drop of about 11.43 counts.
- Including detuning with P(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)) gives the same 0.7809 minimum ratio if the resonance is on a sampled grid point, with broad neighboring dips over the 5 MHz-spaced scan.

Data comparison:
- Mean readout 1 = 52.1566; mean readout 2 = 51.1227.
- The minimum readout 2 value is 48.8462, far above the approximately 40.73 count resonant prediction.
- The minimum readout2/readout1 ratio is 0.9140, much shallower than the expected 0.7809 resonant ratio.
- The largest pointwise readout2 - readout1 drop is 4.596 counts, less than half the expected resonant drop.
- The per-average traces show tracking-scale shifts and point scatter, not a consistent resonance-shaped depletion in the signal channel.

Decision:
The expected resonant response for the active 52 ns, mod_depth = 1 pulse is a large near-pi-pulse fluorescence dip. The observed data do not contain a dip of the required magnitude or coherent lineshape, so I decide that a pODMR resonance is absent.
