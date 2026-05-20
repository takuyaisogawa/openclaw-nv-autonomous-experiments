Case podmr_066_2026-05-17-072831

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, sibling cases, previous outputs, or external context.

Active sequence and readout roles:
- The sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first performs adj_polarize followed by detection. This first detection is the bright m_S = 0 reference/readout.
- full_expt = 0, so the optional separate m_S = +1 reference block is inactive.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse before the second detection. The second detection is therefore the pODMR signal readout after the microwave pulse.
- From the provided sequence XML, mod_depth = 1 and length_rabi_pulse = 52 ns.

Quantitative physical model:
- Given setup Rabi frequency 10 MHz at mod_depth = 1, the relevant Rabi frequency is approximately 10 MHz.
- For a resonant square pulse, the transferred population is P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant optical drop is 0.22 * 0.996 = 0.219, or about 21.9%.
- At the observed raw readout level near 45 counts, that corresponds to roughly 9.9 counts of depletion in the signal readout relative to the bright reference.

Observed data check:
- The measured second-readout minus first-readout differences range from -3.06 to +2.40 counts, with mean -0.53 counts and standard deviation 1.62 counts.
- The measured readout2/readout1 ratios range from 0.936 to 1.054, with mean 0.989 and standard deviation 0.035.
- The deepest apparent depletion cluster is only about 5-6% relative to the first readout, far below the approximately 22% depletion expected from the active 52 ns, mod_depth = 1 pulse.
- The per-average traces show substantial tracking-like offsets between stored averages, so the two stored averages are not a strong independent repeatability test.

Decision:
The active sequence should produce an almost full pi-pulse response on resonance, but the observed normalized depletion is much smaller and comparable to baseline/readout drift. I therefore decide that a pODMR resonance is absent.
