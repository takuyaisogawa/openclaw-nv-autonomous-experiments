Sequence interpretation

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence polarizes the NV, takes a detection readout, waits, applies one Rabi-modulated microwave pulse, then takes a second detection readout. The optional "1 level reference" branch is disabled because full_expt = 0, so do_adiabatic_inversion is not active in the executed sequence.

Readout roles:
- readout 1: optically polarized m_S = 0 reference detection.
- readout 2: post-microwave-pulse signal detection.

Pulse parameters from the provided XML and exported variable values:
- mod_depth = 1.
- length_rabi_pulse = 5.2e-8 s.
- sample_rate = 250 MHz, so the rounded pulse length is round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns.

Quantitative model

Given the supplied setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square microwave pulse, the expected transferred population versus detuning is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),

using cycle-frequency units. With f_R = 10 MHz and t = 52 ns, the on-resonance transfer is

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale C = 0.22, the expected normalized post-pulse signal/reference ratio on resonance is

R(0) = 1 - C * P(0) = 1 - 0.22 * 0.996 = 0.781.

The mean reference readout is 51.72 counts, so the expected resonant signal would be about 40.38 counts, a drop of about 11.33 counts. Because the scan step is 5 MHz, any resonance inside the scanned range should have a sampled point within 2.5 MHz of its center. At 2.5 MHz detuning, the same model gives P = 0.929 and R = 0.796, still an about 20.4 percent normalized drop.

Observed data comparison

The combined readout2/readout1 ratios are:
1.0027, 0.9833, 1.0065, 1.0045, 1.0142, 1.0026, 1.0080, 1.0027, 1.0022, 1.0091, 0.9537, 0.9627, 0.9446, 1.0504, 1.0052, 0.9916, 0.9819, 0.9830, 1.0170, 1.0195, 1.0011.

The smallest combined ratio is 0.9446 at 3.885 GHz, a 5.54 percent drop and only -2.98 counts relative to the reference at that point. This is far smaller than the expected near-pi-pulse pODMR contrast of about 20 to 22 percent. A grid fit of the square-pulse model y = b - A P(f - f0), allowing the resonance center to vary over the scanned range, gives a best positive amplitude A = 0.055, about one quarter of the expected 0.22 contrast. Forcing A = 0.22 gives a predicted minimum ratio around 0.820 even after fitting a baseline, which is still much lower than the observed minimum.

The stored averages show tracking-scale variation rather than a stable deep resonant dip; their minimum ratios are about 0.927 and 0.945. Since the expected physical signal is large for this pulse duration and mod_depth, and the observed normalized depression is small and not compatible with the near-pi-pulse model, I decide that a pODMR resonance is absent.
