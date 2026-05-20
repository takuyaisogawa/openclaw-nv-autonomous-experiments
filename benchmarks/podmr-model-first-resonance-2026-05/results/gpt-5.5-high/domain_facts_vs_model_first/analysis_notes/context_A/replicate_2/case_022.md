The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 to 3.925 GHz. In the provided sequence XML, mod_depth is 1 and length_rabi_pulse is 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth 1, this is approximately a pi pulse, so on resonance the pulsed readout should show close to the full m_S = 0 to m_S = +1 contrast, about a 22% fluorescence drop.

The instruction block first polarizes and detects the true m_S = 0 level. Because full_expt is 0, the optional "1 level reference" block is skipped despite the adiabatic-inversion flag. The second active detection happens after rabi_pulse_mod_wait_time with the 52 ns, mod_depth 1 pulse, so readout 1 is the zero-level reference and readout 2 is the resonance-sensitive pulsed signal.

The combined readouts show readout 1 staying roughly flat near 35 to 37 counts across the sweep, while readout 2 has a pronounced localized dip around 3.875 to 3.880 GHz, reaching about 28 counts from a surrounding level near 35 to 36. That drop is roughly 20% to 22%, consistent with the expected contrast for a near-pi pulse. The per-average traces have tracking-related offsets, but both averages contribute to the same central depression in the pulsed readout rather than a comparable dip in the zero reference.

Decision: a pODMR resonance is present.
