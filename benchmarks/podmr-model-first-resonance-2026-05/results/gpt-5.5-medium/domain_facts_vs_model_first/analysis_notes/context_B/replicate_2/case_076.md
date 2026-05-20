Case: podmr_062_2026-05-17-063134

Sequence/readout interpretation:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first polarizes the NV and performs detection. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active microwave operation is therefore a single rabi_pulse_mod_wait_time pulse followed by detection. This second detection is the post-Rabi-pulse readout.
- mod_depth = 1 from the provided sequence/variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the pulse is already on a 4 ns sample grid.

Physical model calculation:

The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so the expected on-resonance population transfer for a square pulse is

P(+1) = sin^2(pi * f_R * t)
      = sin^2(pi * 10 MHz * 52 ns)
      = 0.996.

Thus a real resonance should make the post-pulse readout lower than the m_S = 0 reference by approximately

0.22 * 0.996 = 0.219, or about 22% of the fluorescence.

At a raw fluorescence level near 49 counts, this is an expected on-resonance drop of roughly 10.7 counts.

Data comparison:

Using the measured combined readouts, the post-pulse/reference fractional drop 1 - readout2/readout1 has:

- mean = -0.0011
- standard deviation = 0.0253
- maximum positive drop = 0.0626 at 3.920 GHz

The largest apparent drop is only about 6.3%, far below the expected 21.9%, and it is not accompanied by the neighboring broad response expected from a 52 ns Rabi pulse. Adjacent points around 3.920 GHz do not show a consistent dip: 3.915 GHz is essentially flat and 3.925 GHz has the opposite sign.

I also evaluated the square-pulse detuned Rabi model

P(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega/2pi = 10 MHz and t = 52 ns across possible resonance centers in the scan range. A free-amplitude fit prefers only about 0.042 contrast amplitude, much smaller than the expected 0.22. Forcing the expected 0.22 amplitude makes the residual sum of squares about 4.8 times worse than a flat no-resonance baseline.

Decision:

The measured readout difference is dominated by small point-to-point fluctuations/tracking-scale variation, not the large, broad post-pulse fluorescence drop expected for a resonant 52 ns near-pi pulse. I therefore classify this case as resonance absent.
