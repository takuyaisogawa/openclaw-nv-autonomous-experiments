Case podmr_031_2026-05-16-195907

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the conditional +1 reference branch is inactive even though do_adiabatic_inversion is true. The readout roles are therefore:

- readout 1: polarized mS = 0 reference acquired immediately after adj_polarize and before the microwave pulse.
- readout 2: signal readout acquired after rabi_pulse_mod_wait_time.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1, this is approximately a pi pulse. If a pODMR resonance were present in this sweep, the signal readout should show a clear fluorescence reduction on resonance, on the order of the stated 22% mS = 0 to mS = +1 contrast scale.

The combined raw readouts are instead both centered near 52.7 counts. Readout 2 ranges only from about 51.08 to 54.5 counts, while the pre-pulse reference readout itself ranges from about 49.81 to 55.54 counts. The readout2/readout1 ratio ranges roughly 0.929 to 1.044, with isolated points rather than a coherent resonance feature. The strongest low point in readout 2 is small compared with the expected near-pi-pulse contrast and is not supported by a stable, repeatable resonance shape. The per-average overlays are dominated by a large offset between averages, consistent with tracking cadence rather than an independent repeatability test.

Decision: resonance_absent.
