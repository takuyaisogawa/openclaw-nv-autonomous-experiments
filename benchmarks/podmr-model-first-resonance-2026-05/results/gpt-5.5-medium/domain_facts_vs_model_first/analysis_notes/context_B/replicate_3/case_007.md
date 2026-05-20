Case podmr_011_2026-05-11-181506.

Sequence inspection:
- SequenceName is Rabimodulated.xml.
- The active sequence has full_expt = 0, so the optional "1 level reference" block is skipped.
- Active readout roles:
  - readout 1 is the polarized ms=0 reference immediately after adj_polarize and detection, with no microwave pulse before it.
  - readout 2 is the signal readout after a microwave rabi_pulse_mod_wait_time and detection.
- The standalone sequence.xml and Variable_values report length_rabi_pulse = 52 ns and mod_depth = 1. The embedded saved Sequence string in raw_export.json has mod_depth = 0.3, but the provided XML/Variable_values indicate mod_depth = 1, so I use mod_depth = 1 for the decision and note the discrepancy.
- sample_rate = 250 MHz, so 52 ns rounds to 52 ns.

Physical model calculation:
Use a two-level rectangular-pulse model. The setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so for mod_depth = 1:

f_R = 10 MHz
t = 52 ns
on-resonance transition probability P = sin^2(pi f_R t)
P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996

With the setup ms=0 to ms=+1 contrast scale of about 22%, the expected on-resonance readout deficit is:

0.996 * 22% = 21.9%

A more explicit detuned rectangular-pulse model uses:

P(delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

where Omega = 2 pi * 10 MHz and Delta = 2 pi * (mw_freq - f0). Fitting only the resonance center and an amplitude/offset scale to the observed fractional contrast (readout1 - readout2) / readout1 gives a best center near 3.877 GHz. The fitted scale is 0.90 relative to the nominal 22% model and the RMS residual is about 2.9 percentage points, which is reasonable for this noisy/tracking-affected scan.

Data calculation:
The combined readouts give fractional deficits:
- Off-resonance edge mean, using the first four and points 3.910-3.925 GHz: about 0.6%.
- Central mean from 3.865 to 3.890 GHz: about 11.1%.
- Maximum deficit: 20.5% at 3.880 GHz.

The observed central dip has the correct sign for a pODMR transition: the post-microwave signal readout is lower than the ms=0 reference. Its peak size is close to the 21.9% expected from the active 52 ns, mod_depth 1 pulse. Stored per-average traces show strong drift/tracking cadence structure, so I do not treat the two stored averages as an independent repeatability test. The combined readout pattern is nevertheless quantitatively consistent with a pODMR resonance.

Decision: resonance_present.
