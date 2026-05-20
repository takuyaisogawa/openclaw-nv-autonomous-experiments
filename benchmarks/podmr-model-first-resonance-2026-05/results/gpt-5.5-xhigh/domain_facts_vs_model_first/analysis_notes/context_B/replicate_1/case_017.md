Case: podmr_002_2026-05-16-002114

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence name from the export is Rabimodulated.xml.
- The sequence varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In inputs/sequence.xml, full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- Readout 1 is the first detection immediately after adj_polarize. The sequence comment identifies this as the true m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so this is the microwave-pulse signal readout.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, round(length_rabi_pulse * sample_rate) gives 13 samples, so the effective duration remains 52 ns.
- mod_depth = 1.

Quantitative model:
For a square resonant microwave pulse, use

P1(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega / (2*pi) = 10 MHz * mod_depth = 10 MHz and t = 52 ns. On resonance this gives

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fluorescence dip is

0.22 * 0.996 = 0.219, or about 21.9%.

Using the combined readout 2 baseline median outside the candidate dip window gives 36.769 counts. The model therefore expects an on-resonance drop of about

36.769 * 0.219 = 8.06 counts,

with a minimum signal around 28.7 counts for a resonance centered on a sampled frequency.

Data comparison:
- Combined readout 2 has its minimum at 3.880 GHz: 26.962 counts.
- Relative to the 36.769 count baseline, the observed readout 2 drop is 9.808 counts, or 26.7%.
- Normalizing the signal readout by the 0-reference readout gives a median off-window ratio of 0.981 and a minimum ratio of 0.707 at 3.880 GHz, a relative normalized drop of 27.9%.
- The detuned square-pulse model centered at 3.880 GHz predicts fluorescence fractions near the dip of about 0.940 at -10 MHz, 0.835 at -5 MHz, 0.781 on resonance, 0.835 at +5 MHz, and 0.940 at +10 MHz.
- The observed readout 2 fractions over baseline near the same region are about 0.855 at 3.870 GHz, 0.756 at 3.875 GHz, 0.733 at 3.880 GHz, 0.879 at 3.885 GHz, and 1.002 at 3.890 GHz. The feature is somewhat deeper and asymmetric, but its scale and width are close to the physical model for a near-pi pulse.
- The two stored averages both show the normalized minimum in this region: average 1 at 3.875 GHz and average 2 at 3.880 GHz. I do not treat this as a strong independent repeatability test because stored averages can reflect tracking cadence, but it is consistent with the combined trace.

Decision:
The active readout roles and pulse parameters predict a large pODMR dip when the scan crosses resonance, and the signal readout shows a localized dip of the expected order near 3.88 GHz while the reference readout does not show an equivalent feature. A pODMR resonance is present.
