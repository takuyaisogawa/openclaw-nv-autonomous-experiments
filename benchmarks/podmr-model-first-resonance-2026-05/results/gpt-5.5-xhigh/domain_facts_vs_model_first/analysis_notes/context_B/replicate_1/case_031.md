Case: podmr_016_2026-05-16-131456

I used the provided sequence XML to identify the active measurement path. The sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

polarize -> detection -> wait -> rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) -> detection -> wait

The full_expt variable is 0, so the conditional m_S = +1 reference branch is not active. Readout 1 is therefore the post-polarization m_S = 0 fluorescence reference. Readout 2 is the fluorescence after the scanned microwave Rabi pulse. The sequence has sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and mod_depth = 1; 52 ns is exactly 13 samples at 250 MHz.

Physical model calculation:

For a square Rabi pulse, the transition probability from m_S = 0 to m_S = +1 is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

where f_R is the resonant Rabi frequency in cycles/s, delta is the detuning in Hz, and t is the pulse duration. The setup calibration gives f_R = 10 MHz at mod_depth = 1. With t = 52 ns:

f_R * t = 10e6 * 52e-9 = 0.52 cycles
P(0) = sin^2(pi * 0.52) = 0.996

The setup m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected on-resonance fractional fluorescence depletion is:

0.22 * 0.996 = 0.219

Thus an on-resonance readout 2 should be roughly 22% lower than the m_S = 0 reference, allowing for imperfect contrast and sampling.

Measured comparison using readout2/readout1:

- At 3.875 GHz: readout1 = 47.8269, readout2 = 39.6538, ratio = 0.8291, depletion = 0.1709.
- At 3.880 GHz: readout1 = 47.6731, readout2 = 39.6154, ratio = 0.8310, depletion = 0.1690.
- Off resonance, excluding points within 25 MHz of the fitted dip center, the mean depletion is 0.0042 with standard deviation 0.0222.

I also fit the finite-duration pulse model to the readout2/readout1 ratios with center frequency, baseline ratio, and depletion amplitude free while keeping f_R = 10 MHz and t = 52 ns fixed. The best fit has center = 3.8772 GHz, baseline ratio = 1.0002, fitted depletion amplitude = 0.2041, compared with the expected contrast amplitude 0.22. A flat no-resonance ratio gives SSE = 0.0811, while the Rabi-lineshape model gives SSE = 0.0124.

The measured narrow depletion near 3.875-3.880 GHz is quantitatively consistent with the expected pODMR signal from the active sequence and is much larger than the off-resonance fluctuations. Decision: resonance_present.
