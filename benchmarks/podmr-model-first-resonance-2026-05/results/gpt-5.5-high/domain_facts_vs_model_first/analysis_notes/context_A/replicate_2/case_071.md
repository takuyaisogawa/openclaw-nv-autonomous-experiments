Case podmr_057_2026-05-17-051839.

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml / Rabimodulated, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executable instruction flow first polarizes and detects a true m_S = 0 optical reference, then because full_expt = 0 it skips the optional m_S = +1 reference block, then applies one modulated Rabi microwave pulse and detects the post-pulse signal. Thus the two combined readouts are the 0-level reference readout and the post-Rabi-pulse readout, not two independent ODMR repetitions.

The exported variable values give mod_depth = 1 and length_rabi_pulse = 5.2e-08 s = 52 ns. At the stated setup scale, the Rabi frequency is about 10 MHz at mod_depth = 1, so the pulse is essentially a pi pulse near resonance. If a pODMR resonance were present, the post-pulse readout should show a clear fluorescence decrease relative to the 0-reference readout, with order-22% contrast possible for strong inversion.

The raw readouts do not show such a feature. The signal-minus-reference differences are small and change sign across the sweep; the largest negative combined difference is about -2.08 counts, roughly -4.5%, far below the expected contrast scale, and comparable to the fluctuations visible between stored averages. The stored averages are also not a strong independent repeatability test because they can reflect tracking cadence.

Decision: resonance_absent.
