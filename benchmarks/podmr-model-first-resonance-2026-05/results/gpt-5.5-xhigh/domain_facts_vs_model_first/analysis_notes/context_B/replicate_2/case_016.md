Case: podmr_001_2026-05-16-000631

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz.
- length_rabi_pulse = 5.2e-08 s. The code rounds this to the sample grid:
  round(52 ns * 250 MHz) / 250 MHz = 13 / 250 MHz = 52 ns.
- mod_depth = 1.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive.
- Readout roles:
  - readout 1 follows adj_polarize and detection before the microwave pulse, so it is the true m_S = 0 reference/control readout.
  - readout 2 follows the active rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and detection, so it is the pODMR signal readout.

Physical model calculation:

Use the provided setup facts: contrast between m_S = 0 and m_S = +1 is about C = 0.22, and the Rabi frequency is f_R = 10 MHz at mod_depth = 1. The active pulse is tau = 52 ns at mod_depth = 1.

For a resonant rectangular microwave pulse starting in m_S = 0, the transferred population is

P_1(0) = sin^2(pi * f_R * tau)

Numerically:

pi * f_R * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P_1(0) = sin^2(1.6336) = 0.9961

Expected on-resonance fluorescence ratio relative to the m_S = 0 reference:

R_signal / R_ref = 1 - C * P_1 = 1 - 0.22 * 0.9961 = 0.7809

So the expected pODMR signature for this sequence is a narrow signal-readout dip of about 21.9% relative to readout 1 near the resonance frequency. Because tau = 52 ns, the frequency response should have a scale of order 1/tau = 19.2 MHz, so a dip spanning several 5 MHz scan points is physically plausible.

Observed normalized data:

I normalized each scan point by readout 2 / readout 1. Away from the central dip, the median ratio excluding 3.865-3.890 GHz is 0.9899. The minimum ratio occurs at 3.880 GHz:

- readout 1 = 37.1346
- readout 2 = 28.9808
- ratio = 0.7804
- fractional drop from readout 1 = 21.96%
- drop relative to the off-center median ratio = 0.2095

The adjacent points are also depressed:

- 3.870 GHz: ratio = 0.8621
- 3.875 GHz: ratio = 0.7851
- 3.880 GHz: ratio = 0.7804
- 3.885 GHz: ratio = 0.9274
- 3.890 GHz: ratio = 0.9477

The two stored averages are not treated as a strong repeatability test, but they do show the same central feature in the signal/reference ratio:

- 3.875 GHz ratios: 0.7899 and 0.7805
- 3.880 GHz ratios: 0.7830 and 0.7777

Explicit model fit:

I fit the normalized ratio to a rectangular-pulse two-level response

ratio(f) = B - A * [Omega^2 / (Omega^2 + Delta^2)] * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau)

with Omega = 2*pi*10 MHz, tau = 52 ns, Delta = 2*pi*(f - f0), and free parameters B, A, and f0. The best grid fit over the central region gave:

- f0 = 3.87725 GHz
- B = 0.9986
- A = 0.2297
- A / B = 0.2300
- predicted minimum ratio = 0.7823

This fitted amplitude is essentially the expected 22% contrast for a near-pi pulse, and the predicted minimum is almost identical to the measured 0.7804. A constant-ratio null model gave SSE = 0.1111, while the pulse-response fit gave SSE = 0.0241.

Decision:

The active sequence should produce a strong negative-going pODMR feature in readout 2 relative to readout 1 if a resonance is present. The observed dip depth, center, and width are quantitatively consistent with the expected near-pi-pulse pODMR response. I therefore decide that a pODMR resonance is present.
