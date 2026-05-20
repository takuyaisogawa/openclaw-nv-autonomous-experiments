Case: podmr_078_2026-05-17-102220

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML has full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- readout 1 is therefore the true mS = 0 reference after optical polarization and detection.
- readout 2 is the signal readout after the active microwave pulse and detection.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Quantitative model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the resonant rectangular-pulse transition probability is
  P = sin^2(pi * f_Rabi * t).
- For f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% mS = 0 to mS = +1 contrast scale, the expected on-resonance post-pulse signal ratio is
  signal/reference = 1 - 0.22 * 0.996 = 0.781.
- With the measured readout 1 mean of 51.83 counts, the expected resonant drop is about 11.36 counts.
- Even if the resonance were halfway between 5 MHz-spaced samples, the 52 ns pulse at 10 MHz Rabi rate would still produce a large sampled excitation, not a percent-level fluctuation.

Observed data:
- readout 1 mean = 51.83 counts; readout 2 mean = 51.76 counts.
- The readout2/readout1 ratio has mean 0.999, minimum 0.969, and maximum 1.040.
- The largest observed readout2 - readout1 deficit is -1.60 counts, far smaller than the approximately -11.36 count resonant signal expected from the active pulse.
- There is no clear dip in readout 2 relative to the mS = 0 reference at the expected physical scale.

Decision: resonance_absent.
