Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

The provided XML runs a bright reference readout immediately after optical polarization, then waits, applies a rabi_pulse_mod_wait_time pulse, and performs the second detection. The optional 1-level reference block is disabled because full_expt = 0, so readout 1 is the m_S = 0 bright reference and readout 2 is the microwave-pulsed signal readout.

The relevant XML parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so on resonance it should transfer population from m_S = 0 toward m_S = +1 and reduce fluorescence by roughly the stated 22% contrast scale.

The combined raw readouts show a localized dip in readout 2 relative to readout 1 near 3.875-3.885 GHz. At 3.875 GHz the suppression is about 22.7%, and at 3.880-3.885 GHz it remains about 19-20%, matching the expected contrast for a near-pi pODMR response. Outside this region, readout 2 is mostly close to readout 1 aside from drift/noise. The per-average traces show strong drift consistent with tracking cadence, so I do not treat them as independent repeatability, but the combined differential feature has the correct amplitude, polarity, and localization for a pODMR resonance.

Decision: resonance present.
