Case: podmr_029_2026-05-16-193002

Sequence and roles

The provided sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence first polarizes the NV, then performs a detection before the microwave pulse. Since full_expt = 0, the conditional "Acquire 1 level reference" block is inactive. Therefore readout 1 is the polarized m_S = 0 reference detection, and readout 2 is the detection after the active Rabi-modulated microwave pulse.

The active microwave pulse is:

- rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)
- length_rabi_pulse = 52 ns, rounded at 250 MS/s and unchanged
- mod_depth = 1 in the provided XML variable values

Physical expected-signal model

Using the supplied setup facts, the on-resonance Rabi frequency at mod_depth = 1 is approximately 10 MHz. For a square pulse with detuning Delta, I used the two-level transition probability

P1(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

with Omega = 10 MHz and t = 52 ns. The fluorescence ratio model is

readout2 / readout1 = baseline * (1 - C * P1)

with C = 0.22 for the m_S = 0 to m_S = +1 contrast scale.

This gives:

- Delta = 0 MHz: P1 = 0.996, expected ratio = 0.781
- Delta = 2.5 MHz: P1 = 0.929, expected ratio = 0.796
- Delta = 5 MHz: P1 = 0.749, expected ratio = 0.835
- Delta = 10 MHz: P1 = 0.273, expected ratio = 0.940
- Delta = 20 MHz: P1 = 0.048, expected ratio = 0.989

Thus a true resonance within the scan should create a broad, large dip in readout2 relative to readout1, with a near-sampled resonance giving approximately 16% to 22% contrast loss.

Data comparison

The combined readout means are:

- readout 1 mean = 44.929
- readout 2 mean = 44.908

The normalized ratios readout2/readout1 have:

- mean = 0.9999
- standard deviation = 0.0281
- minimum = 0.9440
- maximum = 1.0762

The lowest ratio occurs near 3.855 GHz and is only about a 5.6% loss, much smaller than the expected 16% to 22% loss for the 52 ns, mod_depth 1 pulse. It is also not accompanied by the broad model-compatible line shape expected from a 10 MHz Rabi drive.

I also fit the ratio data against the explicit Rabi-detuning model. A constant-baseline null model has SSE = 0.01662. With the expected 22% contrast fixed and the center allowed to vary, the best fit has SSE = 0.01727, worse than the null, and places the center outside the scan to avoid producing a dip. Allowing the contrast amplitude to float gives SSE = 0.00972 only by choosing an effective negative contrast, i.e. the wrong physical sign for a pODMR fluorescence dip.

Decision

The active sequence and quantitative model predict a large normalized readout2 dip if a pODMR resonance is present. The observed readout2/readout1 data stay near unity with small tracking-scale fluctuations and do not match the expected sign, size, or line shape. I therefore decide that a pODMR resonance is absent.
