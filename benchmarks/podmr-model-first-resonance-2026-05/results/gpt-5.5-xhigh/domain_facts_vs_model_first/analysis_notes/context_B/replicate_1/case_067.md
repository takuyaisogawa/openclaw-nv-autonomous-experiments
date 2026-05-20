Case: podmr_053_2026-05-17-042031

Sequence interpretation

The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence polarizes the NV, acquires a first detection window labeled in the XML as the true m_S = 0 level reference, waits, applies one modulated Rabi microwave pulse, and then acquires a second detection window. The full_expt variable is 0, so the optional m_S = +1 reference branch is not active. The do_adiabatic_inversion variable is true, but the adiabatic inversion calls are commented out and are inside the inactive full_expt branch, so they are not active in this run.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At sample_rate = 250 MHz, the pulse duration rounds to 13 samples, still 52 ns.

Quantitative physical model

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is approximately f_R = 10 MHz. For a square pulse of duration t = 52 ns, the transition probability versus detuning is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

The expected post-pulse fluorescence relative to the m_S = 0 reference is approximately

signal/reference = baseline * (1 - 0.22 * P(Delta)),

where the 0.22 factor is the current m_S = 0 to m_S = +1 contrast scale. On resonance, P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996, so the expected resonance dip is 21.9 percent. With the observed reference mean of about 45.2 raw units, that is about 9.9 raw units. With the 5 MHz scan step, the same model predicts P(+-5 MHz) = 0.749, or a 16.5 percent dip, about 7.5 raw units. At +-10 MHz the expected dip is still about 6.0 percent, about 2.7 raw units. Therefore a real resonance within the scanned range should be a strong multi-point depression in the second readout relative to the first readout.

Data check

I used readout 1 as the m_S = 0 reference and readout 2 as the post-pulse signal. The normalized signal deficit z = (readout1 - readout2) / readout1 has a maximum of only 0.0717 at 3.880 GHz. Nearby points do not follow the pulse model: at 3.875 GHz the signal is brighter than the reference by about 4.1 percent, at 3.885 GHz the deficit is essentially absent, and at 3.890 GHz there is another isolated 7.0 percent deficit. This is much smaller and less coherent than the expected 22 percent center dip with broad neighboring shoulders.

I also fit the normalized ratio y = readout2 / readout1 to a slowly varying linear baseline plus the square-pulse Rabi line shape, y = a + b(f - mean_f) - A * P(f - f0). The best free-amplitude fit gave A = 0.0436 with standard error 0.0251 and center about 3.8867 GHz. That fitted amplitude is only about 20 percent of the physically expected A = 0.22. The baseline-only fit has RMSE 0.0333 in normalized units, while the free line-shape fit has RMSE 0.0317, only a small improvement. A fixed 22 percent contrast line shape inside the scan fits poorly because it predicts large neighboring-point dips that are not observed.

Stored averages show changes, but they are not a strong independent repeatability test here because stored averages can reflect tracking cadence. I therefore base the decision on the active pulse model and the combined normalized readouts.

Decision

The expected pODMR signal for this sequence would be large and structured across multiple frequency points. The measured differential readout contains only small, isolated fluctuations and does not match the expected 52 ns, mod_depth 1 Rabi-pulse ODMR line shape. I therefore classify this case as resonance_absent.
