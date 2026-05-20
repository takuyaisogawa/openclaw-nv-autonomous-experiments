Case: podmr_007_2026-05-16-013306

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first runs adj_polarize, then detection. This first detection is the true m_S = 0 reference readout and is not preceded by the scanned microwave pulse.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- The active experiment pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second detection is the signal readout after the scanned microwave pulse.
- The relevant active pulse duration is length_rabi_pulse = 52 ns. The supplied sequence XML variable list gives mod_depth = 1.

Quantitative model:
- Given setup Rabi frequency f_Rabi ~= 10 MHz at mod_depth = 1 and linear scaling, f_Rabi = 10 MHz.
- For a square resonant pulse, the transferred population is modeled as P = sin^2(pi f_Rabi t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With m_S = 0 to m_S = +1 contrast scale 22%, expected fluorescence depletion on resonance is 0.22 * 0.996 = 0.219, or 21.9% of the bright reference.
- The off-resonant signal-readout baseline estimated from readout 2 excluding the central dip points is 35.27 counts, giving an expected on-resonance drop of 35.27 * 0.219 = 7.73 counts.

Observed data comparison:
- Readout 1, the pre-microwave m_S = 0 reference, remains relatively flat: mean 35.99, min 34.31, max 37.21.
- Readout 2, the post-microwave signal, has a pronounced dip with minimum 28.21 counts at 3.880 GHz.
- Relative to the off-resonant baseline 35.27 counts, the observed drop is 7.06 counts, or 20.0%.
- A simple Gaussian-dip fit to readout 2 gives center 3.8775 GHz, amplitude 7.60 counts, sigma 5.76 MHz, and reduces SSE from 127.06 for a flat model to 32.12. The same dip-style fit gives only weak improvement for readout 1 and a much smaller apparent amplitude.

Decision:
The expected resonant pulse effect is a near-maximum 22% fluorescence depletion, and the post-pulse readout shows a quantitatively matching dip of about 20% centered in the scan while the pre-pulse reference does not. A pODMR resonance is present.
