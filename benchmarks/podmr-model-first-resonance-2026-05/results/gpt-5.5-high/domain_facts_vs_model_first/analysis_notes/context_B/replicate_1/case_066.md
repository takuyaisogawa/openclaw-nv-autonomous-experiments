Case: podmr_052_2026-05-17-015447

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence identification:

- SequenceName in the export is Rabimodulated.xml.
- The provided sequence XML sets up a microwave-frequency scan and executes:
  1. adj_polarize
  2. detection
  3. wait
  4. optional +1 reference block only if full_expt is nonzero
  5. rabi_pulse_mod_wait_time
  6. detection
  7. wait
- full_expt = 0, so the +1 reference block is disabled.
- Therefore the two raw readouts have these roles:
  - readout 1: bright m_S = 0 reference after optical polarization, before the test microwave pulse.
  - readout 2: signal readout after the Rabi-modulated microwave pulse.
- Active pulse duration: length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this remains exactly 13 samples = 52 ns.
- Active mod_depth: mod_depth = 1 in the provided sequence XML and in Variable_values.

Physical model calculation:

Use the stated setup facts:

- m_S = 0 to m_S = +1 fluorescence contrast scale: about 22%.
- Rabi frequency at mod_depth = 1: about 10 MHz.
- Rabi frequency scales linearly with mod_depth, so f_R = 10 MHz here.
- Pulse duration tau = 52 ns.

For a square microwave pulse on a two-level transition, the transferred population versus detuning is

P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

where f_R and delta are in cycles/s. The expected normalized optical contrast is then

C(delta) = 0.22 * P_1(delta)

At resonance:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = about 0.996
C(0) = about 0.219, or a 21.9% drop of readout 2 relative to readout 1.

On the 5 MHz scan grid, if the resonance were centered on a sampled frequency, the expected contrasts near the line are approximately:

- delta = 0 MHz: 21.9%
- delta = +/-5 MHz: 16.5%
- delta = +/-10 MHz: 6.0%
- delta = +/-15 MHz: 0.3%

If the resonance fell halfway between two sampled points, the two nearest points would still be close to the resonant response, so this sequence should produce a large local feature, not only a weak one-point excursion.

Observed normalized contrast:

I computed C_obs = 1 - readout2/readout1 from the combined raw readouts. Across the scan the values are:

-1.9%, +1.4%, +3.1%, -10.1%, +4.0%, -0.5%, +1.1%, +4.2%, +2.7%, -1.0%, +2.5%, +1.4%, +5.3%, +0.1%, -0.9%, +6.0%, +0.8%, +0.9%, +4.6%, -2.0%, +10.0%.

The maximum combined contrast is only about 10.0% at the final scan point, 3.925 GHz. A physical 22% endpoint-centered resonance would also require the preceding point at 3.920 GHz to show roughly 16.5% contrast, but it is -2.0%, opposite in sign. Likewise, possible interior bumps near 3.885 or 3.900 GHz are only about 5-6% and do not have the adjacent-point structure expected from the 52 ns, 10 MHz pulse.

Fit/check against the explicit model:

- A nonnegative-amplitude fit of the expected Rabi-pulse lineshape to C_obs chooses an endpoint center near 3.925 GHz, but with only about 5.1% fitted amplitude, far below the approximately 22% expected physical amplitude.
- For the physically expected 22% amplitude, the best center is also at the endpoint, but the model mismatches the adjacent points strongly because the neighboring scan point should already be a large dip.
- The two stored averages do not provide strong repeatability evidence: their normalized-contrast maxima occur at different frequencies and their contrast correlation is about -0.06. This is consistent with the warning that stored averages often reflect tracking cadence rather than an independent repeatability test.

Decision:

The active sequence should have produced an easily visible pODMR dip if the scanned range contained the transition. The observed signal is too small, lacks the required Rabi-pulse lineshape, and is not repeatable across stored averages. I therefore classify this case as resonance_absent.
