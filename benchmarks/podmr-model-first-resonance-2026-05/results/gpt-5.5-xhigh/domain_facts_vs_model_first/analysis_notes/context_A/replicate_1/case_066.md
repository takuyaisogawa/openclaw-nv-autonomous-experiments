Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true. The active detections are:

1. Readout 1: immediately after adj_polarize, the true m_S = 0 fluorescence reference.
2. Readout 2: after rabi_pulse_mod_wait_time, the microwave-driven pODMR signal.

The active microwave pulse is length_rabi_pulse = 52 ns with mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so an on-resonance response should produce a clear drop of readout 2 relative to the readout 1 reference, with a scale approaching the stated 22% m_S = 0 to m_S = +1 contrast.

The raw counts show substantial common-mode drift and average-to-average tracking behavior. Normalizing the signal readout to the reference readout gives mostly small differences, generally a few percent, with no localized feature of the expected pi-pulse contrast scale. The largest negative relative point is at the high-frequency edge rather than a convincing resonance shape, and there is also a positive outlier elsewhere. Because the apparent structure is dominated by common-mode/tracking changes rather than a robust readout-2 suppression relative to readout 1, I do not identify a pODMR resonance in this scan.
