<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_002

Sequence interpretation:
- Active sequence: Rabimodulated.xml / Rabimodulated pulse ODMR.
- The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active sequence has full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout 1 is the detection immediately after optical polarization, i.e. the bright m_S = 0 reference.
- Readout 2 is the detection after a microwave rabi_pulse_mod_wait_time pulse, i.e. the pODMR signal channel.
- The relevant microwave pulse is length_rabi_pulse = 52 ns.
- mod_depth = 1 from the provided sequence variable values, giving an estimated Rabi frequency of about 10 MHz.

Quantitative model:
Use the finite square-pulse transition probability

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau)

with Omega = 10 MHz, tau = 52 ns, and Delta = f - f0, all in cycles/s. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the setup contrast scale of 22%, the expected normalized fluorescence drop at resonance is

0.22 * 0.996 = 0.219

or about 9.2 counts for a 42 count bright reference.

Observed normalized signal:
I normalized the pulsed signal by the bright reference, readout2/readout1. Around the central feature:

- 3.870 GHz: 38.038 / 43.115 = 0.882, contrast 0.118
- 3.875 GHz: 35.654 / 42.615 = 0.837, contrast 0.163
- 3.880 GHz: 34.731 / 41.692 = 0.833, contrast 0.167
- 3.885 GHz: 36.808 / 42.423 = 0.868, contrast 0.132

The minimum near 3.880 GHz is a drop of about 16.7%, or 7.0 counts relative to the simultaneous bright reference. This is smaller than the ideal 21.9% expected for a perfect pi pulse but is close enough for a real single-NV pODMR measurement with drift, imperfect contrast, and finite sampling.

I also fit the normalized data to a linear baseline plus the finite-pulse model above. A free-amplitude fit gives a center near 3.87725 GHz and a fitted contrast amplitude of 0.176. A fixed-contrast model using the expected 0.22 contrast gives the best center near 3.8775 GHz. Both improve substantially over a linear baseline-only model.

There is another low point at the high-frequency endpoint, but the stored averages differ there and stored averages can reflect tracking cadence. The central dip has the correct width, location coherence across adjacent frequency points, and amplitude scale for the 52 ns, mod_depth = 1 pulse model.

Decision: resonance_present.
