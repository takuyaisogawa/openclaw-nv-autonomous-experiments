Case: podmr_070_2026-05-17-082720

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML performs an initial adj_polarize laser pulse followed by detection; this is the true mS = 0 reference readout.
- full_expt = 0, so the optional mS = +1 reference block is inactive.
- The active microwave operation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- Therefore readout 1 is the mS = 0 reference and readout 2 is the post-microwave pODMR signal.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is exactly 13 samples, so rounding leaves it at 52 ns.
- mod_depth = 1 in the provided XML and in the exported variable values.

Expected signal model:
Use a driven two-level rectangular-pulse model for the mS = 0 to mS = +1 transition. The given setup has Rabi frequency about 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so here f_R = 10 MHz. For a pulse duration t = 52 ns, the on-resonance transferred population is:

P1(0) = sin^2(pi * f_R * t)
      = sin^2(pi * 10e6 * 52e-9)
      = 0.996.

The contrast scale between mS = 0 and mS = +1 is about 22%, so an on-resonance pODMR feature should produce a relative readout drop of:

0.22 * 0.996 = 0.219, or about 21.9%.

The mean reference readout is 50.71 counts, so the expected on-resonance count drop is:

50.71 * 0.219 = 11.11 counts.

Even if the resonance lies halfway between two 5 MHz scan points, the rectangular-pulse detuned model,

P1(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

still gives a large expected feature at delta = 2.5 MHz:

P1(2.5 MHz) is about 0.93, corresponding to about 20% contrast and about a 10 count drop.

Measured data:
- readout 1 mean = 50.71, standard deviation across scan points = 1.35.
- readout 2 mean = 50.23, standard deviation across scan points = 1.69.
- readout2 - readout1 mean = -0.48 counts.
- The largest measured reference-normalized dip, 1 - readout2/readout1, is 3.87% at 3.885 GHz, corresponding to only 1.96 counts.
- The per-average contrast scatter is about 3.58%, and the two stored averages mainly indicate tracking cadence rather than a strong repeatability test.

Decision:
The active pulse should create an approximately 22% dip if a pODMR resonance is in the scanned range, with a feature still near 20% even for half-step detuning. The observed dips are at most 3.9%, have no large near-pi-pulse response, and are comparable to the measured scatter and slow baseline drift. Therefore the pODMR resonance is absent in this scan.
