Case podmr_022_2026-05-16-172725

Sequence and roles

The active saved sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction path is:

1. adj_polarize for 1 us.
2. detection: this is the true m_S = 0 reference readout.
3. wait_for_awg for 2 us.
4. The "Acquire 1 level reference" block is skipped because full_expt = 0.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
6. detection: this is the post-microwave signal readout.
7. wait_for_awg for 1 us.

The saved export contains an older embedded sequence text showing mod_depth = 0.3, but the exported Variable_values for this scan give mod_depth = 1, and inputs/sequence.xml also has mod_depth = 1. I therefore use mod_depth = 1 for the physical calculation.

Quantitative expected signal model

Given setup facts:

- Contrast between m_S = 0 and m_S = +1 is about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Pulse duration is 52 ns.

For a resonant square Rabi pulse, the transferred population is modeled as:

P_1 = sin^2(pi * f_Rabi * tau)

With f_Rabi = 10 MHz * 1 = 10 MHz and tau = 52 ns:

pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 0.52*pi
P_1 = sin^2(0.52*pi) = 0.996

Thus the expected on-resonance fluorescence change is approximately:

0.22 * 0.996 = 0.219, or 21.9% of the baseline.

The mean combined raw readout level is 46.80 counts, so the expected resonant contrast for a full pi-like pulse is:

46.80 * 0.219 = 10.25 raw-count units.

Observed data check

The combined readout mean over both readouts is 46.80 counts. The full observed combined range across the scan is only 2.66 counts, from 45.64 to 48.31 counts. A linear-baseline residual analysis gives residual sigma about 0.85 counts, with the largest negative residual about -1.30 sigma. There is no localized dip or feature approaching the expected approximately 10 count resonant signal.

The two readouts have nearly identical means: readout 1 mean = 46.76, readout 2 mean = 46.83, with mean readout2-readout1 = 0.07 counts. This is also inconsistent with the expected strong post-pulse resonance response.

Decision

Because the active pulse is essentially a resonant pi pulse at mod_depth = 1, a real pODMR resonance in this scan should be large, about 22% or 10 counts. The measured frequency dependence is small, irregular, and lacks a localized resonance-scale dip. I therefore decide that a pODMR resonance is absent.
