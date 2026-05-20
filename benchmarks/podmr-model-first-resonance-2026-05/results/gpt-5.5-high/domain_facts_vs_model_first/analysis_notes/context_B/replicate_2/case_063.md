Case: podmr_049_2026-05-17-004217

Sequence interpretation

The provided sequence XML is Rabimodulated.xml. The active scan variable is mw_freq over 3.825 to 3.925 GHz in 5 MHz steps. The sequence first performs optical polarization and detection, then waits. Because full_expt = 0, the optional "1 level reference" block is skipped. The active microwave operation is therefore one rabi_pulse_mod_wait_time call followed by detection.

Readout roles:
- readout 1: true m_S = 0 optical reference acquired immediately after polarization.
- readout 2: signal readout after the modulated Rabi pulse.

Active pulse parameters from the provided XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- sample_rate = 250 MHz, so the rounded pulse length remains 52 ns.

Expected signal model

Use the resonant Rabi population-transfer model:

P_transfer(Delta = 0) = sin^2(pi * f_R * t)

The supplied setup facts give f_R about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. Thus for this sequence:

f_R = 10 MHz
t = 52 ns
P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22 percent. A resonant pulse should therefore reduce the signal readout relative to the 0-state reference by:

expected fractional dip = 0.22 * 0.996 = 0.219
expected normalized signal/reference = 1 - 0.219 = 0.781

At the observed reference level of roughly 50 counts, a resonance should give readout 2 near 39 counts, a dip of about 11 counts relative to readout 1.

Observed data comparison

The combined readout 1 mean is 49.856 counts and the combined readout 2 mean is 49.775 counts. The normalized readout 2 / readout 1 ratios across the scan have:

- mean = 0.9986
- standard deviation = 0.0299
- minimum = 0.9487 at 3.850 GHz

The largest observed signal deficit is only 5.1 percent, or 2.62 counts, much smaller than the approximately 21.9 percent, approximately 11-count dip expected from an on-resonance 52 ns pulse at mod_depth = 1. The per-average traces show drifting levels and minima at different scan points, consistent with tracking/cadence variation rather than a stable pODMR resonance.

Decision

The expected resonant signal should be large and unmistakable for this pulse setting, but the measured post-pulse signal stays close to the 0-state reference throughout the scan. I therefore decide that a pODMR resonance is absent.
