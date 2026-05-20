Case: podmr_034_2026-05-15-235221

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:

- SequenceName in the raw export is Rabimodulated.xml, and inputs/sequence.xml is a Rabimodulated sequence.
- The active instructions first polarize and detect, then skip the optional "Acquire 1 level reference" block because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and detect again.
- Readout 1 is therefore the true m_S = 0 post-polarization reference.
- Readout 2 is the signal after the microwave Rabi pulse.
- Active pulse duration is length_rabi_pulse = 52 ns. At the 250 MHz sample rate this is already on the 4 ns timing grid.
- Active mod_depth is 1 from the provided XML and the raw export Variable_values.

Quantitative expected-signal model:

The relevant two-level model for the second readout is a detuned square-pulse Rabi response:

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * T * sqrt(f_R^2 + delta^2))

where f_R is the on-resonance Rabi frequency in cycles/s, T is the pulse duration, and delta is the microwave detuning in cycles/s. The detected fluorescence is modeled as

readout_2(delta) = baseline * (1 - C * P_1(delta))

with setup contrast C = 0.22. The given setup has f_R about 10 MHz at mod_depth = 1, so with T = 52 ns:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected resonant fluorescence reduction is therefore 0.22 * 0.996 = 0.219, i.e. about 22% of the m_S = 0 level. Using the measured readout-1 mean baseline 36.01 counts, the expected resonant readout-2 value is about 36.01 * (1 - 0.219) = 28.12 counts.

Observed data:

- Readout 1 mean is 36.01 counts and has no matching narrow dip at the resonance-like frequency.
- Readout 2 reaches 26.81 counts at 3.875 GHz and 26.29 counts at 3.880 GHz.
- The deepest observed drop relative to the readout-1 mean is 9.72 counts, or 27.0%. This is somewhat larger than but close to the expected 22% contrast-scale drop, and it is within a plausible range given raw count noise and baseline scatter.
- A least-squares fit of the detuned Rabi response to readout 2 gives a center near 3.87665 GHz, baseline 35.79 counts, and amplitude 9.39 counts. The model SSE is 27.6, compared with 172.8 for a constant null and 172.1 for a linear null.
- The stored two averages both show suppressed readout 2 in the same frequency neighborhood, but this is treated only as supporting context because stored averages can reflect tracking cadence rather than independent repeatability.

Decision:

The active pulse is expected to produce an approximately full population transfer on resonance and thus a large single-readout fluorescence dip. The observed readout-2 dip is localized, has the expected width scale for a 52 ns pulse, has the expected sign and approximate magnitude, and is absent from readout 1. I therefore decide that a pODMR resonance is present.
