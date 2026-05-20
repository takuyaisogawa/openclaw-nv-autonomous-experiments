Case: podmr_059_2026-05-17-054846

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, sibling cases, prior outputs, or external context.

Active sequence and readout roles:
- SequenceName in the export is Rabimodulated.xml.
- The sequence first runs adj_polarize followed by detection, then wait_for_awg. This is the bright m_S = 0 reference readout, corresponding to readout 1.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) and detects again. This is the post-pulse pODMR signal readout, corresponding to readout 2.

Active pulse parameters from the provided XML/export variable values:
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- scan range = 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model:
For a square resonant microwave pulse starting in m_S = 0, the transferred population is

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * T * sqrt(f_R^2 + delta^2)),

using f_R in cycles/s and detuning delta in Hz. The setup gives f_R about 10 MHz at mod_depth = 1, and the pulse duration is T = 52 ns. On resonance:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated bright-to-dark contrast scale of about 22%, the expected resonant optical drop is

0.22 * 0.996 = 0.219, or 21.9% of the bright readout.

The mean readout 1 value is 42.67, so the expected resonant drop in raw readout units is about

42.67 * 0.219 = 9.35 units,

which would place readout 2 near 33.3 at a sampled resonance. With a 5 MHz scan step and a 10 MHz Rabi frequency, even a resonance midway between adjacent scan points would still produce a large response, not a narrow feature that can be missed entirely.

Observed data:
- Mean readout 1 = 42.67.
- Mean readout 2 = 42.11.
- Mean normalized drop 1 - readout2/readout1 = 1.28%.
- Largest normalized drop = 6.43% at 3.880 GHz.
- The full observed normalized contrast range is about -3.62% to +6.43%, with standard deviation 2.54%.

I also fit the two-level square-pulse response shape over possible line centers using the observed normalized drop. For f_R = 10 MHz and T = 52 ns, the best center was 3.875 GHz with a fitted optical contrast amplitude of about 4.98%, whereas the setup model expects about 22%. The fitted/observed amplitude is therefore only about 23% of the expected resonant signal. The largest raw drop, 2.87 units, is also only about 31% of the expected 9.35-unit drop.

Decision:
The post-pulse readout does not show the large, broad, near-pi-pulse optical drop required by the active mod_depth = 1, 52 ns Rabimodulated sequence. The small few-percent fluctuations are well below the expected 21.9% resonant signal and are not sufficient evidence for a pODMR resonance.
