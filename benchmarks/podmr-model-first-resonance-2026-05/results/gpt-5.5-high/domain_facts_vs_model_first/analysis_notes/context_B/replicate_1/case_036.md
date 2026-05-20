Case podmr_021_2026-05-16-171244

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:

- Active sequence file: Rabimodulated.xml.
- The sequence first polarizes and performs a detection before any microwave pulse. This is the true m_S = 0 bright reference, so readout 1 is the no-pulse reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active experiment then applies one rabi_pulse_mod_wait_time pulse and performs detection. This makes readout 2 the pulsed-MW signal readout.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s = 52 ns. At sample_rate = 250 MHz this is already on a 4 ns grid.

Expected quantitative signal:

Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, this sequence uses f_R = 10 MHz. For a square pulse, the excited-state population versus detuning in Hz is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

On resonance, with t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated bright-to-dark contrast scale is about 22%, so the expected on-resonance fractional depletion of the active readout relative to the bright reference is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout 1 level is 46.49 counts, so an on-resonance point should be lower by about

46.49 * 0.219 = 10.19 counts.

Observed data check:

- readout 1 mean = 46.49 counts.
- readout 2 mean = 46.41 counts.
- readout2 - readout1 ranges from -2.27 to +1.81 counts.
- readout2/readout1 ranges from 0.9528 to 1.0398.
- The deepest normalized depletion is only 4.7%, or about 2.27 counts, far smaller than the expected 21.9%, about 10.2 counts.

I also fit the normalized ratio readout2/readout1 against the square-pulse Rabi lineshape plus a linear baseline. The best unconstrained Rabi amplitude has the wrong sign for a depletion feature, and a forced 22% contrast lineshape is not supported by the data in the scanned interval. The per-average traces show large baseline/tracking changes, so the apparent small dips are compatible with cadence and drift rather than a reproducible pulsed ODMR resonance.

Decision: resonance_absent.
