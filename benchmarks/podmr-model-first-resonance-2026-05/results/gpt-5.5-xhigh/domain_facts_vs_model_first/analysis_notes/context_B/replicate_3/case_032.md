Case: podmr_017_2026-05-16-132945

Inputs used: inputs/sequence.xml for the pulse sequence and inputs/raw_export.json for the numeric readouts. I did not use labels, previous outputs, sibling cases, or external context.

Sequence and readout roles:

- Active sequence: Rabimodulated.xml, swept parameter mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz.
- length_rabi_pulse = 52 ns. The sequence rounds it by sample_rate; 52 ns is exactly 13 samples, so the active pulse remains 52 ns.
- mod_depth = 1 from the provided XML/variable values.
- full_expt = 0, so the optional "1 level reference" block is skipped.
- readout 1 is the true 0-level reference after adj_polarize followed by detection.
- readout 2 is the pODMR signal after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) followed by detection.

Quantitative expected signal model:

Given the setup facts, the Rabi frequency is f_R = 10 MHz * mod_depth = 10 MHz. For a rectangular pulse, I modeled the transition probability versus detuning delta as

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

with tau = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

Using the stated 0 to +1 contrast scale of 22%, the expected normalized optical readout on resonance is

1 - 0.22 * 0.9961 = 0.7809,

or a 21.9% dip relative to the off-resonant 0-level readout.

Observed signal:

The combined readout ratio readout2/readout1 has its minimum at 3.875 GHz:

- readout1 = 45.4038
- readout2 = 34.1731
- ratio = 0.75265

Excluding points within 10 MHz of the minimum, the off-feature mean readout2/readout1 ratio is 0.98560 with standard deviation 0.02645. Relative to that off-feature ratio, the minimum ratio is 0.76365, a 23.6% drop. This is close to the 21.9% dip predicted by the pulse model for a near-pi pulse.

The two stored averages both have their minimum ratio at the same 3.875 GHz point:

- average 1 ratio at 3.875 GHz = 0.7206
- average 2 ratio at 3.875 GHz = 0.7847

I also fit the fixed pulse-response model above to the readout2/readout1 ratios with only a multiplicative baseline and resonance center free. The best center was 3.8764 GHz with baseline scale 0.9923. The model RMSE was 0.02585, versus 0.06864 for a constant-ratio no-resonance model, an 85.8% SSE reduction.

Decision:

The active pulse should produce a large on-resonance pODMR dip, and the measured readout2/readout1 dip has the expected size, location coherence across averages, and pulse-response shape. A pODMR resonance is present.
