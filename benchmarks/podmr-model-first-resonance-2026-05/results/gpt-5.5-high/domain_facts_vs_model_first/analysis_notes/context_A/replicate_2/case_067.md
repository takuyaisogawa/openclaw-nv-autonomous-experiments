Active sequence: Rabimodulated.xml, swept parameter mw_freq from 3.825 GHz to 3.925 GHz. The active instructions polarize first, then detect the bright m_S = 0 reference readout; because full_expt = 0, the optional m_S = 1 reference block is skipped. The second active detection is after rabi_pulse_mod_wait_time and is therefore the pODMR test readout after the microwave pulse.

Sequence parameters used for interpretation: mod_depth = 1 and length_rabi_pulse = 52 ns. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, the pulse is about 0.52 Rabi cycles, close to a pi pulse. If the swept microwave frequency hit a real resonance, the post-pulse readout should show a strong contrast against the polarized reference, on the order of the stated 22% scale.

The combined readouts do not show such a feature. Readout 2 is sometimes below and sometimes above readout 1, with only a modest single-point depression near 3.88 GHz and substantial shared drift/tracking structure across the scan. The per-average traces also look dominated by tracking changes rather than a repeatable resonance-shaped contrast feature. Given the near-pi pulse condition, the observed relative change is too small and inconsistent for a pODMR resonance.

Decision: resonance_absent.
