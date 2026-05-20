I used the supplied sequence XML and raw readouts only.

The active sequence is Rabimodulated.xml. It first polarizes and detects, which is the true m_S = 0 reference readout. The optional m_S = +1 reference section is skipped because full_expt = 0, so the only active microwave-dependent measurement is the later rabi_pulse_mod_wait_time followed by detection. Therefore readout 1 is the no-microwave bright reference and readout 2 is the pulsed measurement.

The active pulse has length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse because half a 10 MHz Rabi period is 50 ns. A resonance should therefore produce a large fluorescence drop in readout 2 relative to readout 1, with a scale approaching the stated 22% m_S = 0 to m_S = +1 contrast.

The combined raw data show a narrow, selective depression in readout 2 near scan values 3.875e9 to 3.880e9. At the deepest point, readout 2 is about 39.1 while readout 1 is about 48.5, a drop of about 19%. The neighboring point remains strongly depressed as well. Readout 1 does not show a matching dip, and both stored averages show the same readout-2 depression despite the caveat that stored averages may mostly reflect tracking cadence.

Because the pulse duration and modulation depth make the expected contrast large, and the observed contrast is large, localized, and specific to the pulsed readout, I decide that a pODMR resonance is present.
