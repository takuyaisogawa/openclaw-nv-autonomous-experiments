Case: podmr_053_2026-05-17-042031

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets full_expt = 0, so the "Acquire 1 level reference" block is skipped. The do_adiabatic_inversion boolean is therefore not active for the acquired readouts.
- Readout 1 role: detection immediately after adj_polarize, before any microwave pulse; this is the true mS=0 reference.
- Readout 2 role: detection after the active rabi_pulse_mod_wait_time call; this is the pODMR signal readout after the microwave pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- sample_rate = 250 MHz and length_rabi_pulse = 52 ns, which rounds to 13 samples and remains 52 ns.
- mod_depth = 1 in the provided XML and in the exported Variable_values.

Quantitative expected-signal model:

Use the relevant two-level Rabi response for a square pulse,

P_transfer(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)).

For this setup, f_R = 10 MHz at mod_depth = 1. With t = 52 ns:

- On resonance: P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the given contrast scale C = 0.22, the expected normalized readout ratio on resonance is
  readout2/readout1 = 1 - C * P_transfer = 1 - 0.22 * 0.996 = 0.781.
- Thus the expected pODMR dip is about 21.9% of the mS=0 reference. With the observed readout1 mean of 45.20 counts, that is about 9.9 counts.
- Even if the resonance fell halfway between scan points, df = 2.5 MHz gives P_transfer = 0.929 and an expected dip of about 20.4%. At df = 5 MHz the expected dip is still about 16.5%.

Measured comparison:

- The measured combined readout2/readout1 ratios have mean 0.996.
- The deepest measured ratio is 0.928 at 3.880 GHz, a 7.17% drop or 3.29 counts.
- Another low point occurs at 3.890 GHz with ratio 0.930, but the intervening 3.885 GHz point has ratio 1.005.
- A physical resonance near 3.880-3.890 GHz with this pulse should produce a strong central-lobe dip at adjacent 5 MHz-spaced points, especially at the point nearest the resonance. The missing dip at 3.885 GHz is inconsistent with that line shape.

Fit check:

- Null model on the normalized ratios, using a constant ratio: RMSE = 0.0331.
- Fixed physical resonance model using C = 0.22, f_R = 10 MHz, and t = 52 ns, with center constrained inside the scan and only an overall scale fitted: best center about 3.887 GHz, RMSE = 0.0587. This is worse than the null model because the model predicts a much deeper dip than measured.
- Allowing the dip amplitude to float gives a best positive effective contrast of about 4.9%, far below the expected 22% contrast for mod_depth = 1, and it still does not reproduce the isolated low/high/low pattern around 3.880-3.890 GHz.

Decision:

The data do not show a pODMR resonance consistent with the active sequence and expected signal size. The small low points are much weaker than the expected near-pi-pulse contrast and do not follow the required Rabi spectral shape. I classify this case as resonance_absent.
