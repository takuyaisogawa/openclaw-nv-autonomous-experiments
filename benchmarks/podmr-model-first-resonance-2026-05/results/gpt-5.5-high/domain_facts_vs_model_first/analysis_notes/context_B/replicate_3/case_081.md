Case podmr_067_2026-05-17-074342

I used the provided sequence XML and raw export only.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first call adj_polarize, then detection. This first stored readout is the optically polarized mS=0 bright reference.
- full_expt is 0, so the optional mS=1 reference block is skipped.
- The active microwave operation is a single rabi_pulse_mod_wait_time followed by detection. This second stored readout is the post-pulse signal readout.
- The active pulse duration is length_rabi_pulse = 52 ns.
- The active mod_depth is 1 from the provided XML and exported variable values.

Physical model calculation:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1, the 52 ns pulse is very close to a pi pulse: pi-pulse time is 1/(2*f_Rabi) = 50 ns.
- For a rectangular pulse, using detuning in cycles/s, the transfer probability is
  P_flip(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t).
- At zero detuning with f_R = 10 MHz and t = 52 ns, P_flip = sin^2(pi*10e6*52e-9) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of about 22%, an on-resonance point should make readout 2 lower than readout 1 by about 0.22*0.996 = 21.9%.
- At the endpoint 3.925 GHz, where the scan and XML nominal mw_freq meet, readout 1 = 47.846 and readout 2 = 50.423, giving (readout1-readout2)/readout1 = -5.39%, opposite in sign from a dark resonant response. The expected on-resonance readout 2 from the model would be about 37.36 if readout 1 is used as the bright reference.

Quantitative data check:
- The observed normalized contrast values (readout1-readout2)/readout1 range from -6.28% to +4.77%, with a standard deviation of about 3.23%. They never approach the expected ~22% resonant dip.
- Fitting the expected rectangular-pulse line shape at the nominal 3.925 GHz center gives a negative fitted amplitude (-2.66%), again opposite to the expected positive darkening.
- Allowing the resonance center to float over the scan gives a best fitted positive amplitude of only about 4.55%, far below the expected 22%.
- Forcing the physical 22% amplitude and floating the center gives a residual sum of squares of 0.0681, much worse than a flat no-resonance model at 0.0208.
- The two stored averages at the endpoint both show readout 2 brighter than readout 1, so the average overlay does not rescue a hidden resonant dip.

Decision:
The pulse should have produced a large post-pulse fluorescence decrease at resonance, but the signal readout shows only small scan-to-scan fluctuations and no physically sized dark dip. I therefore classify this case as resonance_absent.
