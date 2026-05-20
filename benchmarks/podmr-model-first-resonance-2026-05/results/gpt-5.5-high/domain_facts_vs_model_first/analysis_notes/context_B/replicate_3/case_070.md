Case: podmr_056_2026-05-17-050447

Inputs used: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles:
- The active pulse sequence is Rabimodulated.xml.
- The XML sets full_expt = 0, so the optional m_S = +1 reference block is not active.
- The first active detection occurs immediately after adj_polarize and is therefore the pumped m_S = 0 reference readout.
- The second active detection occurs after rabi_pulse_mod_wait_time and is therefore the post-microwave-pulse pODMR signal readout.
- The microwave scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Pulse parameters from the provided XML:
- sample_rate = 250 MHz.
- length_rabi_pulse = 52 ns; rounding to the sample clock gives 52 ns exactly because 52 ns is 13 samples at 250 MHz.
- mod_depth = 1.
- Current setup Rabi frequency at mod_depth = 1 is about 10 MHz.

Explicit physical model:
I modeled the driven two-level population transfer from m_S = 0 to m_S = +1 for a square pulse as

P1(delta) = Omega^2 / (Omega^2 + delta^2) * sin^2(pi * sqrt(Omega^2 + delta^2) * tau)

using cycle-frequency units, Omega = 10 MHz and tau = 52 ns. The fluorescence model is

readout2/readout1 = 1 - C * P1(delta)

with contrast C = 0.22 for m_S = 0 versus m_S = +1.

Model expectation:
- On resonance, P1 = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- Expected on-resonance readout2/readout1 = 1 - 0.22 * 0.996 = 0.781.
- At a typical reference level of about 44 counts, the expected resonant drop is about 9.6 counts.
- Even 2.5 MHz off resonance, the model predicts readout2/readout1 about 0.796.
- At 5 MHz off resonance, the model predicts readout2/readout1 about 0.835.

Observed quantitative checks:
- Mean readout1 = 43.77 counts; mean readout2 = 43.93 counts.
- Mean readout2 - readout1 = +0.16 counts.
- The normalized readout2/readout1 values range from 0.943 to 1.068, with mean 1.004.
- The deepest normalized dip, 0.943 at 3.900 GHz, is only a 5.7% drop, far smaller than the expected near-22% resonant drop.
- Several points have readout2 above readout1, and the apparent dips are not a single broad resonance-shaped feature.

Simple model comparison:
- A linear drift-only baseline for readout2/readout1 has SSE 0.0191.
- A resonance model with fixed physical contrast C = 0.22 plus a linear baseline has best SSE 0.0532, worse than drift-only.
- Allowing the resonance amplitude to float gives a best amplitude of only 0.056, about one quarter of the expected 0.22 contrast, so it is not consistent with the supplied physical contrast and pulse model.

Decision:
Given the active readout roles, mod_depth = 1, and 52 ns near-pi pulse, a true pODMR resonance in this scan should produce a much deeper normalized signal drop than observed. The data are better explained by drift/noise between the reference and post-pulse readouts than by the expected pODMR resonance response.

Prediction: resonance_absent.
