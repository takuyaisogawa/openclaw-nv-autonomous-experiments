Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The provided XML is Rabimodulated.xml logic.
- full_expt = 0, so the optional "1 level reference" block is inactive.
- The sequence first performs adj_polarize and detection: this is the true mS=0 bright reference readout.
- After a wait, it applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detection: this is the pODMR readout after the microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this remains 52 ns after rounding.

Quantitative model:
Use a rectangular resonant microwave pulse on a two-level mS=0 to mS=+1 transition. The setup Rabi frequency is about 10 MHz at mod_depth = 1, so f_R = 10 MHz. For detuning df, the transition probability is

P(df) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau)

with Omega = 2*pi*10 MHz, Delta = 2*pi*df, and tau = 52 ns. On resonance,

P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

With the given 22% contrast scale, a fully resonant pulse should reduce the bright readout by about 0.22 * 0.996 = 0.219 of the bright level. The measured bright reference readout has median 29.731 counts, so the expected resonant drop is 6.515 counts and the expected on-resonance pODMR readout is about 23.216 counts. This is the expected signal for a resonance; far from resonance the transition probability is small and the second readout should return toward the bright level.

Data comparison:
- Scan range: 3.825 to 3.925 GHz in 5 MHz steps.
- Readout 1 median: 29.731 counts.
- Readout 2 minimum: 24.154 counts at 3.880 GHz.
- Observed drop from the bright median: 5.577 counts, or 18.8% of the bright reference.
- The second readout is depressed over the center of the scan and recovers toward the sides; edge mean for readout 2 is 28.592 counts.
- A least-squares rectangular-pulse lineshape fit for readout 2 gives a best center near 3.8785 GHz and improves residual sum of squares over a flat model by a factor of about 4.12.

Decision:
The active pulse is effectively a pi pulse at the stated modulation depth, so a real resonance should produce a large dip close to the full 22% contrast scale. The observed centered dip in the microwave readout has the right sign, location within the scanned band, and magnitude close to the model expectation. The stored averages show tracking-like drift and are not treated as independent repeatability evidence, but the combined readout is quantitatively consistent with a pODMR resonance.

Prediction: resonance_present.
