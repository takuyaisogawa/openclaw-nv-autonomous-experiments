Case podmr_057_2026-05-17-051839

Sequence and roles

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The saved active variable values in raw_export.json are the run state: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, delay_wrt_1mus = 0.2 us.

The instruction block first polarizes and detects immediately. With full_expt = 0, the optional "Acquire 1 level reference" block is skipped. It then applies one rabi_pulse_mod_wait_time pulse with length_rabi_pulse and mod_depth, followed by detection. Therefore readout 1 is the bright m_S = 0 reference, and readout 2 is the post-microwave-pulse readout whose value should drop at resonance.

Expected signal model

Given the stated setup calibration, f_Rabi ~= 10 MHz * mod_depth = 10 MHz. For a square resonant pulse with duration t = 52 ns, the transition probability is

P_flip = sin^2(pi * f_Rabi * t)
       = sin^2(pi * 10e6 * 52e-9)
       = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected fractional pODMR drop in readout 2 at resonance is approximately

C_expected = 0.22 * P_flip = 0.219, or 21.9%.

The mean readout level is about 45.5 counts, so the expected absolute resonant drop is

45.5 * 0.219 = 10.0 counts.

Data comparison

The observed combined readout difference readout2 - readout1 has mean -0.035 counts and standard deviation 0.985 counts across scan points. Individual differences range from -2.08 to +1.79 counts, or roughly -4.5% to +4.0% relative to readout 1. The most negative single endpoint is only -2.08 counts, and the strongest three-point averaged negative feature is about -0.67 counts. This is far smaller than the approximately -10 count signal expected from a near-pi pulse on resonance.

The apparent fluctuations also alternate in sign and do not show a robust resonance-shaped depletion of the post-pulse readout. Stored averages are only two and can reflect tracking cadence, so they do not provide a strong independent repeatability test.

Decision

A pODMR resonance is absent in this scan. The physical model predicts an on-resonance signal near the full 22% contrast scale, but the observed differential signal is consistent with small noise or drift and lacks the expected large readout-2 depletion.
