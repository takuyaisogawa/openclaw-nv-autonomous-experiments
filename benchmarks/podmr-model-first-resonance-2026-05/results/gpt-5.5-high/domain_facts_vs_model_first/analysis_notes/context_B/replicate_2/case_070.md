Case podmr_056_2026-05-17-050447

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The scan reports SequenceName = Rabimodulated.xml, and the provided XML is the Rabimodulated sequence.
- full_expt = 0, so the optional mS=+1 reference block is inactive.
- The first detection occurs immediately after adj_polarize and is the true mS=0 reference readout.
- The second detection occurs after one rabi_pulse_mod_wait_time call and is the microwave-pulsed signal readout.
- The active microwave pulse has length_rabi_pulse = 52 ns after sample-rate rounding.
- mod_depth = 1 in the provided sequence XML and in the exported active Variable_values.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- Rectangular resonant-pulse transition probability: P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected pODMR contrast from mS=0 to mS=+1 is about 22%, so the expected fractional PL drop on resonance is 0.22 * 0.996 = 0.219, about 21.9%.
- The mean reference readout is 43.77 raw counts, so the expected resonant signal readout is lower by about 9.59 counts, near 34.18 counts if the reference is 43.77.
- Including detuning for a rectangular pulse with P(df) = (f_R^2/(f_R^2+df^2)) * sin^2(pi * t * sqrt(f_R^2+df^2)), a resonance halfway between 5 MHz-spaced scan points still gives P(2.5 MHz) = 0.929, corresponding to an expected sampled drop of about 20.4%. Thus a real resonance in this scan range should produce a large negative readout2-readout1 feature at one or more scan points.

Observed quantitative comparison:
- Combined readout means: readout1 = 43.77, readout2 = 43.93.
- The observed readout2-readout1 differences range from -2.60 to +2.90 counts.
- The most negative fractional change is -5.7%, far smaller than the expected approximately -22% resonant drop.
- The average difference is +0.16 counts with standard deviation 1.42 counts; no point approaches the expected roughly -9.6 count decrease.
- A flat model has SSE 0.0209 in fractional readout difference. A fixed-contrast 22% Rabi lineshape over possible resonance centers has best SSE 0.0724, worse than flat. A free-amplitude lineshape fit prefers a negative drop amplitude of -3.95%, meaning the best fit is not a pODMR dip.

Decision:
The active sequence would produce a large, sampled PL decrease if an mS=+1 pODMR resonance were present in the scanned frequency range. The observed data show only small fluctuations and no quantitatively compatible dip, so I decide resonance_absent.
