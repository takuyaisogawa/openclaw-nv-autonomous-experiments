Case podmr_079_2026-05-17-103702

Sequence interpretation:
- Sequence name: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Active readout 1 role: true m_S = 0 optical reference after adj_polarize and detection.
- Active readout 2 role: signal readout after the microwave rabi_pulse_mod_wait_time block and detection.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s still 52 ns.
- mod_depth: active value is 1 in the provided sequence XML/exported variable values.

Physics expectation:
- The stated setup has about 10 MHz Rabi frequency at mod_depth = 1, scaling linearly with mod_depth.
- A 52 ns pulse at mod_depth = 1 is essentially a pi pulse, so on resonance the post-pulse readout should be strongly reduced relative to the m_S = 0 reference, approaching the 22% contrast scale.

Data check:
- Combined readout2/readout1 ratios range from about 0.9607 to 1.0476.
- The deepest apparent post-pulse deficits are only about 3.9% contrast, far smaller than the expected near-pi-pulse contrast.
- The low-ratio points are not a clean resonance feature and are comparable to point-to-point/reference fluctuations; stored averages are only two and can reflect tracking cadence rather than a strong repeatability test.

Decision:
- No convincing pODMR resonance is present in this scan.
