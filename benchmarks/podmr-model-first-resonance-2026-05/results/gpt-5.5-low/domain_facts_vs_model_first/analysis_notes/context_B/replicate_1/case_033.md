Case: podmr_018_2026-05-16-134409

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 role: after adj_polarize only, so it is the bright m_S = 0 reference for each frequency point.
- Readout 2 role: after adj_polarize, a modulated microwave Rabi pulse, and detection, so it is the signal channel that should dip if the microwave pulse drives the NV transition.
- mod_depth = 1 in the provided sequence XML variable list.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the rounded pulse duration remains 52 ns.

Quantitative expected signal model:

Use the supplied setup facts: contrast between m_S = 0 and m_S = +1 is about 22%, and Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For the active pulse, f_R = 10 MHz and t = 52 ns. On resonance the driven population transfer is modeled as

P_transfer = sin^2(pi * f_R * t)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

The expected resonant fluorescence reduction in readout 2 relative to the m_S = 0 bright level is therefore

expected fractional dip = 0.22 * 0.996 = 0.219, or about 21.9%.

Using the combined data, the off-resonance readout-2 baseline excluding the central dip region is about 47.08 counts, giving an expected resonant drop of about 10.32 counts for a full-contrast ideal case. A local off-resonance baseline around the dip, using nearby points outside the minimum region, is about 47.31 counts. The observed readout-2 minimum is 38.96 counts at 3.880 GHz, so the observed local drop is about 8.35 counts, or 17.7%.

Readout 1 remains comparatively flat: mean 48.07 counts with population standard deviation 1.05 counts. The readout-2 central feature is therefore not mirrored in the bright reference channel. Stored averages both show the same broad readout-2 depression around the same frequency region, but I do not treat that as a strong independent repeatability test because stored averages can mainly reflect tracking cadence.

Decision:

The active physical model predicts a large negative readout-2 feature for a resonance, and the measured signal shows a localized readout-2 dip of the expected sign and roughly expected scale near 3.875-3.880 GHz while readout 1 stays near baseline. I therefore decide that a pODMR resonance is present.
