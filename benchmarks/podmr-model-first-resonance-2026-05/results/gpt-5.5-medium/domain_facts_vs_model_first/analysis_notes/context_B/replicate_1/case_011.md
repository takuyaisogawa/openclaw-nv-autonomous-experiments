Case: podmr_028_2026-05-13-100213

Active sequence and readout roles

I used inputs/sequence.xml as the provided sequence definition. The active sequence is the Rabimodulated pODMR sequence: polarize, detect, wait, apply one rabi_pulse_mod_wait_time pulse, detect, then final wait. The conditional "Acquire 1 level reference" block is inactive because full_expt = 0, so the two stored readouts are not mS=0 and mS=+1 references. Readout 1 is the initialized mS=0 fluorescence reference acquired before the microwave pulse. Readout 2 is the signal fluorescence after the modulated microwave Rabi pulse.

Sequence parameters used for the physical expectation:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate remains 52 ns (13 samples)
- scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- setup contrast between mS=0 and mS=+1 is about 22%
- Rabi frequency is about 10 MHz at mod_depth = 1

Quantitative model

For a rectangular resonant drive, I modeled the transition probability as

P(detuning) = (fR^2 / (fR^2 + detuning^2)) * sin^2(pi * sqrt(fR^2 + detuning^2) * tau)

with fR = 10 MHz and tau = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

so the expected fluorescence loss in readout 2 relative to readout 1 is

0.22 * 0.996 = 0.219 of the mS=0 readout.

The measured readout 1 mean is 27.69 counts, so the expected on-resonance dip is about

27.69 * 0.219 = 6.07 counts.

The finite 52 ns pulse is broad, so adjacent 5 MHz points should also show a substantial dip if the resonance sits on a sampled frequency. For example, at +/-5 MHz the same model gives P = 0.749, corresponding to about 4.56 counts expected dip.

Observed comparison

The combined readout difference readout1 - readout2 across the scan is:

-1.92, -3.96, 2.23, 1.46, 0.23, 1.46, 2.04, -0.77, 0.15, 1.15, -0.08, 1.50, 1.54, -1.00, -1.15, 1.69, 3.50, -0.46, -0.08, 0.04, 1.58 counts.

The largest positive difference is 3.50 counts at 3.905 GHz. That is only about 58% of the expected on-resonance dip. More importantly, the neighboring points do not follow the expected pulse response: if 3.905 GHz were the resonance, the 3.900 and 3.910 GHz points should be elevated by roughly 4.6 counts, but they are 1.69 and -0.46 counts. The feature is also not consistently repeated as a clean resonance-like profile in the two stored averages; stored averages are treated cautiously because they often reflect tracking cadence rather than a strong independent repeatability test.

Conclusion

The active pulse should produce a large, broad pODMR dip if a resonance were present in this scan. The observed data show only small irregular readout differences and do not match the expected detuned Rabi line shape. I therefore decide that a pODMR resonance is absent.
