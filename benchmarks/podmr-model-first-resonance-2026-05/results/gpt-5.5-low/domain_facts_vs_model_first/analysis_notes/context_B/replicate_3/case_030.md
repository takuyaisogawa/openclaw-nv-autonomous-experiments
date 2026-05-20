Case podmr_015_2026-05-16-130043

Sequence identification:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed branch has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout roles: the first detection is immediately after optical polarization and is the true m_S = 0 reference. The second detection is after the Rabi-modulated microwave pulse and is the pODMR signal readout.
- Pulse parameters from the provided XML / variable values: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The pulse length is already quantized to 13 samples.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1 is about 10 MHz, use f_R = 10 MHz.
- For a resonant square pulse, population transfer is P = sin^2(pi * f_R * t).
- With t = 52 ns, f_R * t = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- With m_S = 0 to m_S = +1 contrast scale about 22%, the expected fractional fluorescence loss on resonance is 0.22 * 0.996 = 0.219, or about 21.9% of the signal baseline.
- The signal readout baseline, using the median excluding the central dip neighborhood, is about 44.65 counts. The expected resonant drop is therefore 0.219 * 44.65 = 9.79 counts.

Observed data:
- The second readout has a minimum at 3.875 GHz: 35.87 counts.
- Relative to the same baseline estimate of 44.65 counts, the observed drop is 8.79 counts, or 19.7%.
- The first readout at the same frequency is 46.21 counts versus a median reference baseline of 45.80 counts, so the reference does not show a matching dip.
- A square-pulse detuning model centered at 3.875 GHz gives expected drops of about 7.36 counts at +/-5 MHz and 2.68 counts at +/-10 MHz, consistent with a narrow microwave-driven feature at the observed dip, within the noise and averaging cadence.

Decision:
The observed signal-channel dip magnitude is close to the expected 52 ns resonant Rabi-pulse contrast, and the reference readout is not responsible for the feature. This is a pODMR resonance.
