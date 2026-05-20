Case podmr_081_2026-05-17-110558

Sequence and active readouts:
- The provided sequence XML is Rabimodulated.xml.
- Active variables: length_rabi_pulse = 5.2e-08 s, mod_depth = 1, full_expt = 0.
- Because full_expt = 0, the optional +1 reference block is skipped.
- The active measurement therefore has readout 1 as the initial optically polarized m_S = 0 reference, then a modulated Rabi pulse, then readout 2 as the post-pulse signal.

Quantitative model:
- Given the setup fact, f_Rabi = 10 MHz at mod_depth = 1.
- For a rectangular two-level pulse, the transferred population versus detuning is
  P1(df) = f_Rabi^2 / (f_Rabi^2 + df^2) * sin^2(pi * t * sqrt(f_Rabi^2 + df^2)).
- On resonance with t = 52 ns, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% m_S = 0 to m_S = +1 contrast scale, the expected resonant PL drop in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, about 21.9%.
- The scan step is 5 MHz. Scanning possible resonance centers inside the measured frequency window, the largest sampled transfer probability would still be at least 0.929, giving an expected sampled PL drop of at least 20.4% if a resonance were present in range.

Observed comparison:
- The normalized observed drop (readout1 - readout2) / readout1 has mean 0.48%.
- Its maximum positive value is 4.52%, and several neighboring points have negative drop where readout 2 is brighter than readout 1.
- A least-squares fit of the rectangular-pulse response shape with free amplitude gives only 2.7% fitted contrast, far below the about 22% physical expectation.
- A fixed 22% contrast model does not match the data; the best fixed-center fit is driven outside the scan and still does not improve meaningfully over a zero-resonance model.

Decision:
The physically expected pODMR dip for this active sequence would be large and unavoidable at the sampled resolution, but the observed readout difference is only small drift/noise-scale variation. I therefore classify this case as resonance_absent.
