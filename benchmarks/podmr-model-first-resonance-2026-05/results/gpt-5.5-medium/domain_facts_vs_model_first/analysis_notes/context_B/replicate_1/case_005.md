<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_005

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, sibling cases, prior outputs, or external context.

Active pulse sequence and readout roles

- SequenceName in the export is Rabimodulated.xml.
- The provided sequence has full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- The executed detections are therefore:
  1. Readout 1: after adj_polarize, before the microwave Rabi pulse. This is the bright m_S = 0 reference/readout.
  2. Readout 2: after rabi_pulse_mod_wait_time, then detection. This is the pODMR-sensitive readout.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse parameters from the provided XML and exported variable values:
  - mod_depth = 1
  - length_rabi_pulse = 52 ns
  - sample_rate = 250 MHz, so the pulse is 13 samples and remains 52 ns after rounding.

Expected signal model

Given the domain facts, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant square pulse with Rabi frequency f_R, the transferred population is

P_transfer = sin^2(pi * f_R * t).

Using f_R = 10 MHz and t = 52 ns:

pi * f_R * t = pi * 10e6 * 52e-9 = 1.6336 rad
P_transfer = sin^2(1.6336) = 0.9961

With a setup contrast scale of 22% between m_S = 0 and m_S = +1, the expected fractional fluorescence dip in the signal readout on resonance is:

0.22 * 0.9961 = 0.2191, or about 21.9%.

At the observed count scale of about 20 counts, this corresponds to an expected drop of about 4.4 counts, and a signal/reference ratio near:

1 - 0.2191 = 0.7809

Data check

I computed the pointwise ratio readout2/readout1 across the combined raw readouts:

- Mean ratio: 0.9878
- Standard deviation: 0.0553
- Minimum ratio: 0.8815 at 3.840 GHz
- Maximum ratio: 1.0615
- Linear-detrended ratio residual standard deviation: 0.0512
- Deepest detrended ratio residual: -0.1305 at 3.840 GHz

The largest raw negative difference readout2 - readout1 is -2.5 counts, substantially smaller than the expected approximately -4.4 count resonant drop. The readout2 minimum is 18.596 counts, not near the roughly 15.6 count signal expected for a near-complete resonant transfer from a 20-count bright reference. The low-ratio points are also not a clean resonance feature: the deepest point at 3.840 GHz is isolated and partly caused by a high readout1 value, while other lower ratios occur broadly near the high-frequency end without a corresponding expected-depth pODMR dip.

Stored per-average overlays show large opposite tracking drifts between averages, so the averages mainly reflect tracking cadence rather than an independent repeatability test.

Decision

The active pulse should produce a strong near-pi-pulse pODMR contrast if the scan crosses a resonance. The observed signal is much smaller than the quantitative expectation and lacks a coherent resonance-shaped dip in the microwave-after-pulse readout relative to the m_S = 0 reference. I therefore classify this case as resonance_absent.
