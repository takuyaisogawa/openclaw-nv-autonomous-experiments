Case: podmr_042_2026-05-16-225623

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name in export: Rabimodulated.xml.
- The XML instructions polarize the NV, then call detection once before any Rabi pulse. This first readout is therefore the optically polarized m_S = 0 / no-microwave reference.
- full_expt = 0, so the optional +1 reference block is not active.
- The second active detection follows PSeq = rabi_pulse_mod_wait_time(... length_rabi_pulse, mod_depth ...), so the second readout is the pODMR signal after the microwave pulse.
- Provided sequence variables give length_rabi_pulse = 5.2e-08 s and mod_depth = 1.

Quantitative physical model:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Resonant population transfer for a square Rabi pulse is P_1 = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 0.52 cycles, so P_1 = sin^2(pi * 0.52) = 0.996.
- Expected fractional readout drop on resonance is C * P_1 = 0.219, i.e. about 21.9%.
- The mean first readout is 46.72 counts, so the expected absolute resonant drop in readout 2 relative to readout 1 is about 10.24 counts.

Measured comparison:
- The measured readout2 - readout1 differences have mean +0.14 counts and standard deviation 1.43 counts.
- The most negative raw difference is -2.54 counts at 3.840 GHz, not at the apparent center near 3.875 GHz.
- At 3.875 GHz, readout2 - readout1 is -1.83 counts and readout2/readout1 = 0.960, a 4.0% drop.
- The measured drops are far below the expected 21.9% / 10.24-count resonant response for the active pulse and are comparable to point-to-point scatter and baseline drift.
- The per-average traces mainly show cadence/tracking drift and do not provide a strong independent repeatability test.

Decision:
No pODMR resonance is present. The active sequence should create a large post-pulse readout suppression if on resonance, but the observed data show only small, nonlocalized fluctuations and drift.
