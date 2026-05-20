The active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz. The sequence first polarizes and detects the bright reference readout, then waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the pODMR signal detection. full_expt is 0, so the optional mS=+1 reference block is not active; readout 1 is the mS=0 bright reference and readout 2 is the post-microwave-pulse signal.

Using the supplied setup facts, mod_depth = 1 implies about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. With a current setup contrast of about 22% between mS=0 and mS=+1, a true resonance should make readout 2 substantially darker than readout 1 near the resonant frequency.

The combined readouts do not show that behavior. The readout 1 minus readout 2 contrast is only a few percent, changes sign repeatedly, and has no stable localized dip in readout 2 relative to the bright reference. Around 3.900 GHz, where readout 1 is low, readout 2 is actually higher than readout 1, which is the opposite of a resonant pi-pulse darkening signature. The per-average overlay also shows substantial tracking-like variation between stored averages, so the two averages should not be treated as strong repeatability evidence.

Decision: resonance_absent.
