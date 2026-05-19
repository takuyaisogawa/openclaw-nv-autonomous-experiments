<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_079

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml / 1DExp-seq-Rabimodulated-vary-mw_freq. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout roles:

- The first detection occurs immediately after adj_polarize, so readout 1 is the true m_S = 0 bright reference.
- full_expt = 0, so the intermediate "Acquire 1 level reference" block is inactive. do_adiabatic_inversion is therefore not used in the actual pulse train.
- The active experiment pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 2 is the post-microwave pODMR signal readout.

Physical model calculation:

- Given Rabi frequency approximately 10 MHz at mod_depth = 1, the driven rotation angle for a 52 ns pulse is theta = 2*pi*(10 MHz)*(52 ns) = 3.267 rad = 187.2 deg.
- The resonant transition probability for a rectangular pulse is sin^2(theta/2) = 0.996.
- With the setup m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fluorescence drop in readout 2 relative to the m_S = 0 reference is 0.22*0.996 = 0.219, so the expected on-resonance readout2/readout1 ratio is about 0.781.

Observed combined data:

- Mean readout1 = 47.478, mean readout2 = 47.207, mean readout2/readout1 = 0.994.
- The minimum combined readout2/readout1 ratio is 0.952 at 3.830 GHz, a 4.77% drop from readout 1.
- Other low ratios are similarly small and not close to the approximately 22% drop expected for the active near-pi pulse on resonance.
- The per-average traces show substantial baseline/tracking offsets between averages, so the stored averages are not treated as independent repeatability evidence.

Decision:

The active pulse should produce a large pODMR contrast if a resonance is present in the scanned band. The observed normalized signal never approaches the modeled on-resonance drop and lacks a localized feature on the expected scale. I therefore classify this case as resonance_absent.
