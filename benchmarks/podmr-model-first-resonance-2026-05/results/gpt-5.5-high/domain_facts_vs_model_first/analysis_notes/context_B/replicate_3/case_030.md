Case: podmr_015_2026-05-16-130043

Active sequence and readout roles:

The provided sequence is Rabimodulated.xml. The active instructions first run adj_polarize, then detection, then wait_for_awg. This first detection is the true m_S = 0 reference readout. The "Acquire 1 level reference" block is guarded by full_expt, and full_expt = 0 in the sequence, so that block is inactive despite do_adiabatic_inversion being true. The active signal block then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. Therefore readout 1 is the post-polarization m_S = 0 reference, and readout 2 is the signal after the pulsed microwave/Rabi drive.

Relevant sequence parameters:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- scan variable = mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- active microwave pulse = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

Explicit model calculation:

The supplied setup facts give Rabi frequency f_R ~= 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For the active pulse, f_R = 10 MHz and t = 52 ns. Using the standard driven two-level population transfer model in frequency units,

P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t).

At resonance, Delta = 0:

P_1(0) = sin^2(pi * 10e6 * 52e-9)
       = sin^2(1.6336)
       ~= 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant point should show an optical drop of approximately

0.22 * 0.996 ~= 0.219, or 21.9%.

Data check:

I normalized the active signal readout by the reference readout, readout2/readout1. The minimum normalized point occurs at 3.875 GHz:

- readout1 = 46.2115
- readout2 = 35.8654
- ratio = 0.7761

The median normalized ratio at the outer edge points is about 0.9754, so the observed fractional drop is

1 - 0.7761 / 0.9754 ~= 0.204, or 20.4%.

This is close to the 21.9% expected from a resonant 52 ns near-pi pulse at mod_depth = 1. A quantitative line-shape fit using the Rabi detuning model above and a linear baseline gave:

- best center ~= 3.8777 GHz
- fitted normalized depth ~= 0.198 relative to baseline
- null linear-baseline SSE = 0.07147
- Rabi-model SSE = 0.00927
- residual reduction versus null ~= 87%

The stored two averages both show the central normalized suppression at the dip point, but I treat them mainly as tracking-cadence information rather than an independent repeatability test.

Decision:

The active sequence predicts a large near-pi-pulse pODMR dip on resonance, and the measured readout2/readout1 trace shows a dip with the expected magnitude and a compatible Rabi line shape near 3.875-3.880 GHz. I decide that a pODMR resonance is present.
