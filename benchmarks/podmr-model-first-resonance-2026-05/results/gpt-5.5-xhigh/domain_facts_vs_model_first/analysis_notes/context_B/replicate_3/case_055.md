Case podmr_041_2026-05-16-224136

Active sequence and readout roles:
- The provided XML is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is the polarized mS = 0 reference acquired immediately after adj_polarize.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time.
- mod_depth = 1 from the provided sequence variable values.
- length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz, the rounding step leaves this at 13 samples = 52 ns.

Quantitative model:
Using the stated setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a rectangular pulse of duration t = 52 ns, I used

P1(delta) = (fr^2 / (fr^2 + delta^2)) * sin^2(pi * t * sqrt(fr^2 + delta^2))

with fr = 10 MHz in cycles/s. The readout model is

S2 / S1 = 1 - C * P1(delta)

with contrast C = 0.22.

On resonance, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, giving expected S2/S1 = 0.7809. With the observed readout-1 baseline near 46.35 counts, this would be a drop of about 10.1 counts. The model still predicts a strong multi-point feature at the scan spacing: at 5 MHz detuning, P1 = 0.749 and S2/S1 = 0.835; at 10 MHz detuning, P1 = 0.273 and S2/S1 = 0.940.

Observed data:
- Combined readout-1 mean = 46.354 counts.
- Combined readout-2 mean = 46.142 counts.
- S2/S1 mean = 0.9955, minimum = 0.9437, maximum = 1.0484.
- The deepest observed drop is 2.60 counts, or about 5.6%, far smaller than the expected 22% pi-pulse contrast.

I also fit the normalized trace to y = b - A * P1(f - f0) over candidate f0 values. The best fit gives A/b = 0.052, only about one quarter of the expected 0.22 contrast. A fixed-contrast physical model with C = 0.22 fits worse than a constant trace: RSS = 0.0655 versus constant-trace RSS = 0.0192. The stored averages have large offsets consistent with tracking cadence, so I did not treat their similarity or difference as a strong independent repeatability test.

Decision:
The active pulse should produce a large, broad normalized dip if a pODMR resonance is within the scanned range. The measured trace shows only small fluctuations and rejects the expected-contrast physical model, so I classify this case as resonance_absent.
