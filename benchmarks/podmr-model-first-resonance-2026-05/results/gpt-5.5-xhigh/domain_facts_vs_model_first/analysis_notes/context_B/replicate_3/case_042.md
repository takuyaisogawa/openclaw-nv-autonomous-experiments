Case: podmr_028_2026-05-16-185605

Sequence interpretation

The provided sequence is Rabimodulated.xml with mw_freq as the scanned variable. The active instructions are:

1. adj_polarize
2. detection
3. wait_for_awg
4. skip the +1 reference block because full_expt = 0
5. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth)
6. detection
7. wait_for_awg

Thus readout 1 is the post-polarization m_S = 0 reference detection, and readout 2 is the detection after the scanned microwave Rabi pulse. The +1 reference block is inactive. The active parameters from the provided XML/exported variable values are length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation

Use the two-level pulsed ODMR Rabi model for transition probability after a rectangular pulse:

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)

where f_R is the on-resonance Rabi frequency in Hz, delta is detuning in Hz, and t is the pulse duration. With the stated setup f_R = 10 MHz at mod_depth = 1 and t = 52 ns.

On resonance:

P1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance readout-2 suppression relative to readout 1 is:

0.22 * 0.996 = 0.219, about 22%.

The frequency step is 5 MHz, so if a resonance lies anywhere inside the scan range, the nearest sampled point is at most 2.5 MHz detuned. At 2.5 MHz detuning:

P1(2.5 MHz) = 0.929
expected contrast = 0.22 * 0.929 = 0.204, about 20%.

At 5 MHz detuning the expected contrast is still about 16.5%, and at 10 MHz detuning it is about 6.0%.

Data comparison

I normalized the raw readouts as contrast = (readout1 - readout2) / readout1 because readout 1 is the m_S = 0 reference and readout 2 should drop on resonance. Across the 21 scanned points, the observed contrast ranges from -5.0% to +5.5%, with the largest positive value 5.54% at 3.885 GHz. The group near 3.875 to 3.885 GHz has positive contrast of 4.63%, 3.73%, and 5.54%, but this is far below the >=20% nearest-point contrast expected from the active 52 ns, mod_depth = 1 pulse.

I also compared simple residuals. A no-resonance constant-offset model for the normalized contrast had RSS = 0.0111. A fixed physical resonance model using the expected 22% contrast scale and scanning the resonance center over the measured range had best RSS = 0.0509, worse than the no-resonance model. Allowing the resonance amplitude to float gave an amplitude near 5.5%, only about one quarter of the physically expected contrast for the active pulse, and comparable to point-to-point fluctuations from the two stored averages.

Decision

The active sequence should produce a large readout-2 suppression if a pODMR resonance is present in the scan range. The measured normalized readout difference never approaches the expected signal size, and the fixed-amplitude physical resonance model is rejected by the data. I therefore decide that no pODMR resonance is present.
