Case podmr_001_2026-05-16-000631 analysis note

Sequence identification:
- The provided XML and embedded scan metadata identify the active sequence as Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The two active detections are therefore:
  - readout 1: true m_S = 0 bright reference after optical polarization, before the microwave pulse.
  - readout 2: signal readout after the modulated Rabi microwave pulse.
- mod_depth = 1 from the active variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already an integer 13 samples and remains 52 ns after rounding.

Quantitative physical model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the pulse area is f_R * tau = 10e6 * 52e-9 = 0.52 Rabi cycles.
- For a square pulse, the transition probability versus detuning df is:
  P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * tau * sqrt(f_R^2 + df^2)).
- On resonance, P(0) = sin^2(pi * 0.52) = 0.9961, essentially a pi pulse.
- With the stated bright-to-dark contrast scale of 22%, the expected fractional drop of readout 2 relative to the bright reference on resonance is 0.22 * 0.9961 = 0.2191, so the expected normalized resonant signal is about 1 - 0.2191 = 0.7809 of readout 1.

Observed data check:
- The measured readout2/readout1 ratios near the dip are:
  - 3.870 GHz: 32.231 / 37.385 = 0.862
  - 3.875 GHz: 30.000 / 38.212 = 0.785
  - 3.880 GHz: 28.981 / 37.135 = 0.780
  - 3.885 GHz: 31.923 / 34.423 = 0.927
  - 3.890 GHz: 35.212 / 37.154 = 0.948
- The minimum observed ratio is 0.780 at 3.880 GHz, corresponding to a 22.0% drop, matching the 21.9% on-resonance model prediction.
- A least-squares fit of the square-pulse model shape to the ratio data gives a center near 3.8775 GHz, baseline about 0.999, and fitted contrast amplitude about 0.230, close to the expected 0.22 contrast scale.
- The stored averages both show the same central readout-2 depression, but I treat this only as consistency under the tracking cadence, not as a strong independent repeatability test.

Decision:
The readout-2 dip has the expected role, magnitude, and frequency-localized shape for a pODMR resonance under the active 52 ns, mod_depth 1 Rabi pulse model. A pODMR resonance is present.
