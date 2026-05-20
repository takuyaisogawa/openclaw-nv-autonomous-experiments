Case: podmr_034_2026-05-15-235221

I used the provided sequence XML rather than labels or prior outputs. The active sequence is Rabimodulated.xml. With full_expt = 0, the optional m_S = +1 reference block is skipped. The two acquired readouts are therefore:

- readout 1: detection immediately after optical polarization, the bright m_S = 0 reference for each scan point.
- readout 2: detection after a single modulated microwave Rabi pulse, the pODMR signal channel.

The active pulse parameters from the provided sequence XML are length_rabi_pulse = 52 ns and mod_depth = 1. The pulse is rounded to the 250 MHz sample clock, and 52 ns is already an integer 13 samples. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:

For a square resonant microwave pulse on a two-level transition, the transferred population is

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * t),

where Omega/(2*pi) is the Rabi frequency and delta/(2*pi) is the detuning. The setup facts give f_Rabi approximately 10 MHz at mod_depth = 1, so on resonance:

P1(0) = sin^2(pi * f_Rabi * t)
      = sin^2(pi * 10e6 * 52e-9)
      = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fluorescence drop is

C_expected = 0.22 * 0.996 = 0.219, or about 22%.

Using the combined raw readouts, I normalized the microwave-pulse readout by the preceding bright reference at each frequency:

C_obs = 1 - readout2/readout1.

The largest observed drops are:

- 3.870 GHz: C_obs = 0.193
- 3.875 GHz: C_obs = 0.217
- 3.880 GHz: C_obs = 0.246

The off-feature baseline, excluding 3.865-3.885 GHz, is mean C = 0.023 with standard deviation 0.038. Thus the central feature is about 17-22 percentage points deeper than the local baseline, matching the approximately 22% signal expected from a near-pi pulse on resonance. The absolute readout difference also reaches -8.60 counts at 3.880 GHz, compared with an off-feature mean of -0.84 counts and standard deviation 1.37 counts.

The two stored averages are not treated as independent strong repeatability tests, since averages can reflect tracking cadence, but they are directionally consistent: average 1 shows central drops of 0.187, 0.207, and 0.301 at 3.870-3.880 GHz, and average 2 shows 0.198, 0.228, and 0.189 at 3.870-3.880 GHz.

Decision: the observed dip has the correct readout role, sign, frequency-localized shape, and quantitative amplitude for the active 52 ns, mod_depth = 1 pODMR pulse. A pODMR resonance is present.
