<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_070

I used only the provided XML/raw export for this isolated case.

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR scan with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect the m_S = 0 level, then wait, then apply a modulated Rabi pulse, then detect again.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive.
- Readout 1 role: true m_S = 0 fluorescence reference after optical polarization.
- Readout 2 role: signal fluorescence after the microwave Rabi pulse.
- mod_depth from the provided sequence XML/variable values: 1.
- Rabi pulse duration: length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the rounded pulse remains 52 ns.

Expected physical signal calculation:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a resonant rectangular pulse, the transition probability is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce the signal readout by approximately 0.22 * 0.996 = 21.9% relative to the m_S = 0 reference.
- The mean readout-1 reference is 43.77 raw counts, giving an expected on-resonance drop of 43.77 * 0.219 = 9.59 raw counts, i.e. an on-resonance signal around 34.18 counts if the resonance is sampled near its center.

Explicit model/simulation check:
- I modeled the transition probability across detuning using the rectangular-pulse Rabi expression
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- I compared the measured readout 2 against a physical resonance model y = k * readout1 * (1 - 0.22 * P(mw_freq - f0)), scanning f0 across and just beyond the measured frequency range, and also against a no-resonance scaled-reference model y = k * readout1.
- No-resonance scaled-reference fit: k = 1.003, SSE = 40.38.
- Best fixed-contrast physical resonance fit: best f0 was outside the scan at 3.8145 GHz, k = 1.011, SSE = 30.83. This avoids putting the expected pi-pulse dip inside the data; any in-range centered resonance would require a much larger drop than observed.
- A free-amplitude dip fit found an in-range dip amplitude of only about -3.24 counts, far below the approximately -9.6 counts predicted by the supplied physical model. Because the user requested the decision be based on the relevant physical model, this smaller empirical fluctuation is not sufficient evidence for resonance.

Observed data check:
- Readout 2 ranges from 41.35 to 46.37 counts and does not approach the approximately 34-count signal expected for an on-resonance 52 ns, mod_depth 1 pulse.
- Pointwise readout2 - readout1 ranges only from -2.60 to +2.90 counts.
- The readout2/readout1 ratio ranges from 0.943 to 1.068; a resonant pi pulse should be near 0.781 under the stated 22% contrast model.
- Stored averages are only two and can reflect tracking cadence, so I did not treat average-to-average behavior as strong independent repeatability evidence.

Decision:
The active pulse sequence should produce a large near-pi-pulse pODMR fluorescence loss if a resonance is present in the scan, but the measured signal shows only small tracking-scale fluctuations around the reference. I therefore decide resonance_absent.
