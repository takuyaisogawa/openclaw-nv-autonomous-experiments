Case: podmr_016_2026-05-12-120649

Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first acquire a true m_S = 0 reference using adj_polarize followed by detection.
- full_expt = 0, so the optional "1 level reference" branch is inactive even though do_adiabatic_inversion is true. Thus there is no active independent m_S = +1 reference in this scan.
- The active experiment readout is after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- Readout roles: readout 1 is the 0-level laser-polarized reference; readout 2 is the post-microwave Rabi-pulse readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already on the 4 ns sample grid.

Explicit physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling, f_R = 10 MHz.
- For a resonant square pulse, the transferred population is P = sin^2(pi * f_R * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should reduce fluorescence by approximately 0.22 * 0.996 = 0.219, or 21.9% relative to the 0 reference.
- The mean 0-reference readout is about 25.73 counts, so the expected on-resonance drop is about 5.64 counts, giving a post-pulse readout near 20.1 counts at resonance if the sequence is driving the transition.

Data comparison:
- Combined readout 1 mean: 25.73.
- Combined readout 2 mean: 26.17.
- Mean fractional difference, readout2 vs readout1: +1.7%, not a 21.9% drop.
- The readout2/readout1 ratio ranges from about 0.947 to 1.096. The lowest ratios correspond to about 5.3% apparent drops, much smaller than the expected resonant pi-pulse contrast and not forming a convincing localized resonance feature.
- Both readouts show broad drift across the scan. The stored two averages have strongly different slow trends, consistent with tracking cadence or drift rather than an independent repeatability test of a resonance.
- A simple line-plus-Lorentzian comparison on the readout ratio gives only a modest improvement over a linear drift baseline and chooses a narrow positive feature near 3.905 GHz rather than the expected fluorescence dip from resonant spin transfer.

Decision:
The active pulse should produce a large, localized fluorescence decrease if a pODMR resonance is present, but the measured post-pulse readout does not show the expected magnitude or shape after accounting for reference behavior and drift. I therefore classify this case as resonance_absent.
