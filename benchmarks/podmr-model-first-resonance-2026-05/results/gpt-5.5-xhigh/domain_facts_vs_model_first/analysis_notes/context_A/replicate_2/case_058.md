Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction block first polarizes and detects, explicitly marked as the true mS=0 reference. Because full_expt = 0, the separate mS=1 reference branch is skipped. The only driven measurement is then a rabi_pulse_mod_wait_time call followed by detection, so readout 1 is the polarized mS=0 reference and readout 2 is the post-microwave-pulse signal.

The active parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. At the stated setup scale this corresponds to a Rabi frequency of about 10 MHz, so the pulse is close to a pi pulse. A real resonance should therefore strongly depress the post-pulse signal relative to the mS=0 reference, with an expected scale approaching the approximately 22% mS=0 to mS=+1 contrast.

The measured readout2/readout1 differences are small and inconsistent with that expectation. The largest combined negative contrast is only about -4.8% near 3.865 GHz, with other points showing positive or weak negative differences and substantial tracking-like per-average offsets. The stored averages do not provide a strong independent repeatability test, and the raw readouts do not show a clear resonant dip of the expected size.

Decision: resonance_absent.
