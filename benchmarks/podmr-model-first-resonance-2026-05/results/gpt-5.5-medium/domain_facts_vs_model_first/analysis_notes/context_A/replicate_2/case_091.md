Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- readout 1 is the true mS = 0 reference acquired immediately after optical polarization.
- full_expt = 0, so the optional mS = 1 reference block is skipped.
- readout 2 is the signal after a modulated Rabi pulse followed by detection.

Pulse settings:
- mod_depth = 1 from the stored variable values.
- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse on resonance, so a real resonance should produce a sizable readout 2 reduction relative to the mS = 0 reference, on the order of the 22% contrast scale.

Data assessment:
The combined raw readouts do not show a coherent contrast-scale dip in readout 2 relative to readout 1. The signal-reference difference changes sign across the scan, with mean difference only about -0.17 counts on a roughly 51 count baseline. The largest ratio excursions are only a few percent and appear comparable to point-to-point scatter and tracking/average drift. Stored averages are not strong independent repeatability evidence here.

Decision: resonance_absent.
