Case podmr_061_2026-05-17-061719

Sequence interpretation from inputs/sequence.xml:

- Sequence name in the export is Rabimodulated.xml. The active pulse sequence in the XML is the Rabi-modulated pulse path.
- The first detection immediately follows adj_polarize and is explicitly commented as the true 0 level reference. This is readout 1.
- full_expt = 0, so the conditional mS = +1 reference block is skipped. The adiabatic inversion setting is therefore not active in the acquired readouts.
- The active measurement is a single rabi_pulse_mod_wait_time call using length_rabi_pulse, mod_depth, and switch_delay, followed by detection. This is readout 2.
- length_rabi_pulse is 52 ns before rounding. With sample_rate = 250 MHz, round(52 ns * 250 MHz) / 250 MHz = 52 ns, so the effective pulse duration remains 52 ns.
- mod_depth = 1.

Physical signal model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so the relevant resonant Rabi frequency here is 10 MHz. For a resonant square pulse starting in mS = 0, the transferred population is

P_transfer = sin^2(pi * f_Rabi * tau)

Using f_Rabi = 10e6 Hz and tau = 52e-9 s:

P_transfer = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.9961.

The stated mS = 0 to mS = +1 contrast scale is about 22%, so the expected resonant fractional fluorescence drop in readout 2 relative to the readout 1 reference is

0.22 * 0.9961 = 0.2191, or about 21.9%.

The mean readout 1 level is 49.615 counts, so the expected resonant count drop is approximately

49.615 * 0.2191 = 10.87 counts.

Observed data:

- Mean readout 1 = 49.615 counts.
- Mean readout 2 = 49.086 counts.
- Mean readout 2 minus readout 1 = -0.529 counts.
- Standard deviation of pointwise readout 2 minus readout 1 = 1.723 counts.
- Largest observed fractional drop, computed as (readout 1 - readout 2) / readout 1, is 0.0753 at 3.880 GHz, corresponding to a 3.73 count drop.
- Similar sized apparent drops also occur away from that point, for example 0.0741 at 3.830 GHz and 0.0658 at 3.845 GHz.

Decision:

For the active pulse settings, a true pODMR resonance should produce an approximately 21.9% drop, about 10.9 counts on this baseline. The observed deviations are much smaller, not spectrally isolated, and comparable to scan-to-scan fluctuations. Stored averages are not treated as strong independent repeatability evidence. Based on the quantitative resonant-pulse model and the observed readout scale, I decide that a pODMR resonance is absent.
