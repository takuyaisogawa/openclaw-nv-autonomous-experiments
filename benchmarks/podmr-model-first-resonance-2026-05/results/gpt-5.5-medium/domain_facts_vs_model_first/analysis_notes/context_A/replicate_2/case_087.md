Active sequence: Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active instructions first polarize the NV and take a detection readout, which serves as the mS=0 optical reference. Because full_expt is 0, the optional mS=+1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection readout, which is the microwave-affected signal readout.

Using the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. With an mS=0 to mS=+1 contrast scale near 22%, an on-resonance point should show a substantial reduction of the post-pulse signal readout compared with the mS=0 reference. The observed combined readouts instead stay around 47-52 counts with readout 2 sometimes above and sometimes below readout 1, and there is no consistent dip near the expected microwave resonance region or a feature with amplitude approaching the expected contrast. The two stored averages vary noticeably and are not a strong independent repeatability test, but the averaged signal itself lacks a physically plausible pODMR resonance signature.

Decision: resonance_absent.
