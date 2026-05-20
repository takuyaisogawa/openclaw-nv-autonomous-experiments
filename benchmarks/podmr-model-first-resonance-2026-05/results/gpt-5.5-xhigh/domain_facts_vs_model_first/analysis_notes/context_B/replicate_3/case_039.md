Case: podmr_024_2026-05-16-175646

I used the provided sequence XML before judging the trace. The active sequence is the Rabimodulated pODMR scan with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the instructions, the first detection occurs immediately after optical polarization, so readout 1 is the true m_S = 0 fluorescence reference. The block that would acquire an m_S = 1 reference is skipped because full_expt = 0. The active microwave manipulation is therefore the later rabi_pulse_mod_wait_time call, followed by detection, so readout 2 is the signal after the Rabi pulse. The sequence values used for the model are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, and the pulse rounds to 13 samples = 52 ns.

Quantitative model:

For the stated setup, the Rabi frequency is about 10 MHz at mod_depth = 1. Starting in m_S = 0, I modeled the population transferred to m_S = +1 as

P(+1, Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2)),

with Omega = 10 MHz and t = 52 ns. On resonance this gives P(+1) = sin^2(pi * 10 MHz * 52 ns) = 0.996. With the stated 22% fluorescence contrast between m_S = 0 and m_S = +1, the expected resonant fluorescence drop in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 21.9%. For a typical reference count of 53.9, that is an expected drop of about 11.8 raw-readout units. Because the frequency step is 5 MHz, an in-range resonance would be sampled within 2.5 MHz of a scan point; the same model predicts about a 20.4% drop at 2.5 MHz detuning and 16.5% at 5 MHz detuning, so a real resonance should be an obvious dip in readout 2.

Measured comparison:

Using the combined readouts, the normalized drop y = (readout1 - readout2) / readout1 has mean -0.0061 and standard deviation 0.0211. The largest positive drop is only 0.0307 at 3.895 GHz, while several points have readout 2 above readout 1. The average readout 2 is slightly higher than readout 1: 54.17 versus 53.86. A fixed positive resonance model with the expected 22% contrast fits much worse than a constant baseline. Allowing the amplitude and offset to float gives a best-fit drop amplitude of about -0.032 times the Rabi line shape, opposite in sign and far smaller than the expected +0.22.

The stored averages have different count offsets, consistent with tracking cadence effects, so I did not treat them as a strong independent repeatability test. They also do not show the large expected readout-2 suppression.

Decision: resonance_absent. The physically expected near-pi-pulse pODMR dip is not present in the measured readout comparison.
