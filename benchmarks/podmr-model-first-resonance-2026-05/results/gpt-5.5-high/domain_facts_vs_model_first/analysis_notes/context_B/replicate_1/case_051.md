Case: podmr_037_2026-05-16-213011

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR frequency sweep.
- Swept parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- Readout 1 role: bright m_S = 0 reference after optical polarization and before the microwave pulse.
- Readout 2 role: signal readout after a modulated microwave Rabi pulse.
- mod_depth = 1.
- Rabi pulse duration = 52 ns, rounded at 250 MHz sample rate and unchanged.

Explicit quantitative model:
- Given Rabi frequency f_R ~= 10 MHz at mod_depth = 1, a resonant square pulse has transition probability
  P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale about 22%, the expected resonant fractional fluorescence drop in the signal readout relative to the bright reference is 0.22 * 0.996 = 0.219.
- At a raw level near 48 counts, that corresponds to an expected drop of about 10.5 counts at resonance.

Data comparison:
- Combined readout 1 mean = 47.63 counts, sd across scan = 1.03.
- Combined readout 2 mean = 47.93 counts, sd across scan = 0.79.
- The signal/reference ratio readout2/readout1 has mean 1.0068, sd 0.0280, minimum 0.9563, and maximum 1.0619.
- The largest observed positive contrast 1 - readout2/readout1 is only 0.0437, far below the expected 0.219 resonant contrast, and it occurs at the scan edge rather than as a convincing Rabi/ODMR line.

Rectangular-pulse frequency-response check:
- I used P(detuning) = (Omega^2/(Omega^2+Delta^2)) * sin^2(0.5 * sqrt(Omega^2+Delta^2) * t), with Omega/2pi = 10 MHz and t = 52 ns.
- Fitting readout2/readout1 to baseline - A * P(detuning) over possible resonance centers gave best A = -0.047 at 3.90025 GHz, i.e. the best fit is an upward feature, not a dip.
- A constant-ratio model had SSE = 0.0157.
- Forcing the physically expected A = 0.22 dip gave best SSE = 0.0552, about 3.5 times worse than the constant model.

Decision:
No pODMR resonance is present. The physical model predicts a large near-pi-pulse contrast if the swept microwave frequency crosses the transition, but the observed signal readout stays close to the bright reference and is better described by no resonance than by the expected dip.
