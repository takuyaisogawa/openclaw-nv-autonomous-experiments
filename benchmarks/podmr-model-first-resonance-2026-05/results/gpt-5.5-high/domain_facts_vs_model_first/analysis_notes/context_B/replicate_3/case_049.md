Case podmr_035_2026-05-16-210045

I used only the files in this isolated workspace.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions acquire a polarized true m_S = 0 reference, then, because full_expt = 0, skip the explicit m_S = 1 reference block.
- Readout 1 role: optical readout after adj_polarize, the m_S = 0 reference.
- Readout 2 role: optical readout after rabi_pulse_mod_wait_time, the pODMR signal readout.
- From the provided sequence XML and exported variable values, mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already an integer 13 samples and remains 52 ns after rounding.

Quantitative signal model:
The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular driven two-level pulse, the transfer probability versus microwave detuning df is

P1(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * tau * sqrt(f_R^2 + df^2))

with f_R = 10 MHz and tau = 52 ns.

Model values:
- df = 0 MHz: P1 = 0.996, expected contrast = 0.22 * 0.996 = 21.9%, expected raw drop at a 50-count baseline = 10.96 counts.
- df = 5 MHz: P1 = 0.749, expected contrast = 16.5%, expected raw drop = 8.24 counts.
- df = 10 MHz: P1 = 0.273, expected contrast = 6.0%, expected raw drop = 3.00 counts.
- df = 15 MHz: P1 = 0.012, expected contrast = 0.3%, expected raw drop = 0.13 counts.

Because the scan step is 5 MHz, a resonance within the scanned interval should place at least one measured point within about 2.5 MHz of the resonance center, giving nearly the full expected 22% contrast, roughly a 10-count decrease of readout 2 relative to the m_S = 0 reference. Even a point 5 MHz away should show an about 8-count effect.

Observed data:
- Readout 1 mean = 50.94 counts.
- Readout 2 mean = 50.08 counts.
- Difference readout1 - readout2 has mean = 0.85 counts, standard deviation = 1.06 counts, minimum = -1.06 counts, maximum = 2.81 counts.
- Normalized difference has maximum = 5.65%, far below the expected 21.9% near resonance.
- The largest positive differences are isolated at 3.830 GHz, 3.865 GHz, and the high-frequency edge, not a single Rabi-response lobe with adjacent points showing the expected 5 MHz and 10 MHz detuning behavior.
- Stored per-average traces are not a strong repeatability test here, but their largest differences occur at different frequencies, consistent with tracking/noise rather than a stable resonance.

I also fitted the expected Rabi lineshape P1(df) plus a constant baseline to readout1 - readout2 while allowing the center to vary across the scan. The best unconstrained fit used a negative amplitude, meaning the observed structure is opposite in sign to the expected resonant population-transfer drop. A positive-amplitude resonance with the expected approximately 11-count scale is not present.

Decision:
No pODMR resonance is present in this scan.
