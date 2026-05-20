Case: podmr_071_2026-05-17-084118

Sequence identification from inputs/sequence.xml and the embedded sequence in raw_export.json:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 role: after adj_polarize, before the Rabi pulse; this is the true m_S = 0 fluorescence reference.
- Readout 2 role: after the single modulated Rabi pulse; this is the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.

Expected signal calculation:

The setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so here f_R = 10 MHz. For a square resonant Rabi pulse, the transferred population is

  P_transfer = sin^2(pi * f_R * t)

with t = 52 ns. This gives

  f_R * t = 10e6 * 52e-9 = 0.52 cycles
  P_transfer = sin^2(pi * 0.52) = 0.996

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a resonant pODMR feature from this pulse should produce an approximate fractional fluorescence dip of

  0.22 * 0.996 = 0.219, or about 22%

relative to the m_S = 0 reference, subject to linewidth and detuning.

Observed quantitative comparison:

Using the combined readouts, readout2/readout1 ranges from about 0.946 to 1.057. The largest raw fractional decreases are therefore only about 5.4%, much smaller than the expected about 22% resonant dip for this pulse. After subtracting a linear baseline from the readout2/readout1 trace, the most negative residual is about -5.7% at 3.860 GHz, with residual standard deviation about 3.1%. Other negative points of similar scale occur at 3.850, 3.890, 3.905, and 3.915 GHz rather than forming a clear single resonance feature.

The two stored averages are not a strong independent repeatability test because averages can track cadence, but they still do not support a stable resonance: the first average has its most negative readout2-readout1 point at index 7, while the second average has its most negative point at index 18.

Decision:

Given the active 52 ns, mod_depth 1 Rabi pulse, a true on-resonance response should be near a full-contrast pODMR dip of order 22%. The measured deviations are much smaller, scattered, and not consistently repeated across stored averages. I therefore decide that a pODMR resonance is absent in this scan.
