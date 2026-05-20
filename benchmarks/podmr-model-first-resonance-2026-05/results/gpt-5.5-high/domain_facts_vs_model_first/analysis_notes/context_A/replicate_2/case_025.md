Case podmr_010_2026-05-16-114624.

The provided sequence XML is Rabimodulated.xml. It first polarizes and detects the true m_S = 0 level, then waits. The full_expt branch is disabled (full_expt = 0), so the optional m_S = +1 reference readout is not active. After that, the sequence applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detects again. Thus readout 1 is the bright 0-level reference/tracking readout, and readout 2 is the microwave-pulse signal readout.

With the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. A true resonance should therefore produce a large signal-readout drop approaching the known m_S = 0 to m_S = +1 contrast scale of about 22%, while the reference readout mainly tracks brightness.

The combined data show readout 2 falling from roughly 39-40 counts off resonance to about 31 counts near 3.875 GHz, a drop of about 20% relative to the local off-resonant level. This is centered where a resonant pi-like transfer would be expected in a frequency scan. Readout 1 does not show the same narrow deep minimum; it mostly reflects baseline/tracking changes. The per-average traces have substantial tracking offsets, so they are not a strong independent repeatability test, but the active signal readout contains a contrast-scale dip consistent with pODMR.

Decision: resonance present.
