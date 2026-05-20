Case podmr_023_2026-05-16-174219

I used only the provided XML/exported raw data for this case.

Active sequence and readout roles:
- SequenceName: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The first active block polarizes the NV and immediately performs detection. This is the bright m_S = 0 reference, corresponding to readout 1.
- full_expt is 0, so the optional "Acquire 1 level reference" block is inactive. There is no independent dark-state reference in the acquired data.
- The active microwave operation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. Thus readout 2 is the signal after the microwave pulse.

Physical model calculation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the relevant Rabi frequency here is 10 MHz.
- For a square pulse with detuning Delta, the transition probability is modeled as:
  P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * t)
  with Omega = 10 MHz and t = 52 ns.
- On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fluorescence reduction is 0.22 * 0.996 = 0.219 of the bright reference.
- The mean readout 1 level is 47.55 counts, so a real on-resonance pi-like response should produce an approximately 10.4 count drop in readout 2 relative to readout 1 at the resonance point.

Observed quantitative comparison:
- Mean readout 1: 47.55 counts.
- Mean readout 2: 47.69 counts.
- Mean readout2 - readout1: +0.14 counts.
- Standard deviation of readout2 - readout1 across scan points: 1.46 counts.
- Most negative observed readout2 - readout1 point: -2.48 counts.
- The smallest observed ratio readout2/readout1 is about 0.949, a 5.1% drop, while the expected resonant contrast is about 21.9%.
- A least-squares fit allowing a resonance-shaped dip anywhere in the scanned points prefers an amplitude of only about 2.5 counts, much smaller than the physically expected 10.4 counts. Forcing the expected 22% contrast dip gives a substantially poor mismatch to the data.

Decision:
The active sequence should show a large, localized reduction in readout 2 if a pODMR resonance is present, because the 52 ns pulse at mod_depth = 1 is essentially a pi pulse on resonance. The measured readout 2 is not suppressed relative to the bright reference at the expected scale; fluctuations are small and inconsistent with the calculated resonance signal. I therefore decide that a pODMR resonance is absent.
