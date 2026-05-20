Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active instruction flow is:
1. polarize, then detection: this is the true mS = 0 reference readout;
2. the "Acquire 1 level reference" block is skipped because full_expt = 0;
3. apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1;
4. detection: this is the post-pulse signal readout.

With the stated setup, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the microwave frequency is resonant, this should transfer population away from mS = 0 and reduce the post-pulse readout by a contrast on the order of the setup scale, about 22%, relative to the 0-reference.

The combined raw traces do not show that behavior. Readout 2 is not consistently suppressed relative to readout 1 over a resonance-like frequency region. There is an isolated low point near 3.905 GHz, but it is comparable to the size and irregularity of fluctuations elsewhere, and stored averages are not a strong independent repeatability test here because they can reflect tracking cadence. The two readout channels remain mostly similar in level, without a coherent ODMR dip of the expected scale.

Decision: resonance_absent.
