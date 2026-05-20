Case: podmr_060_2026-05-17-060259

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, sibling cases, or any prior outputs.

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence.
- The instruction flow has an initial polarization pulse followed by detection, then the "Acquire 1 level reference" block is skipped because full_expt = 0, then a single modulated Rabi pulse is applied and followed by detection.
- Readout 1 role: polarized m_S = 0 optical reference / tracking reference.
- Readout 2 role: signal readout after the modulated Rabi pulse.
- Active pulse parameters from the provided sequence XML: mod_depth = 1, length_rabi_pulse = 5.2e-08 s = 52 ns, sample_rate = 250 MHz, so the pulse length is already on the 4 ns sample grid.

Physical signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling, f_R = 10 MHz.
- For a resonant square pulse, the m_S = +1 population transfer is P = sin^2(pi * f_R * tau).
- With tau = 52 ns, f_R * tau = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22 percent. Therefore a resonant pulse should reduce the signal readout by approximately 0.22 * P = 0.219 of the local m_S = 0 fluorescence.
- The median signal readout is 50.0769 raw-count units, so the expected resonant dip is 50.0769 * 0.219 = 10.97 raw-count units. A resonant point should be near 39.10 raw-count units, apart from tracking and noise.

Observed quantitative comparison:
- Scan range: 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Combined readout 2 statistics: mean 50.1969, median 50.0769, min 48.6731, max 52.75, standard deviation 1.0788.
- The deepest raw readout 2 dip is only 1.4038 counts below the median, about 13 percent of the expected 10.97-count resonant dip.
- The pointwise readout2/readout1 ratio has median 0.9832 and minimum 0.9308, a 0.0525 ratio drop. The expected resonant ratio drop is about 0.219, so the observed normalized dip is only about 24 percent of the expected resonant contrast.
- The largest structures are comparable to the stored-average/tracking scatter rather than a near-pi-pulse ODMR response. Since stored averages mainly reflect tracking cadence, their partial repeatability is not treated as an independent resonance confirmation.

Decision:
The active sequence should produce an almost full Rabi inversion on resonance, giving a roughly 22 percent optical dip. No such dip is present in the MW-dependent readout, either in raw counts or normalized to the m_S = 0 reference. I therefore classify this case as resonance_absent.
