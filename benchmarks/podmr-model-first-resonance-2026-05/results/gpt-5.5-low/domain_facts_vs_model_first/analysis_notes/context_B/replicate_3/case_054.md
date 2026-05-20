Case: podmr_040_2026-05-16-222642

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- SequenceName is Rabimodulated.xml.
- The executed instructions polarize, detect, wait, apply one modulated Rabi pulse, detect, then wait.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. There is no separate m_S = +1 reference acquisition in this run.
- Therefore readout 1 is the polarized m_S = 0 reference readout, and readout 2 is the signal readout after the microwave/Rabi pulse.

Pulse parameters from the XML/export:

- vary_prop: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already on the 4 ns sample grid.

Explicit physical model calculation:

Given the supplied calibration, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Thus this run has f_Rabi ~= 10 MHz. For a square resonant pulse, the transferred population is

P_transfer = sin^2(pi * f_Rabi * t_pulse)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a true on-resonance pi pulse should reduce the signal readout by

expected fractional PL drop = 0.22 * 0.996 = 0.219.

The mean m_S = 0 reference readout is 47.19 raw units, so the expected resonant raw-count drop is

expected drop = 47.19 * 0.219 = 10.34 raw units.

Observed data:

- Mean readout 1: 47.19.
- Mean readout 2: 46.66.
- Readout 2 ranges from 44.67 to 48.42, a total span of 3.75 raw units.
- The minimum readout2/readout1 ratio is 0.924 at 3.885 GHz. This is a 7.6% normalized dip relative to the local readout 1 reference, much smaller than the expected 21.9% dip.
- The largest raw difference readout2 - readout1 is -3.69 raw units, also far smaller than the expected -10.34 raw units.
- The stored two averages have large offset shifts, consistent with tracking cadence. Their per-average traces do not provide a strong independent repeatability test for a weak spectral line.

Decision:

The relevant pulse is effectively a pi pulse, so if the scan crossed a pODMR resonance the expected signal should be a large fluorescence drop, about 10 raw-count units or 22% normalized contrast. The observed variations are only a few raw-count units, include comparable positive and negative excursions across the scan, and do not show a convincing pODMR resonance with the expected amplitude. I therefore decide resonance_absent.
