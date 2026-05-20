Case: podmr_009_2026-05-16-113112

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive. The do_adiabatic_inversion flag is therefore not used in the active path.
- Readout 1 role: detection immediately after adj_polarize, so it is the true m_S = 0 optical reference for the point.
- Readout 2 role: detection after the modulated Rabi pulse, so it is the pODMR signal readout after microwave excitation.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounding step gives round(52 ns * 250 MHz) / 250 MHz = 13 / 250 MHz = 52 ns.

Quantitative expected-signal model:

The relevant active operation is a single square Rabi pulse before readout 2. Using the stated setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a two-level square pulse,

P_excited(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz and t = 52 ns. On resonance this gives

P_excited(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant normalized post-pulse readout is

readout2 / readout1 = 1 - 0.22 * 0.996 = 0.781.

Data check:

Using the combined raw readouts and normalizing the post-pulse signal by the preceding zero-state reference gives a minimum ratio of 24.288 / 31.423 = 0.773 at 3.875 GHz. Nearby ratios are also suppressed: 0.882 at 3.870 GHz, 0.804 at 3.880 GHz, and 0.813 at 3.885 GHz, while off-dip values are generally near 0.95 to 1.0.

A grid fit of the fixed-contrast square-pulse model, allowing only a baseline scale and small linear drift, gives a best center near 3.8784 GHz. The model residual sum of squares is 0.0247, compared with 0.1115 for a linear no-resonance baseline, an improvement factor of about 4.5. The fitted model predicts the observed dip depth expected from a near-pi pulse. The two stored averages both show the normalized dip near 3.875 GHz, but I do not treat them as strong independent repeats because the stored averages mainly reflect tracking cadence.

Decision:

The observed normalized dip has the amplitude expected from the active 52 ns, mod_depth 1 near-pi pulse and follows the expected pODMR line shape over the scan. A pODMR resonance is present.
