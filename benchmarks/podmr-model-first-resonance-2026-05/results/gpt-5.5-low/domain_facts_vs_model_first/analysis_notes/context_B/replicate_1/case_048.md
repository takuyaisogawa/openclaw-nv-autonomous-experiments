Case: podmr_034_2026-05-16-204545

Sequence identification from inputs/sequence.xml:
- Active sequence: Rabimodulated-style pODMR / Rabi-modulated microwave pulse sequence, scanned over mw_freq.
- Readout roles: the first detection after adj_polarize is the true m_S=0 bright reference. The optional m_S=+1 reference block is inactive because full_expt = 0. The final detection after rabi_pulse_mod_wait_time is the pulsed signal readout.
- mod_depth: 1.
- Microwave pulse duration: length_rabi_pulse = 5.2e-08 s = 52 ns. With sample_rate = 250 MHz this is already exactly 13 samples, so rounding does not change it.

Quantitative expected-signal model:
The given setup has Rabi frequency about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For a square pulse, the resonant transition probability is

P = sin^2(pi * f_R * tau)

with f_R = 10 MHz and tau = 52 ns. This gives

pi * f_R * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P = sin^2(1.6336) = 0.996

Using the stated m_S=0 to m_S=+1 contrast scale of about 22%, the expected fractional fluorescence drop in the pulsed readout at resonance is

0.22 * 0.996 = 0.219

The raw readouts are around 50 counts, so an on-resonance point should show an approximately

50 * 0.219 = 10.96 count

drop of the pulsed signal readout relative to the m_S=0 reference, before allowing for any additional broadening or imperfect contrast. A detuned square-pulse model,

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

still predicts a pronounced dip centered at the resonance frequency, with the deepest point near 0.78 of the bright reference for this pulse.

Observed data:
- readout 1 mean = 50.016 counts, population standard deviation = 0.942 counts.
- readout 2 mean = 49.366 counts, population standard deviation = 1.187 counts.
- readout2 - readout1 mean = -0.649 counts.
- readout2 - readout1 range = -2.654 to +1.808 counts.

The largest observed pulsed-readout deficit is only about 2.65 counts, roughly one quarter of the expected resonant contrast for the active 52 ns, mod_depth 1 pulse. The deficits are scattered across the scan and alternate with positive differences, rather than forming the expected Rabi-detuned resonance profile. Stored averages are only two averages and should mainly be treated as tracking cadence, so the key comparison is the combined raw readout behavior against the expected physical signal size.

Decision:
No pODMR resonance is present. The active pulse should produce a large near-pi-pulse contrast if it crosses resonance, but the measured readout separation is small, noisy, and inconsistent with the quantitative square-pulse resonance model.
