Active sequence and roles

The provided sequence is Rabimodulated.xml. With full_expt = 0, the conditional "Acquire 1 level reference" block is inactive. The actually acquired pair is therefore:

1. readout 1: detection immediately after adj_polarize, the true m_S = 0 optical reference.
2. readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, the pODMR signal readout.

The relevant active pulse parameters from the provided XML/exported variable values are mod_depth = 1 and length_rabi_pulse = 52 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Explicit signal model

Use the supplied setup facts:

- Optical contrast between m_S = 0 and m_S = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Rabi frequency scales linearly with mod_depth, so here f_R = 10 MHz.

For a square resonant Rabi pulse, the population transferred out of m_S = 0 is

P_1(t) = sin^2(pi f_R t).

With t = 52 ns and f_R = 10 MHz:

P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected signal/reference ratio on resonance is then

R_sig / R_ref = 1 - C * P_1 = 1 - 0.22 * 0.996 = 0.781.

At the observed mean reference readout of 47.11 counts, a resonant pi-like response should give a signal readout near 36.79 counts, a drop of about 10.32 counts.

Data comparison

The combined readouts have mean readout 1 = 47.114 and mean readout 2 = 47.554. The pointwise signal/reference ratios range from 0.976 to 1.041, with the minimum at 3.885 GHz. The largest observed signal drop is only 1.19 counts, and most points have readout 2 above readout 1. This is not compatible with the expected 10.32 count resonant drop from the active 52 ns, mod_depth 1 pulse.

Stored per-average overlays show drift/tracking-scale offsets and are not treated as an independent repeatability test, consistent with the prompt guidance. They do not reveal a reproducible resonance-shaped depletion.

Decision

No pODMR resonance is present. The physically expected resonant signal is a large negative contrast in the post-pulse readout relative to the m_S = 0 reference, but the measured ratios stay near unity and never approach the modeled on-resonance ratio of about 0.78.
