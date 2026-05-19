<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_077

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided XML has full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout 1 is the initial polarized mS=0 fluorescence reference, acquired before the microwave pulse.
- Readout 2 is the fluorescence after the active Rabi-modulated microwave pulse.
- Active pulse duration: length_rabi_pulse = 52 ns. At 250 MS/s this is already on the 4 ns sample grid.
- mod_depth = 1 in the provided sequence/variable values.

Quantitative expected signal model:
- Given the setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the pulse is nearly a pi pulse.
- For a rectangular resonant pulse, the excited-state transfer probability is
  P(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t).
- With t = 52 ns and delta = 0, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated contrast scale of 22%, the expected fractional fluorescence drop in readout 2 relative to readout 1 at resonance is 0.22 * 0.996 = 0.219.
- The mean readout 1 level is 51.82 counts, so the expected resonant dip is about 11.36 counts, corresponding to readout2/readout1 near 0.781.
- Since the frequency step is 5 MHz, a resonance inside the scanned range should land within at most 2.5 MHz of a sampled point; the expected sampled dip would still be of order 10 counts.

Observed comparison:
- readout1 mean/std = 51.82 / 1.49 counts.
- readout2 mean/std = 51.40 / 1.53 counts.
- readout2 - readout1 mean/std = -0.42 / 1.36 counts, with extrema -2.73 to +1.69 counts.
- readout2/readout1 mean/std = 0.992 / 0.026, with extrema 0.950 to 1.033.
- The largest observed negative difference is much smaller than the approximately 11 count dip expected from a 52 ns, mod_depth 1 resonant pulse.
- A line-shape fit of ratio = c - D * P(delta) at plausible centers inside the scan gives fitted D values near zero, not the expected D about 0.22.

Decision:
The active pulse should produce a large, localized pODMR dip if a resonance is present in the scan range, but the data show only small point-to-point fluctuations and slow baseline drift. Therefore the pODMR resonance is absent.
