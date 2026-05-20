Case podmr_026_2026-05-16-182622

Inputs used: inputs/sequence.xml and inputs/raw_export.json.

Sequence and readout roles:
- Active sequence: Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is the first detection immediately after optical polarization, i.e. the bright m_S = 0 reference.
- Readout 2 is the detection after the Rabi-modulated microwave pulse and is the pODMR signal channel.
- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.
- mod_depth = 1 in the provided sequence XML / exported variable values.

Physical model calculation:
Use a rectangular driven two-level model starting in m_S = 0. With Rabi frequency f_R = 10 MHz * mod_depth = 10 MHz and pulse duration tau = 52 ns, the transition probability versus detuning delta is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996. The stated bright-to-dark contrast scale is 22%, so a resonant pulse should reduce readout 2 relative to the m_S = 0 reference by about 0.22 * 0.996 = 0.219 of the bright signal. The mean readout-1 level is 49.61 counts, giving an expected resonant drop of 49.61 * 0.219 = 10.87 counts, i.e. an on-resonance readout near 38.74 counts if a resonance lies on the sampled frequency grid.

Observed data:
- Readout 1 mean = 49.61 counts, standard deviation = 1.13 counts, range = 47.10 to 52.10.
- Readout 2 mean = 49.58 counts, standard deviation = 0.97 counts, range = 47.85 to 51.71.
- The pointwise difference readout2 - readout1 has mean = -0.03 counts, standard deviation = 1.47 counts, and minimum = -3.10 counts.
- The normalized contrast 1 - readout2/readout1 has mean = 0.00007, standard deviation = 0.0296, and maximum = 0.0594.

Model comparison:
Fitting the rectangular-pulse lineshape to the normalized contrast while allowing the center frequency and amplitude to vary gives a best-fit amplitude of only 0.0316, far below the expected 0.22. For the physically expected amplitude 0.22, the best-center residual is much worse than the no-resonance residual. The largest observed dip, about 3.1 counts or 5.9%, is also much smaller than the expected approximately 10.9 count / 21.9% resonant signal and is comparable to ordinary point-to-point scatter.

Decision:
The active pulse should generate a large, easily visible pODMR dip if a resonance were present in the scan. The measured signal channel stays essentially equal to the bright reference and lacks the expected rectangular-pulse resonance amplitude. Therefore the pODMR resonance is absent.
