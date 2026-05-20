Sequence and readout identification

The provided sequence is Rabimodulated.xml. The active scan variable is mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse after the initial detection is
rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth,
switch_delay, ch_on). The parameters used for the model are length_rabi_pulse =
52 ns and mod_depth = 1. The full_expt variable is 0, so the conditional "Acquire 1
level reference" block is skipped. Therefore readout 1 is the true m_S = 0 optical
reference after polarization, and readout 2 is the signal after the scanned microwave
Rabi pulse.

Explicit expected-signal calculation

Given the supplied setup facts, the resonant Rabi frequency is approximately
10 MHz at mod_depth = 1. For a square pulse of duration t = 52 ns, the resonant
transition probability is

P = sin^2(pi * f_R * t)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

With a 22% contrast between m_S = 0 and m_S = +1, a resonant point should reduce
the post-pulse readout to approximately

readout_2 / readout_1 = 1 - 0.22 * P = 0.781.

For a typical readout_1 near 50 counts, this corresponds to an expected dip of
about 11 counts. Including off-resonant square-pulse response,

P(delta) = (f_R^2 / (f_R^2 + delta^2)) *
           sin^2(pi * sqrt(f_R^2 + delta^2) * t),

and sampling possible resonance centers on the 5 MHz scan grid, the expected
minimum sampled ratio remains approximately 0.781 to 0.796 for centers within the
scan range. Thus a real resonance in this scan should produce a large and obvious
dip in readout 2 relative to readout 1.

Observed quantitative comparison

The measured combined readouts have mean readout_1 = 49.62 and mean readout_2 =
49.09, giving mean readout_2/readout_1 = 0.990. The minimum observed ratio is
0.925 at 3.880 GHz, a dip of only 3.73 counts or 7.5%. This is far smaller than
the approximately 22% / 11-count dip predicted for a resonant 52 ns pulse at
mod_depth = 1.

The per-average traces are noisy and the apparent low points are not a strong
independent repeatability test because only two averages are stored and stored
averages can reflect tracking cadence. Fitting the fixed-contrast Rabi response
does not materially improve over a constant-ratio no-resonance model; the best
fit prefers a resonance center outside the scanned region and still has only a
shallow sampled minimum near 0.967 after baseline scaling.

Decision

The expected physical signal for a pODMR resonance is much larger than the
observed variations. The data do not show the required resonant readout-2 dip, so
I decide resonance_absent.
