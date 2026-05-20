Case podmr_018_2026-05-16-134409

Sequence interpretation:
- Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and detects immediately. This is the bright m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The experiment readout is taken after one rabi_pulse_mod_wait_time pulse followed by detection.
- Pulse duration: length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding gives 13 samples, still 52 ns.
- mod_depth = 1 from the provided XML variable values.

Physical model calculation:
Use the rectangular driven two-level transition probability

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

with f_R = 10 MHz * mod_depth = 10 MHz and t = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected fractional fluorescence loss at resonance is

0.22 * 0.996 = 0.219, or about 21.9%.

For a bright reference near 48 counts, that is an expected on-resonance dip of about 10.5 counts.

Observed quantitative comparison:
- readout 1 is the bright reference, with mean 48.07 counts and standard deviation 1.08 counts over the scan.
- readout 2 is the post-pulse signal.
- The observed fractional drop 1 - readout2/readout1 reaches 0.193 at 3.875 GHz and 0.172 at 3.880 GHz.
- In counts, the signal drops from reference levels near 47 to 49 counts down to about 39 to 40 counts at the dip, an 8 to 10 count loss.
- A fixed-contrast model scan fit gives best center about 3.877 GHz and predicts large drops at 3.870, 3.875, 3.880, and 3.885 GHz, matching the localized dip width and location.
- The sum of squared residuals for the fixed 22% contrast resonance model is 0.0263 in fractional-drop units, versus 0.0811 for a flat no-resonance model. Allowing the amplitude to float gives best contrast 0.204, close to the expected 0.219.

Decision:
The post-pulse readout shows a localized dip with the expected magnitude for a near-pi pulse at mod_depth = 1. Stored averages are only two averages and mainly reflect tracking cadence, so I do not treat them as independent repeatability proof, but the combined signal is quantitatively consistent with the driven-transition model and substantially better than a flat no-resonance explanation.

Prediction: resonance_present.
