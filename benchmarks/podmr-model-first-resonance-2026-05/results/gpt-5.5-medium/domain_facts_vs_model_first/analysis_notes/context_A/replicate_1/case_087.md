<!-- Model-generated analysis note. Not a ground-truth label. -->

Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- The first detection follows optical polarization only, so readout 1 is the true m_S = 0 reference.
- full_expt is 0, so the optional m_S = +1 reference block is inactive.
- The second detection follows rabi_pulse_mod_wait_time, so readout 2 is the microwave-pulse signal channel.

Pulse parameters from inputs/sequence.xml:
- length_rabi_pulse = 5.2e-08 s = 52 ns, rounded at 250 MS/s.
- mod_depth = 1.
- With the provided setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so 52 ns is approximately a pi pulse.

Decision:
For a single NV pODMR resonance under these conditions, a near-pi pulse on resonance should drive population from m_S = 0 toward m_S = +1 and reduce the post-microwave readout by a large fraction of the stated 22% contrast scale relative to the zero reference. The combined raw readouts instead track each other at the percent-level noise scale, with no narrow, reproducible suppression of readout 2 relative to readout 1 across the microwave frequency sweep. The two stored averages vary substantially and mainly reflect tracking/noise rather than independent confirmation. Therefore I do not identify a pODMR resonance in this dataset.
