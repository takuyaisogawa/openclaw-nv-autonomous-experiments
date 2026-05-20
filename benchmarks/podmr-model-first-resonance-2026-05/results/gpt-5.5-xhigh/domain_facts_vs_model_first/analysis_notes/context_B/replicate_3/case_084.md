Case: podmr_070_2026-05-17-082720

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels,
previous outputs, sibling cases, or external context.

Sequence interpretation

The active sequence is Rabimodulated.xml. In inputs/sequence.xml, the relevant
settings are:

- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, rounded by the sequence to the sample clock; this is
  already exactly 13 samples at 250 MHz
- mod_depth = 1
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped
- do_adiabatic_inversion = 1 is present as a boolean variable, but no active
  adiabatic inversion instruction runs because that code is commented and the
  full_expt reference block is disabled

The executed readout roles are therefore:

1. Readout 1: after adj_polarize, before the swept microwave pulse. This is the
   pumped mS = 0 reference readout.
2. Readout 2: after a swept 52 ns rabi_pulse_mod_wait_time pulse at mod_depth 1.
   This is the signal readout that should drop near resonance if the pulse drives
   population from mS = 0 to mS = +1.

Physical model calculation

Given facts:

- mS = 0 to mS = +1 contrast scale C = 0.22
- Rabi frequency at mod_depth = 1 is f_R = 10 MHz
- pulse duration tau = 52 ns

For a rectangular driven two-level pulse, using detuning delta in cycles/s:

P_1(delta) = f_R^2 / (f_R^2 + delta^2) *
             sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

The predicted fluorescence ratio is:

signal/reference = 1 - C * P_1(delta)

At zero detuning:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996
signal/reference = 1 - 0.22 * 0.996 = 0.781

The observed readout-1 mean is 50.71 counts, so an on-resonance point should be
about 50.71 * 0.781 = 39.60 counts, an expected drop of about 11.11 counts.
Even at 5 MHz detuning, the model gives P_1 = 0.749 and an expected drop of
about 8.35 counts. At 10 MHz detuning, the expected drop is still about
3.05 counts.

Observed data check

The combined readouts from raw_export.json have:

- readout 1 mean = 50.71, standard deviation across scan = 1.35
- readout 2 mean = 50.23, standard deviation across scan = 1.69
- readout 2 - readout 1 mean = -0.48 counts
- most negative readout 2 - readout 1 point = -1.96 counts
- normalized contrast 1 - readout2/readout1 ranges from -0.033 to 0.039

The largest observed post-pulse deficit is only about 1.96 counts, or 3.9% of
the local reference. This is far below the predicted 22% on-resonance contrast
and also below the expected several-count response for a resonance within one
or two 5 MHz scan steps.

I also fit the normalized contrast to the Rabi line-shape model with a linear
background. The best nonnegative resonance amplitude was about 0.047, compared
with the expected 0.22. The residual improvement over a background-only trend
was small, and the selected edge frequency is not compelling evidence of a
real resonance feature.

Decision

The physically expected pODMR signal for the active 52 ns, mod_depth 1 pulse
would be a large readout-2 depression relative to the mS = 0 reference. The
observed readout-2 trace stays close to readout 1 with only small common drift
and point-to-point fluctuations. I therefore decide that a pODMR resonance is
absent.
