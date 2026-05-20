Case: podmr_008_2026-05-16-014743

Inputs used:
- inputs/sequence.xml and the embedded Sequence/Variable_values in inputs/raw_export.json.
- No labels, previous outputs, sibling cases, or external context were used.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions polarize, detect the true m_S = 0 reference, wait, apply one modulated Rabi pulse, then detect the pulsed readout.
- full_expt = 0, so the optional m_S = 1 reference block is inactive even though it remains in the XML.
- Readout 1 is therefore the direct post-polarization m_S = 0 fluorescence reference.
- Readout 2 is the fluorescence after the microwave Rabi pulse and is the resonance-sensitive pODMR channel.
- mod_depth = 1 from Variable_values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already on the 4 ns sample grid.

Quantitative expected signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant two-level transfer probability for a rectangular pulse of duration t is:
  P_1 = sin^2(pi f_R t / 2).
- With t = 52 ns and f_R = 10 MHz:
  P_1 = sin^2(pi * 10e6 * 52e-9 / 2) = 0.5314.
- The stated optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected fractional fluorescence loss on resonance is:
  0.22 * 0.5314 = 0.1169, or about 11.7%.
- Using the off-resonance readout-2 baseline excluding the central dip region (indices 9-12), the baseline is 40.99 counts, so the expected resonant drop is about 4.79 counts.

Observed data calculation:
- Readout 2 has a minimum at 3.875 GHz: 31.31 counts.
- Off-resonance readout-2 baseline, excluding 3.870-3.885 GHz points, is 40.99 counts.
- Observed central drop is 9.68 counts, about 23.6% of that baseline.
- Off-resonance readout-2 scatter over the same excluded-baseline set has sigma = 1.28 counts, making the central drop about 7.6 sigma relative to the off-resonance scatter.
- Normalizing readout 2 by readout 1 gives an off-resonance ratio baseline of 0.990 and a minimum at 3.875 GHz with a fractional ratio drop of about 25.5%.
- The dip is also visible in both stored averages at the same central region, although the averages are treated mainly as tracking cadence and not as a strong repeatability test.

Decision:
The relevant channel is readout 2, and it shows a centered, quantitatively large dip consistent with the expected pODMR response of the 52 ns mod_depth 1 Rabi pulse. The observed dip is larger than the simple expected 11.7% contrast estimate, but it is in the correct direction, localized in frequency, and far above off-resonance scatter. I therefore decide that a pODMR resonance is present.
