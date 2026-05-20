Case: podmr_004_2026-05-10-171142

I used only the local sequence XML and raw export for this case.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active XML path has full_expt = 0, so the optional "1 level reference" block is skipped.
- Readout 1 is the true 0-level reference after optical polarization and before the swept microwave pulse.
- Readout 2 is the signal readout after the Rabi-modulated microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s = 52 ns. With the 250 MHz sample rate, this is already exactly 13 samples, so rounding does not change it.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a square pulse with detuning delta in Hz, I used
  P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t).
- On resonance, P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The mean readout-1 level is 43.6795. With a 22% mS=0 to mS=+1 contrast, the expected on-resonance drop in readout 2 relative to readout 1 is
  43.6795 * 0.22 * 0.996 = 9.57 raw-readout units.
- Therefore a resonance inside the scan should appear as a broad negative feature in readout2 - readout1, with the second readout approaching about 34.1 near line center if the first readout is 43.7.

Measured comparison:
- readout2 - readout1 has mean +0.570, minimum -2.462, and maximum +3.962 raw-readout units.
- The most negative point is at 3.855 GHz, where readout1 = 43.038 and readout2 = 40.577, a drop of only 2.462 units. That is about 26% of the expected resonant drop and is isolated rather than a clear 52 ns Rabi spectral response.
- Around 3.910-3.915 GHz the second readout increases above the first by 3.35 to 3.96 units, opposite to the expected pODMR contrast sign.
- A least-squares comparison using a baseline plus the Rabi spectral response prefers the opposite sign feature; forcing the expected 9.57-unit dip worsens the residuals relative to a simple baseline. This is not consistent with the active pulse producing a resolved pODMR resonance in the scan window.

Decision: resonance_absent.
