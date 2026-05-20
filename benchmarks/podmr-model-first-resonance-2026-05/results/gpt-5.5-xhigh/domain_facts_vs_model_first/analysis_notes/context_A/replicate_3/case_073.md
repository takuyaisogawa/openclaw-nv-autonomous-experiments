I used the provided sequence XML and the exported raw readouts for this case only.

The active sequence is Rabimodulated with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The variable full_expt is 0, so the optional +1 reference branch is not executed. The readout before the microwave pulse is therefore the true m_S = 0 reference, and the readout after the single rabi_pulse_mod_wait_time call is the pODMR signal readout.

The active microwave pulse is length_rabi_pulse = 52 ns. At the 250 MHz sample rate this is already sample-aligned. The active mod_depth is 1, giving an expected Rabi frequency of about 10 MHz, so a 52 ns pulse is approximately a pi pulse on resonance. With the stated setup contrast scale of about 22%, a real resonance should produce a large reduction of the signal readout relative to the 0-reference readout, roughly 9 counts on a 42-count baseline.

The combined raw readouts do not show that scale of contrast. The largest positive separation between the 0-reference readout and signal readout is about 2.9 counts, the mean separation is about 0.6 counts, and the separation changes sign at some scan points. The stored per-average traces mostly show a baseline shift between averages, consistent with tracking cadence effects, rather than a reproducible spectral feature. There is no clear, stable pODMR dip across the microwave-frequency scan.

Decision: resonance_absent.
