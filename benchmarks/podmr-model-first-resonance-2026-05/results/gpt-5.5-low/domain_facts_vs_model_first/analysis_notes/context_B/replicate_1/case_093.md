Case podmr_079_2026-05-17-103702

Sequence interpretation from inputs/sequence.xml:
- Active sequence file/name: Rabimodulated.xml / Rabi-modulated pODMR scan.
- Scan parameter: mw_freq over 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- The active detections are:
  1. After adj_polarize: true mS = 0 reference readout.
  2. After rabi_pulse_mod_wait_time: pODMR signal readout after the microwave pulse.
- mod_depth = 1.
- active Rabi pulse duration length_rabi_pulse = 52 ns, rounded at 250 MS/s. Since 52 ns is exactly 13 samples, no rounding change is expected.

Quantitative physical expectation:
- Given setup Rabi frequency approximately 10 MHz at mod_depth = 1.
- For a resonant rectangular Rabi pulse, transferred population is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between mS = 0 and mS = +1 is about 22%.
- The observed mS = 0 reference baseline is about 50.72 raw counts.
- Expected on-resonance fluorescence change is therefore approximately:
  50.72 * 0.22 * 0.996 = 11.11 raw counts.
- Thus a real resonance under this pulse should produce an order-10-count dip in the post-pulse signal relative to the mS = 0 reference, centered at the resonant drive frequency, up to normal linewidth and sampling effects.

Observed data check:
- Combined readout 1 mean = 50.72 counts; readout 2 mean = 50.78 counts.
- Difference readout2 - readout1 has mean +0.064 counts, standard deviation 1.29 counts.
- The most negative observed difference is -2.10 counts, only about 19% of the expected resonant drop.
- Differences alternate sign across the scan, with no coherent resonance-like dip. The apparent point-to-point excursions are comparable to tracking/average scatter and are not repeatable evidence from the two stored averages.

Decision:
The expected resonant response for the active pulse sequence is much larger than the observed changes. Since the measured data do not show the required large, localized post-pulse fluorescence reduction, I decide that a pODMR resonance is absent.
