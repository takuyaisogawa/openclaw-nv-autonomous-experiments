Case podmr_044_2026-05-16-232730

I used inputs/sequence.xml as the active sequence description. The active pulse sequence is Rabimodulated.xml. In the instructions, the first detection follows adj_polarize and is the true m_S = 0 reference. The "Acquire 1 level reference" block is disabled because full_expt = 0, so there is no separate m_S = +1 reference readout. The second detection follows the active rabi_pulse_mod_wait_time call and is the pODMR signal readout. The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz, the rounded pulse length remains 52 ns.

Physical model calculation:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1, so f_R = 10 MHz. For a square pulse with detuning Delta, the driven transfer probability is

P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With t = 52 ns and f_R = 10 MHz, the on-resonance transfer is sin^2(pi * 10e6 * 52e-9) = 0.996. Using the stated 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance signal in readout 2 relative to readout 1 is a fractional drop of 0.22 * 0.996 = 0.219, or about 21.9%. Because the scan step is 5 MHz, any resonance whose center lies inside the scanned range has a sampled point within 2.5 MHz. The same model gives P_1(2.5 MHz) = 0.929, corresponding to at least about a 20.4% sampled drop. At a typical 48 count readout, that would be roughly a 9.8 to 10.5 count depression.

Observed combined readout comparison:

The combined readout-2/readout-1 fractional differences have mean +0.29%, standard deviation 2.22%, and minimum -4.78% at 3.865 GHz. The largest negative excursion is therefore far smaller than the expected 20% or larger drop from the active 52 ns, mod_depth = 1 pulse. A linear-detrended comparison gives a residual standard deviation of about 2.08% and a most negative residual of about -4.82%, still much smaller than the model expectation. A fixed-contrast model with any in-range resonance center fits substantially worse than a no-resonance linear baseline, because it predicts a deep dip that is absent. Allowing the dip amplitude to float gives only about 3.8% fitted contrast near 3.866 GHz, far below the 21.9% physical expectation for the active pulse.

The stored averages show tracking-level offsets and are not treated as an independent repeatability test. They do not change the model comparison: the expected pODMR feature for this sequence would be much larger than the observed few-percent fluctuations.

Decision: resonance_absent.
