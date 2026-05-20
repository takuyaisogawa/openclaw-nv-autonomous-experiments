Case podmr_007_2026-05-11-064944.

Sequence interpretation from inputs/sequence.xml and the exported variable values:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Active detections:
  - readout 1 is the true m_S = 0 reference after optical polarization and before the microwave test pulse.
  - readout 2 is the signal readout after the modulated Rabi pulse.
- The active microwave operation before readout 2 is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns. At 250 MS/s it remains 13 samples = 52 ns after rounding.
- mod_depth = 1 in inputs/sequence.xml and in the exported Variable_values.

Expected physical signal:

The setup contrast between m_S = 0 and m_S = +1 is about 22 percent. The Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the transfer probability is

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * t),

using cyclic frequencies in Hz. On resonance, with Omega = 10 MHz and t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Thus a true resonance should make readout 2 lower than the m_S = 0 reference by about

0.22 * 0.996 = 0.219, or 21.9 percent.

The measured readout 1 mean is 31.722, so the expected on-resonance drop is about 6.95 raw-readout units, giving an expected resonant readout 2 level near 24.77. Even if the resonance were offset by one 5 MHz scan step, the model still gives P = 0.749 and an expected drop of about 16.5 percent, or 5.23 raw-readout units. If centered halfway between two scan points, the nearest sampled point would be only 2.5 MHz detuned and the expected drop would still be about 20.4 percent.

Observed data:

- Mean readout 1 = 31.722.
- Mean readout 2 = 31.546.
- Mean fractional suppression, 1 - readout2/readout1, is about 0.45 percent.
- The strongest single-point suppression is at 3.855 GHz: readout 1 = 33.769, readout 2 = 29.962, fractional suppression = 11.3 percent.
- Several points have readout 2 above readout 1, and no scan point approaches the modeled 20-22 percent resonant suppression expected for the active 52 ns, mod_depth 1 pulse.
- Stored averages are only two and may reflect tracking cadence, so I do not treat them as a strong repeatability test; however, the combined data still lacks the expected large resonance-scale dip.

Decision:

The relevant model predicts an almost full pi-pulse transition and therefore a large pODMR contrast dip. The observed readout-2 suppression is small, irregular, and at most about half of the expected resonance contrast. I therefore decide that a pODMR resonance is absent.
