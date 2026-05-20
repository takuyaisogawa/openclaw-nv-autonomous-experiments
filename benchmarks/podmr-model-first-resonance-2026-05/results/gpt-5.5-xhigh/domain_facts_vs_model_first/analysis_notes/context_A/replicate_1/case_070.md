Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The active XML has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The two active detections are therefore:
- readout 1: after optical polarization, the true ms=0 reference.
- readout 2: after a modulated Rabi pulse, the pODMR signal readout.

The active pulse before readout 2 is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse. On resonance I would expect readout 2 to be substantially lower than readout 1, approaching the setup contrast scale of about 22% for a good flip.

The combined raw data do not show that. The lowest readout2/readout1 ratio is about 0.943 near 3.900 GHz, only about a 5.7% drop, and other nearby or comparable excursions go in the opposite direction. The raw reference also drifts over the scan, and the stored two averages should not be treated as a strong independent repeatability test. The weak single-point notch near 3.900 GHz is therefore not enough evidence for a real pODMR resonance under this near-pi-pulse sequence.

Decision: resonance_absent.
