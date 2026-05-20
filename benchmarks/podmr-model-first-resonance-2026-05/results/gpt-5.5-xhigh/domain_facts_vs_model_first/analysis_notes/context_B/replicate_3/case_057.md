Active sequence and readout roles

The provided sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction path is:

1. adj_polarize for pumping.
2. detection immediately after pumping.
3. skip the m_S = +1 reference branch because full_expt = 0.
4. one rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth.
5. detection after that pulse.

Therefore readout 1 is the pumped m_S = 0 reference, and readout 2 is the post-microwave-pulse signal. There is no active independent m_S = +1 reference readout in this run.

Pulse parameters from the provided XML

sample_rate = 250 MHz, so the 52 ns rabi pulse is exactly 13 samples and remains 52 ns after rounding. mod_depth = 1. freqIQ = 50 MHz is used by set_microwave, but the resonance decision can be made by asking whether any scan point shows the expected resonance-shaped drop in readout 2 relative to readout 1.

Quantitative model calculation

Using the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse, the driven population transfer versus detuning df is

P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2))

with f_R = 10 MHz and t = 52 ns. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

With a 22% fluorescence contrast scale between m_S = 0 and m_S = +1, an on-resonance pulse should reduce the post-pulse readout by

0.22 * 0.996 = 0.219

or about 21.9% relative to the readout 1 reference. Around a 47 count baseline this is about 10.3 counts. The same model predicts about 20.4% contrast at 2.5 MHz detuning, 16.5% at 5 MHz detuning, and 6.0% at 10 MHz detuning, so the 5 MHz scan spacing should still show a large dark feature if the resonance is inside the scanned interval.

Observed comparison

I used y = (readout1 - readout2) / readout1 as the resonance-like contrast, where positive y means readout 2 is darker than the m_S = 0 reference. Across the 21 scan points:

mean(y) = -0.0095
sd(y) = 0.0200
max positive y = 0.0243 at 3.885 GHz

The maximum observed darkening is only about 2.4%, roughly one ninth of the expected 21.9% line-center response for the active pulse. The average sign is also opposite to a resonance: readout 2 is generally brighter than readout 1.

I also fit the explicit line-shape model y = baseline + A * P(df), allowing the resonance center to vary across the scanned interval. With A constrained to be positive, the best fit gives A = 0.023 at about 3.8408 GHz, only about one tenth of the expected contrast scale of 0.22. If A is unconstrained, the best fit has A = -0.036 near 3.8649 GHz, which is the wrong sign for a pODMR resonance under this readout assignment.

Decision

The active pulse should produce a large negative-going post-pulse fluorescence signal if a pODMR resonance is present in this scan. The data show only small few-percent fluctuations, no compatible line-shape amplitude, and the strongest fitted line-shaped component has the wrong sign when unconstrained. I therefore decide that a pODMR resonance is absent.
