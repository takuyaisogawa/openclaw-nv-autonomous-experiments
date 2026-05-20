Case: podmr_040_2026-05-16-222642

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence name in the scan export is Rabimodulated.xml.
- The provided XML performs: optical polarization, detection, wait, optional +1 reference block, one rabi_pulse_mod_wait_time pulse, detection, final wait.
- full_expt = 0, so the optional +1 reference block is inactive.
- Readout 1 role: bright m_S = 0 reference immediately after optical polarization.
- Readout 2 role: signal after the microwave-modulated Rabi pulse.
- The pulse used for the pODMR test is length_rabi_pulse = 5.2e-08 s = 52 ns.
- The provided XML gives mod_depth = 1.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Linear scaling gives f_R = 10 MHz for this case.
- For a resonant square pulse, transition probability P = sin^2(pi * f_R * t).
- With t = 52 ns, f_R * t = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- The current setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected fractional drop in readout 2 at resonance is 0.22 * 0.996 = 0.219.
- The observed bright reference level is about 47.19 counts, so a resonant point should be lower by roughly 47.19 * 0.219 = 10.34 counts relative to readout 1.

Data comparison:
- Mean readout 1 = 47.19 counts.
- Mean readout 2 = 46.66 counts.
- Mean readout2 - readout1 = -0.53 counts.
- Standard deviation of readout2 - readout1 across the sweep = 1.34 counts.
- The largest observed deficit is -3.69 counts at 3.885 GHz, with readout2/readout1 = 0.924.
- A resonant pi-pulse response should have readout2/readout1 near 0.781, far below any observed point.
- Stored averages are only 2 and can reflect tracking cadence, so I did not treat the two averages as a strong repeatability test.

Decision:
The relevant physical model predicts an approximately 10-count dip at resonance for this pulse and contrast scale, but the measured differences show only small scatter-level variations and no point close to the expected resonant contrast. I therefore decide that a pODMR resonance is absent.
