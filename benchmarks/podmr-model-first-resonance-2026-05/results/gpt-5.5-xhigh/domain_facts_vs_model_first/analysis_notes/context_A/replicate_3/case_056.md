Sequence and readout interpretation:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML has full_expt = 0, so the optional +1 reference block is skipped.
- Readout 1 is the polarized m_S = 0 reference acquired immediately after optical pumping.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time.
- mod_depth is 1 and length_rabi_pulse is 52 ns. At the stated setup scale, this is about a 10 MHz Rabi rate, so 52 ns is approximately a pi pulse and should give a near-full m_S = 0 to m_S = +1 contrast response on resonance.

Data assessment:

The two raw readouts share a downward drift over the scan, from roughly 48-50 counts early to roughly 45-46 counts late. Normalizing readout 2 to the m_S = 0 reference does not reveal a clean resonance-shaped feature. Around 3.875 GHz, readout 2/readout 1 is about 0.960, only a roughly 4% drop, and comparable off-center ratio fluctuations are present elsewhere. With a near-pi pulse at mod_depth = 1, a real resonance should approach the setup contrast scale of about 22%, far larger than the observed feature. Stored averages are not enough to treat the small dip as independent repeatability.

Decision: resonance_absent.
