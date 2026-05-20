Case: podmr_027_2026-05-16-184117

Input basis:
- Used only the isolated workspace files: inputs/sequence.xml, inputs/raw_export.json, and the raw readout plot.
- The active sequence is Rabimodulated.xml / Rabimodulated. The standalone sequence XML has sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, delay_wrt_1mus = 0.2 us, and pumping_time = 1 us.

Active pulse sequence and readout roles:
- The sequence first polarizes the NV, then performs detection. This is the true m_S = 0 optical reference and corresponds to readout 1.
- Because full_expt = 0, the "Acquire 1 level reference" block is inactive. The do_adiabatic_inversion flag is therefore not part of the active pulse path.
- The active microwave operation is one square Rabi pulse:
  rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)
  with length_rabi_pulse rounded to round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- The second detection follows this Rabi pulse and is the post-pulse signal readout, readout 2.

Physical model calculation:
- Given setup facts, f_Rabi(mod_depth = 1) = 10 MHz.
- For a square pulse, the transition probability versus detuning is modeled as:
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))
  where f_R and delta are in cycles/s and t is the pulse duration.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.
- The expected optical contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional drop in the post-pulse readout relative to the m_S = 0 reference is:
  0.22 * 0.996 = 0.219.
- The measured readout 1 mean is 53.794 raw counts, so a resonance should produce an on-resonance post-pulse signal near:
  53.794 * (1 - 0.219) = 42.006 raw counts,
  i.e. a drop of about 11.79 raw counts from readout 1.

Observed data:
- readout 1 mean = 53.794, standard deviation across scan points = 1.043.
- readout 2 mean = 52.947, standard deviation across scan points = 1.094.
- readout 2 - readout 1 has mean -0.847 raw counts, standard deviation 1.468, minimum -3.462, maximum +1.635.
- The normalized deficit 1 - readout2/readout1 has mean 0.0154, minimum -0.0318, and maximum 0.0632. The largest observed drop is only about 6.3%, far below the expected 21.9% on-resonance drop.

Line-shape check:
- I fit the same Rabi line shape over possible resonance centers within the scanned 3.825 to 3.925 GHz range using the normalized deficit y = 1 - readout2/readout1.
- With a free amplitude and offset, the best fit center is near 3.880 GHz and the fitted contrast amplitude is 0.038, not 0.22.
- A null constant-offset model gives RMS residual 0.0265 in normalized units.
- Forcing the physical 0.22 contrast line shape gives best RMS residual 0.0566, worse than the null model, and predicts a large local deficit near the candidate center that is not present.

Decision:
- The active pulse should be nearly a pi pulse at mod_depth = 1, so a real pODMR resonance in the sweep would make readout 2 sharply and substantially lower than readout 1 by roughly 12 raw counts at/near resonance.
- The measured post-pulse readout changes are small, inconsistent between stored averages, and consistent with noise/tracking-scale variation rather than the expected physical contrast.
- I decide the pODMR resonance is absent.
