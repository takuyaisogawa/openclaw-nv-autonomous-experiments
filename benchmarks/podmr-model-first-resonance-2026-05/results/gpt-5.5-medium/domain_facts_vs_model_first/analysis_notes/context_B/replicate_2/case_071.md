Case: podmr_057_2026-05-17-051839

Input restrictions used: only inputs/sequence.xml, inputs/raw_export.json, and the provided raw readout plot.

Active sequence and readout roles

The active sequence is Rabimodulated.xml. The XML sets full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. The executed readouts are therefore:

1. readout 1: fluorescence after adj_polarize, before the microwave Rabi pulse. This is the bright m_S = 0 reference.
2. readout 2: fluorescence after one rabi_pulse_mod_wait_time pulse and before the final wait. This is the pODMR signal readout.

Relevant pulse settings from the provided XML:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- scanned variable = mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- sample_rate = 250 MHz, so 52 ns rounds to 52 ns exactly at the 4 ns sample grid

Quantitative model calculation

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the transfer probability from m_S = 0 to m_S = +1 is:

P = sin^2(pi * f_Rabi * tau)

With f_Rabi = 10 MHz and tau = 52 ns:

pi * f_Rabi * tau = pi * 0.52 = 1.6336 rad
P = sin^2(1.6336) = 0.9961

The stated bright/dark contrast scale is about 22%, so the expected on-resonance fractional signal in readout 2 relative to the m_S = 0 reference is approximately:

0.22 * 0.9961 = 0.2191, or a 21.9% fluorescence drop.

At the measured readout 1 mean of 45.46 raw counts, this would be an expected on-resonance drop of:

45.46 * 0.2191 = 9.96 raw-count units.

Observed data check

The combined readout means are:

- mean readout 1 = 45.455
- mean readout 2 = 45.420
- mean readout2 - readout1 = -0.035 counts

Across the scan, the largest observed readout-2 drop relative to readout 1 is at 3.925 GHz:

- readout 1 = 46.154
- readout 2 = 44.077
- drop = 2.077 counts
- fractional drop = 4.50%

That is much smaller than the approximately 9.96-count, 21.9% drop expected for an on-resonance pi pulse under the given calibration. Other points fluctuate in both directions, including cases where readout 2 is brighter than readout 1. The two stored averages should not be treated as a strong independent repeatability test, but the combined trace still lacks the expected pODMR-scale signal.

Decision

The physically expected pODMR signal for this active sequence and pulse setting is a large readout-2 dip versus the bright reference. The observed readout differences are only small raw-count fluctuations compared with the expected model amplitude. I therefore decide that a pODMR resonance is absent.
