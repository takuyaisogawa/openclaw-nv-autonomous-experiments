Analysis note for podmr_021_2026-05-16-171244

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first performs adj_polarize, then detection. This first detection is the true m_S = 0 reference readout.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. No active m_S = +1 reference readout is acquired.
- The active microwave manipulation is one rabi_pulse_mod_wait_time call followed by detection. This second detection is the post-Rabi signal readout.
- The active pulse settings from the provided XML/recorded values are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounding step keeps this at 13 samples = 52 ns.

Physical model calculation:
For a rectangular resonant Rabi pulse, the transferred population is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

using frequencies in cycles/s. The given setup has f_R = 10 MHz * mod_depth = 10 MHz and contrast scale C = 0.22. With t = 52 ns:
- On resonance: P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected fluorescence loss is C * P = 21.9%.
- At 2.5 MHz detuning, the worst-case nearest point for a 5 MHz-spaced sweep: P = 0.929, so the expected loss is 20.4%.
- In raw-readout units near the observed baseline of about 46 counts, this corresponds to about 9.4 to 10.1 counts of signal decrease in readout 2 relative to readout 1 at the resonant sampled point.

Measured quantitative check:
- Mean readout 1 = 46.49; mean readout 2 = 46.41.
- The measured fractional loss (readout1 - readout2) / readout1 has maximum 4.72%, equal to 2.27 counts, at 3.830 GHz.
- Several points have the opposite sign, with readout 2 larger than readout 1; the most opposite point is -3.98%.
- A resonance anywhere inside the swept range should have produced at least one sampled point with about 20.4% loss, far larger than the observed 4.72% maximum.
- The broad motion visible in both readouts is common-mode tracking/baseline variation, not a selective post-Rabi depletion matching the expected pODMR line.

Decision:
The expected near-pi-pulse pODMR signal is absent from the differential readout. I classify this case as resonance_absent.
