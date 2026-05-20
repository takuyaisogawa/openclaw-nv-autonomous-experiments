Case: podmr_004_2026-05-16-005019

Sequence interpretation from the provided XML:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first polarizes the NV and performs detection. Because this is before any microwave pulse in the main experiment, the first readout is the m_S = 0 fluorescence reference.
- The optional "1 level reference" block is inactive because full_expt = 0, so there is no separate m_S = +1 reference in the acquired readouts.
- The active microwave operation is then PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second readout is the pODMR signal after the microwave pulse.
- Active pulse settings: mod_depth = 1, length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so the rounding step gives round(52 ns * 250 MHz) = 13 samples, i.e. 52 ns exactly.

Expected quantitative signal:

Use the two-level rectangular-pulse model for a transition driven with Rabi frequency f_R and detuning df:

P_1(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * t).

The setup facts give f_R = 10 MHz * mod_depth = 10 MHz. With t = 52 ns,

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The m_S = 0 to m_S = +1 fluorescence contrast scale is about 22%, so the expected on-resonance normalized readout is approximately

1 - 0.22 * 0.996 = 0.781,

or a resonant dip of about 21.9% relative to the m_S = 0 fluorescence level. For the measured off-resonant signal level near 40.5 counts, this corresponds to an expected minimum near 31.6 counts.

Data comparison:

- First readout: mean 41.15 counts, standard deviation 0.85 counts, no comparable narrow central dip.
- Second readout: off-dip baseline about 40.50 counts, minimum 31.81 counts at 3.880 GHz. This is an 8.69 count drop, or 21.5% of the off-dip signal level.
- The signal/reference ratio has a minimum of 0.785 near 3.875 GHz, very close to the 0.781 expectation from the 52 ns, mod_depth = 1 pulse model.
- Fitting the fixed-contrast rectangular-pulse model to the signal/reference ratio gives a resonance center near 3.878 GHz and reduces the sum of squared error by about 81% relative to a flat model. A free-contrast version gives contrast about 0.224, consistent with the stated 22% contrast scale.

The stored per-average traces both show the same central feature, but I do not treat the two stored averages as a strong independent repeatability test because they can reflect tracking cadence. The decision is based on the active pulse model and the combined readout behavior.

Decision: resonance_present.
