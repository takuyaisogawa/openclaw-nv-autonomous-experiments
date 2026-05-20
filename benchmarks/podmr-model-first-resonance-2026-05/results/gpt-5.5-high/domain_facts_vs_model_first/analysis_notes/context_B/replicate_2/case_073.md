Case: podmr_059_2026-05-17-054846

I used inputs/sequence.xml to identify the active sequence and readout roles. The sequence is Rabimodulated. It first runs adj_polarize followed by detection, so readout 1 is the bright m_S = 0 reference after optical polarization. The explicit m_S = 1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion is set. After the skipped reference block, the active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection, so readout 2 is the signal after the microwave pulse.

Relevant active parameters from the provided sequence/export are:
- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, rounded to 13 samples at 250 MHz, still 52 ns
- mod_depth = 1
- scan variable = mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- full_expt = 0, so there is no active independent dark-state reference in this run

Quantitative expected-signal model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant square Rabi pulse, the transfer probability is

P_flip = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10 MHz and tau = 52 ns. This gives

P_flip = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a true resonance should produce a readout-2 fluorescence drop of

0.22 * 0.996 = 0.219, or about 21.9% relative to the readout-1 reference.

Using the finite scan step does not remove this expectation. With the two-level detuned Rabi model

P_flip(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * tau * sqrt(f_Rabi^2 + delta^2)),

a resonance halfway between two 5 MHz-spaced scan points has delta = 2.5 MHz at the nearest point, giving P_flip = 0.929 and an expected fluorescence drop of 20.4%. At delta = 5 MHz the expected drop is still 16.5%.

Observed combined readout comparison:

The combined readout-2/readout-1 ratios have median 0.9856 and minimum 0.9357 at 3.880 GHz. The largest pointwise drop at the minimum is therefore only 6.43% relative to that point's readout-1 reference, or about 5.0 percentage points below the median ratio. At 3.880 GHz, readout 1 is 44.5385 and readout 2 is 41.6731. The resonant model would predict readout 2 near 44.5385 * (1 - 0.2191) = 34.7786, so the observed signal is about 6.89 raw units brighter than expected for resonance.

The surrounding points also do not show the expected near-pi-pulse ODMR dip: the 3.875, 3.880, and 3.885 GHz ratios are approximately 0.9808, 0.9357, and 0.9724, much shallower than the expected 0.78 to 0.84 range for a resonance sampled at or near these spacings. The saved averages have strong baseline shifts consistent with tracking cadence, and their local minima are not a strong independent repeatability test.

Decision: resonance_absent. The observed readout-2 suppression is much smaller than the quantitative model requires for the active 52 ns, mod_depth = 1 pulse.
