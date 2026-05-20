Case podmr_060_2026-05-17-060259 analysis

Sequence and readout roles

The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. From the provided sequence XML and variable values, mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so the pulse is already on the 4 ns grid.

The instruction block first performs optical polarization and detection. That first detection is the true m_S = 0 reference readout. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and performs a second detection. Thus readout 1 is the 0-reference/tracking readout, and readout 2 is the pODMR signal readout after the microwave pulse.

Quantitative model

Use the given setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Therefore f_R = 10 MHz here. For a rectangular resonant pulse, the transferred population is

P_1(t) = sin^2(pi f_R t).

With t = 52 ns:

P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated fluorescence contrast between m_S = 0 and m_S = +1 is about 22 percent. The readout 1 mean is 50.943 raw-count units, so a resonant 52 ns pulse should reduce the second readout by approximately

50.943 * 0.22 * 0.996 = 11.16 raw-count units.

That corresponds to an expected resonant readout 2 near 39.8 counts if the scan crosses a driven transition, ignoring smaller broadening and detuning effects. Off resonance the pulse should not transfer population and readout 2 should remain near the readout 1/reference level.

Observed data check

The measured combined readouts are:

- readout 1 mean = 50.943, population standard deviation across scan points = 1.098
- readout 2 mean = 50.197, population standard deviation across scan points = 1.053
- readout2 - readout1 mean = -0.746
- readout2 - readout1 range = -3.635 to +1.962
- minimum readout 2 = 48.673 at 3.890 GHz

The deepest observed readout2-reference deficit is 3.63 counts, and it is not close to the expected roughly 11.16-count resonant response from a near-pi pulse. The expected resonant contrast is about 7.6 times the standard deviation of the observed combined readout2-readout1 differences. Stored averages are only two averages and can reflect tracking cadence, so I do not treat the per-average overlays as independent confirmation of repeatability; they mainly show fluctuations of a few counts.

Decision

Given the active sequence, readout roles, mod_depth = 1, and 52 ns pulse, a real resonance in this scan should produce a large negative feature in the second readout relative to the first reference readout. The observed data stay near the reference level with only small fluctuations. I therefore decide that no pODMR resonance is present.
