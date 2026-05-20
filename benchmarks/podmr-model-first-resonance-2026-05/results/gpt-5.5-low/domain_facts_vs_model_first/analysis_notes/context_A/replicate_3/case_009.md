Case podmr_016_2026-05-12-120649

Inputs inspected:
- sequence.xml
- raw_export.json
- raw_readouts.png

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional m_S = +1 reference block is not active.
- The first detection after adj_polarize is the true m_S = 0 reference readout.
- The second active detection follows rabi_pulse_mod_wait_time and is the pODMR signal readout after the microwave pulse.

Pulse settings used for the decision:
- mod_depth = 1 from the provided sequence XML / variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s.
- With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi-pulse scale drive on resonance.

Expected resonance signature:
- For a single NV pODMR resonance with this pulse, the driven readout should show a clear fluorescence reduction relative to the m_S = 0 reference, with a scale that can approach the stated 22% contrast between m_S = 0 and m_S = +1.
- Stored per-average traces should not be treated as a strong repeatability test because they can mainly reflect tracking cadence.

Observed data:
- Both raw readouts show a broad downward trend across the frequency scan.
- The driven readout is not consistently depressed relative to the m_S = 0 reference at a localized microwave frequency.
- At many scan points the driven readout is equal to or higher than the reference readout, and the largest local excursions are comparable to drift/tracking structure rather than a clear 22%-scale ODMR contrast.
- The per-average overlay does not provide an independent stable resonance feature; its large separation mainly tracks cadence-like changes.

Decision:
No reliable pODMR resonance is present in this scan. The data show drift and readout-to-readout variation, but not the expected localized driven-readout fluorescence dip relative to the 0 reference for the active Rabimodulated sequence.
