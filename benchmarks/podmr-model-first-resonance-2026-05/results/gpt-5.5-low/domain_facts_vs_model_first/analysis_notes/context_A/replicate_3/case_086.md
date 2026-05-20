Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to
3.925 GHz in 5 MHz steps. The instructions first acquire a true m_S = 0
reference by optical polarization and detection. Because full_expt = 0, the
conditional m_S = +1 reference block is skipped. The active signal readout is
therefore the detection after a rabi_pulse_mod_wait_time pulse.

Readout roles:

Readout 1 is the optical m_S = 0 reference. Readout 2 is the post-microwave
Rabi-pulse signal. It is not an independently acquired m_S = +1 reference in
this run.

Pulse parameters:

The XML gives mod_depth = 1 and length_rabi_pulse = 52 ns. With the provided
setup fact of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is
approximately a pi pulse. If the microwave frequency is resonant, the signal
readout should show a sizeable fluorescence reduction relative to the m_S = 0
reference, on the order of the setup contrast scale, about 22%.

Data assessment:

The combined readouts fluctuate around roughly 50 counts. The post-microwave
readout is sometimes below and sometimes above the reference, with typical
point-to-point differences of only a few percent. The mean signal/reference
ratio is about 0.988, and the deepest individual ratios are around 0.952 to
0.953. These features are much smaller than the expected pi-pulse contrast and
do not form a convincing localized pODMR resonance. The per-average traces also
show substantial tracking-like shifts and do not provide strong independent
repeatability evidence.

Decision:

No convincing pODMR resonance is present in this scan.
