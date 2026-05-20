Case: podmr_044_2026-05-16-232730

I used the provided sequence XML to identify the active experiment. The sequence is Rabimodulated.xml with mw_freq as the scanned variable. The instruction block first performs polarization and detection for the true m_S = 0 reference, so combined raw readout 1 is the 0-level reference. The optional 1-level reference block is inactive because full_expt = 0. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection, so combined raw readout 2 is the microwave-pulsed signal readout.

Active pulse parameters from the provided XML / scan variable values:
- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so the pulse is 13 samples and remains 52 ns after rounding
- scan range = 3.825 GHz to 3.925 GHz in 5 MHz steps

Physical model calculation:

For a rectangular resonant microwave pulse, I used the two-level transition probability

P_transfer(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * t)

with f_R = 10 MHz at mod_depth = 1 and t = 52 ns. The fluorescence signal model is

signal/reference = 1 - C * P_transfer(df)

with C = 0.22 for the m_S = 0 to m_S = +1 contrast scale.

At df = 0, P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996, so an on-resonance point should have signal/reference = 1 - 0.22 * 0.996 = 0.781, a 21.9% dip. At 5 MHz detuning, the model still gives P_transfer = 0.749 and signal/reference = 0.835, a 16.5% dip. Because the frequency spacing is 5 MHz, a resonance inside the scanned range should therefore produce a large local depression in readout 2 relative to readout 1 at one or more neighboring points.

Measured paired readout comparison:
- mean readout 1 = 48.56
- mean readout 2 = 48.69
- mean signal/reference ratio = 1.003
- minimum signal/reference ratio = 0.952 at 3.865 GHz
- largest observed positive contrast, (readout1 - readout2) / readout1, is 4.78%

This is far smaller than the 16% to 22% dip expected for a resonance sampled on or near a scan point with the active mod_depth = 1, 52 ns pulse. The shallow minimum is also not a convincing independent repeatability check because the stored averages can reflect tracking cadence; in paired normalized form the two readouts remain close rather than showing the large state-dependent fluorescence drop predicted by the model.

Decision: resonance_absent.
