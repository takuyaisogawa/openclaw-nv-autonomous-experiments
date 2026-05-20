Case: podmr_076_2026-05-17-095337

Sequence identification:
- SequenceName: Rabimodulated.xml.
- Active instructions: polarize, detection, wait, then a single rabi_pulse_mod_wait_time, then detection.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 role: true m_S = 0 optical reference after polarization.
- Readout 2 role: signal readout after the modulated Rabi pulse.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth: using the provided sequence XML variable value, mod_depth = 1.

Quantitative model:
- Setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square pulse, excited-state population transfer versus detuning is
  P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * t),
  with Omega = 10 MHz and t = 52 ns.
- On resonance this gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The measured m_S = 0 reference level is mean(readout 1) = 51.03 raw counts, so the expected resonant fluorescence change is
  51.03 * 0.22 * 0.996 = 11.18 raw counts lower in readout 2 than readout 1.

Observed data:
- Across the 21 scanned microwave frequencies, readout2 - readout1 has mean -0.21 counts and standard deviation 1.42 counts.
- The most negative observed point is -2.73 counts, far smaller than the expected -11.18 count resonant change.
- A detuned Rabi model scanned over possible resonance centers fits much worse than a flat/no-resonance model: best physical-model SSE about 224 versus flat-mean SSE about 40.5.
- Stored averages are not treated as independent strong repeatability evidence because they can reflect tracking cadence.

Decision:
The active pulse should produce an approximately 22% raw-count drop at resonance, but the observed readout difference is small, noisy, and not improved by the expected resonance profile. Therefore this pODMR resonance is absent.
