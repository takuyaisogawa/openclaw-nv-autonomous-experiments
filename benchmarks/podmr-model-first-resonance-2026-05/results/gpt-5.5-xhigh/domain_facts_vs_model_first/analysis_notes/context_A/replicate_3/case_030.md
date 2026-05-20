The active pulse program is Rabimodulated.xml. With full_expt = 0, the enabled detections are the initial polarized reference and the post-Rabi-pulse signal; the optional m_S = +1 reference block is skipped. Therefore readout 1 is the true m_S = 0 optical reference after adj_polarize, and readout 2 is the signal after a swept microwave Rabi pulse.

The provided sequence file and exported active variable values give length_rabi_pulse = 52 ns and mod_depth = 1. At the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is effectively a pi pulse on resonance, so a real resonance should be able to approach the full optical contrast scale of about 22%.

The combined readouts show a localized dip in readout 2 centered near 3.875 GHz while readout 1 stays near its usual reference level. At 3.875 GHz, readout 1 is 46.21 and readout 2 is 35.87, giving readout2/readout1 = 0.776 or about 22.4% contrast. The dip spans adjacent scan points and is visible in both stored averages, though the stored averages should mainly be treated as tracking-cadence samples. This depth and localization are consistent with an on-resonance pODMR response from a near-pi pulse, not just broadband drift.

Decision: resonance_present.
