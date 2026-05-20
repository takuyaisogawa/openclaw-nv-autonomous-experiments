pODMR decision note for podmr_015_2026-05-16-130043

Sequence inspection:
- The sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is the detection immediately after adj_polarize, before the microwave pulse. This is the true m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...). This is the pODMR signal readout after the microwave drive.
- mod_depth is 1.
- length_rabi_pulse is 5.2e-08 s. With sample_rate 250 MHz, the rounded duration remains 52 ns.

Pulse interpretation:
At mod_depth 1 the stated Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse. On resonance this should move population out of m_S = 0 and produce a fluorescence drop approaching the setup contrast scale of about 22 percent.

Data inspection:
The reference readout stays near 44-48 counts without a matching narrow resonance-shaped dip. The post-pulse readout shows a strong localized decrease centered near 3.875-3.880 GHz: at 3.875 GHz readout 1 is 46.21 and readout 2 is 35.87, a 22.4 percent drop relative to the reference; at 3.880 GHz the drop is 18.0 percent. This amplitude is consistent with the expected contrast for an on-resonance pi-scale pulse. The stored average traces have tracking-related offsets, so I did not treat them as a strict repeatability test, but the resonance feature is visible in the active post-pulse readout.

Decision:
The data contain a pODMR resonance.
