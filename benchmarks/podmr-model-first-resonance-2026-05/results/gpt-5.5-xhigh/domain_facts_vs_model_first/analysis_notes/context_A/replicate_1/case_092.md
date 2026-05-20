Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction order gives the readout roles. The first active detection follows adj_polarize and is the true m_S = 0 reference. The full_expt branch is inactive because full_expt = 0, so the sequence does not acquire a separate m_S = +1 reference. The second active detection follows rabi_pulse_mod_wait_time and is the microwave-pulse signal readout.

The active pulse is length_rabi_pulse = 52 ns after sample-rate rounding, with mod_depth = 1. Using the provided setup facts, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is essentially a pi pulse. On resonance this should produce a large drop in the post-pulse signal relative to the m_S = 0 reference, on the order of the stated 22% contrast scale.

The paired raw readouts differ only by small, sign-changing amounts across the sweep, and both channels show comparable slow drift/noise. There is no localized, reproducible contrast dip in the microwave-pulse readout of the size expected for a near-pi pulse at full modulation depth.

Decision: resonance absent.
