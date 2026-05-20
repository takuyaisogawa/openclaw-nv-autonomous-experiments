Case: podmr_067_2026-05-17-074342

Active sequence and readout roles

The sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. The active detections are:

1. readout 1: after adj_polarize, before the microwave pulse. This is the bright m_S = 0 reference / tracking readout.
2. readout 2: after a rabi_pulse_mod_wait_time pulse, followed by detection. This is the pODMR signal readout.

Relevant pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already aligned to 13 samples, so the rounded duration remains 52 ns.

Expected signal model

Given the domain facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square pulse with resonant Rabi frequency f_R = 10 MHz and pulse duration t = 52 ns, the resonant transfer probability is

P_on = sin^2(pi * f_R * t)
     = sin^2(pi * 10e6 * 52e-9)
     = 0.996.

With a setup contrast scale of about 22% and a bright reference near the readout 1 mean of 48.92 raw-count units, a real resonance should cause an on-resonance loss in the post-pulse signal of about

48.92 * 0.22 * 0.996 = 10.72 raw-count units.

I also used the detuned square-pulse response

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz and Delta = 2*pi*(f - f0), as an explicit quantitative line-shape model. Fitting readout 2 to c + A*P(f) over trial resonance centers gives the best least-squares result outside the scanned band at f0 = 3.8125 GHz with A = +17.35, i.e. the wrong sign for an ODMR dip. The physically expected amplitude sign and scale would be A approximately -10.76 raw-count units.

Observed data

Mean readout 1 is 48.92 with population standard deviation 0.78. Mean readout 2 is 48.76 with population standard deviation 1.22. The pointwise readout2 - readout1 differences have mean -0.16, standard deviation 1.53, minimum -2.35, and maximum +2.96 raw-count units.

The observed fluctuations are far smaller than the approximately 10.7-count loss expected from the active near-pi pulse at resonance, and the quantitative line-shape fit does not find a negative resonance-shaped feature. Stored averages are not treated as strong independent repeatability evidence because they can reflect tracking cadence.

Decision: resonance_absent.
