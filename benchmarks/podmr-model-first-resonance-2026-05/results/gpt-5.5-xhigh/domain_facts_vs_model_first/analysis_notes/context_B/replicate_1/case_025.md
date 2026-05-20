Case: podmr_010_2026-05-16-114624

Sequence interpretation

The active sequence is Rabimodulated.xml, scanned in mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence XML uses sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, freqIQ = 50 MHz, and delay_wrt_1mus = 0.2 us.

The instruction order is:

1. adj_polarize, then detection: this is the true m_S = 0 bright-state reference and corresponds to readout 1.
2. The "Acquire 1 level reference" block is skipped because full_expt = 0.
3. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detection: this is the pODMR signal after the microwave pulse and corresponds to readout 2.

Physical model calculation

Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. With a 52 ns pulse, the on-resonance transfer probability for a square pulse is

P1(Delta=0) = sin^2(pi * f_Rabi * tau)
            = sin^2(pi * 10e6 * 52e-9)
            = 0.996.

Using the 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance readout ratio is

signal/reference = 1 - 0.22 * P1 = 0.781.

For detuning Delta, I used the driven two-level expression

P1(Delta) = f_Rabi^2 / (f_Rabi^2 + Delta^2)
            * sin^2(pi * sqrt(f_Rabi^2 + Delta^2) * tau).

This gives expected signal/reference ratios:

- Delta = 0 MHz: 0.781
- Delta = 5 MHz: 0.835
- Delta = 10 MHz: 0.940
- Delta = 12.5 MHz: 0.978
- Delta = 15 MHz: 0.997

Data comparison

Normalizing the pODMR readout by the bright reference gives a clear dip:

- 3.870 GHz: readout2/readout1 = 0.824, contrast = 17.6%
- 3.875 GHz: readout2/readout1 = 0.763, contrast = 23.7%
- 3.880 GHz: readout2/readout1 = 0.843, contrast = 15.7%

The off-dip points are mostly near a ratio of about 0.95 to 1.00, with scatter and tracking drift. A fixed-physics fit using f_Rabi = 10 MHz, tau = 52 ns, and contrast = 22%, with only the center frequency and overall baseline factor fitted, gives:

- fitted center = 3.8753 GHz
- fitted baseline factor = 0.9939
- SSE = 0.0146

For comparison, a constant-ratio model gives SSE = 0.0914 and a linear baseline without resonance gives SSE = 0.0901. Allowing the contrast amplitude to float gives a fitted contrast amplitude of 0.216, essentially the expected 0.22, centered at 3.8753 GHz.

Stored averages are not treated as a strong independent repeatability test, but they are consistent with the same feature: both averages have their minimum normalized signal at 3.875 GHz.

Decision

The measured dip magnitude, width, and center match the expected near-pi-pulse pODMR response for the active 52 ns, mod_depth = 1 Rabimodulated sequence. A pODMR resonance is present.
