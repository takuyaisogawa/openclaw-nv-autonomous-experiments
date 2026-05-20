Case podmr_070_2026-05-17-082720

Sequence and readout roles:
- The provided sequence is Rabimodulated.xml / Rabimodulated.
- Active variables from the provided XML/raw export values: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- With full_expt = 0, the conditional "Acquire 1 level reference" block is inactive.
- The active detections are therefore:
  1. readout 1: after optical polarization, before the microwave pulse; this is the m_S = 0 reference / tracking-normalization channel.
  2. readout 2: after the 52 ns modulated microwave pulse; this is the pODMR signal channel.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, use f_R = 10 MHz.
- For a resonant square Rabi pulse, transition probability P = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- With the setup contrast scale of 22%, the expected fractional fluorescence drop at resonance is 0.22 * 0.996 = 0.219, i.e. about 21.9%.
- The measured m_S = 0 readout scale is about 51 counts, so an on-resonance pODMR dip should lower the post-pulse readout by about 51 * 0.219 = 11.2 counts, to roughly 40 counts.
- Detuned Rabi model used for the line shape:
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
  This predicts a deep, localized dip near any resonance inside the swept range, with the on-resonance fractional signal near 0.781 of the m_S = 0 reference.

Observed data check:
- readout 1 mean = 50.71 counts, standard deviation = 1.35, range = 48.35 to 52.46.
- readout 2 mean = 50.23 counts, standard deviation = 1.69, range = 47.33 to 53.27.
- readout2/readout1 mean = 0.9906, standard deviation = 0.0233, minimum = 0.9613.
- The largest observed relative reduction is only about 3.9%, not the expected about 21.9%.
- The minimum readout 2 value is 47.33 counts at 3.915 GHz; its ratio to readout 1 is 0.975, also far above the expected resonant ratio near 0.781.
- A no-resonance scaled-baseline model gives SSE about 28.0.
- A fixed 22% contrast resonance model, allowing the resonance center to scan across the measured range, gives best SSE about 179.1 and predicts a minimum signal near 38.3 counts where the observed signal remains about 47.9 counts.
- If the contrast amplitude is allowed to fit freely but capped at 22%, the best fitted amplitude is only about 3.9%, consistent with small drift/noise rather than the expected pODMR response.

Decision:
The active sequence should produce a large, near-pi-pulse ODMR dip if a resonance is present in the scan. The measured post-pulse readout does not show a quantitatively compatible dip or line shape, and the apparent variations are much smaller than the physical expectation. Therefore I decide resonance_absent.
