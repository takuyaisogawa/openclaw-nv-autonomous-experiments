Case podmr_046_2026-05-16-235726

Sequence identification:
- Sequence name: Rabimodulated.xml.
- Active scan parameter: mw_freq, from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse sequence: polarize, detection, wait, one rabi_pulse_mod_wait_time pulse, detection, wait.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 role: true m_S = 0 bright reference immediately after optical polarization.
- Readout 2 role: signal after the microwave Rabi-modulated pulse.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 from the active variable values/provided sequence.

Physical model calculation:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_Rabi = 10 MHz.
- For a rectangular resonant pulse, transfer probability is P = sin^2(pi * f_Rabi * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With m_S = 0 to m_S = +1 contrast scale about 22%, the expected resonant fluorescence change is about -0.22 * 0.996 = -0.219, or a 21.9% drop in readout 2 relative to readout 1.
- The observed mean readout 1 level is 52.16 counts, so the expected resonant dip amplitude is about 52.16 * 0.219 = 11.43 counts.

Data comparison:
- Observed readout 1 mean/std: 52.16 / 1.40 counts.
- Observed readout 2 mean/std: 51.12 / 1.08 counts.
- Observed readout2-readout1 mean/std: -1.03 / 1.59 counts.
- Observed normalized contrast (readout2-readout1)/readout1 ranges from +1.78% to -8.60%.
- The deepest point is at 3.860 GHz with readout2-readout1 = -4.60 counts, or -8.60%.
- This is less than half of the expected -21.9% resonant response and is not a clear line-like feature at the expected model scale.
- The stored averages are only two averages and likely reflect tracking cadence; they do not provide strong independent repeatability. The per-average traces show substantial baseline drift, so the isolated dips are not persuasive evidence for a pODMR resonance.

Decision:
The active 52 ns, mod_depth 1 pulse should produce an almost full pi-pulse response and an approximately 22% dip if an addressed resonance were present. The measured scan shows only small, drifting, non-repeatable changes far below that model expectation, so I decide resonance_absent.
