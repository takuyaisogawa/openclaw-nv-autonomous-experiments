Case: podmr_018_2026-05-16-134409

I used inputs/sequence.xml as the sequence definition. The active sequence is Rabimodulated.xml with sample_rate = 250 MHz, mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps, freqIQ = 50 MHz, mod_depth = 1, and length_rabi_pulse = 52 ns. The 52 ns pulse is already an integer 13 samples at 250 MHz, so the rounded pulse duration remains 52 ns.

Readout roles from the instruction flow:
- readout 1: after adj_polarize and before any microwave pulse, labelled in the XML as the true m_S = 0 level reference.
- readout 2: after the active rabi_pulse_mod_wait_time call with length_rabi_pulse and mod_depth, so this is the pODMR signal readout.
- the optional m_S = 1 reference block is inactive because full_expt = 0, even though the adiabatic inversion boolean is set.

Physical expectation:
For this setup the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the driven population transfer is

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

With f_R = 10 MHz and t = 52 ns, the on-resonance transfer is sin^2(pi * 10e6 * 52e-9) = 0.996. With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance readout-2/reference ratio is 1 - 0.22 * 0.996 = 0.781. For a reference count near 48, that predicts an on-resonance readout near 37.5. The same model gives transfer probabilities of about 0.749 at 5 MHz detuning, 0.273 at 10 MHz detuning, and 0.012 at 15 MHz detuning, so a narrow dip over a few 5 MHz scan steps is expected.

Measured comparison:
The combined readout-2 minimum is 38.96 at 3.880 GHz. The lowest normalized readout-2/readout-1 ratio is 39.77 / 49.27 = 0.807 at 3.875 GHz. These are close to the expected 0.781 ratio and 37.5 count level given the approximate contrast and Rabi-frequency calibration. The dip spans the expected coarse linewidth: readout 2 is 42.88, 39.77, 38.96, and 42.63 at 3.870, 3.875, 3.880, and 3.885 GHz, while off-dip values are mostly in the mid to high 40s.

I also fit the normalized ratio r = readout2/readout1 with the above Rabi model. A linear baseline-only model had SSE = 0.0806 in ratio units. A fixed-contrast model using C = 0.22 and fitting only the resonance center plus linear baseline gave best center 3.8771 GHz and SSE = 0.0257. Allowing the dip amplitude to float gave best center 3.8771 GHz, effective contrast amplitude 0.186, and SSE = 0.0238. The fitted amplitude is reasonably close to the expected 0.22 scale.

The two stored averages should not be treated as a strong independent repeatability test because they can reflect tracking cadence, but both have their lowest readout-2 values at the central dip points around 3.875 to 3.880 GHz.

Decision: resonance_present.
