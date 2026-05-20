Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The instruction block first polarizes and detects the bright m_S = 0 reference, then because full_expt = 0 it skips the separate m_S = +1 reference branch, then applies rabi_pulse_mod_wait_time followed by the signal detection. Thus readout 1 is the bright/reference detection and readout 2 is the post-microwave-pulse detection.

The provided sequence parameters give mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse, so on resonance the signal readout should approach the darker m_S = +1 level. Given the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a real resonance should produce a much larger signal/reference drop than a few percent.

The measured signal/reference differences fluctuate around zero. The largest deficit of readout 2 relative to readout 1 is about 5.3%, with nearby high-frequency points at only about 2-5% deficit and no clear resonance-shaped feature. The stored two averages show broad tracking-like offsets rather than a strong independent repeatable dip. These observations are inconsistent with a near-pi-pulse pODMR resonance under the provided contrast scale.

Decision: resonance_absent.
