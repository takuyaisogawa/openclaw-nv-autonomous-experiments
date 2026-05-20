Case podmr_017_2026-05-12-134151

Input sequence and active readouts

The provided XML is Rabimodulated.xml. The active instruction block first polarizes the NV and performs a detection before any microwave pulse; this is the true m_S = 0 reference readout. The optional m_S = +1 reference block is guarded by full_expt, and full_expt is 0, so that block is inactive. The only active microwave manipulation before the second detection is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on)

Therefore readout 1 is the m_S = 0 reference and readout 2 is the pODMR signal after the Rabi pulse. The relevant parameters from the XML are mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate rounding leaves 52 ns unchanged because 52 ns * 250 MHz = 13 samples.

Physical model calculation

Use the driven two-level transition probability for a square pulse:

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

where Omega is the on-resonance Rabi frequency in cycles/s, Delta is the detuning in cycles/s, and t is the pulse length. The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected fractional readout drop is C(Delta) = 0.22 * P(Delta).

For the stated setup, Omega = 10 MHz * mod_depth = 10 MHz. With t = 52 ns:

Omega * t = 10e6 * 52e-9 = 0.52 cycles
P(0) = sin^2(pi * 0.52) = 0.9961
C(0) = 0.22 * 0.9961 = 0.2191, or about a 21.9% signal drop at resonance.

Even if using the embedded raw-export sequence default of mod_depth = 0.3 as a conservative cross-check, Omega = 3 MHz and P(0) = sin^2(pi * 0.156) = 0.2216, giving an expected peak contrast of 4.87%. The provided XML value is mod_depth = 1, so the primary expected signal is the much larger 21.9% feature.

Data comparison

The scan covers 3.825 to 3.925 GHz in 5 MHz steps. For each point I normalized the signal readout to the preceding reference readout as:

contrast = (readout1 - readout2) / readout1

The measured contrast values, in percent, are:

-10.31, -1.26, 3.00, 6.03, 0.66, -4.77, 8.73, -8.68, 3.32, -1.58, 2.25, -2.86, -1.99, -6.34, 1.72, 3.66, -2.72, 4.54, -6.46, 0.00, 3.52

Their mean is -0.45% and their standard deviation is 4.85%. The largest positive point is 8.73%, far below the 21.9% drop expected from the active XML pulse, and it is not supported by neighboring points. A grid fit of the square-pulse resonance model with fixed mod_depth = 1 gives a best resonance center near 3.83975 GHz but would predict a broad local feature of about 12.9% to 17.8% around 3.835 to 3.840 GHz after baseline offset; the measured points in that region are only 3.00% and 6.03%, and the residual error is dominated by mismatch rather than a coherent dip. The apparent per-average structure is consistent with tracking drift/cadence, not independent repeatability of a resonance.

Decision

The active sequence should produce a large, model-shaped pODMR contrast feature if a resonance is present. The paired readouts do not show that feature, and their normalized differences fluctuate around zero at the few-percent level. I therefore classify this case as resonance_absent.
