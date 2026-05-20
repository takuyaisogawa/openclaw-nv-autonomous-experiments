Case: podmr_076_2026-05-17-095337

Sequence/readout identification

The provided XML is Rabimodulated.xml. The scan variable is mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active sequence first polarizes
the NV center and immediately performs detection:

  adj_polarize(...) -> detection(...)

This first detection is therefore the true m_S = 0 reference readout
("readout 1" in the raw export). The optional m_S = 1 reference branch is
guarded by full_expt, and full_expt = 0, so that branch is inactive even
though do_adiabatic_inversion is true. The sequence then applies the active
pODMR microwave pulse:

  rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)

followed by detection. This second detection is the pODMR signal after the
microwave pulse ("readout 2" in the raw export).

Pulse parameters from the XML:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so the rounded pulse length remains 13 samples =
  52 ns

Physical model calculation

For a rectangular Rabi pulse with Rabi frequency f_R = 10 MHz at mod_depth = 1,
the transition probability versus detuning df is

  P(df) = f_R^2 / (f_R^2 + df^2) *
          sin^2(pi * t * sqrt(f_R^2 + df^2)).

With t = 52 ns:

- P(0 MHz) = 0.996
- P(5 MHz) = 0.749
- P(10 MHz) = 0.273
- P(15 MHz) = 0.012

Using the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected
normalized signal readout2/readout1 is:

- on resonance: 1 - 0.22 * 0.996 = 0.781
- 5 MHz detuned: 1 - 0.22 * 0.749 = 0.835
- 10 MHz detuned: 1 - 0.22 * 0.273 = 0.940

Thus any resonance inside the scanned range should create a broad, multi-point
dip in readout 2 relative to readout 1. At the observed count level of about
51 counts, the on-resonance drop expected from this near-pi pulse is about
11 counts.

Observed data/model comparison

The measured normalized ratios readout2/readout1 have mean 0.996 and standard
deviation 0.0277. The minimum ratio is only 0.948 at 3.905 GHz, a drop of about
5.2% or 2.63 counts relative to the paired reference. Neighboring points do
not show the expected broad Rabi lineshape: the ratios at 3.900 and 3.910 GHz
are 1.002 and 1.010.

I fit the normalized trace to two models:

- null model: constant plus linear baseline, SSE = 0.0153
- physical resonance model with fixed 22% contrast and the 10 MHz, 52 ns
  Rabi response, scanning the unknown resonance center across the full range,
  best SSE = 0.0499

The fixed physical resonance model is substantially worse than the baseline.
Allowing the resonance amplitude to float gives a best amplitude of only 0.034,
far below the expected 0.22 contrast for this pulse, and the improvement over
baseline is small and not physically persuasive. Since stored averages can
track cadence rather than repeatability, I do not treat the two averages as a
strong independent confirmation.

Decision

No pODMR resonance is present in this scan. The active pulse should produce a
large, broad normalized fluorescence dip if it hits resonance, and the measured
trace shows only small unstructured fluctuations.
