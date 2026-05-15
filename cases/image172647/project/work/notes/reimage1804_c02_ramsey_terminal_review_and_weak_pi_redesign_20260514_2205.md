# reimage1804_c02 Ramsey terminal review and weak-pi redesign

Created: 2026-05-14T22:05 EDT

## Terminal Ramsey result

Bridge job `nv23_ramsey_20260514_201034_auto_ramsey` completed at 2026-05-14 21:45:59 EDT with saved data `1DExp-seq-ramsey-vary-tau-2026-05-14-201247.mat`. Counts were healthy: pre-run TrackCenter final 43.710 kcps and post-run final 41.020 kcps. There was no stop request, monitor error, or safety abort.

Raw export verified `ramsey.xml`, 43 tau points over 0..8 us, `det=1.5 MHz`, `mw_freq=3.876461010 GHz`, 8 averages x 50000 reps, and snake scan order. Scan-order-aware drift analysis used `Scan.ScanOrderEachAvg` and found no flagged averages.

## Readout-aware interpretation

Signal readout/self-baseline and fitted-reference-normalized views both show a weak empirical Ramsey oscillation near 1.9 MHz. In the readout2 self-baseline FFT, target-bin amplitudes were:

- direct 13C Larmor bin near 0.366 MHz: 1.39%
- det - 13C bin near 1.099 MHz: 0.79%
- nominal det carrier bin near 1.465 MHz: 0.45%
- det + 13C bin near 1.831 MHz: 1.95%

Free-frequency exponential fits prefer about 1.92-1.95 MHz. The fitted T2* is about 1.47 us if tau=0 is included and about 2.4 us if the first one or two tau points are excluded; excluding more early points or shortening the fit window makes the scalar still less stable. This supports a short/few-us T2* order, but not a final scalar T2*.

The 13C conclusion is not established. The high-frequency power near the nominal det+13C sideband is ambiguous with an effective Ramsey carrier shifted by about +0.4 MHz from the broad strong-pi pODMR center, while the nominal carrier and det-13C sideband are weak. Do not claim 13C from this isolated/ambiguous FFT feature.

## Redesign decision

Do not blindly accumulate more Ramsey averages using the broad strong-pi center. First refine the electron resonance with bounded weak-pi pulsed ODMR. This directly tests whether the ~+0.4 MHz Ramsey carrier shift is due to resonance-center error and will make the next Ramsey/13C design less ambiguous.

Proposed next experiment if gates pass:

- sequence: `pulsed_odmr_rabimodulated_v1` / `Rabimodulated.xml`
- purpose: weak-pi pODMR resonance refinement for accepted aligned branch `reimage1804_c02`
- scan: `mw_freq = 3.873461010..3.879461010 GHz`, 31 points (~200 kHz spacing)
- pulse: `length_rabi_pulse = 1 us`, `mod_depth = 0.05`
- MW/IQ: keep same strong-pi-compatible settings unless advisory blocks (`mw_ampl=-5`, `ampIQ=5`, `freqIQ=50 MHz`, `switch_delay=100 ns`, `full_expt=0`, `detuning=0`)
- acquisition: 4 averages x 50000 reps, even averages, no average-continuously
- target seed: current c02/NV23 position with auto-align and minimum final 8 kcps
- analysis: no automatic bridge fit; terminal raw export, readout-aware center review, then redesign Ramsey with a carrier separated from expected 13C sidebands.

Expected-signal calculation: the current calibrated weak-pi operating point is `length_rabi_pulse=1 us`, `mod_depth=0.05`. The +/-3 MHz scan covers the strong-pi center uncertainty (~0.69 MHz) and the Ramsey-inferred shift (~0.4 MHz). A conservative 5% resonance dip would be ~22x the binomial floor for 200k total shots (`1/sqrt(200000) = 0.224%`) and the 200 kHz spacing gives several samples across a ~0.8-1 MHz weak-pi feature. If the advisory estimates an excessive tracking window, reduce repetitions per average before changing the resonance-refinement purpose.

Artifacts:

- summary: `work/artifacts/analysis/reimage1804_c02_ramsey_terminal_8avg_summary_20260514_2150.json`
- figure: `work/artifacts/figures/reimage1804_c02_ramsey_terminal_8avg_20260514_2150.png`
- drift: `work/artifacts/analysis/reimage1804_c02_ramsey_terminal_8avg_drift_20260514_2150.json`
