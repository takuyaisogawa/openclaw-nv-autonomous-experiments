Active sequence and readout roles

The provided sequence is Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect, giving readout 1 as the true m_S = 0 fluorescence reference. The block that would acquire an m_S = 1 reference is gated by full_expt, and full_expt = 0, so it is inactive. The only subsequent active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

followed by detection, giving readout 2 as the signal after the Rabi pulse.

Relevant sequence parameters

- length_rabi_pulse = 52 ns
- mod_depth = 1
- sample_rate = 250 MHz, so the 52 ns pulse rounds to 13 samples and remains 52 ns
- mw_freq is the scanned frequency
- no adiabatic inversion is active in the measured branch

Expected signal calculation

The setup Rabi frequency is about 10 MHz at mod_depth = 1, with linear scaling, so here Omega_R = 10 MHz. For a square pulse with detuning Delta, I used the two-level Rabi population model:

P_1(Delta) = Omega_R^2 / (Omega_R^2 + Delta^2) * sin^2(pi * t * sqrt(Omega_R^2 + Delta^2))

where frequencies are in cycles/s and t = 52 ns. On resonance:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance fluorescence reduction is:

0.22 * 0.996 = 0.219, or about 21.9%.

Using the observed readout-1 mean as the local m_S = 0 reference, mean(readout 1) = 42.075 counts, the expected resonant readout-2 minimum is:

42.075 * (1 - 0.219) = 32.86 counts.

Observed data comparison

The observed readout-2 minimum is 33.923 counts at 3.880 GHz. Relative to the readout-1 value at the same scan point, 41.231 counts, this is a ratio of 0.823 and a drop of 17.7%. Relative to the mean readout-1 level, it is a drop of 19.4%. This is close to the 21.9% expected resonant drop given the approximate contrast and Rabi-frequency calibration.

I also fit the detuned Rabi model above to readout 2 with fixed Omega_R = 10 MHz, t = 52 ns, contrast = 22%, and baseline = mean(readout 1), varying only the resonance center. The best center is 3.8784 GHz. The model minimum is 33.11 counts. The sum of squared residuals is 30.71, compared with 144.17 for a constant readout-2 null model and 198.29 for a flat m_S = 0 reference model. Thus the physically expected pODMR line shape explains about 79% of the variance versus a flat readout-2 null.

The per-average traces should not be overinterpreted as independent repeatability because stored averages may reflect tracking cadence. Even so, both averages show the same readout-2 depression around the same frequency region.

Decision

The magnitude, frequency-localized dip, and quantitative agreement with the 52 ns mod_depth = 1 Rabi model support a pODMR resonance being present.
