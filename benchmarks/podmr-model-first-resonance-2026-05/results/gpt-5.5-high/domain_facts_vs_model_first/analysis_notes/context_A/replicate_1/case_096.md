Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect, giving readout 1 as the mS = 0 fluorescence reference. Because full_expt = 0, the optional mS = 1 reference block is inactive. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, giving readout 2 as the post-microwave signal.

Using the provided setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. With the stated mS = 0 to mS = +1 contrast scale of about 22%, a real resonance should produce a substantial localized reduction in readout 2 relative to readout 1 near the resonant frequency.

The measured readout 2 minus readout 1 differences are small and irregular rather than a coherent resonance feature. The strongest apparent reductions are only about 3.46 counts at 3.850 GHz, 2.44 counts at 3.905 GHz, and 2.35 counts at 3.915 GHz, corresponding to roughly 5-7% contrast at most, and readout 2 is higher than readout 1 at several neighboring frequencies. The per-average traces also show cadence/noise-level variability rather than a stable repeated spectral dip. This is not consistent with a clear pODMR resonance under the active pulse conditions.

Decision: resonance_absent.
