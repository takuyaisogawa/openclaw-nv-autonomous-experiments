Case: podmr_007_2026-05-16-013306

I used only the provided sequence XML and raw export data in this workspace.

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout 1 is the detection immediately after optical polarization, i.e. the bright mS = 0 reference.
- Readout 2 is the detection after the scanned microwave Rabi pulse.
- Therefore a pODMR resonance should appear as a dip in readout 2 relative to readout 1, not as a symmetric feature in both readouts.

Pulse parameters from sequence XML:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s, which remains 52 ns.
- The relevant pulse is PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).

Quantitative expected-signal model:
- Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1.
- For a resonant square Rabi pulse, the transferred population is modeled as P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The optical contrast scale between mS = 0 and mS = +1 is about 22%, so the expected fractional fluorescence drop on resonance is:
  0.22 * 0.996 = 0.219, or 21.9%.
- The mean readout 1 level is 35.99 counts, so the expected resonant readout 2 level is:
  35.99 * (1 - 0.219) = 28.10 counts.

Observed data comparison:
- The strongest readout 2 dip is at 3.880 GHz, where readout 1 = 36.90 and readout 2 = 28.21.
- The fractional drop at that point is (36.90 - 28.21) / 36.90 = 23.6%, close to the 21.9% model expectation.
- Excluding the central trough points, the off-resonant readout 2 mean is 35.27 with point-to-point standard deviation 1.36; the 28.21 minimum is about 5.2 such standard deviations below that off-resonant level.
- The per-average traces both show a local readout 2 depression around the same central frequency, but I treat stored averages mainly as tracking-cadence context rather than a strong independent repeatability test.

Decision:
The dip magnitude, location, and readout role are quantitatively consistent with the expected near-pi-pulse pODMR response. A pODMR resonance is present.
