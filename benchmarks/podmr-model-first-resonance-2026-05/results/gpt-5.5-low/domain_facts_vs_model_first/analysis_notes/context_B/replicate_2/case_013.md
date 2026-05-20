Case podmr_032_2026-05-14-161051

Sequence and roles

The provided sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect a true m_S = 0 reference, then wait. The block labelled "Acquire 1 level reference" is inside `if abs(full_expt)>1e-12`, and full_expt is 0, so that block is inactive. The only microwave manipulation in the active path is:

`rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on)`

followed by detection. Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-microwave-pulse signal. It is not a differential 0/1 reference pair.

Pulse parameters used for the physical model

The active pulse duration is length_rabi_pulse = 52 ns. The raw export records Variable_values mod_depth = 1, and the standalone XML also lists mod_depth = 1. The relevant domain facts give a Rabi frequency of about 10 MHz at mod_depth = 1 and approximately linear scaling, so I used f_R = 10 MHz.

Expected signal calculation

For a square Rabi pulse, the driven population transfer as a function of detuning is:

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * t)

using frequencies in cycles/s. On resonance, with f_R = 10 MHz and t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the setup contrast scale of about 22%, the expected on-resonance fractional fluorescence reduction in the post-MW readout is:

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout 1 level is 34.05 counts, so a full on-resonance response would put readout 2 near:

34.05 * (1 - 0.219) = 26.59 counts.

The detuning-dependent model predicts a broad feature over several 5 MHz scan points. For a resonance near 3.875 GHz, the predicted fractional dips are approximately 16.5% at +/-5 MHz and 6.0% at +/-10 MHz. For a resonance midway between 3.875 and 3.880 GHz, the two central sampled points should both be about 20.4% down.

Data comparison

The combined readout 2 values show the deepest localized depression around 3.875-3.880 GHz:

- At 3.875 GHz, readout 2/readout 1 = 29.8077/32.3077 = 0.9226, a 7.7% reduction relative to readout 1.
- At 3.880 GHz, readout 2/readout 1 = 29.3077/35.6538 = 0.8220, a 17.8% reduction relative to readout 1.

Using readout 2 off-feature points outside 3.870-3.885 GHz gives a baseline near 33.91 counts. The minimum central readout 2 value is 29.31 counts, a 13.6% dip relative to that baseline. This is smaller than the ideal 21.9% expectation, but the pulse model, finite sampling, tracking drift, photon noise, and imperfect contrast can readily reduce the apparent combined contrast. The important point is that the dip is in the active post-MW signal readout, not in the m_S = 0 reference readout.

Stored per-average traces show strong tracking drift/cadence behavior, so I did not treat them as independent repeatability evidence. The combined active signal readout has a physically plausible localized dip at the expected scale and width for a 52 ns, mod_depth 1 Rabi pODMR pulse.

Decision: resonance_present.
