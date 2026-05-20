Case: podmr_006_2026-05-11-020739

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first performs adj_polarize, detection, and wait_for_awg. This is the true m_S = 0 optical reference, so readout 1 is the pre-microwave reference.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. The data do not contain a separate m_S = +1 reference.
- The active pODMR measurement is then one rabi_pulse_mod_wait_time followed by detection, so readout 2 is the post-microwave signal.
- The provided sequence XML sets length_rabi_pulse = 5.2e-08 s and mod_depth = 1. The pulse duration is rounded to the 250 MHz sample clock; 52 ns is already 13 samples.

Expected signal calculation:

- Given the setup facts, the cyclic Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square pulse, the excited-state transfer probability versus detuning is
  P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau),
  using cyclic frequencies in Hz.
- With Omega = 10 MHz and tau = 52 ns, the on-resonance probability is
  sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected maximum fluorescence depression in readout 2 relative to the m_S = 0 reference is about
  0.22 * 0.996 = 0.219, or 21.9%.
- The expected square-pulse spectral shape is broad on the scale of the 5 MHz scan step: if centered at 3.880 GHz, the modeled fractional drops at 3.875, 3.880, and 3.885 GHz are about 16.5%, 21.9%, and 16.5%, with much smaller off-resonant sidelobes elsewhere.

Observed quantitative comparison:

- The combined readout ratio readout2/readout1 has its minimum at 3.880 GHz: 40.5385 / 47.9231 = 0.8459.
- Using the median off-line ratio outside indices 9-12 as a baseline gives 0.9610. The observed ratio depressions are therefore about 5.0% at 3.875 GHz, 11.5% at 3.880 GHz, and 9.1% at 3.885 GHz.
- The raw readout1-readout2 difference is also largest at 3.880 GHz: 7.3846 counts. The neighboring 3.885 GHz point is 6.2692 counts.
- The stored averages are not a strong independent repeatability test because they often reflect tracking cadence, but both averages have their minimum readout2/readout1 ratio at 3.880 GHz.

Decision:

The observed amplitude is below the ideal 21.9% contrast-scale prediction, but the pulse should produce a large post-microwave fluorescence depression if resonant, and the data show a localized readout-2 dip centered at 3.880-3.885 GHz with the correct readout role and frequency-local structure. I classify this case as resonance_present.
