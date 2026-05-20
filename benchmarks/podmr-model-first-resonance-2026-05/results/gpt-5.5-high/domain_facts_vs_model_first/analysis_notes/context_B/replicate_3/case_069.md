Case: podmr_055_2026-05-17-045046

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence XML, length_rabi_pulse is 52 ns and sample_rate is 250 MHz, so the rounded pulse length remains 52 ns.
- mod_depth is 1 in the provided sequence XML and in the exported variable values.
- full_expt is 0, so the "Acquire 1 level reference" block is inactive. The active readouts are:
  - readout 1: polarized m_S = 0 reference after laser polarization and detection.
  - readout 2: signal readout after the modulated Rabi microwave pulse.

Physical model calculation:
- The setup contrast between m_S = 0 and m_S = +1 is about 22%.
- The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so f_R = 10 MHz here.
- For a resonant square pulse, the transfer probability is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected resonant fractional fluorescence drop in readout 2 relative to readout 1 is therefore 0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout 1 level is 43.81 raw-count units, so an on-resonance point should show a drop of about 9.6 raw-count units.
- Even if the resonance falls halfway between 5 MHz scan points, the detuned Rabi model
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)
  gives P(2.5 MHz) = 0.929, implying an expected drop of about 20.4%, or 9.0 raw-count units.
- At 5 MHz detuning the expected drop is still about 16.5%, or 7.2 raw-count units.

Observed data comparison:
- Across the 21 scan points, mean readout 1 is 43.81 and mean readout 2 is 43.45.
- The difference readout2 - readout1 has mean -0.37 raw-count units, standard deviation 1.61, minimum -2.62, and maximum +3.19.
- The largest observed fractional negative difference is about -5.9%, far below the expected approximately -22% resonant signature for the active pulse.
- The negative excursions are scattered at several frequencies rather than forming a frequency-localized ODMR dip with the expected Rabi-broadened scale.
- A least-squares fit of the expected dip shape to readout2 - readout1 prefers an unphysical negative dip amplitude rather than the fixed positive drop of about 9.6 counts expected from the sequence.
- The two stored averages show substantial baseline/tracking variation, so they do not provide a strong independent repeatability test; the combined readout comparison is the relevant check.

Decision:
The active pulse should produce a large, easily visible readout 2 suppression if a pODMR resonance is present in the scan range. The observed differential signal is small, sign-changing, and not frequency-localized. I therefore decide that a pODMR resonance is absent.
