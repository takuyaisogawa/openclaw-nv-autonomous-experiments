Case: podmr_011_2026-05-11-181506

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- Sequence name in the export is Rabimodulated.xml.
- The provided XML has full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- Readout 1 is acquired immediately after adj_polarize and before the swept microwave pulse, so it is the polarized m_S = 0 reference for the shot.
- Readout 2 is acquired after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so it is the signal readout after the active microwave pulse.
- Active pulse parameters from the provided XML: length_rabi_pulse = 52 ns, sample_rate = 250 MHz, mod_depth = 1, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected-signal calculation:

Use the driven two-level Rabi model for population transfer from m_S = 0 to m_S = +1:

P(+1, Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau)

where f_R is the on-resonance Rabi frequency in cycles/s, Delta is detuning in Hz, and tau is the microwave pulse duration. The setup facts give f_R ~= 10 MHz at mod_depth = 1, and tau = 52 ns. On resonance:

P(+1, 0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance fractional fluorescence drop in readout 2 relative to readout 1 is:

0.22 * 0.9961 = 0.2191, or about 21.9%.

For the point with the largest observed normalized drop, readout 1 = 21.346 at 3.880 GHz. The expected readout 2 value on resonance is:

21.346 * (1 - 0.2191) = 16.67.

The observed readout 2 at 3.880 GHz is 16.981, giving an observed normalized drop:

(21.346 - 16.981) / 21.346 = 0.2045, or 20.45%.

This is close to the 21.9% expected drop for a near-pi pulse. The simple detuned model also gives expected fractional drops of about 16.5% at +/-5 MHz and 6.0% at +/-10 MHz from the resonance center. The measured normalized drops around the feature are 11.6% at 3.870 GHz, 16.7% at 3.875 GHz, 20.5% at 3.880 GHz, 8.8% at 3.885 GHz, and 3.7% at 3.890 GHz. The feature is somewhat asymmetric, but its peak amplitude and width are on the correct scale for the active pulse.

Away from the central feature, the edge points have mean readout2/readout1 ratio 0.994 with standard deviation 0.034, while the 3.880 GHz point has ratio 0.795. Stored per-average traces show substantial tracking-like drift, so I do not treat the two stored averages as a strong independent repeatability test. The combined readout-2 depression relative to the same-shot readout-1 reference has the expected sign, frequency-localized shape, and near-pi-pulse amplitude.

Decision: a pODMR resonance is present.
