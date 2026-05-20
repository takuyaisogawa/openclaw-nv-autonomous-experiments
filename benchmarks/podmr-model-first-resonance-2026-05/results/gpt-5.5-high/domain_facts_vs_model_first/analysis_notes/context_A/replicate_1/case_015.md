Active sequence: Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz.

Sequence roles:
- The first detection occurs immediately after adj_polarize and is the true mS = 0 optical reference.
- full_expt = 0, so the optional mS = 1 reference block is inactive.
- The second detection follows rabi_pulse_mod_wait_time and is the microwave-pulse-dependent pODMR signal readout.

Pulse settings from the provided sequence inputs:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s but unchanged because 52 ns is exactly 13 samples.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so an on-resonance transition can produce close to the full available contrast.

Data assessment:
Readout 1 stays roughly flat in the mid-30 count range and does not show a matching dip. Readout 2 shows a localized decrease from about 34-35 counts to about 26 counts around 3.875-3.880 GHz, then recovers on both sides. The depth is about 8 counts relative to a mid-30 baseline, consistent with the stated roughly 22% contrast scale for mS = 0 to mS = +1 under an approximately pi-length pulse. The two stored averages show the same central depression in the second readout, but I treat that only as supporting context because stored averages can reflect tracking cadence.

Decision: a pODMR resonance is present.
