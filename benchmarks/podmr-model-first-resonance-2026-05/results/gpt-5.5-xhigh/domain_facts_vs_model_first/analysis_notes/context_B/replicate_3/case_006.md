Sequence and readout identification

The sequence file is Rabimodulated.xml. The active scan variable is mw_freq, from
3.825 GHz to 3.925 GHz in 5 MHz steps. In the XML, full_expt = 0, so the
"Acquire 1 level reference" block is skipped. The active readouts are therefore:

1. readout 1: after adj_polarize and detection, before any microwave pulse in
   the active path. This is the true m_s = 0 reference readout.
2. readout 2: after rabi_pulse_mod_wait_time with length_rabi_pulse =
   5.2e-08 s and mod_depth = 1, followed by detection. This is the pODMR signal
   readout after the microwave pulse.

The active pulse duration is 52 ns. With the provided setup calibration, the
Rabi frequency at mod_depth = 1 is about 10 MHz.

Expected-signal model

I used the square-pulse two-level Rabi response, with frequencies in cycles/s:

P_transfer(delta) =
  Omega^2 / (Omega^2 + delta^2)
  * sin^2(pi * tau * sqrt(Omega^2 + delta^2))

where Omega = 10 MHz, tau = 52 ns, and delta = mw_freq - f0. The expected signal
readout ratio is

readout2 / readout1 = alpha * (1 - C * P_transfer)

with C = 0.22 from the stated m_s = 0 to m_s = +1 contrast scale and alpha a
single readout-scale factor.

On resonance, P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996. The expected
fractional fluorescence loss is therefore 0.22 * 0.996 = 0.219, or about
8.7 raw-readout units at the observed mean readout 1 level of 39.83. At +/-5 MHz
detuning the model still predicts P_transfer about 0.749, i.e. about 16.5%
loss. At +/-10 MHz it predicts about 6.0% loss.

Data comparison

The combined ratio readout2/readout1 has mean 0.986 and a minimum of 0.908 at
3.875 GHz, corresponding to only a 9.18% loss or 3.87 raw-readout units. If the
physical 22% contrast model is centered at this apparent minimum, the fitted
alpha is 1.023 and the expected ratios near the center are:

- 3.870 GHz: expected 0.855, observed 0.935
- 3.875 GHz: expected 0.799, observed 0.908
- 3.880 GHz: expected 0.855, observed 1.003

Thus the expected resonance would be much deeper and would also depress both
neighboring 5 MHz points; the observed feature is shallow and asymmetric.

I also fit the full ratio trace quantitatively. A null model with a constant
ratio gives SSE = 0.022425. The fixed-contrast pODMR model with C = 0.22 gives
best SSE = 0.019650, but with best f0 = 3.803685 GHz, outside the scanned
region, and BIC is slightly worse than the null model (-140.37 versus -140.64).
A free-contrast line-shape fit prefers f0 = 3.875085 GHz but only
C_eff = 0.057, far below the stated 0.22 contrast scale; its BIC is also not
better than the null under the extra parameter count.

The stored averages show strong tracking-level changes, so I do not treat them
as independent repeatability tests. They also do not give a stable resonance
position: the lowest stored-average ratios occur at 3.830 GHz and 3.885 GHz for
the two stored averages.

Decision

The active sequence should produce an approximately full-contrast pi-pulse dip
if a resonance is present in the scanned range. The observed signal deficit is
too small, not shaped like the expected Rabi response, and not quantitatively
favored over a no-resonance baseline. I therefore decide that a pODMR resonance
is absent.
