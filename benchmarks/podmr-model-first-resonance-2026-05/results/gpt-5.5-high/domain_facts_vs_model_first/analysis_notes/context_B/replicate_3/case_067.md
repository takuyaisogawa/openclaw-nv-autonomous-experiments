Case: podmr_053_2026-05-17-042031

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual check of the exported values

Sequence identification:
- Active sequence: Rabimodulated.xml.
- The first detection is after adj_polarize and is the polarized m_S = 0 reference readout.
- full_expt = 0, so the explicit m_S = 1 reference block is skipped.
- The second detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so it is the pODMR signal readout after the microwave pulse.
- Active mod_depth = 1 from the provided sequence XML and exported Variable_values.
- Active pulse duration: length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) / 250 MHz = 52 ns, so the pulse duration is unchanged.

Quantitative physical model:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: t = 52 ns.
- For a square pulse at detuning delta, the transition probability is
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- On resonance:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected normalized fluorescence loss at resonance is
  0.22 * P(0) = 0.219, i.e. about 21.9%.
- The mean m_S = 0 reference readout is 45.20 counts, so the expected resonant count drop is about
  45.20 * 0.219 = 9.90 counts.

Observed readout comparison:
- Mean readout 1: 45.20 counts.
- Mean readout 2: 45.02 counts.
- Mean readout-2/readout-1 ratio: 0.9965.
- The strongest observed normalized loss is at 3.880 GHz:
  readout 1 = 45.885, readout 2 = 42.596, ratio = 0.9283, loss = 7.17%, count drop = 3.29 counts.
- This is only about one third of the expected pi-pulse contrast and is not accompanied by the neighboring multi-point dip expected from the Rabi response.

Explicit model comparison:
- I fit the normalized signal ratio readout2/readout1.
- A no-resonance linear baseline in frequency gives SSE = 0.0211 and residual sigma = 0.0333 in ratio units.
- A fixed-contrast resonance model with the above Rabi response and an unknown linear multiplicative baseline, constrained to have the resonance center inside the scanned frequency range, gives best SSE = 0.0720 at 3.88745 GHz. This is worse than the no-resonance baseline because a real mod_depth 1, 52 ns resonance would force an approximately 22% dip that is not present.
- If the resonance amplitude is allowed to float freely inside the scan, the best fitted dip amplitude is only -0.0436 in ratio units, far below the physically expected -0.22 for this pulse.

Decision:
The active pulse should be nearly a pi pulse on resonance and should produce a large pODMR dip. The measured second readout remains close to the m_S = 0 reference, with only small noisy point-to-point excursions and no physically sized Rabi-line-shaped dip. I therefore decide that a pODMR resonance is absent in this scan.
