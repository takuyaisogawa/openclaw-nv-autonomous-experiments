Case podmr_008_2026-05-16-014743 analysis

Sequence and readout roles:
- The scan sequence is Rabimodulated.xml / Rabimodulated.
- The instruction block first performs adj_polarize followed by detection, giving the true m_S = 0 optical reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is inactive.
- The active experimental readout is after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- The relevant variables are length_rabi_pulse = 52 ns, mod_depth = 1, mw_freq swept from 3.825 GHz to 3.925 GHz, and freqIQ = 50 MHz.

Quantitative model:
- Given the setup fact f_Rabi(mod_depth=1) ~= 10 MHz and approximately linear scaling with mod_depth, the active pulse has f_Rabi ~= 10 MHz.
- For a resonant square Rabi pulse, P(m_S=+1) = sin^2(pi f_Rabi t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the setup contrast scale of about 22% between m_S = 0 and m_S = +1, the expected resonant readout drop is 0.22 * 0.996 = 0.219, or about 21.9% of the bright reference.
- Using the off-dip median of readout 2, about 41.37 counts, the expected resonant readout is 41.37 * (1 - 0.219) = 32.30 counts.

Data comparison:
- Readout 1, the m_S = 0 reference, stays near 41.44 counts with standard deviation about 1.01 counts.
- Readout 2, the post-Rabi signal, has an off-dip median near 41.37 counts and a minimum of 31.31 counts at 3.875 GHz.
- The measured fractional drop is (41.37 - 31.31) / 41.37 = 24.3%, close to the 21.9% model expectation.
- The dip is localized in the active post-pulse readout and is also visible in both stored averages, although stored averages are not treated as a strong independent repeatability test.

Decision:
The sequence and quantitative Rabi/contrast model predict a large resonant depletion for this pulse, and the measured active readout shows a localized depletion of the expected size while the reference readout remains bright. I decide that a pODMR resonance is present.
