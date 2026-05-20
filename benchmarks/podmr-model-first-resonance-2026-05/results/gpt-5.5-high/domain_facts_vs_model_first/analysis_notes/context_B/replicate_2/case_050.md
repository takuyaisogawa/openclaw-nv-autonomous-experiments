Case podmr_036_2026-05-16-211536

I used only the supplied XML and raw export. The active sequence is Rabimodulated.xml. With full_expt = 0, the sequence performs adj_polarize, then a first detection that serves as the polarized m_S = 0 reference, then a single modulated Rabi pulse, then a final detection. The optional m_S = +1 reference block is inactive. Thus readout 1 is the m_S = 0 reference and readout 2 is the post-pulse signal. The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns, rounded at 250 MS/s to the same 52 ns.

Physical model calculation:

For a rectangular Rabi pulse, using cyclic frequencies,

P(+1) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * tau)

The setup facts give f_R about 10 MHz at mod_depth = 1. With tau = 52 ns:

- On resonance: P = 0.996, so the expected optical readout ratio is 1 - 0.22 * P = 0.781.
- At 2.5 MHz detuning, the worst case for a resonance halfway between 5 MHz scan points: P = 0.929, expected ratio = 0.796.
- At 5 MHz detuning: P = 0.749, expected ratio = 0.835.
- At 10 MHz detuning: P = 0.273, expected ratio = 0.940.

The observed combined readouts have mean readout 1 = 50.99 and mean readout 2 = 50.48. The observed readout2/readout1 ratio ranges from 0.946 to 1.070, with mean 0.990. The deepest observed deficit is at 3.920 GHz: readout 1 = 51.69, readout 2 = 48.90, ratio = 0.946, a drop of 2.79 counts. A true on-grid resonance should have produced about 11.17 counts of drop from the measured reference level, and even a resonance centered halfway between adjacent scan points should still have produced about 10.42 counts of drop.

I also scanned resonance-center hypotheses across the measured frequency range using the fixed 22% contrast model and the measured readout 1 as the local baseline. The best fixed-contrast resonance model still requires a minimum ratio of about 0.781 somewhere in the scan, far below the observed minimum ratio of 0.946. If the contrast amplitude is allowed to float, the best fit contrast is only about 0.050, much smaller than the expected 0.22 for this setup and pulse.

The stored two averages do not provide a strong independent repeatability test, and the per-average overlays are consistent with tracking or baseline variation. The combined trace lacks the large, physically expected post-pulse darkening. I therefore decide that a pODMR resonance is absent.
