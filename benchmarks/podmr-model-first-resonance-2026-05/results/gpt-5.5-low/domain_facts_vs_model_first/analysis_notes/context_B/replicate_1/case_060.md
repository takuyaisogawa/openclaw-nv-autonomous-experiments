Case: podmr_046_2026-05-16-235726

Active sequence and readout roles:

The active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided inputs/sequence.xml and the exported Variable_values both give length_rabi_pulse = 52 ns and mod_depth = 1. The pulse program performs a single modulated Rabi pulse followed by detection, with full_expt = 0 so the optional m_S = +1 reference block is inactive.

The first detection immediately after adj_polarize is the bright m_S = 0 reference readout. The second detection is the measurement readout after the Rabi pulse. If the microwave frequency is resonant, the pulse transfers some population from m_S = 0 to m_S = +1 and the second readout should be lower than the first readout.

Quantitative expected signal:

Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1, the active mod_depth = 1 gives f_Rabi ~= 10 MHz. For a square resonant pulse of duration t = 52 ns, the transferred population is

P = sin^2(pi f_Rabi t)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

The m_S = 0 to m_S = +1 contrast scale is about 22%, so a resonant point should reduce the post-pulse readout by approximately

0.996 * 0.22 = 0.219, or 21.9%.

The observed mean raw baseline is about 51.64 counts, so the expected resonant dip is about

51.64 * 0.219 = 11.32 raw-count units

in readout 2 relative to readout 1, before accounting for noise and drift.

Observed data:

The mean readout values are readout 1 = 52.16 and readout 2 = 51.12. The pointwise difference readout2 - readout1 has mean -1.03 and standard deviation 1.59. The largest negative difference is -4.60 at 3.860 GHz, with other smaller negative excursions spread across the scan. Even the largest excursion is far below the approximately -11.3 raw-count resonant signal expected from the active pi-like 52 ns pulse, and the excursions are not frequency-localized into a clear ODMR feature.

Decision:

The physical model says a real resonance should appear as an approximately 11 count localized reduction of the post-pulse readout relative to the bright reference. The observed differences are much smaller and not frequency-localized; the global readout2 baseline is only slightly lower than readout1 over much of the scan. With only two stored averages, and with stored averages likely reflecting tracking cadence rather than a strong repeatability test, these broad/nonlocal differences are more consistent with drift or readout normalization structure than a clear pODMR resonance. I therefore decide resonance_absent.
