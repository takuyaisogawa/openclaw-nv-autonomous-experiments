Case podmr_032_2026-05-14-161051

I used only the provided XML/exported raw data. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction flow is:

1. adj_polarize, then detection: readout 1 is the optically polarized mS=0 reference.
2. The "Acquire 1 level reference" block is skipped because full_expt = 0.
3. rabi_pulse_mod_wait_time, then detection: readout 2 is the post-microwave-pulse signal.

The relevant active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding leaves the pulse duration at round(52 ns * 250 MHz) / 250 MHz = 13 / 250 MHz = 52 ns.

Quantitative signal model:

The stated setup has Rabi frequency about 10 MHz at mod_depth = 1, with approximately linear scaling. For a resonant square Rabi pulse, the transition probability is

P(delta=0) = sin^2(pi * f_R * t)
           = sin^2(pi * 10e6 * 52e-9)
           = sin^2(1.6336)
           = 0.996.

The setup contrast between mS=0 and mS=+1 is about 22%, so an on-resonance 52 ns pulse should produce an expected fluorescence reduction of

0.22 * 0.996 = 0.219, or about 21.9%, in the post-pulse readout relative to the mS=0 reference.

For off-resonance points I used the standard detuned Rabi population model,

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

so the expected readout ratio is approximately readout2/readout1 = 1 - 0.22 * P(delta). This model predicts a localized dip with a frequency width set by the 52 ns pulse, on the order of tens of MHz.

Measured comparison from the combined raw readouts:

- At 3.880 GHz, readout 1 = 35.6538 and readout 2 = 29.3077.
- The ratio readout2/readout1 is 0.8220, a drop of 17.8%.
- At 3.875 GHz the drop is 7.7%, and at 3.870 GHz the drop is 6.7%, forming a localized low-readout region around 3.875-3.880 GHz.
- Away from the strongest dip, the mean readout2/readout1 drop is near zero with about 5.0% scatter, so the 17.8% point is about 3.5 standard deviations below the off-feature baseline.

The stored per-average traces have strong opposite drift with scan order, consistent with tracking cadence effects rather than independent repeatability. I therefore do not treat the two averages as a strong repeatability test. The combined post-pulse signal nonetheless shows a localized dip whose magnitude is close to the 21.9% expected from the active 52 ns, mod_depth 1 Rabi pulse.

Decision: resonance_present.
