Case: podmr_057_2026-05-17-051839

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

1. adj_polarize, then detection: this is the true m_S = 0 reference readout.
2. The optional +1 reference block is skipped because full_expt = 0.
3. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detection: this is the pODMR signal readout after the microwave pulse.

Thus readout 1 is the pumped m_S = 0 reference and readout 2 is the post-microwave signal. There is no active m_S = +1 calibration readout in this sequence.

Pulse parameters from the XML/exported variable values:

- length_rabi_pulse = 52 ns. At 250 MHz sample rate this is exactly 13 samples, so no effective rounding change.
- mod_depth = 1.
- The relevant microwave pulse is the 52 ns rabi_pulse_mod_wait_time call after the skipped full_expt block.

Expected signal model

Using the supplied setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a rectangular driven two-level pulse, the excited-state probability at detuning df is

P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * t),

with f_R = 10 MHz and t = 52 ns.

On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so an in-band resonance should reduce the signal/reference ratio by

0.22 * 0.996 = 0.219, or about 21.9%.

At the observed count level, mean readout 1 is 45.46 counts, so the expected on-resonance drop is about

45.46 * 0.219 = 9.96 counts.

Data comparison

The measured combined readout ratios readout2/readout1 have:

- mean = 0.9993
- standard deviation across scan points = 0.0216
- minimum = 0.9550 at 3.925 GHz
- maximum apparent contrast drop = 1 - 0.9550 = 0.0450, or 4.5%

The largest combined deficit is readout2 - readout1 = -2.08 counts, far smaller than the approximately -10 count drop expected for an in-band resonance under the active pulse parameters.

I also fit the finite-pulse model to the measured ratios. For the physically expected fixed contrast amplitude of 0.22, the best one-sided fit places the resonance center outside the scan, near 3.9357 GHz, and only accounts for a small edge dip. The data do not show the required deep, broad finite-pulse dip that would appear if the pODMR resonance were inside the scanned range.

Stored averages are not treated as a strong repeatability test because they can track cadence. Still, the largest edge deficit is not a robust in-band resonance signature, and the combined trace lacks the expected 22% signal depression.

Decision

No pODMR resonance is present in this scanned data.
