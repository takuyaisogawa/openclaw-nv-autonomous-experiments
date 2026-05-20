Case: podmr_030_2026-05-16-194429

Inputs used only from this workspace: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles:
- The saved scan reports SequenceName = Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The saved sequence variables are the operative values for this measurement: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz, mw_freq final value = 3.925 GHz, freqIQ = 50 MHz.
- In the instruction block, the sequence first performs adj_polarize followed by detection. This is the true m_S = 0 reference readout.
- The optional m_S = 1 reference block is skipped because full_expt = 0.
- The only driven measurement block is rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) followed by detection. Thus readout 1 is the bright m_S = 0 reference and readout 2 is the post-microwave-pulse readout.

Quantitative expected signal model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, the expected resonant Rabi frequency here is f_R = 10 MHz.
- For a square resonant pulse of duration t = 52 ns, the transferred population fraction is sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected fractional pODMR signal for a resonance is 0.22 * 0.996 = 0.219.
- The mean bright-reference readout is 53.512 counts, so an on-resonance driven readout dip should be about 53.512 * 0.219 = 11.73 counts if the scanned transition is addressed.

Observed data:
- Combined readout means are readout 1 = 53.512 and readout 2 = 53.432 counts.
- The largest negative point in readout2 - readout1 is at 3.895 GHz: 49.808 - 52.577 = -2.769 counts, corresponding to only about 5.3% of the local reference.
- A linear-baseline residual check gives this point about -2.4 to -2.5 sigma depending on whether the candidate point and neighbors are excluded from the residual estimate. The residual amplitude is still only about one quarter of the 11.7 count model expectation.
- Other points fluctuate at the 1 to 2 count level and the per-average traces differ substantially, consistent with tracking cadence and measurement scatter rather than a robust pODMR lineshape.

Decision:
The active pulse should produce a near-full population transfer and therefore a large readout-2 dip if a pODMR resonance is present. The observed feature is much smaller than the quantitative expectation and not repeatable enough across stored averages to overcome that mismatch. I decide resonance_absent.
