<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_084

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabimodulated.xml-style pODMR scan varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize, then acquire a detection immediately after polarization. This is readout 1 and is the true m_S = 0 reference.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The active microwave operation is then rabi_pulse_mod_wait_time followed by the second detection. This is readout 2, the post-pulse signal readout.
- From inputs/sequence.xml, mod_depth = 1 and length_rabi_pulse = 5.2e-08 s = 52 ns. The sample-rate rounding leaves 52 ns unchanged at 250 MS/s.

Physical model:
The stated setup has about 22% readout contrast between m_S = 0 and m_S = +1. The Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For a rectangular pulse with cycle-frequency Rabi rate f_R and detuning Delta, I used

P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

The expected fractional fluorescence drop in readout 2 relative to readout 1 is approximately 0.22 * P_1(Delta), because readout 1 is the m_S = 0 reference and readout 2 follows the microwave pulse.

For f_R = 10 MHz and t = 52 ns, the on-resonance transition probability is sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected on-resonance fractional drop is about 0.219, i.e. roughly an 11-count drop on a 51-count baseline. Even at 5 MHz detuning the expected drop is about 0.165, and at 10 MHz detuning it is about 0.060.

Observed data:
- Mean readout 1 = 50.7097.
- Mean readout 2 = 50.2289.
- Mean fractional contrast (readout1 - readout2) / readout1 = 0.00942.
- Largest observed fractional drop = 0.03872 at 3.885 GHz.
- Several frequencies show the opposite sign, with readout 2 larger than readout 1.

Model comparison:
I fitted the measured fractional contrast to an offset plus the rectangular-pulse response while scanning the resonance center. The null model with only a constant offset had RSS = 0.010818 and residual sigma = 0.02326. For the 10 MHz Rabi model, the best free-amplitude fit put the center near 3.84875 GHz but required a negative response amplitude, beta = -0.04186, meaning the data prefer an increase rather than the expected pODMR decrease there. Enforcing the physically expected positive 22% response gave RSS = 0.123679, 11.4 times worse than the null model. At the nearest measured point to that fitted center, 3.850 GHz, the observed contrast was -0.0174 while the expected drop for the provided-sequence model was 0.215.

Decision:
The provided sequence should produce a large, easily visible readout-2 suppression on resonance. The measured readout differences are small, inconsistent in sign, and not compatible with the expected positive 22%-scale Rabi response. I therefore decide that a pODMR resonance is absent.
