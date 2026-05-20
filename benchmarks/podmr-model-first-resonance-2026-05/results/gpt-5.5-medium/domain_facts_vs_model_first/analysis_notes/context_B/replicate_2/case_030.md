Case: podmr_015_2026-05-16-130043

Sequence identification:
- Active sequence file: Rabimodulated.xml.
- The sequence first performs adj_polarize, then detection, then wait_for_awg. This first detection is the bright m_S = 0 reference readout.
- The "Acquire 1 level reference" block is inactive because full_expt = 0, so there is no separate dark-reference readout in the active sequence.
- The active experiment readout is after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- From inputs/sequence.xml, length_rabi_pulse = 5.2e-08 s and mod_depth = 1. The pulse duration is rounded at 250 MS/s, but 52 ns is already 13 samples.

Quantitative model:
- Given setup Rabi frequency approximately 10 MHz at mod_depth = 1 and linear scaling with mod_depth, f_Rabi = 10 MHz.
- For a resonant square Rabi pulse, transfer probability from m_S = 0 to m_S = +1 is P = sin^2(theta/2), theta = 2*pi*f_Rabi*t.
- With t = 52 ns, theta = 2*pi*10e6*52e-9 = 3.267 rad, so P = sin^2(1.6336) = 0.996.
- With optical contrast scale 22%, an on-resonance point should reduce the second readout by about 0.22*0.996 = 21.9% relative to the bright level.

Observed data check:
- The first readout is the bright reference and stays around 44 to 48 counts.
- The second readout has a sharp minimum at scan value 3.875e9 Hz: readout 1 = 46.2115, readout 2 = 35.8654.
- The same-point fractional drop is (46.2115 - 35.8654) / 46.2115 = 0.2239, matching the expected 21.9% resonant contrast.
- Using off-dip readout-2 baseline from the first and last five scan points gives 44.6154 counts. The expected resonant minimum is 44.6154*(1 - 0.22*0.996) = 34.84 counts, close to the observed 35.87 counts.
- The stored per-average difference gives an approximate combined-point scatter scale near 1.98 counts, while the dip depth from the off-dip baseline is 8.75 counts, about 4.4 sigma. The two stored averages are not a strong independent repeatability test because averages can reflect tracking cadence, but both show the same broad depression near the center.

Decision:
The resonance is present. The active pulse is effectively a pi pulse at the stated contrast scale, and the observed central dip has the expected magnitude and location within the swept microwave frequency range.
