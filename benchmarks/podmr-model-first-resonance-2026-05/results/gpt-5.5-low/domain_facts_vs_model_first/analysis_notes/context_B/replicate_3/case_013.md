Case: podmr_032_2026-05-14-161051

Input basis used
- Used only inputs/sequence.xml and inputs/raw_export.json.
- Active sequence name in export: Rabimodulated.xml.
- Scan variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Averages: 2; repetitions: 50000.

Active pulse sequence and readout roles
- The instructions first run adj_polarize, then detection. This is the true m_S = 0 reference readout.
- The separate m_S = +1 reference block is gated by if abs(full_expt)>1e-12. full_expt is 0, so this block is inactive.
- The active experimental pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second readout is the post-microwave signal readout.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the pODMR signal after the resonant microwave pulse.

Relevant active parameters
- sample_rate = 250 MHz.
- length_rabi_pulse = 52 ns. Rounding to the 250 MHz sample clock gives 13 samples, still 52 ns.
- mod_depth = 1.
- mw_freq is swept; detuning = 0.
- full_expt = 0, so no independent +1 reference is acquired.

Quantitative expected signal model
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Active mod_depth = 1, so f_Rabi ~= 10 MHz.
- For a square resonant Rabi pulse, population transferred from m_S = 0 to m_S = +1 is:
  P_+1 = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns:
  pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 0.52*pi.
  P_+1 = sin^2(0.52*pi) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%.
- The mean readout-1 reference level is 34.055 raw-count units.
- Expected resonant signal drop ~= 34.055 * 0.22 * 0.996 = 7.46 raw-count units.
- So a real resonance should appear as a pronounced local reduction in readout 2 relative to readout 1, potentially up to roughly 20-22% of the reference level for this near-pi pulse.

Observed data check
- The largest localized readout-2 deficit occurs at 3.880 GHz:
  readout 1 = 35.654, readout 2 = 29.308, difference = 6.346 counts, ratio = 0.822.
- That ratio corresponds to a 17.8% reduction relative to the same-point reference, close to the 22% maximum expected from the model after allowing for detuning, linewidth, finite contrast calibration error, and measurement noise.
- Neighboring frequencies also show weaker deficits around the same region: 3.870 GHz difference 2.346 counts and 3.875 GHz difference 2.500 counts.
- Away from the central dip, differences are generally much smaller and often change sign. For example, the first eight points have mean readout1-readout2 difference -0.543 counts with standard deviation 1.664 counts.
- The 3.880 GHz deficit is therefore about 4.1 standard deviations below that off-resonant baseline estimate and has the correct sign and magnitude for the active readout roles.

Per-average caution
- The stored averages show large opposing slow trends between averages, so they are not a strong independent repeatability test; this is consistent with the supplied note that stored averages often reflect tracking cadence.
- However, the combined readout comparison uses the active physical readout roles and shows a localized signal of the expected magnitude.

Decision
- A pODMR resonance is present.
