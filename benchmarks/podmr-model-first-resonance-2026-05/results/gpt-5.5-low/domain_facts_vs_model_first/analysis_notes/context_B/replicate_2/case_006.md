Case podmr_010_2026-05-11-155154

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, scanned parameter mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS=+1 reference block is inactive.
- Readout 1 role: true mS=0 fluorescence reference after optical polarization.
- Readout 2 role: signal readout after the modulated Rabi microwave pulse.
- mod_depth from the provided sequence XML is 1.
- length_rabi_pulse is 52 ns. At the 250 MHz sample rate this is already exactly 13 samples, so rounding does not change it.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the resonant two-level transition probability after a rectangular pulse is
  P(+1) = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns:
  P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of 22%, the expected on-resonance pODMR reduction in the signal readout relative to the mS=0 reference is
  0.22 * 0.996 = 0.219, or about 21.9%.
- This is the relevant expectation because the active sequence compares the post-Rabi readout to the preceding mS=0 reference; the stored averages are not treated as a strong independent repeatability test.

Observed quantitative signal:
- Mean readout 1 = 39.826, mean readout 2 = 39.261.
- The pointwise normalized signal readout2/readout1 ranges from 0.908 to 1.034.
- The largest normalized dip, 1 - readout2/readout1 = 9.18%, occurs at 3.875 GHz, the center of the scan.
- Although this dip is smaller than the ideal 21.9% expected for a resonant pi-like pulse, it is localized at the nominal resonance region and has the correct sign for pODMR: the post-microwave readout is suppressed relative to the mS=0 reference.

Decision:
The data show a center-localized reference-normalized fluorescence suppression consistent with a pODMR resonance, though with reduced observed contrast relative to the simple ideal model. I therefore classify the resonance as present.
