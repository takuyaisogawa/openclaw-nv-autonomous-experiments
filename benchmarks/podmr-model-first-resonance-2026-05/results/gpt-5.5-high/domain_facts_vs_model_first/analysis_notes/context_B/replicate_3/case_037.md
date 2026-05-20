Analysis note for podmr_022_2026-05-16-172725

I used the provided sequence XML and the raw export values for the scan data. The active sequence is Rabimodulated.xml. With full_expt = 0, the "Acquire 1 level reference" block is skipped. The executed measurement is:

1. adj_polarize
2. detection: true m_S = 0 fluorescence reference, corresponding to readout 1
3. wait_for_awg
4. rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth
5. detection: post-microwave signal readout, corresponding to readout 2

The relevant pulse parameters from the provided XML are length_rabi_pulse = 52 ns and mod_depth = 1. The scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical expectation:

The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, I used the detuned two-level Rabi model

P_transfer(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * sqrt(f_R^2 + df^2) * t)

with f_R = 10 MHz and t = 52 ns. On resonance this gives

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence drop in readout 2 relative to readout 1 is

0.22 * 0.996 = 0.219, or about 22%.

The expected fractional drops from the same model are about 21.9% at zero detuning, 20.4% at 2.5 MHz detuning, 16.5% at 5 MHz detuning, 6.0% at 10 MHz detuning, and 1.1% at 20 MHz detuning. Therefore, if a resonance were in the scan window, it should create a strong dark feature spanning more than one sampled point unless it were far between points or strongly suppressed.

Observed data:

Readout 1 mean = 46.76 counts and readout 2 mean = 46.83 counts. The mean readout2/readout1 ratio is 1.002 with standard deviation 0.032. The lowest observed ratio is 0.931 at 3.890 GHz, a 6.9% drop, but the adjacent points do not show the expected broadened dark feature: 3.885 GHz is bright relative to readout 1 and 3.895 GHz is nearly flat.

I also fit the readout2/readout1 ratio to the detuned Rabi lineshape above with a linear baseline. A full-strength resonance model gives a worse residual than a flat/linear baseline. Letting the resonance amplitude float gives only about 0.147 of the expected contrast scale, i.e. an on-resonance drop near 3.2%, not the expected approximately 22% response for these pulse settings.

Decision:

The active pulse is essentially a pi pulse at the given mod_depth, so a real pODMR resonance should be large and physically shaped. The data show no such feature. The small one-point dip is inconsistent with the expected Rabi-broadened resonance and is more consistent with readout noise or drift. I decide resonance_absent.
