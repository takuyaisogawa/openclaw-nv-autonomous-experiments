Case podmr_058_2026-05-17-053345

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active pulse sequence is: optical polarize, detection, wait, then a single rabi_pulse_mod_wait_time pulse followed by detection. The optional "Acquire 1 level reference" block is inactive because full_expt = 0.
- Readout role: readout 1 is the true m_S = 0 bright reference after polarization and before the microwave pulse. Readout 2 is the pODMR signal readout after the Rabi-modulated microwave pulse.
- Active pulse duration length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is already an integer 13 samples, so rounding leaves it at 52 ns.
- Active mod_depth = 1 from Variable_values in raw_export.json, despite the embedded saved Sequence text showing an older/default 0.3 value. I use Variable_values and inputs/sequence.xml as the active run parameters.

Explicit quantitative model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling with mod_depth, f_R = 10 MHz.
- For a resonant rectangular pulse, the transition probability is P = sin^2(pi f_R t / 2), where t is the pulse length and f_R is in cycles/s.
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9 / 2) = sin^2(0.8168) = 0.531.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence change is 0.22 * 0.531 = 0.1169, about 11.7% of the bright level.
- The mean raw count level is about 45.6, so a resonance at full relevant coupling should produce an expected signal reduction of about 45.6 * 0.1169 = 5.3 raw-count units in readout 2 relative to readout 1.

Observed data comparison:
- Mean readout 1 = 45.681; mean readout 2 = 45.584.
- Mean difference readout2 - readout1 = -0.097 raw-count units, or about -0.16% fractional difference. This is far smaller than the modeled -5.3 count, -11.7% resonance signal.
- Pointwise readout2 - readout1 values range from -3.231 to +3.038 counts with standard deviation 1.834 counts. The largest negative deviations are still below the expected full resonant drop, and they occur as isolated/noise-scale points rather than a coherent resonance feature.
- Stored averages mainly show vertical tracking offsets, so I did not treat the two averages as a strong independent repeatability test.

Decision:
The active physical model predicts a clearly resolvable negative pODMR contrast if a resonance is present. The measured signal readout is essentially equal to the bright reference on average and lacks a coherent frequency-localized loss of the expected amplitude. I therefore decide that a pODMR resonance is absent.
