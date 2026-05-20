Case: podmr_026_2026-05-16-182622

Sequence identification:

The XML sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, pumping_time = 1 us, wait_time = 2 us, and length_last_wait = 1 us.

The instruction block first polarizes and detects, so readout 1 is the bright mS = 0 reference. The optional "Acquire 1 level reference" block is skipped because full_expt = 0, even though do_adiabatic_inversion is true. The active measurement pulse is therefore a single rabi_pulse_mod_wait_time call with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection; readout 2 is the post-microwave signal readout.

Expected signal calculation:

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square pulse, the transition probability versus detuning df is

P_flip(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * tau),

with f_R = 10 MHz and tau = 52 ns. On resonance this gives P_flip(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With a 22% mS = 0 to mS = +1 contrast scale, the expected fractional PL change in readout 2 relative to readout 1 is about -0.22 * 0.996 = -21.9%. At the observed mean readout-1 level of 49.61 counts, that is an expected drop of about 10.87 counts.

The scan grid spacing is 5 MHz, so a resonance inside the scanned range should be no more than 2.5 MHz from a sampled point. The same model gives P_flip(2.5 MHz) = 0.929, expected drop = 20.4% or about 10.14 counts. At 5 MHz detuning the expected drop is still 16.5% or about 8.17 counts. Thus an in-range pODMR resonance from this pulse should create a large localized suppression in readout 2.

Observed data:

The combined readout means are readout 1 = 49.61 and readout 2 = 49.58. The pointwise difference readout2 - readout1 has mean -0.027 counts, standard deviation 1.47 counts, minimum -3.10 counts, and maximum +3.17 counts. In relative units the most negative point is -5.94% at 3.835 GHz, far smaller than the expected about -20% to -22% near a true resonance. A second negative feature near 3.900 GHz is only about -4.23%, and the trace also contains positive differences of similar magnitude.

I also compared the measured relative signal to the explicit Rabi-response model over candidate resonance centers across the scan. A flat model has SSE 0.0175 in relative units. The fixed 22% contrast Rabi model, allowing only a constant baseline offset and scanning the resonance center, gives a worse best SSE of 0.0661. If the response amplitude is allowed to float, the best fitted amplitude is only 0.0438, about one fifth of the expected contrast scale, which is consistent with noise rather than the predicted spin-flip response.

Decision:

The active pulse would have produced an approximately pi-pulse response and a large readout-2 suppression if a resonance were present in the scanned band. The measured readout differences are small, inconsistent across frequency, and much closer to noise than to the quantitative physical model. I therefore decide that a pODMR resonance is absent.
