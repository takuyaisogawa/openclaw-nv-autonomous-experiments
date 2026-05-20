Sequence review:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the "Acquire 1 level reference" branch is inactive. The two active detections are the initial polarized mS=0 bright reference and the post-Rabi-pulse signal readout.
- The provided sequence has mod_depth = 1 and length_rabi_pulse = 52 ns. At the stated setup calibration, this is close to a pi pulse because the Rabi frequency is about 10 MHz at mod_depth 1.

Data interpretation:
The combined normalized contrast (readout 1 - readout 2) / readout 1 has a localized maximum at 3.845 GHz: readout 1 is about 48.23 and readout 2 is about 43.94, giving roughly 8.9% contrast. Adjacent points are weaker, but the scan contains a distinct post-pulse fluorescence dip relative to the bright reference at that frequency. The two stored averages sit on different brightness baselines, consistent with tracking cadence, so I do not treat them as a strong independent repeatability test. Even so, the relevant comparison is within each scan point between the bright reference and the post-pulse signal.

Decision:
A pODMR resonance is present. The observed contrast is below the full 22% mS=0 to mS=+1 scale expected for ideal inversion, but it is a localized normalized dip in the correct readout under a near-pi pulse rather than a label-only or average-baseline artifact.
