Case: podmr_030_2026-05-16-194429

Sequence identification

The provided sequence is Rabimodulated.xml. The active instructions polarize, detect, wait, then execute a single `rabi_pulse_mod_wait_time` block followed by detection. `full_expt = 0`, so the optional m_S = +1 reference block is inactive. Therefore readout 1 is the true m_S = 0 optical reference after polarization, and readout 2 is the signal after the Rabi-modulated microwave pulse.

Relevant active parameters from the provided sequence/exported variable values:

- `length_rabi_pulse = 5.2e-08 s` = 52 ns.
- `mod_depth = 1`.
- `mw_freq` is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The stored averages are only 2 averages and are treated mainly as tracking cadence, not as a strong independent repeatability test.

Quantitative physical expectation

Using the supplied setup facts, the Rabi frequency at `mod_depth = 1` is about 10 MHz. For a square pulse, the resonant transfer probability is

`P1(Delta=0) = sin^2(pi * f_Rabi * t)`.

With `f_Rabi = 10 MHz` and `t = 52 ns`,

`P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996`.

The m_S = 0 to m_S = +1 contrast scale is about 22%, so a resonant point should reduce the post-pulse readout by roughly

`mean(readout1) * 0.22 * 0.996 = 53.51 * 0.22 * 0.996 = 11.7 raw-count units`.

Thus an on-resonance second readout should be near `53.5 - 11.7 = 41.8`, modulo ordinary noise and slow tracking.

Observed data check

The combined readouts have:

- mean readout 1 = 53.51, population standard deviation across scan = 1.14.
- mean readout 2 = 53.43, population standard deviation across scan = 1.25.
- readout2 - readout1 mean = -0.08, RMS spread = 1.23.
- largest negative readout2 - readout1 excursion = -2.77 counts at 3.895 GHz.

The largest observed dip is only about 24% of the expected 11.7-count resonant pi-pulse contrast and is comparable to ordinary point-to-point scatter. It is also not a clean resonance line shape in the scan.

I also evaluated an explicit detuned Rabi model,

`P1(Delta) = f_Rabi^2/(f_Rabi^2 + Delta^2) * sin^2(pi * sqrt(f_Rabi^2 + Delta^2) * t)`,

with fixed `f_Rabi = 10 MHz`, `t = 52 ns`, and 22% contrast, allowing the resonance center to move over the scan. The best such physical model still predicts an approximately 11.6-count dip and gives RMSE about 3.32 raw-count units against readout 2. A no-resonance model where readout 2 is readout 1 plus a constant offset gives RMSE about 1.23 raw-count units. The physical resonance model is therefore strongly disfavored by the data.

Decision

No pODMR resonance is present in this scan. The pulse should have produced a large near-pi-pulse contrast feature if the transition were within the scanned band, but the measured post-pulse readout remains close to the m_S = 0 reference across the scan.
