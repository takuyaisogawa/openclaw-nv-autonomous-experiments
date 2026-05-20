Case: podmr_060_2026-05-17-060259

Input restrictions followed: I used only inputs/sequence.xml and inputs/raw_export.json from this isolated workspace, plus the provided domain facts.

Active sequence and readout roles:
- SequenceName in the raw export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed variable values in raw_export.json are the relevant run settings: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz, pumping_time = 1 us, delay_wrt_1mus = 0.2 us.
- The standalone sequence.xml default lists mod_depth = 1 and length_rabi_pulse = 52 ns; the embedded sequence text shows an older/default value mod_depth = 0.3, but the exported Variable_values for this run explicitly record mod_depth = 1, so I use mod_depth = 1 for the decision.
- Because full_expt = 0, the conditional mS=+1 reference block is skipped. The active sequence first polarizes and detects the true mS=0 reference, then applies one modulated Rabi pulse and detects the signal. Thus readout 1 is the mS=0 reference and readout 2 is the post-pulse pODMR signal.

Quantitative physical model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling, f_R = 10 MHz here.
- For a resonant square Rabi pulse of duration t = 52 ns, the transferred population is P = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With mS=0 to mS=+1 optical contrast scale about 22%, the expected on-resonance fractional depletion of the post-pulse readout relative to the mS=0 reference is 0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout 1 level is 50.94 counts, so the expected resonant readout drop is about 50.94 * 0.219 = 11.16 counts. A resonant point should therefore look like readout 2 near 39.8 counts if readout 1 is near 50.9, up to normal noise and calibration imperfections.

Observed data calculation:
- Mean readout 1 = 50.94 counts; mean readout 2 = 50.20 counts.
- Mean difference readout2 - readout1 = -0.75 counts; standard deviation across scan points = 1.51 counts.
- The largest observed depletion is at 3.875 GHz: readout 1 = 52.50, readout 2 = 48.87, difference = -3.63 counts, fractional depletion = 6.92%.
- The maximum absolute fractional role contrast across all scan points is about 6.9%, far below the modeled 21.9% depletion expected for a real resonance with this near-pi pulse.
- Stored averages are only two averages and may mainly reflect tracking cadence, so I do not treat their overlay as an independent repeatability test. Still, the per-average difference standard deviation is about 1.97 counts, and no point approaches the roughly 11-count expected resonant drop.

Decision:
The active pulse is effectively a pi pulse at the stated setup calibration, so a pODMR resonance in the scanned window should create a large readout-2 depletion relative to readout 1. The observed trace has only small count-scale fluctuations and no feature with the expected amplitude. I decide resonance_absent.
