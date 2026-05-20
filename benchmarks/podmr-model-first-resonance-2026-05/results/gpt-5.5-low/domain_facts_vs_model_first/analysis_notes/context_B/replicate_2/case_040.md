case_id: podmr_026_2026-05-16-182622

Sequence/readout identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect, then wait, then apply a Rabi-modulated microwave pulse and detect again.
- full_expt = 0, so the optional "1 level reference" branch is inactive.
- Readout 1 is therefore the polarized m_S = 0 reference. Readout 2 is the signal after the Rabi pulse.
- Provided sequence values give mod_depth = 1 and length_rabi_pulse = 52 ns. The pulse duration is already on the 250 MHz sample grid: round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, use Omega_R = 10 MHz.
- For a square pulse with detuning Delta, the driven transition probability is
  P(Delta) = (Omega_R^2 / (Omega_R^2 + Delta^2)) * sin^2(pi * sqrt(Omega_R^2 + Delta^2) * tau),
  with tau = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale of 22%, an on-resonance pi-like transfer should reduce the post-pulse readout by 0.22 * 0.996 = 21.9% relative to the m_S = 0 reference.
- Around 50 raw counts, this corresponds to an expected drop of about 10.96 counts, so readout2/readout1 should be about 0.781 at resonance.
- For comparison, the model still predicts readout2/readout1 about 0.835 at 5 MHz detuning and about 0.940 at 10 MHz detuning; a sampled resonance or near-resonance point should be visible as a substantial localized readout-2 depression.

Observed data comparison:
- Combined readout 1 mean: 49.611.
- Combined readout 2 mean: 49.583.
- Mean readout2 - readout1: -0.027 counts.
- Mean readout2/readout1: 0.9999.
- Minimum combined readout2/readout1 is 0.9406 at 3.835 GHz, a 3.10 count drop. This is far smaller than the 10.96 count on-resonance expectation and is comparable to scattered fluctuations elsewhere, including a maximum ratio of 1.065 at 3.830 GHz.
- The two stored averages do not show a stable common dip pattern; they mainly reflect tracking/cadence variation rather than independent repeatability.

Decision:
The active pulse should produce a large pODMR dip if a resonance is in the scanned range. The measured readout roles show no such contrast-scale feature; readout 2 tracks readout 1 around unity with only noisy excursions. I therefore decide that a pODMR resonance is absent.
