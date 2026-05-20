Active sequence: Rabimodulated.xml.

The XML uses a frequency scan of mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active branch has full_expt = 0, so the "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is set. The actual executed measurement is:

1. adj_polarize
2. detection: true m_S = 0 bright reference
3. wait
4. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1
5. detection: post-pulse signal readout
6. final wait

Thus readout 1 is the pre-microwave bright-state reference, and readout 2 is the post-Rabi-pulse signal. There is no active independent m_S = +1 reference in this stored data.

With the stated setup, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the microwave frequency is resonant, this pulse should transfer population from m_S = 0 toward m_S = +1 and reduce the second readout by a scale approaching the setup contrast of about 22%.

The data show that readout 1 remains comparatively flat near 40.4 to 44.1 counts, without a matching localized dip. Readout 2 is near 41 to 43 counts away from resonance, but drops strongly around 3.870 to 3.885 GHz: 36.87, 35.54, 33.92, and 36.73 counts, with the minimum at 3.880 GHz. At the minimum, readout 2 / readout 1 is about 0.823, a roughly 17.7% reduction relative to the simultaneous bright reference, which is close to the expected contrast scale for a near-pi pulse.

The two stored averages should not be treated as a strong repeatability test because they can reflect tracking cadence, but both averages preserve the same broad dip in the post-pulse readout around the same frequency region. The localized suppression appears in the signal readout and not in the bright reference, so this is consistent with a real pODMR resonance.

Decision: resonance_present.
