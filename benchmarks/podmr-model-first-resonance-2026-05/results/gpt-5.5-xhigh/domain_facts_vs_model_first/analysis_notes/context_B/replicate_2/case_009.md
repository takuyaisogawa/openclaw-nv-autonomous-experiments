Case: podmr_016_2026-05-12-120649

Sequence interpretation

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect the bright mS=0 state, so readout 1 is the local mS=0 reference. Because full_expt = 0, the optional mS=1 reference block is skipped. The only microwave operation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so readout 2 is the post-Rabi-pulse readout.

The active pulse parameters from inputs/sequence.xml are:

- sample_rate = 250 MHz, so the 52 ns pulse is exactly 13 samples and remains 52 ns after rounding.
- mod_depth = 1.
- The setup Rabi frequency is therefore about 10 MHz.

Quantitative model

I modeled the pulse as a driven two-level transition starting in mS=0. For a rectangular pulse with Rabi frequency fR and detuning delta, the transferred population is

P1(delta) = fR^2 / (fR^2 + delta^2) * sin^2(pi * tau * sqrt(fR^2 + delta^2)).

With fR = 10 MHz and tau = 52 ns, the on-resonance transfer is

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996057.

Using the stated 22% mS=0 to mS=+1 contrast scale, the expected resonant fractional darkening of readout 2 relative to readout 1 is

0.22 * 0.996057 = 0.219133, or 21.9%.

The mean readout 1 level is 25.7335 counts, so the expected resonant count drop is about

25.7335 * 0.219133 = 5.639 counts.

Because the frequency grid spacing is 5 MHz, any resonance inside the scan range should be sampled within 2.5 MHz of a measured point. Scanning the possible resonance center across the whole 3.825-3.925 GHz range with the same two-level model gives a minimum possible maximum sampled contrast of 0.204421, still about 20.4%.

Measured comparison

Using the local reference contrast c = (readout1 - readout2) / readout1 from the combined data:

- mean c = -0.017098
- standard deviation across scan points = 0.039505
- maximum observed positive darkening = 0.053263, or 5.3%
- maximum observed count drop = 1.365 counts

The largest measured darkening is therefore only about one quarter of the minimum expected sampled resonant darkening and far below the expected 5.6 count drop. The per-average traces are dominated by tracking-level changes, as expected, and do not show a repeatable approximately 20% pulse-induced dip.

Decision

Under the active mod_depth = 1, 52 ns pulse, a real pODMR resonance in the scanned range should produce a large near-pi-pulse darkening. The measured normalized readout difference is small, inconsistent, and much weaker than the physical expectation. I therefore classify this case as resonance_absent.
