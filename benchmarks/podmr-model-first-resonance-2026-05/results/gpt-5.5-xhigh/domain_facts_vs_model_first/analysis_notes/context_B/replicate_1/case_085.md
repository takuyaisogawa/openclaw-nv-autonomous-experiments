Case podmr_071_2026-05-17-084118

I used the provided sequence XML and the raw export values, without using labels or any sibling/external cases.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize the NV, then call detection. This is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is not active. The do_adiabatic_inversion variable is therefore not used in the active measurement path.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is readout 2, the post-microwave pODMR signal readout.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, the 4 ns clock rounding leaves it at 13 samples = 52 ns.
- mod_depth = 1 in the provided sequence XML and in Variable_values.

Quantitative expected-signal model:

For a driven two-level m_S = 0 to m_S = +1 transition, I modeled the population transferred by the microwave pulse as

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

where f_R is the Rabi frequency in cycles/s, delta is detuning in Hz, and tau is the pulse duration. The setup facts give f_R about 10 MHz at mod_depth = 1, so with tau = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so an on-resonance pulse should reduce the post-pulse readout relative to the m_S = 0 reference by

0.22 * 0.996 = 0.219, or about 21.9%.

With the observed readout-1 mean of 49.46 counts, the expected on-resonance readout-2 level is approximately

49.46 * (1 - 0.219) = 38.62 counts,

which is a drop of about 10.84 counts from the reference.

Observed comparison:
- Combined readout-1 mean: 49.459 counts.
- Combined readout-2 mean: 49.448 counts.
- Mean readout2 - readout1: -0.011 counts.
- Standard deviation of readout2 - readout1 across scan points: 1.469 counts.
- Minimum observed readout2/readout1 ratio: 0.9457.
- Expected on-resonance ratio from the active-pulse model: 0.7809.

Thus even the lowest observed normalized point is 0.1649 above the expected resonant ratio. In count units, the strongest observed negative difference is -2.79 counts, far smaller than the approximately -10.84 count resonant depression expected for this pulse.

I also fit the normalized ratio readout2/readout1 to a detuning-dependent Rabi lineshape plus a linear baseline. A no-resonance linear baseline had RMSE 0.0292 in ratio units. Constraining the resonance center to the scanned frequency range and allowing a nonnegative dip amplitude gave a best-fit dip amplitude of only 0.0235, compared with the expected full-contrast amplitude of about 0.22. Forcing the expected 0.22 amplitude within the scanned range worsened the ratio RMSE to 0.0534.

Decision:

The active sequence should have produced a large near-pi-pulse pODMR depression if a resonance were in the scanned range. The measured post-pulse readout tracks the m_S = 0 reference with only small fluctuations and no compatible dip. I therefore decide that a pODMR resonance is absent.
