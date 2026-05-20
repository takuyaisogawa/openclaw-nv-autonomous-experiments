Case: podmr_020_2026-05-16-165809

Inputs used:
- inputs/sequence.xml for the pulse program and variables.
- inputs/raw_export.json for the raw readout arrays and scan axis.

Active sequence and readout roles:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout 1 is the true m_S = 0 brightness reference after adj_polarize and before the swept microwave pulse.
- Readout 2 is the signal readout after one rabi_pulse_mod_wait_time pulse.
- There is no independent m_S = +1 reference readout in this acquisition.
- mod_depth = 1 from inputs/sequence.xml.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse is also 52 ns because this is 13 samples.

Physical model calculation:

The relevant model is a rectangular microwave Rabi pulse applied after optical polarization. For Rabi frequency f_R and detuning Delta, the transferred population is

P1(Delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * t)

where Omega = 2*pi*f_R, delta = 2*pi*Delta, and t = 52 ns.

The setup facts give f_R = 10 MHz at mod_depth = 1. On resonance,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected readout-2 drop at resonance is

0.22 * 0.9961 = 0.219, or about 21.9%.

At the observed brightness scale near 45 raw counts, this is an expected drop of about 9.86 raw-count units in readout 2 relative to the readout-1 reference.

The same model predicts substantial response across the 5 MHz sampled scan:
- Delta = 0 MHz: P1 = 0.996, expected contrast = 21.9%, drop at 45 counts = 9.86.
- Delta = 5 MHz: P1 = 0.749, expected contrast = 16.5%, drop at 45 counts = 7.41.
- Delta = 10 MHz: P1 = 0.273, expected contrast = 6.00%, drop at 45 counts = 2.70.
- Delta = 20 MHz: P1 = 0.0479, expected contrast = 1.05%, drop at 45 counts = 0.47.

Because the frequency spacing is 5 MHz, any resonance inside the scanned range should place at least one sampled point within 2.5 MHz of resonance, so the expected peak contrast should be close to the 21.9% on-resonance value, not merely a single weak point.

Data comparison:

Using normalized contrast c = (readout1 - readout2) / readout1 from the combined raw arrays:
- Mean c = 1.41%.
- Standard deviation of c over scan points = 2.84%.
- Maximum c = 7.06% at 3.825 GHz, corresponding to a 3.21 count drop.
- Minimum c = -3.97% at 3.905 GHz, where readout 2 is brighter than readout 1.

The largest observed drop is only about one third of the predicted resonant contrast for mod_depth = 1 and is at the scan edge rather than a resolved interior resonance. Most points are near zero contrast or have the opposite sign. The two stored averages are not a strong repeatability test here, but they also do not show a consistent resonance-sized feature: average-level peak contrasts are 11.3% and 7.1%, still below the expected near-22% response and not aligned as a stable line.

I also compared the combined contrast trace with a simple linear drift baseline and with the detuned Rabi lineshape. A free-amplitude Rabi component preferred a negative amplitude of about -6.3% near 3.9075 GHz, opposite to the expected pODMR signal sign. Forcing the physical 22% amplitude made the residual RMS worse than the simple drift baseline.

Decision:

The active 52 ns, mod_depth = 1 pulse should produce an approximately pi-pulse response and a large pODMR contrast if a resonance is present in the scanned range. The measured readout differences are much smaller, not consistently shaped like the expected detuned Rabi response, and are compatible with drift/tracking-scale variation. I therefore classify this case as resonance_absent.
