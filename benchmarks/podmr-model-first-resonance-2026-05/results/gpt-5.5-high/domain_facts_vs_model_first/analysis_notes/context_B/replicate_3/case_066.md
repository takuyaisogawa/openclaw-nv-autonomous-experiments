Case podmr_052_2026-05-17-015447

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.
- sample_rate = 250 MHz, so length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- mod_depth = 1.
- full_expt = 0, so the optional mS=+1 reference block is inactive even though do_adiabatic_inversion is true.
- Active readout roles:
  - readout 1: after adj_polarize and before the microwave pulse; this is the bright mS=0 reference.
  - readout 2: after a 52 ns rabi_pulse_mod_wait_time at the scanned mw_freq; this is the pODMR signal readout.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- Pulse duration t = 52 ns.
- Resonant transition probability for a square pulse is P = sin^2(pi f_R t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of 22%, an on-resonance microwave pulse should reduce the signal readout by about 0.22 * 0.996 = 0.219, i.e. about a 21.9% optical drop relative to the mS=0 reference.
- At the observed reference level near 27 counts, that corresponds to an expected on-resonance dip of about 5.9 counts in readout 2 relative to the no-resonance level.

I also evaluated the square-pulse detuning response
P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
The expected fractional optical drops are approximately:
- detuning 0 MHz: 21.9%
- detuning 5 MHz: 16.5%
- detuning 10 MHz: 6.0%
- detuning 15 MHz: 0.3%

Data comparison:
- The raw means are readout 1 = 27.413 and readout 2 = 26.974 counts.
- The pointwise normalized signal readout, readout2/readout1, ranges from 0.900 to 1.101, with strong point-to-point scatter and common drift.
- A linear baseline fit to readout2/readout1 gives RMSE 0.0359.
- Fitting the expected square-pulse resonance profile with fixed 22% amplitude plus a linear baseline makes the fit worse; the best center is at the scan edge, 3.925 GHz, with RMSE 0.0526.
- Allowing the resonance amplitude to float does not recover a positive resonance dip; the best unconstrained amplitude is negative, about -3.85%, so the data prefer no physical dip over the expected pODMR response.

Decision:
No pODMR resonance is present. The active pulse should produce a large, localized contrast feature if resonant, but the measured signal is dominated by drift/scatter and lacks the expected 22% resonance-shaped dip.
