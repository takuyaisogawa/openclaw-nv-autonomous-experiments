Case: podmr_047_2026-05-17-001223

Sequence interpretation
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the conditional m_S=+1 reference block is not executed.
- Readout 1 is the first detection immediately after optical polarization, i.e. the true m_S=0 bright reference.
- Readout 2 is the detection after the active microwave pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this rounds to 13 samples, still 52 ns.
- mod_depth = 1 in the provided sequence XML and in the exported Variable_values.

Physical model calculation

For a rectangular resonant Rabi pulse, using the setup fact f_Rabi ~= 10 MHz at mod_depth = 1, the transition probability versus detuning is modeled as

P(+1 | Delta) = f_Rabi^2 / (f_Rabi^2 + Delta^2) * sin^2(pi * tau * sqrt(f_Rabi^2 + Delta^2)).

With tau = 52 ns and f_Rabi = 10 MHz:
- On resonance: P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected optical drop relative to the m_S=0 reference is 0.22 * P = 0.219, about 11 raw-readout counts for a 50-count reference.
- If a resonance lies halfway between two 5 MHz scan points, the nearest sampled detuning is 2.5 MHz, giving P = 0.929 and an expected drop of 0.204, about 10 counts.
- Therefore any in-scan resonance should create a large, broad dip in readout2/readout1 near 0.78 to 0.80 at at least one sampled point.

Observed quantitative check

Using the combined readouts:
- readout1 mean = 50.383 counts; readout2 mean = 50.062 counts.
- The normalized ratio readout2/readout1 has mean 0.994, standard deviation 0.027, minimum 0.947, and maximum 1.051.
- The largest observed normalized drop, 1 - readout2/readout1, is 0.0529 at 3.905 GHz.
- A linear-baseline residual check gives a largest positive drop residual of about 0.044, still far below the >=0.204 drop expected from the pulse model for an in-scan resonance.
- A least-squares resonance template with free amplitude prefers an amplitude of about 0.065, not the expected 0.22, and this is not stable enough to override the physical expectation. Stored averages are not treated as independent confirmation because they often reflect tracking cadence.

Decision

The active pulse is essentially a pi pulse at the stated contrast scale, so a real pODMR resonance in this scan should be obvious as a roughly 20% normalized PL dip. The data show only small fluctuations and no dip with the expected magnitude or shape. I decide that the pODMR resonance is absent.
