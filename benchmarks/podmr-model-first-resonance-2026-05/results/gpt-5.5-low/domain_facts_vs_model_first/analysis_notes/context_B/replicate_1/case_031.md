Case podmr_016_2026-05-16-131456

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and detects the bright m_S = 0 reference, then waits. Because full_expt = 0, the conditional "1 level reference" block is inactive, so no separate dark-state reference is acquired.
- The second active readout is after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so it is the pODMR signal readout after the microwave pulse.
- Exported run values: mod_depth = 1, length_rabi_pulse = 52 ns, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us.

Quantitative model:
- Given Rabi frequency approximately 10 MHz at mod_depth = 1, the 52 ns pulse corresponds to 10e6 * 52e-9 = 0.52 Rabi cycles.
- For a resonant Rabi pulse, transferred population is sin^2(pi * f_Rabi * t) = sin^2(pi * 0.52) = 0.996.
- With a setup contrast of about 22%, the expected ideal on-resonance fractional fluorescence drop in the post-pulse readout is 0.22 * 0.996 = 0.219, essentially the full available contrast.
- Using the observed readout 2 off-dip baseline excluding indices 8-12 gives 46.756 counts. The ideal expected resonant minimum is therefore 46.756 * (1 - 0.219) = 36.51 counts.

Observed data:
- Readout 1 is the bright reference and stays near 47 counts, with no matching resonance-shaped dip.
- Readout 2 has a pronounced trough: 44.63, 42.17, 39.65, 39.62, 41.15 counts at 3.865, 3.870, 3.875, 3.880, and 3.885 GHz.
- The minimum is 39.615 counts at 3.880 GHz. Relative to the off-dip baseline of 46.756 counts, the observed drop is 7.141 counts or 15.3%.
- The off-dip standard deviation of readout 2 is about 0.720 counts, so the trough depth is about 9.9 times that scatter estimate.
- The observed 15.3% drop is below the ideal 21.9% calculated for a perfect centered resonant pi pulse, but it is the correct sign, localized in frequency, large relative to noise, and of the expected scale for a broadened or slightly detuned resonance.

Decision: resonance_present.
