Case podmr_067_2026-05-17-074342

Inputs used
- Used only inputs/sequence.xml and inputs/raw_export.json in this workspace.
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Sequence structure:
  - First detection occurs immediately after adj_polarize, so readout 1 is the polarized m_S = 0 fluorescence reference.
  - full_expt = 0, so the optional m_S = 1 reference branch is inactive.
  - The active MW operation is rabi_pulse_mod_wait_time followed by detection, so readout 2 is the MW-pulsed pODMR signal readout.
- Pulse parameters:
  - sample_rate = 250 MHz.
  - length_rabi_pulse = 52 ns, which is exactly 13 samples after rounding.
  - mod_depth = 1.

Physical model calculation
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore the active pulse has f_Rabi = 10 MHz.
- For a square pulse, the resonant transition probability is modeled as
  P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance, nearly full-transfer pulse should reduce the MW-pulsed readout by about
  0.22 * P = 21.9% relative to the m_S = 0 reference.
- The readout 1 mean is 48.920 counts, so the expected resonant drop is
  48.920 * 0.22 * 0.996 = 10.72 counts.
- Equivalently, on resonance readout2/readout1 should be about 0.781 if the resonance is in the scan and driven by this pulse.

Observed data check
- Combined readout 1 mean/std: 48.920 / 0.804 counts.
- Combined readout 2 mean/std: 48.757 / 1.250 counts.
- Difference readout2 - readout1:
  - mean = -0.163 counts.
  - std = 1.568 counts.
  - minimum = -2.346 counts at 3.885 GHz.
  - maximum = +2.962 counts.
- Observed minimum readout2/readout1 = 0.952 at 3.885 GHz.
- The largest observed suppression is only about 4.8% of readout 1, versus the approximately 21.9% suppression expected for a resonant 52 ns mod_depth 1 pulse. In count units, the largest observed suppression is 2.35 counts, about 22% of the expected 10.72-count resonant drop.
- Stored per-average traces show similar small, noisy fluctuations and only two averages; these averages mainly reflect tracking cadence and are not treated as a strong repeatability test.

Decision
- The expected signal from the relevant model is a large readout 2 dip relative to readout 1.
- The measured trace does not show a resonance-scale dip or a coherent pODMR lineshape across the frequency sweep.
- Prediction: resonance_absent.
