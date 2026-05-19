<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions polarize, detect the mS=0 reference, wait, apply one rabi_pulse_mod_wait_time, then detect the post-pulse signal. full_expt is 0, so the optional explicit mS=+1 reference block is not active even though it is present in the XML.

Readout roles: readout 1 is the true 0-level/polarized reference detection. readout 2 is the detection after the microwave pulse. The XML variables give length_rabi_pulse = 52 ns and mod_depth = 1. With the given setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so on resonance the post-pulse readout should show a large drop from the mS=0 reference, on the order of the stated 22% contrast scale.

Observed data: the two combined readouts are both around 53-55 counts across the sweep and do not show a stable, localized fluorescence decrease in readout 2 relative to readout 1. At several frequencies readout 2 is comparable to or higher than readout 1. The per-average traces show large tracking offsets between averages, and the stored two averages should not be overinterpreted as an independent repeatability test. The feature near 3.895 GHz is a low point in readout 2, but it is not a coherent resonance signature because the expected post-pulse contrast relative to the reference is absent and the surrounding behavior is dominated by readout scatter/tracking drift.

Decision: resonance_absent.
