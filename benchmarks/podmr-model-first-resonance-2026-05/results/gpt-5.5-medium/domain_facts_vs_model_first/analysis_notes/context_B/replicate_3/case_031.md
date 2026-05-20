Case: podmr_016_2026-05-16-131456

Sequence and readout interpretation:
- The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML uses length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, delay_wrt_1mus = 0.2 us, pumping_time = 1 us.
- Because full_expt = 0, the "Acquire 1 level reference" block is skipped. The two stored readouts are therefore:
  - readout 1: the true m_S = 0 fluorescence reference after optical polarization and immediate detection.
  - readout 2: the fluorescence after the modulated Rabi pulse and detection.
- Thus a resonance should appear as a dip in readout 2 relative to readout 1, not as a calibrated 0/1 reference pair.

Explicit physical model calculation:
- Given the stated setup, Rabi frequency at mod_depth = 1 is about 10 MHz.
- For a resonant rectangular pulse of duration t = 52 ns, the rotation angle is theta = 2*pi*f_R*t = 2*pi*10e6*52e-9 = 3.267 rad.
- The transferred population is P_1 = sin(theta/2)^2 = sin(1.6336)^2 = 0.996.
- With a 22% fluorescence contrast between m_S = 0 and m_S = +1, the expected on-resonance signal/reference ratio is approximately 1 - 0.22*0.996 = 0.781, i.e. an expected dip of about 21.9% relative to the readout 1 reference.
- Detuned two-level model, using angular detuning Delta and Omega = 2*pi*10 MHz:
  P_1(Delta) = (Omega^2/(Omega^2 + Delta^2))*sin^2(0.5*t*sqrt(Omega^2 + Delta^2)).
  This gives expected signal/reference ratios of about 0.781 at 0 MHz detuning, 0.835 at 5 MHz detuning, 0.940 at 10 MHz detuning, and nearly baseline by 15 MHz detuning.

Observed quantitative comparison:
- The minimum readout 2/readout 1 ratio occurs at 3.875 GHz:
  readout 1 = 47.8269, readout 2 = 39.6538, ratio = 0.8291, fractional dip = 17.1%.
- Using off-resonance points away from the central dip, the mean readout 2/readout 1 ratio is 0.9938 with standard deviation 0.0236.
- The minimum ratio is therefore lower than the off-resonance ratio by about 6.97 off-resonance standard deviations.
- A grid fit of the two-level Rabi response to the readout ratio gives a best center near 3.877 GHz, fitted contrast amplitude about 0.204, and baseline ratio about 1.000. This is close to the independently expected 0.22 contrast scale.
- The individual stored averages both show a central depression in the signal readout near the same scan region, but since averages can reflect tracking cadence, the decision rests on the combined readout ratio and the pulse-response calculation above.

Decision:
The signal-channel dip has the correct sign, location within the scanned band, approximate depth, and approximate width expected from a 52 ns, mod_depth = 1 Rabi pulse on a single NV center with about 22% contrast. I therefore classify this case as resonance_present.
