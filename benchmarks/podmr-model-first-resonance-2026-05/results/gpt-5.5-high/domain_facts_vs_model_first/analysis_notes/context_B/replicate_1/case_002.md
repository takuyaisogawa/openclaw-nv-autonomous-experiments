Active sequence and readout roles

The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to
3.925 GHz in 5 MHz steps. The instructions first polarize and detect, giving
readout 1 as the true m_S=0 reference. Because full_expt = 0, the separate
m_S=1 reference block is skipped. The sequence then applies
rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) and detects
again, so readout 2 is the pODMR signal after the microwave pulse.

The provided sequence XML and variable values give length_rabi_pulse = 52 ns,
sample_rate = 250 MHz, and mod_depth = 1. The 52 ns duration is exactly 13
samples, so rounding leaves it at 52 ns. I noted that the embedded raw_export
Sequence string contains a stale-looking mod_depth = 0.3 entry, but the provided
sequence XML and exported Variable_values both specify mod_depth = 1, so I used
mod_depth = 1 for the physical expectation.

Quantitative physical expectation

Use a two-level Rabi model. The setup Rabi frequency is about 10 MHz at
mod_depth = 1 and scales linearly with mod_depth, so here f_R = 10 MHz. For a
square resonant pulse of duration tau = 52 ns, the transfer probability is

P(+1) = sin^2(pi * f_R * tau)
      = sin^2(pi * 10e6 * 52e-9)
      = sin^2(1.6336)
      = 0.996.

The setup contrast between m_S=0 and m_S=+1 is about 22%, so the expected
on-resonance pODMR fluorescence drop relative to the m_S=0 reference is

0.22 * 0.996 = 0.219, or about 21.9%.

With the measured readout 1 mean of 42.29 counts, this predicts an on-resonance
signal near

42.29 * (1 - 0.219) = 33.02 counts,

or a drop of about 9.27 counts from the paired reference.

Observed quantitative comparison

The combined readouts show a clear depression in readout 2 while readout 1
stays near its baseline:

- Minimum near 3.880 GHz: readout 1 = 41.69, readout 2 = 34.73, ratio = 0.833,
  a 16.7% drop.
- Center window 3.865-3.885 GHz: mean readout 1 = 42.15, mean readout 2 =
  36.92, ratio = 0.876, a 12.4% drop.
- Off that window: mean readout 1 = 42.33, mean readout 2 = 41.69, ratio =
  0.986, only a 1.4% drop.

The minimum observed drop is somewhat smaller than the ideal 21.9% model
expectation, which is reasonable for finite linewidth, detuning-grid placement,
readout noise, and imperfect contrast. Its magnitude and localization are far
larger than the off-resonance readout mismatch. The two stored averages both
show a lower readout-2/readout-1 ratio in the same central frequency window, but
I treat that only as consistency with tracking cadence rather than as a strong
independent repeatability test.

Decision

A pODMR resonance is present.
