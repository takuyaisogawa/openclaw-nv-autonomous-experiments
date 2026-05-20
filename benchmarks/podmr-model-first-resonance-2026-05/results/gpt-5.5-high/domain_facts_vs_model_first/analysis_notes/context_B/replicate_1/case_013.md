Case: podmr_032_2026-05-14-161051

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The active sequence is Rabimodulated.xml. The instructions first polarize the NV and immediately call detection, so readout 1 is the bright m_S=0 reference. The block labelled "Acquire 1 level reference" is conditional on full_expt, but full_expt = 0, so it is skipped. The remaining active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

followed by detection. Therefore readout 2 is the microwave-pulsed pODMR signal. The relevant pulse parameters from the provided sequence are mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so the sequence rounding keeps the pulse at round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns.

Expected signal model

Use a square-pulse two-level Rabi model for the addressed m_S=0 to m_S=+1 transition. The stated setup gives f_R = 10 MHz at mod_depth = 1, approximately linear in mod_depth, so here f_R = 10 MHz. For detuning delta f, the transition probability is:

P(delta f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2*pi*10 MHz, Delta = 2*pi*delta f, and t = 52 ns. On resonance this reduces to:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.

The current setup contrast scale between m_S=0 and m_S=+1 is about 22%, so an on-resonance pi-like pulse should reduce the post-pulse readout relative to the m_S=0 reference by:

0.22 * 0.996 = 0.219, or about 21.9%.

Data comparison

I compared readout 2 to readout 1 at each frequency, using ratio = readout2 / readout1 and deficit = 1 - ratio. The largest deficit is at 3.880 GHz:

- 3.875 GHz: readout1 = 32.31, readout2 = 29.81, ratio = 0.923, deficit = 7.7%
- 3.880 GHz: readout1 = 35.65, readout2 = 29.31, ratio = 0.822, deficit = 17.8%
- 3.885 GHz: readout1 = 33.62, readout2 = 34.31, ratio = 1.021, deficit = -2.1%

The off-feature ratios have median near 1.0. Excluding the two lowest points at 3.875 and 3.880 GHz, the mean ratio is 0.994 and the median is 0.997. Thus the 3.880 GHz point is about 17.2 percentage points below the off-feature median, close to the 21.9 percentage point deficit expected from the physical model. In raw counts, readout 1 is not low at 3.880 GHz; the deficit is specific to the microwave-pulsed readout 2.

I also checked the stored per-average traces, but the two averages are dominated by opposite tracking-like drifts, so I did not treat them as a strong independent repeatability test.

Decision

A pODMR resonance is present. The evidence is a pulsed-readout-only dip near 3.880 GHz with normalized depth close to the expected pi-pulse contrast scale for mod_depth = 1 and 52 ns.
