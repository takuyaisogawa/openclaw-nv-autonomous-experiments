Sequence and decision note for podmr_014_2026-05-12-081841

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed sequence first polarizes the NV and records a "true 0 level" detection readout, then skips the optional 1-level reference because full_expt = 0. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection readout. Thus readout 1 is the bright m_S = 0 reference and readout 2 is the post-microwave readout used to look for spin transfer.

Given the supplied setup facts, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. With an expected m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance response should cause a clear drop of the post-pulse readout relative to the bright reference, not just small point-to-point fluctuations.

The raw readouts do not show a coherent pODMR dip. The second readout is sometimes below and sometimes above the first, with excursions that are narrow, inconsistent, and comparable to the per-average scatter. The stored two averages mainly reflect tracking cadence and are not strong independent repeatability evidence, but they also do not reveal a stable resonance-shaped feature. I therefore classify this case as resonance absent.
