Case podmr_049_2026-05-17-004217

I used the provided sequence XML and raw export only.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and detects immediately. This is the true m_S = 0 bright reference, readout 1.
- full_expt = 0, so the optional separate m_S = 1 reference block is inactive.
- The active experiment pulse is one rabi_pulse_mod_wait_time call with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. This post-pulse detection is readout 2.

Quantitative physical model:
- Given setup Rabi frequency = 10 MHz at mod_depth = 1, the active pulse has Omega_R/(2*pi) about 10 MHz.
- For a resonant square Rabi pulse, transferred population P = sin^2(pi*f_R*t).
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi*10e6*52e-9) = 0.996.
- The m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected fractional signal drop at resonance is 0.22*0.996 = 0.219, or about 21.9%.
- With the observed bright reference mean readout 1 = 49.86 raw counts, this corresponds to an expected resonant drop of about 10.93 raw-count units in readout 2 relative to readout 1.

Measured comparison:
- Mean readout 1 = 49.856, mean readout 2 = 49.775.
- Mean readout2-readout1 = -0.082 counts with standard deviation 1.49 counts across frequency.
- The strongest observed drop readout1-readout2 is only 2.62 counts at 3.850 GHz, about 5.1% of the local reference and far below the expected about 10.9-count, 21.9% resonant drop.
- Several frequencies have readout 2 brighter than readout 1; the largest positive readout2-readout1 excursion is +3.54 counts at 3.890 GHz.
- The readout2/readout1 ratios range from 0.949 to 1.072, while the resonant model predicts a ratio near 0.781 at resonance.

Decision:
The active 52 ns, mod_depth 1 pulse should be essentially a pi pulse on resonance and should create a large, obvious pODMR contrast dip in the signal readout. The data show only small fluctuations and drift-scale differences, not the expected resonant response. I therefore decide that a pODMR resonance is absent.
