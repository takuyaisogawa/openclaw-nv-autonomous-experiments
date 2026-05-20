Case: podmr_024_2026-05-16-175646

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- The sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active experiment has full_expt = 0, so the intermediate "1 level reference" block is skipped.
- Readout 1 is acquired immediately after adj_polarize and is therefore the bright m_S = 0 reference.
- Readout 2 is acquired after a rabi_pulse_mod_wait_time pulse and is the pODMR signal channel.
- The relevant pulse is length_rabi_pulse = 52 ns, rounded at 250 MS/s, so it remains 52 ns.
- The active modulation depth from the provided sequence values is mod_depth = 1.

Quantitative physical expectation:

Given the supplied calibration, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant square pulse, the transferred population is

P = sin^2(pi * f_R * t)

with f_R = 10 MHz and t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant pODMR contrast for this pulse is

C_expected = 0.22 * 0.996 = 0.219, or about 21.9%.

The measured readout 1 mean is 53.86. A resonant response should therefore reduce readout 2 by approximately

53.86 * 0.219 = 11.80 readout units,

placing readout 2 near 42.05 at resonance, aside from noise and tracking drift.

Observed data comparison:

- Mean readout 1: 53.86.
- Mean readout 2: 54.17.
- Mean difference readout2 - readout1: +0.32.
- Standard deviation of pointwise differences: 1.13.
- Most negative readout2 - readout1 point: -1.65 at 3.895 GHz.
- Largest positive apparent contrast (readout1 - readout2)/readout1: 3.07%.

The largest observed darkening is about 1.65 readout units, far below the approximately 11.8 units expected for a resonant 52 ns pulse at mod_depth = 1. The observed contrast extrema are only a few percent and include many points where readout 2 is brighter than readout 1. Stored averages show large vertical offsets consistent with tracking cadence, so they should not be treated as a strong repeatability test.

Decision:

No pODMR resonance is present in this scan. A true resonance under this sequence should produce a large dip in readout 2 relative to the m_S = 0 reference; the measured data show no such feature.
