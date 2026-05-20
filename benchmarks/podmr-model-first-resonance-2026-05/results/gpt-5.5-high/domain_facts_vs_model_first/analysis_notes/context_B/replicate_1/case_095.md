Case: podmr_081_2026-05-17-110558

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation

- Sequence name: Rabimodulated.xml.
- Scanned variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active MW pulse after the bright reference: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the sequence rounds this to round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- mod_depth = 1 from the provided sequence XML and exported active variable values.
- full_expt = 0, so the optional intermediate 1-level reference block is skipped.
- Readout roles: readout 1 is the bright m_s = 0 reference acquired immediately after optical polarization and before the MW pulse. readout 2 is the signal readout after the 52 ns modulated MW pulse.

Physical model calculation

Given the stated setup calibration, the Rabi frequency at mod_depth = 1 is approximately f_R = 10 MHz. For a rectangular resonant pulse, the transferred population is

P_1(Delta=0) = sin^2(pi f_R t)

with t = 52 ns. Numerically:

pi f_R t = pi * 10e6 * 52e-9 = 1.6336 rad
P_1(0) = sin^2(1.6336) = 0.996

The current m_s = 0 to m_s = +1 contrast scale is about 22 percent, so a true on-resonance pODMR response should reduce the post-pulse signal readout by approximately

0.22 * bright_reference_mean * P_1(0).

The mean bright reference readout from readout 1 is 47.3388 counts, giving an expected on-resonance dip of

0.22 * 47.3388 * 0.996 = 10.37 counts.

Including detuning, I used the standard driven two-level rectangular-pulse expression

P_1(Delta) = Omega^2 / (Omega^2 + delta^2) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * t),

where Omega = 2*pi*10 MHz and delta = 2*pi*(f - f0). At the nominal scan endpoint f0 = 3.925 GHz, this predicts transfer probabilities of 0.749 at 3.920 GHz and 0.996 at 3.925 GHz, corresponding to expected dips of about 7.80 and 10.37 counts.

Observed readout comparison

Across the 21 scan points:

- mean readout 1 = 47.3388 counts
- mean readout 2 = 47.0971 counts
- mean readout 2 / readout 1 = 0.9952
- readout 2 - readout 1 ranges from -2.1538 to +1.6923 counts
- at 3.925 GHz, readout 2 - readout 1 = -0.4038 counts

The largest observed deficit of the post-pulse signal relative to the bright reference is only 2.15 counts, about 21 percent of the 10.37-count on-resonance model expectation. At the nominal resonance endpoint, the observed deficit is only 0.40 counts, about 4 percent of expectation. The expected pODMR feature is therefore not present in the active signal readout. The two stored averages are separated by an overall tracking-related offset and are not treated as a strong independent repeatability test.

Decision: resonance absent.
