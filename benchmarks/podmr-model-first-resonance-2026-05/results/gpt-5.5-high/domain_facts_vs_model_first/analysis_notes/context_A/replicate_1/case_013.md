Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The active instruction path first polarizes and detects, giving readout 1 as the true m_S = 0 optical reference before the microwave pulse. The full_expt flag is 0, so the optional m_S = +1 reference block, including the adiabatic-inversion branch, is not executed. The only experimental microwave operation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, so readout 2 is the post-pulse signal.

With the stated setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a pi pulse is about 50 ns. The 52 ns pulse is therefore close to a resonant pi pulse: on resonance it should transfer population out of m_S = 0 and reduce readout 2 relative to the readout 1 reference by a fraction approaching the setup contrast scale of about 22%.

The combined readouts show readout 2 falling below readout 1 most strongly around 3.875-3.880 GHz. The deepest normalized contrast is about -17.8% at 3.880 GHz, with a neighboring depressed point near 3.875 GHz, which is close to the expected scale for this pulse. The per-average traces show strong slow drift/tracking cadence effects, so I do not treat the two stored averages as an independent repeatability test. The relevant same-cycle contrast in the combined raw readouts is nonetheless physically consistent with a pODMR resonance.

Decision: resonance_present.
