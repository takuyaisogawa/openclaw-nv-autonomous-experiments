Case: podmr_042_2026-05-16-225623

Sequence interpretation from inputs/sequence.xml:

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction order is:

1. adj_polarize for 1 us.
2. detection after polarization.
3. optional +1 reference block, but this is inactive because full_expt = 0.
4. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
5. detection after the Rabi pulse.

Therefore there are two active readouts. Readout 1 is the true m_S = 0 reference after optical polarization. Readout 2 is the pODMR signal readout after the microwave Rabi pulse. The skipped full_expt block means there is no recorded +1 reference readout in this run.

Key pulse parameters:

- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding does not change it.
- The setup Rabi frequency is about 10 MHz at mod_depth = 1.

Quantitative expected-signal model:

For a square pulse, using Rabi frequency in cycles/s, the driven population transfer probability versus detuning is

P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

With f_R = 10 MHz and tau = 52 ns:

- P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, essentially a pi pulse.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected active/reference fluorescence ratio on resonance is 1 - 0.22 * 0.996 = 0.781.
- At +/-5 MHz detuning, the same model gives an expected ratio of about 0.835.
- At +/-10 MHz detuning, the expected ratio is about 0.940.

Observed active/reference ratios, where readout 2 is the active readout and readout 1 is the m_S = 0 reference, remain close to 1:

- Mean ratio = 1.0035, standard deviation = 0.0302.
- Minimum ratio over the scan = 0.9479 at 3.840 GHz.
- Around the nominal central resonance region, the ratios are 1.0057 at 3.870 GHz, 0.9597 at 3.875 GHz, and 0.9811 at 3.880 GHz.
- The readout-1 minus readout-2 drop at 3.875 GHz is 1.83 counts, or 4.0% of the reference, far below the approximately 22% drop expected for the active pi pulse.

I also fit the normalized ratio to a linear baseline plus the square-pulse line shape. Letting the line contrast float gives a best positive amplitude of only about 0.046, not the expected 0.22, and a fixed 0.22 contrast line shape is a poor match to the data. The two stored averages show substantial cadence-like baseline changes, so they are not treated as a strong repeatability test.

Decision:

The relevant physical model predicts a large, localized active-readout dip that is not present in the normalized data. The small point-to-point excursions are consistent with baseline/noise compared with the expected pODMR signal. I decide resonance_absent.
