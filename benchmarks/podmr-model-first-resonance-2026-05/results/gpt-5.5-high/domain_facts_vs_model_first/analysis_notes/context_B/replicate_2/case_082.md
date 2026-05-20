Active sequence and readout roles:

- The provided XML is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true.
- The first detection is after optical polarization only, so readout 1 is the same-cycle m_S = 0 optical reference.
- The active microwave manipulation is PSeq = rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...), followed by detection, so readout 2 is the pODMR signal readout after the microwave pulse.
- length_rabi_pulse = 52 ns. sample_rate = 250 MHz gives 13 samples, so rounding leaves the pulse at 52 ns.
- mod_depth = 1.

Quantitative expected signal model:

Use a driven two-level model for the m_S = 0 to m_S = +1 transition. With Rabi frequency f_R = 10 MHz at mod_depth = 1 and pulse duration t = 52 ns, the on-resonance transfer probability is

P_on = sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a real on-resonance pODMR response should reduce the signal readout relative to the 0-reference by

C * P_on = 0.22 * 0.996 = 0.219,

or about 10.96 raw counts for a 50-count reference level. The expected normalized signal/reference ratio on resonance is therefore

R_on = 1 - 0.219 = 0.781.

For detuning Delta in Hz, I used the explicit scan model

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),
R(Delta) = 1 - 0.22 * P(Delta).

This predicts a large, resolvable dip near any resonance in the scanned range. For example, if the resonance is at the upper scan endpoint 3.925 GHz, the model ratios at the last three points are approximately 0.940 at 3.915 GHz, 0.835 at 3.920 GHz, and 0.781 at 3.925 GHz.

Observed data:

The raw readouts both sag at the high-frequency end, indicating common-mode baseline/tracking change rather than selective spin contrast. Normalizing readout 2 by readout 1 gives:

- mean ratio = 0.992
- standard deviation across scan points = 0.0198
- minimum ratio = 0.955 at 3.855 GHz
- ratio at 3.920 GHz = 0.996
- ratio at 3.925 GHz = 0.966

No point approaches the expected 0.781 ratio. A least-squares scan of possible resonance centers using the model above gives a best-fit contrast amplitude of about 0.022, roughly one tenth of the physically expected 0.22, and only a small improvement over a constant ratio model.

Decision:

The normalized measurement readout does not show the large 52 ns pi-pulse pODMR dip expected at mod_depth = 1. The visible high-frequency drop is shared by the reference and signal readouts. I therefore decide that a pODMR resonance is absent.
