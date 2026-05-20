Case podmr_028_2026-05-13-100213.

Sequence identification:

The active saved sequence is Rabimodulated.xml, with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence XML sets length_rabi_pulse = 52 ns and mod_depth = 1. The 250 MHz sample clock gives a 4 ns sample interval, so round(52 ns * 250 MHz) = 13 samples and the pulse remains 52 ns.

Readout roles from the instruction order:

1. adj_polarize followed by detection gives the true m_S = 0 reference. This is readout 1.
2. full_expt = 0, so the optional m_S = +1 reference block is inactive.
3. A rabi_pulse_mod_wait_time pulse of length_rabi_pulse and mod_depth is then applied, followed by detection. This is readout 2, the microwave-affected signal.

Physical model calculation:

For the stated setup, f_Rabi = 10 MHz * mod_depth = 10 MHz. I used the square-pulse two-level transition model

P(Delta) = f_Rabi^2 / (f_Rabi^2 + Delta^2) * sin^2(pi * tau * sqrt(f_Rabi^2 + Delta^2))

with tau = 52 ns and Delta in cycles/s. The expected readout ratio is

readout2 / readout1 = 1 - C * P(Delta)

with C = 0.22 for the m_S = 0 to m_S = +1 contrast scale.

On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected fluorescence drop is 0.22 * 0.996 = 0.219, or about 22%. With a 5 MHz scan step, a resonance centered on a sampled point should still give approximate expected drops of 16.5% at +/-5 MHz and 6.0% at +/-10 MHz. Thus the expected signature is not just one low point; it should be a multi-point dip in readout 2 relative to readout 1.

Observed normalized contrast, computed as 1 - readout2/readout1, has its largest value at 3.905 GHz:

3.895 GHz: -0.0439
3.900 GHz:  0.0638
3.905 GHz:  0.1267
3.910 GHz: -0.0176
3.915 GHz: -0.0027

The maximum observed drop is about 12.7%, below the expected 21.9% on-resonance response, and the neighboring points do not show the required symmetric broad dip. The point at 3.900 GHz is only a modest drop and the 3.910 GHz point goes the wrong way.

I also compared count-space models using readout 1 as the local fluorescence reference. A no-resonance scale model r2 = s * r1 gave SSE = 55.12 counts^2. A fixed physical resonance model r2 = s * r1 * (1 - 0.22 * P) improved only weakly, with best SSE = 52.77 counts^2 and with the best center outside the scan window near 3.951 GHz. Allowing the contrast amplitude to fit freely near the apparent 3.904 GHz feature gave only about 0.066 fitted contrast, far below the expected 0.22 for mod_depth = 1 and a 52 ns near-pi pulse.

Conclusion:

The data contain a low point near 3.905 GHz, but it does not match the quantitatively expected pODMR lineshape or contrast for the active pulse sequence. I therefore decide that a pODMR resonance is absent.
