Case: podmr_006_2026-05-16-011837

I used inputs/sequence.xml as the sequence definition. The active sequence is Rabimodulated.xml with a microwave frequency scan. The instruction block polarizes the NV, performs detection, waits, then conditionally would acquire a 1-level reference only if full_expt is nonzero. Here full_expt = 0, so that branch is inactive. The two active readouts are therefore:

- readout 1: the true m_S = 0 reference immediately after optical polarization, before the microwave pulse.
- readout 2: the pODMR readout after the microwave pulse.

The active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on)

The sequence parameters are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and mod_depth = 1. The duration is rounded to sample clock ticks in the sequence; 52 ns is 13 samples at 250 MHz, so the active pulse remains 52 ns.

Quantitative expected signal model:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1. A square pulse with detuning delta transfers population with

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

where Omega = 10 MHz and t = 52 ns, using cycles/s units. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected fractional fluorescence drop at resonance is:

0.22 * 0.996 = 0.219, or 21.9%

Data comparison:

The combined raw readouts give readout2/readout1 ratios across the scan. Using points away from the visible feature as the off-resonance baseline, excluding 3.865 to 3.890 GHz, the mean baseline ratio is 0.979 with standard deviation 0.032. The minimum ratio is 0.762 at 3.875 GHz. The drop from baseline is:

(0.979 - 0.762) / 0.979 = 0.222, or 22.2%

This closely matches the 21.9% drop predicted by the active 52 ns, mod_depth = 1 near-pi pulse model. A brute-force center-frequency comparison with the same fixed physical model gives the best center at about 3.878 GHz. The model sum of squared residuals for the normalized ratio is 0.0197, compared with 0.119 for a constant off-resonance baseline model, so the resonance-shaped model explains the dominant deviation much better than no resonance.

The two stored averages both show the same feature near the center of the scan, with minimum ratios at 3.875 and 3.880 GHz. I treat that only as consistency with the combined trace because stored averages can mainly reflect tracking cadence, not a strong independent repeatability test.

Decision: resonance_present. The post-microwave readout shows a localized, physically sized dip at the frequency where a 52 ns mod_depth = 1 pODMR pulse should produce nearly full m_S = 0 to m_S = +1 transfer.
