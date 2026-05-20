Sequence/readout identification:

The provided sequence is Rabimodulated.xml. The active measurement initializes with adj_polarize, then records the "true 0 level reference" detection before any microwave pulse. Because full_expt = 0, the optional 1-level reference block is skipped even though do_adiabatic_inversion is set. The measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Therefore readout 1 is the bright m_S = 0 reference, and readout 2 is the post-microwave pODMR signal.

Quantitative model:

For the setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. I modeled the active rectangular pulse with

P1(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),

where Omega = 2*pi*10 MHz, Delta = 2*pi*delta, and tau = 52 ns. On resonance this gives P1 = sin^2(pi * 10 MHz * 52 ns) = 0.996. With a 22% m_S = 0 to m_S = +1 contrast scale, a resonance should reduce the post-pulse readout by about 0.22 * 0.996 = 21.9% relative to the bright reference at the resonant point.

The frequency step is 5 MHz, so if a resonance lies anywhere inside the scan, at least one sampled point is within 2.5 MHz of resonance. The same model gives P1(2.5 MHz detuning) = 0.929, so the guaranteed sampled contrast is still about 20.4%. At 5 MHz detuning the expected contrast is about 16.5%, and at 10 MHz detuning about 6.0%, so a true resonance should appear as a broad dip over multiple adjacent points, not a single small excursion.

Data comparison:

Using readout2/readout1 as the normalized pODMR signal, the mean ratio is 0.9858 with standard deviation 0.0295. The minimum observed ratio is 0.9308 at 3.875 GHz, equivalent to only 6.9% contrast. The neighboring points do not match the expected line shape: at 3.870 GHz the contrast is 0.8%, and at 3.880 GHz it is 2.4%, whereas a resonance centered near 3.875 GHz would predict roughly 16.5% contrast at both neighbors. In counts, the observed largest readout1-readout2 deficit is 3.64 counts, while the expected on-resonance deficit from the model is about 11 counts for a 51-count bright reference.

I also scanned possible resonance centers with the fixed 22% contrast model. The best constrained fit avoided placing a resonance in the scan and improved the constant-ratio null only negligibly. A free-amplitude fit did not find the expected negative dip; its best feature had the opposite sign. The two stored averages show a low correlation in normalized ratio traces, so they do not rescue the single dip as a repeatable resonance feature.

Decision: resonance_absent.
