Sequence and readout interpretation

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825e9 to 3.925e9 Hz in 5 MHz steps. The sequence first calls adj_polarize followed by detection, which is the true mS=0 reference readout. Because full_expt = 0, the optional mS=+1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the bright reference and readout 2 is the pODMR signal after the microwave pulse.

Quantitative expected signal model

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz and scales linearly with mod_depth. For a resonant square pulse, the transfer probability is P = sin^2(pi * f_Rabi * t). With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996. The expected resonant fluorescence contrast is therefore approximately 0.22 * 0.996 = 0.219, or a 21.9% drop from the mS=0 bright level. Off resonance the transfer should be strongly suppressed by detuning, producing a localized dip rather than a broad baseline shift.

Observed signal

Readout 2 has an off-resonance baseline of about 37.41 counts if the central dip region is excluded. Its minimum is 28.98 counts near the center of the scan, giving an observed contrast of (37.41 - 28.98) / 37.41 = 22.5%. This agrees closely with the 21.9% model expectation for a near-pi pulse at mod_depth = 1. The dip is visible in both stored averages, although the stored averages should mainly be treated as tracking-cadence views rather than independent repeatability tests.

Decision

The magnitude and localization of the second-readout dip match the expected pODMR response for the active pulse sequence. A pODMR resonance is present.
