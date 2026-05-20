Sequence and readout interpretation

The XML defines the active sequence as Rabimodulated.xml with a microwave-frequency scan. The executable branch is:

1. adj_polarize for the m_S = 0 preparation.
2. detection immediately after polarization: this is readout 1, the m_S = 0 reference.
3. The optional "Acquire 1 level reference" block is skipped because full_expt = 0, so do_adiabatic_inversion does not create an additional active reference readout.
4. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
5. detection after the microwave pulse: this is readout 2, the pODMR signal readout.

The scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant pulse duration is 52 ns, rounded at the 250 MHz sample rate to the same value. The relevant modulation depth is 1.

Quantitative model

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For an initially polarized two-level NV transition, the microwave population transfer for detuning d is

P_1(d) = (f_R^2 / (f_R^2 + d^2)) * sin^2(pi * t * sqrt(f_R^2 + d^2)),

with f_R = 10 MHz and t = 52 ns. The optical contrast scale between m_S = 0 and m_S = +1 is C = 0.22, so the expected normalized pODMR signal is approximately

readout2/readout1 = 1 - C * P_1(d).

On resonance, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996, giving an expected normalized dip of 0.219, or about 22%. At +/-5 MHz detuning the same model gives P_1 = 0.749, or an expected dip of 0.165. At +/-10 MHz detuning it gives an expected dip of 0.060.

Measured comparison

The measured readout2/readout1 contrast, defined as (readout1 - readout2) / readout1, has mean 0.0148 and standard deviation 0.061. The largest pointwise dip is 0.1267 at 3.905 GHz. Nearby values are 0.064 at 3.900 GHz and -0.018 at 3.910 GHz. Thus the deepest point is well below the expected 0.219 on-resonance dip, and the adjacent 5 MHz points do not show the expected roughly 0.165 contrast from the calculated Rabi-broadened line shape.

I also fit the normalized readout ratio to the explicit Rabi model while scanning the possible resonance center. A no-resonance constant-ratio model has SSE = 0.0746. The best fixed-contrast 22% Rabi model has SSE = 0.108, worse than the constant model. Allowing the contrast amplitude to float but constraining it positive gives a best amplitude of only about 0.066, roughly one third of the expected setup contrast, with only about 10% SSE improvement over constant. The two stored averages have different overall levels and likely reflect tracking cadence, so I do not treat their apparent partial agreement as a strong independent repeatability test.

Decision

There is a small local low point in readout 2 near 3.900-3.905 GHz, but it is not quantitatively consistent with the expected signal from a 52 ns near-pi pulse at mod_depth = 1. I therefore classify this case as resonance_absent.
