Case: podmr_010_2026-05-16-114624

Sequence and readout roles

The provided sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

1. Polarize with the laser.
2. Detect immediately after polarization. This is the bright m_S = 0 reference/readout 1.
3. The optional "Acquire 1 level reference" block is skipped because full_expt = 0.
4. Apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
5. Detect again. This is the microwave-pulse signal/readout 2.

Thus the relevant pODMR observable is the loss in readout 2 relative to readout 1, not two independent resonance traces. The stored averages are only two averages and can reflect tracking cadence, so I use the combined readout ratio as the primary observable.

Quantitative physical model

Given the stated setup, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For this sequence mod_depth = 1, so Omega = 10 MHz. With a square microwave pulse of duration t = 52 ns, the expected population transferred from m_S = 0 to m_S = +1 at detuning Delta is

P1(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * t),

where Omega and Delta are in cycles/s. The detected fluorescence loss is approximately 0.22 * P1 because the stated m_S = 0 to m_S = +1 contrast scale is about 22%.

This gives a predicted resonant loss at Delta = 0 of

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996
expected fluorescence loss = 0.22 * 0.996 = 0.219, or about 21.9%.

At scan points around the resonance, this model predicts approximate losses:

- 3.865 GHz: 6.0%
- 3.870 GHz: 16.5%
- 3.875 GHz: 21.9%
- 3.880 GHz: 16.5%
- 3.885 GHz: 6.0%

Data comparison

Using contrast = 1 - readout2/readout1 from the combined raw readouts:

- 3.865 GHz: 3.1%
- 3.870 GHz: 17.6%
- 3.875 GHz: 23.7%
- 3.880 GHz: 15.7%
- 3.885 GHz: 6.9%

The maximum measured contrast occurs at 3.875 GHz, the center of the scan and the active mw_freq value, with an amplitude of 23.7%. This is close to the model expectation of 21.9% for a near-pi pulse at the known setup contrast. The adjacent points also follow the expected finite-pulse detuning dependence well. Off this window, the contrast is much smaller on average, with residual drift and tracking changes visible in readout 1 and in the per-average overlay.

Decision

The signal readout shows a quantitatively expected resonant dip relative to the m_S = 0 reference, with the correct amplitude, center frequency, and approximate width for the active 52 ns mod_depth = 1 Rabi pulse. A pODMR resonance is present.
