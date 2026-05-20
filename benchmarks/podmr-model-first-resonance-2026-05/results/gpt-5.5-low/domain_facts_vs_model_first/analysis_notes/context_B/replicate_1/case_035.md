Case podmr_020_2026-05-16-165809

Input sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Executed readout roles: the first detection follows laser polarization and is the true mS=0 reference. full_expt = 0, so the explicit mS=+1 reference block is skipped. The second detection follows the modulated Rabi microwave pulse and is the pODMR signal readout.
- mod_depth: 1 from the provided sequence/variable values.
- Rabi pulse duration: length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already on a 4 ns sample grid.

Physical model calculation before deciding:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and approximately linear scaling, the expected resonant Rabi frequency here is 10 MHz.
- For a square resonant pulse, transferred population P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10e6 Hz and t = 52e-9 s:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of about 22%, the expected resonant signal in readout 2 relative to readout 1 is a fractional drop of about 0.22 * 0.996 = 0.219, so readout2/readout1 should be near 0.781 at resonance, aside from noise and drift.

Observed data check:
- Combined readout2/readout1 ratios over the scan range span only 0.929 to 1.040.
- The largest negative point is at the low-frequency scan edge, not a localized interior resonance.
- Around the most plausible interior structure near 3.89 GHz, the ratio is about 0.949, corresponding to only about a 5.1% drop, far smaller than the expected approximately 21.9% resonant contrast for this pulse.
- The two stored averages show strong opposing slow trends, consistent with tracking cadence/drift rather than an independent repeatability test for a narrow resonance.

Decision:
The pulse should be nearly a pi pulse if the drive is resonant, so a true pODMR resonance should produce a large localized readout2 suppression relative to the mS=0 reference. The observed signal lacks that expected magnitude and localization. I therefore decide resonance_absent.
