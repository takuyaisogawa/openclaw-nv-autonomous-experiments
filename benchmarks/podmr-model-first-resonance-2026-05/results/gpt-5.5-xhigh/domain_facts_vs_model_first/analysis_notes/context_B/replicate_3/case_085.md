Case: podmr_071_2026-05-17-084118

I used the provided sequence XML and the numeric export only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is inactive.
- The active detections are therefore: readout 1 = true m_S = 0 reference after optical polarization; readout 2 = final readout after the Rabi-modulated microwave pulse.
- length_rabi_pulse = 52 ns after sample-rate rounding.
- mod_depth = 1.

Quantitative expected-signal model:

For a square microwave pulse, using the setup facts,

f_R = 10 MHz * mod_depth = 10 MHz
tau = 52 ns
C = 0.22

The transition probability versus detuning is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2))

where f_R and Delta are in cycles per second. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

Thus the expected final/reference fluorescence ratio at resonance is

R = 1 - C * P(0) = 0.7809.

The mean readout-1 level is 49.459 counts, so the expected on-resonance drop in readout 2 relative to readout 1 is about

49.459 * 0.22 * 0.9961 = 10.84 counts.

The scan step is 5 MHz, so if a resonance were inside the scanned range the nearest sampled point would be at most 2.5 MHz detuned. At 2.5 MHz detuning the same model gives P = 0.9292, expected ratio = 0.7956, and expected drop = 10.11 counts. This is still a large feature.

Measured combined data:
- readout1 mean = 49.459, range = 44.769 to 51.558.
- readout2 mean = 49.448, range = 45.365 to 51.885.
- final/reference ratio mean = 1.00036, minimum = 0.94573.
- largest measured deficit is at 3.860 GHz: readout1 = 51.385, readout2 = 48.596, deficit = 2.788 counts, ratio = 0.9457.

Model comparison on final/reference ratio:
- Linear no-resonance baseline SSE = 0.01795.
- Best fixed 22% detuned-Rabi resonance model with resonance constrained inside the scan has SSE = 0.05998, much worse than the no-resonance baseline.
- A fit with the resonance amplitude free and constrained positive prefers only 0.0235 contrast, about one tenth of the expected 0.22 contrast.
- The unconstrained best-amplitude fit prefers a negative dip amplitude, i.e. the opposite sign from an ODMR fluorescence loss.

Decision:

The active pulse should produce an approximately pi-pulse ODMR loss near 22% of the reference fluorescence if a resonance is present in the scan. The measured ratios stay near unity and never approach the expected 0.78 to 0.80 resonant ratio, and the fixed physical resonance model is rejected by the data. I therefore decide that a pODMR resonance is absent.
