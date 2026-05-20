Case podmr_010_2026-05-16-114624

I used the provided sequence XML and the raw export values, without labels or external context.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is inactive.
- readout 1 is the detection immediately after optical polarization, i.e. the true m_S = 0 fluorescence reference.
- readout 2 is the detection after the microwave rabi_pulse_mod_wait_time block.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already on the 4 ns grid and remains 52 ns after rounding.

Physical model calculation:
- Given Rabi frequency 10 MHz at mod_depth = 1, the resonant transition probability for a square Rabi pulse is
  P = sin^2(pi * f_Rabi * t).
- For f_Rabi = 10 MHz and t = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With setup contrast scale 22%, the expected resonant readout-2 fluorescence drop relative to the m_S = 0-like off-resonance level is
  0.22 * 0.996 = 0.219, or 21.9%.

Quantitative comparison to the measured data:
- The first eight readout-2 points, before the dip, average 39.683 counts.
- The readout-2 minimum is 31.192 counts at 3.875 GHz.
- Observed fractional drop = (39.683 - 31.192) / 39.683 = 0.214, or 21.4%.
- Expected resonant readout-2 value from the model = 39.683 * (1 - 0.219) = 30.987 counts, matching the observed 31.192 counts.
- At the same point, readout 1 is 40.904 counts, giving readout2/readout1 = 0.763, again consistent with about 22% contrast.
- A square-pulse detuning model P(detuning) = Omega^2/(Omega^2 + Delta^2) * sin^2(pi * t * sqrt(Omega^2 + Delta^2)) gives expected readout-2 values of about 31.0 at zero detuning, 33.1 at 5 MHz detuning, and 37.3 at 10 MHz detuning, consistent with a localized dip over a few 5 MHz samples rather than a broad tracking drift.

Decision:
The readout-2 dip has the expected sign, location-like localization, and amplitude for a resonant 52 ns pi-like Rabi pulse at mod_depth = 1. Readout 1 lacks a comparable narrow dip at the same frequency and serves as the pumped reference. Stored averages are not treated as an independent repeatability proof, but their overlay is compatible with the same feature. I therefore decide that a pODMR resonance is present.
