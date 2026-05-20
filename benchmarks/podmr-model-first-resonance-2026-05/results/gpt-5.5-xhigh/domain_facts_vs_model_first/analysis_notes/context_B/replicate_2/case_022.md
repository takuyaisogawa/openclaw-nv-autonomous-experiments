Case: podmr_007_2026-05-16-013306

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first perform adj_polarize followed by detection, so readout 1 is the bright m_S = 0 reference.
- full_expt is 0, so the optional "1 level reference" block is skipped even though do_adiabatic_inversion is true. There is no active adiabatic inversion readout and no independent m_S = +1 reference in the stored readouts.
- The second stored readout is after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.
- sample_rate is 250 MHz, so the pulse length rounding leaves 52 ns exactly: round(52 ns * 250 MHz) = 13 samples.

Quantitative model:
For a resonant two-level pulse, using the supplied setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. With pulse duration t = 52 ns, the on-resonance transfer probability is

P(0) = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.

With the stated contrast scale of 22 percent, the expected on-resonance readout drop relative to the bright m_S = 0 reference is about 0.22 * 0.996 = 0.219, i.e. about 21.9 percent. For a bright readout near 36 counts, the expected resonant dark readout is 36 * (1 - 0.219) = 28.1 counts.

Using the finite-duration detuned pulse model

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

the expected relative drops for detunings of -10, -5, 0, +5, and +10 MHz are approximately 6.0 percent, 16.5 percent, 21.9 percent, 16.5 percent, and 6.0 percent.

Data comparison:
The combined readouts show readout 2 dropping strongly while readout 1 remains near its usual bright level around 3.870 to 3.885 GHz:

- 3.870 GHz: readout 1 = 35.96, readout 2 = 31.23, relative drop = 13.2 percent.
- 3.875 GHz: readout 1 = 35.48, readout 2 = 28.96, relative drop = 18.4 percent.
- 3.880 GHz: readout 1 = 36.90, readout 2 = 28.21, relative drop = 23.6 percent.
- 3.885 GHz: readout 1 = 36.17, readout 2 = 31.77, relative drop = 12.2 percent.
- 3.890 GHz: readout 1 = 36.79, readout 2 = 35.00, relative drop = 4.9 percent.

A direct grid fit of the measured relative drop (readout1 - readout2) / readout1 to the detuned finite-pulse model gives a center near 3.8785 GHz, fitted amplitude 0.216, and small offset about 0.008. The fitted amplitude is essentially the expected 0.22 contrast scale for a near-pi pulse.

The stored per-average traces both show the same central readout-2 depression, but I treat that mainly as consistency with the combined trace because the stored averages can reflect tracking cadence rather than an independent repeatability test.

Decision:
The measured readout-2 dip has the correct role, sign, depth, and width for the active 52 ns mod_depth = 1 pODMR pulse. The expected on-resonance signal is about 28 counts, and the observed minimum is 28.21 counts. I therefore classify this case as resonance_present.
