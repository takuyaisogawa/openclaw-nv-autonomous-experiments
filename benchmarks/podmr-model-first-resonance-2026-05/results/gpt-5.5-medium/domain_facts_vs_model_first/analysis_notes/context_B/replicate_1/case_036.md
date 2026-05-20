Analysis note for podmr_021_2026-05-16-171244

Input files used: inputs/sequence.xml and inputs/raw_export.json. No labels,
previous outputs, sibling cases, or external context were used.

Active sequence and readout roles:

- Sequence: Rabimodulated.xml.
- Scan axis: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is not
  active.
- The active detection events are therefore:
  1. after adj_polarize: readout 1, the true m_S = 0 reference;
  2. after rabi_pulse_mod_wait_time: readout 2, the driven pODMR readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already an
  integer 13 samples and remains 52 ns after rounding.

Quantitative expected-signal model:

Domain facts supplied in the prompt:

- Contrast between m_S = 0 and m_S = +1 is about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with
  mod_depth.

For a resonant square Rabi pulse, the transferred population is

P(+1) = sin^2(pi * f_Rabi * t).

Here f_Rabi = 10 MHz * mod_depth = 10 MHz and t = 52 ns, so

f_Rabi * t = 10e6 * 52e-9 = 0.52 cycles
P(+1) = sin^2(pi * 0.52) = 0.9960573507.

The expected fluorescence ratio for the driven readout on resonance is

R2/R1 = 1 - 0.22 * P(+1) = 0.7808673829.

The observed mean of readout 1 is 46.487 counts, so the expected resonant
drop is

46.487 * 0.22 * 0.9960573507 = 10.187 counts.

Thus a real on-resonance pODMR response for this pulse should be a large
negative feature in readout2 - readout1, around -10 counts, or a ratio near
0.781 at the resonant scan point.

Observed data:

- mean(readout 1) = 46.487 counts, sample sd = 1.060.
- mean(readout 2) = 46.413 counts, sample sd = 1.267.
- readout2 - readout1 has mean -0.074 counts and sample sd = 1.237.
- The most negative readout2 - readout1 point is -2.269 counts at 3.830 GHz.
- The smallest readout2/readout1 ratio is 0.9528, also far above the expected
  resonant ratio of 0.7809.

The expected resonant signal, about -10.19 counts, is roughly 4.5 times larger
than the most negative observed point and about 8.2 times the sample standard
deviation of the pointwise readout difference. No scan point approaches the
expected contrast scale.

The per-average overlays are not treated as a strong independent repeatability
test because stored averages can reflect tracking cadence. They also do not
show a stable deep readout2 dip: the two average-level readout2 - readout1
traces have different offsets and shapes, with minima of -1.73 and -4.65
counts, still well short of the expected approximately -10 count resonant
drop.

Decision:

The active pODMR measurement should produce a near-pi-pulse contrast-sized
decrease in the driven readout at resonance. The measured driven readout stays
close to the reference throughout the scan, with only small fluctuations and
no feature of the expected amplitude. I therefore decide that a pODMR
resonance is absent.
