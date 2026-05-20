Case podmr_022_2026-05-16-172725.

The provided sequence is Rabimodulated.xml with mw_freq as the scanned variable. The active microwave operation is:

- adj_polarize, then detection: this is the bright m_S = 0 reference readout.
- the full_expt block is disabled because full_expt = 0, so the explicit m_S = +1 reference is not acquired.
- rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detection: this is the microwave-driven signal readout.

With the stated setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. On resonance, the post-pulse readout should therefore show a large drop relative to the m_S = 0 reference, on the order of the setup contrast scale of about 22%.

The raw readouts do not show that behavior. The two combined traces remain near the same absolute level, and their differences fluctuate by only a few counts with no consistent localized dip across the 3.825 to 3.925 GHz sweep. The per-average overlay mainly shows drift between the two stored averages rather than a reproducible resonance-shaped contrast feature; the stored averages are not a strong independent repeatability test here.

Decision: resonance absent.
