Case podmr_064_2026-05-17-065956

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The scan sequence is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence XML, full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- The first active detection happens immediately after adj_polarize, so readout 1 is the m_S = 0 fluorescence reference.
- The second active detection happens after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so readout 2 is the microwave-pulse signal readout.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(length_rabi_pulse * sample_rate) keeps the pulse at 13 samples = 52 ns.
- mod_depth = 1.

Quantitative physical model:
- Setup Rabi frequency: f_R = 10 MHz * mod_depth = 10 MHz.
- Rectangular-pulse transition probability versus detuning Delta is
  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).
- On resonance, tau = 52 ns gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale C = 0.22, the expected on-resonance fractional drop in readout 2 relative to readout 1 is C * P(0) = 0.219.
- Because the frequency step is 5 MHz, any resonance inside the sampled range is at most 2.5 MHz from a sampled point. At 2.5 MHz detuning, the same model gives P = 0.929 and expected fractional drop = 0.204.
- The mean readout 1 level is 50.97 raw counts, so the minimum expected in-range resonance effect at the nearest sampled point is about 10.42 counts below the reference.

Observed data check:
- Mean readout 1 = 50.973; mean readout 2 = 50.921.
- Mean(readout 2 - readout 1) = -0.052 counts, with sample standard deviation 1.376 counts across scan points.
- The largest observed drop is readout 2 / readout 1 = 0.946, i.e. 5.4 percent or 2.85 counts, far smaller than the at least 20.4 percent or 10.42 count drop expected for an in-range resonance.
- A fixed-amplitude Rabi-line fit using the 22 percent contrast and allowing only a baseline offset gives RSS = 0.0722 over line centers inside the scan, worse than the flat model RSS = 0.0143.
- If the line amplitude is allowed to float freely, the best inside-scan dip amplitude is only about 3.1 percent, well below the physical expectation for mod_depth = 1 and a 52 ns pulse.

Decision:
The expected pODMR resonance signal for the active pulse sequence would be large and broad enough to be unmistakable at the sampled spacing. The measured readout 2 signal stays near the m_S = 0 reference and does not show the required drop, so the resonance is absent.
