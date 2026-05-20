Case podmr_050_2026-05-17-005655.

Sequence inspection:
- Active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction path first polarizes and detects the bright m_S = 0 reference.
- full_expt is 0, so the optional m_S = +1 reference block is inactive; the second active detection is after the driven Rabi pulse and is the pODMR signal readout.
- mod_depth is 1 and length_rabi_pulse is 52 ns. With the stated setup scale, this is approximately a pi pulse at 10 MHz Rabi frequency.

Data assessment:
At resonance, a 52 ns pulse at mod_depth 1 should transfer population strongly and the signal readout should show a large contrast change relative to the 0 reference, on the order of the setup contrast scale. The two combined readouts instead remain close together across the sweep, mostly around 52 to 55 raw units, with point-to-point fluctuations and no stable, localized dip or peak of the expected magnitude. The per-average traces show large baseline offsets between averages, consistent with tracking/cadence drift, and the apparent features are not independently stable enough to support a resonance call.

Decision: resonance_absent.
