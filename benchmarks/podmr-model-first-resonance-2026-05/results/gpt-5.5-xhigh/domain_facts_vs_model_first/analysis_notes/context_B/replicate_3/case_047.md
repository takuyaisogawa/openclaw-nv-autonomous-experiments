Case: podmr_033_2026-05-16-203113

I used the provided sequence XML to identify the active sequence. The sequence first polarizes the NV and performs a detection labeled in the comments as the true m_S = 0 level reference. The branch that would acquire a separate m_S = 1 reference is guarded by full_expt, and full_expt is 0, so that branch is inactive. The active scanned measurement is therefore:

1. polarize and detect: readout 1, the bright m_S = 0 reference
2. wait
3. rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth
4. detect: readout 2, the signal after the microwave pulse

The relevant pulse parameters from the XML/variable values are:

- active pulse: rabi_pulse_mod_wait_time
- mod_depth: 1
- sample rate: 250 MHz
- requested pulse duration: 52 ns
- rounded pulse duration: round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns
- scanned variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps

Physical model calculation:

The stated setup has Rabi frequency about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For a square pulse starting from m_S = 0, the transition probability for detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

using frequencies in cycles per second. At resonance delta = 0:

P(0) = sin^2(pi * 10 MHz * 52 ns) = sin^2(1.6336) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected signal/readout-reference ratio at resonance is:

R_res = 1 - 0.22 * 0.996 = 0.7809

With reference counts near 53-55, an on-resonance point should therefore be lower by roughly 11.3 to 12.2 raw-count units. The finite-duration square-pulse model also predicts a broad dip around a resonance, not a single tiny point fluctuation.

Data comparison:

I normalized the measured signal readout by the reference readout at each scan point. The observed readout2/readout1 ratios have mean 1.0076, minimum 0.9728, maximum 1.0457, and standard deviation 0.0191. The largest observed signal deficit is only 2.72%, corresponding to -1.44 raw-count units. Most signal points are equal to or brighter than the reference.

A fixed-contrast resonance model with a resonance constrained inside the scanned frequency interval fits much worse than a flat no-resonance baseline: constrained fixed-contrast SSE = 0.0684 versus flat SSE = 0.00730. If the contrast amplitude is allowed to float freely inside the scan, the best-fit dip amplitude is only about 0.029, far below the physically expected 0.219. Letting a fixed-contrast resonance move outside the scanned interval only gives a weak off-edge tail and does not indicate a resonance within the measured range.

Decision:

The active pulse is strong enough to produce an almost full population transfer on resonance, so a real pODMR resonance in the scan should cause a large, contrast-scale decrease in readout 2 relative to readout 1. The measured normalized data show no such decrease, only small fluctuations on the few-percent scale. I therefore decide that a pODMR resonance is absent in this scan.
