Case: podmr_005_2026-05-10-173726

Sequence identification:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the optional m_S = +1 reference block is skipped. The two acquired readouts are therefore:

1. readout 1: optical polarization followed immediately by detection, a bright m_S = 0 reference.
2. readout 2: optical polarization, a Rabi-modulated microwave pulse, then detection, the resonance-sensitive readout.

The microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. The provided sequence XML has mod_depth = 1, and the exported variable values also report mod_depth = 1. The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1.

Quantitative model:

I modeled the addressed NV transition as a driven two-level system initially in m_S = 0. For a square microwave pulse with Rabi frequency Omega/2pi = 10 MHz and duration tau = 52 ns, the transition probability versus detuning Delta/2pi is:

P(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(pi * tau * sqrt(Omega^2 + Delta^2))

where Omega and Delta are in cycles/s. On resonance, Omega * tau = 0.52 cycles, so P(0) = sin^2(pi * 0.52) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected fluorescence ratio on resonance is approximately 1 - 0.22 * 0.996 = 0.781. For a reference readout near 42 counts, this predicts a resonance-center drop of about 42 * 0.22 * 0.996 = 9.2 counts.

Data comparison:

The resonance-sensitive readout 2 drops from the surrounding baseline near 42 counts to 35.65 at 3.875 GHz and 34.73 at 3.880 GHz, while readout 1 remains near 42 counts there. The normalized ratios readout2/readout1 at these two points are 0.837 and 0.833. The mean normalized ratio within 10 MHz of the fitted center is 0.855, while side points more than 30 MHz away average 0.984, a 13.1% normalized dip. Fitting the same two-level probability model to the ratio data gives a best center of about 3.878 GHz and an effective contrast coefficient of about 18.2% relative to baseline, close to the expected 22% scale given finite noise, tracking drift, and only two stored averages.

Decision:

The observed dip is centered where the two-level pulse model predicts a near-pi-pulse depletion, has the expected sign in the second readout only, and has a magnitude consistent with the known contrast scale. I therefore classify this as resonance_present.
