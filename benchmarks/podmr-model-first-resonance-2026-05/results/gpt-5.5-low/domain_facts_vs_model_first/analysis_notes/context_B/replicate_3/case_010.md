Case podmr_017_2026-05-12-134151

Inputs inspected:
- sequence.xml and raw_export.json only.
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation:
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active sequence first polarizes and detects the true m_S = 0 reference, then applies one rabi_pulse_mod_wait_time pulse, then detects the final signal.
- Readout role assignment: readout 1 is the polarized/0 reference; readout 2 is the post-microwave readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this remains 52 ns after rounding.

Explicit model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a resonant square pulse, rotation angle theta = 2*pi*f_R*t = 2*pi*(10e6)*(52e-9) = 3.267 rad.
- Excited-state population after the pulse is sin(theta/2)^2 = 0.996, essentially a pi pulse.
- With m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant post-MW/reference signal ratio is
  1 - 0.22*0.996 = 0.781.
- Therefore a true resonance under this sequence should produce an approximately 21.9% reduction of readout 2 relative to readout 1 near resonance, not merely a small fluctuation.

Observed quantitative comparison:
- Across the 21 frequency points, readout2 - readout1 has mean +0.069 and standard deviation 1.121 counts.
- The readout2/readout1 ratio has mean 1.005, standard deviation 0.050, minimum 0.913, and maximum 1.103.
- The strongest apparent dip is only about 8.7%, far smaller than the expected approximately 21.9% near-pi-pulse resonance signal.
- No frequency point approaches the modeled resonant ratio of about 0.78.
- The stored per-average traces show large opposite slow drifts between averages/readouts, consistent with tracking cadence effects rather than a stable spectral resonance.

Decision:
The active physical model predicts a large post-MW dip if a pODMR resonance is present, but the measured normalized readout remains near unity and does not show the expected resonant contrast. I therefore classify this case as resonance_absent.
