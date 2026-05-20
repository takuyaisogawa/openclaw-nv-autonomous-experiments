Sequence context:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- The executed values in raw_export.json show length_rabi_pulse = 52 ns and mod_depth = 1.
- full_expt = 0, so the optional 1-level reference block is skipped despite do_adiabatic_inversion being true.
- Readout 1 is the initial polarized m_S = 0 reference detection before the microwave pulse.
- Readout 2 is the detection after the modulated Rabi pulse.

Physical expectation:
- With about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is close to a pi pulse.
- If the swept microwave frequency hits a real pODMR resonance, readout 2 should show a clear fluorescence decrease relative to the readout 1 reference, on the order of the setup contrast scale between m_S = 0 and m_S = +1, about 22%.

Data assessment:
- The combined readouts remain near 50-52 counts across the sweep, with mean readout 1 and readout 2 almost equal.
- The largest negative readout2-readout1 excursions are only a few counts, far smaller than the expected near-pi-pulse contrast.
- The apparent dips are not clean or reproducible across the two stored averages; stored averages can reflect tracking cadence and should not be overinterpreted as independent repeatability.
- There is also a large positive excursion in readout 2 near 3.915 GHz, supporting the interpretation that the structure is noise or drift rather than a resonance lineshape.

Decision:
No convincing pODMR resonance is present in this sweep.
