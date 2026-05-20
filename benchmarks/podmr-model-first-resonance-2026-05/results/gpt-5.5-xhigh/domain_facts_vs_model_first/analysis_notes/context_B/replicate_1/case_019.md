Active sequence and readout roles

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence, mw_freq is used in set_microwave after adding detuning, and the active pulse before the signal readout is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

The first detection occurs immediately after adj_polarize and is the polarized m_S = 0 reference readout. full_expt = 0, so the optional m_S = 1 reference branch is inactive. The second detection occurs after the modulated Rabi pulse and is the pODMR signal readout. The active pulse settings are length_rabi_pulse = 52 ns and mod_depth = 1. With sample_rate = 250 MHz, the rounded duration remains 13 samples = 52 ns.

Quantitative expected-signal model

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1. I modeled the microwave pulse as a driven two-level transition with

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

where Omega = 10 MHz, t = 52 ns, and delta is the microwave detuning in Hz. On resonance, Omega*t = 0.52 cycles, so P1(0) = sin^2(pi*0.52) = 0.996. Using the supplied m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance signal readout is reduced by 0.22*0.996 = 21.9%. For a typical 40.5 count reference readout this predicts about 40.5*(1 - 0.219) = 31.6 counts.

I fit the model directly to the two measured readouts using

R2(freq) = alpha * R1(freq) * (1 - 0.22 * P1(freq - f0))

with only alpha and f0 free. The best fit gives f0 = 3.877572 GHz, alpha = 0.9909, and SSE = 31.75. A no-resonance model R2 = alpha*R1 gives SSE = 168.29, about 5.3 times worse.

Observed comparison

The second readout has its deepest points at 3.875 GHz and 3.880 GHz: 32.42 and 31.81 counts. These are almost exactly the expected near-pi-pulse level of about 31.6 counts. The normalized transfer estimates at these two points are about 0.94 and 0.94, close to the model values 0.925 and 0.933 for the fitted resonance center. The neighboring points at 3.870 GHz and 3.885 GHz show partial reductions consistent with the finite 52 ns Rabi-pulse linewidth.

There are additional point-to-point fluctuations away from the main dip, and the stored averages should not be treated as a strong independent repeatability test because they can reflect tracking cadence. However, the main feature has the expected sign, amplitude, center behavior, and width for a pODMR resonance under the active sequence.

Decision: resonance_present.
