Case podmr_030_2026-05-13-160024

I used the sequence XML and raw export directly. The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions have full_expt = 0, so the optional m_S = +1 reference block is skipped. The acquired readout roles are therefore:

- readout 1: after adj_polarize and detection, a bright m_S = 0 reference.
- readout 2: after a rabi_pulse_mod_wait_time pulse followed by detection, the pODMR signal readout.

The pulse parameters are length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup calibration, the Rabi frequency is approximately 10 MHz at mod_depth = 1. The resonant transition probability for a square pulse is sin^2(pi * f_R * t), giving sin^2(pi * 10e6 * 52e-9) = 0.996. With an m_S = 0 to m_S = +1 contrast scale of about 22% and a readout-1 mean of 27.37 counts, a resonant point should lower readout 2 by about 27.37 * 0.22 * 0.996 = 6.00 counts relative to readout 1.

Observed readout2 - readout1 differences across the scan are:
-0.096, 0.673, 2.067, -0.096, -1.346, 0.913, 1.010, -2.260, 0.529, 2.404, -0.240, 1.923, -2.212, -0.240, 3.269, -0.240, -0.192, 1.635, -1.538, -1.010, 2.644 counts.

The mean difference is +0.362 counts with standard deviation 1.571 counts. The deepest observed negative excursion is only -2.260 counts at 3.860 GHz, far smaller than the approximately -6 count physical expectation for this near-pi pulse. A fixed-amplitude Lorentzian dip model using the expected 6.00 count loss, allowing center and widths from 5 to 50 MHz, gives SSE 49.354 versus 49.365 for a constant baseline, essentially no improvement. An unconstrained negative-dip fit prefers only about 2.46 counts amplitude, below the expected physical contrast and comparable to the scatter.

Decision: resonance_absent. The data do not show the expected pODMR contrast for the active near-pi microwave pulse.
