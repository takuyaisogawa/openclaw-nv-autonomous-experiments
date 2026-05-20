Case: podmr_043_2026-05-16-231159

Only the local inputs were used.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true.
- Readout 1 is the true m_S = 0 reference: adj_polarize for 1 us, then detection, then a 2 us wait.
- Readout 2 is the MW-pulse readout: rabi_pulse_mod_wait_time followed by detection, then a 1 us final wait.
- mod_depth = 1.
- length_rabi_pulse = 52 ns after rounding at the 250 MHz sample rate.

Physical expectation:
At mod_depth = 1, the setup Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse on resonance. With a stated m_S = 0 to m_S = +1 contrast scale of about 22%, a real resonance should produce a clear reduction of the MW-pulse readout relative to the 0-reference near the resonant frequency.

Observed behavior:
The combined readouts do not show a coherent resonance dip. The MW-pulse readout is on average slightly higher than the 0-reference, with mean relative difference about +0.95%. The largest negative relative point is only about -2.43%, while positive excursions reach about +4.06%. The per-average traces vary at the same percent-level scale and do not provide a strong independent repeatability check because stored averages can track cadence effects.

Decision:
No pODMR resonance is present in this scan.
