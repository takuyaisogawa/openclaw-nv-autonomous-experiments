Case podmr_074_2026-05-17-092418

Sequence identification:
- Provided XML sequence: Rabimodulated.xml / Rabimodulated.
- The active microwave pulse is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)` followed by detection.
- `full_expt = 0`, so the optional m_S = +1 reference block is inactive.
- Readout roles: readout 1 is the true m_S = 0 optical reference immediately after polarization; readout 2 is the signal readout after the Rabi-modulated microwave pulse.
- `length_rabi_pulse = 52 ns`, rounded at 250 MS/s but unchanged because 52 ns is 13 samples.
- `mod_depth = 1`.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a resonant rectangular pulse, the transferred population is modeled as P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional fluorescence drop on resonance is C * P = 0.219.
- The mean readout 1 level is 49.08 counts, so the expected on-resonance readout-2 drop is 49.08 * 0.219 = 10.75 counts.

Data comparison:
- Mean readout 1 = 49.08 counts.
- Mean readout 2 = 48.78 counts.
- Mean paired difference readout2 - readout1 = -0.29 counts, with standard deviation 1.72 counts over scan points.
- The largest observed paired drop is 3.92 counts at 3.900 GHz, only 7.7% of the local readout 1 level, far below the expected 21.9% drop.
- A fixed-amplitude Lorentzian-like dip model using the expected 10.75 count drop was tested over centers at the scan points and HWHM values of 5, 10, 15, 20, and 30 MHz. Its best SSE was 117.0, worse than the flat paired-difference model SSE of 59.2.

Decision:
The sequence should produce a large readout-2 fluorescence dip if a resonance is present, but the measured signal does not show the expected amplitude or model improvement. I classify this case as resonance_absent.
