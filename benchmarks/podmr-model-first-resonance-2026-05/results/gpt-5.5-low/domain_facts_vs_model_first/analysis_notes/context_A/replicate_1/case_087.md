Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz. The active instructions polarize, detect the mS=0 level, wait, then apply one rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. full_expt = 0, so the optional mS=+1 reference block is skipped.

Readout roles: readout 1 is the initial polarized mS=0 fluorescence reference; readout 2 is the post-microwave-pulse fluorescence signal. Since the current setup has about 22% contrast between mS=0 and mS=+1, a resonant near-pi pulse should produce a clear decrease of readout 2 relative to readout 1 at resonance. With a Rabi frequency near 10 MHz at mod_depth = 1, the 52 ns pulse is close to the pi-transfer scale.

The combined traces stay close together across the scan, with readout 2 sometimes above and sometimes below readout 1 by only a few counts. There is no localized, repeatable contrast feature near a frequency that approaches the expected 22% mS=0 to mS=+1 change. The two averages mainly show tracking/noise-scale variation rather than an independent repeated resonance.

Decision: resonance_absent.
