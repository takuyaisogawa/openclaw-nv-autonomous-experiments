Case: podmr_030_2026-05-16-194429

Inputs used:
- Sequence XML / exported active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- Active readout structure from the instructions:
  - First detection follows adj_polarize and is the bright m_S = 0 reference.
  - full_expt = 0, so the optional m_S = +1 reference block is skipped.
  - Second detection follows rabi_pulse_mod_wait_time and is the microwave-pulse signal readout.
- Active pulse parameters:
  - length_rabi_pulse = 52 ns after sample-rate rounding.
  - mod_depth = 1 from the active variable values.
  - The adiabatic inversion flag is present but not used in the skipped full_expt block.

Physical model calculation:
The setup contrast between m_S = 0 and m_S = +1 is about 22%. The stated Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. Therefore the active pulse has f_R = 10 MHz and t = 52 ns.

For a square pulse, the driven transition probability versus detuning is modeled as

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)

using frequencies in cycles/s. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The expected fluorescence dip at resonance is therefore approximately

0.22 * 0.996 = 0.219, or 21.9% of the bright readout.

The measured bright reference level is about 53.51 raw counts, so the expected on-resonance raw drop in the post-pulse signal relative to the bright reference is about

53.51 * 0.219 = 11.7 counts.

The model also predicts a broad enough feature at this sampling to be visible across nearby points:
- 2.5 MHz detuning: expected fractional dip = 20.4%.
- 5 MHz detuning: expected fractional dip = 16.5%.
- 10 MHz detuning: expected fractional dip = 6.0%.

Observed data comparison:
- readout 1 mean = 53.51, standard deviation across scan = 1.17.
- readout 2 mean = 53.43, standard deviation across scan = 1.28.
- readout2/readout1 mean = 0.9987.
- Minimum readout2/readout1 = 0.9473 at 3.895 GHz, corresponding to a 5.3% local deficit or 2.77 raw counts.

This observed minimum is much smaller than the 21.9% / 11.7-count dip expected for the active near-pi pulse. It is also an isolated small feature on top of comparable raw fluctuations and does not show the expected strong Rabi-broadened pODMR line shape. The stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.

Decision:
Given the active sequence and quantitative expected signal scale, the data do not show the required pODMR resonance signature. I classify this case as resonance_absent.
