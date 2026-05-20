Case podmr_053_2026-05-17-042031

Sequence interpretation

The provided XML is Rabimodulated.xml. The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction sequence first polarizes the NV center and performs a detection before any scanned microwave pulse; this first readout is therefore the bright m_S = 0 reference. The full_expt variable is 0, so the optional separate m_S = +1 reference block is inactive. The active pODMR contrast readout is the later detection after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. The provided XML has mod_depth = 1.

Quantitative expected signal model

Using the stated setup calibration, the resonant Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square resonant pulse of duration t = 52 ns, the expected population transfer from m_S = 0 to m_S = +1 is

P(+1) = sin^2(pi * f_R * t)
      = sin^2(pi * 10e6 * 52e-9)
      = 0.996.

With the stated bright-to-dark contrast scale of about 22%, the expected post-pulse fluorescence ratio at resonance is

R_res / R_bright = 1 - 0.22 * 0.996 = 0.781.

The mean bright reference readout is 45.20 counts, so an on-resonance point should be near 35.29 counts, corresponding to an approximately 9.90 count dip in readout 2 relative to readout 1. Equivalently, the readout2/readout1 ratio should approach about 0.781 at resonance.

Observed data comparison

The combined readouts have mean readout1 = 45.20 and mean readout2 = 45.02. The lowest readout2 value is 42.60 at 3.880 GHz. The strongest normalized depression is also at 3.880 GHz, with readout2/readout1 = 42.596/45.885 = 0.928, a 3.29 count drop. Another low point around 3.890 GHz has a similar 3.23 count drop. These depressions are much smaller than the approximately 9.90 count drop expected for a resonant 52 ns, mod_depth 1 pulse.

Across all scan points, the readout2 - readout1 differences have mean -0.18 counts and standard deviation about 1.53 counts. A physical resonance under the model above should be a large, easily visible post-pulse dip, about 6.5 times this empirical difference scatter and near 78% of the bright reference. No scan point approaches that expected amplitude.

Decision

Given the active readout role and the quantitative Rabi/contrast model from the provided XML parameters, the observed data do not show the expected pODMR resonance signature. I classify this case as resonance_absent.
