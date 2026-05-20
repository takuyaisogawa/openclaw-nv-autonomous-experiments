Case podmr_066_2026-05-17-072831

Sequence read:
- Active sequence file: inputs/sequence.xml, Rabimodulated style scan over mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 role: true mS = 0 reference after polarization and detection.
- Readout 2 role: signal after one modulated Rabi pulse and detection.
- Active pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz this is 13 samples, so no rounding change.
- mod_depth = 1.

Quantitative physical expectation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1, the resonant transition probability for a rectangular pulse is
  P = sin^2(pi * f_R * tau) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS = 0 to mS = +1 contrast scale of 22%, the expected resonant fluorescence reduction in readout 2 relative to readout 1 is
  0.22 * 0.996 = 0.219, about a 21.9% dip.
- The scan step is 5 MHz. If a resonance is anywhere inside the scan range, one sampled point is within at most 2.5 MHz detuning. Using
  P(Delta) = (f_R^2/(f_R^2 + Delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)),
  P(2.5 MHz) = 0.929, so the expected normalized readout2/readout1 at the nearest sampled point is at most
  1 - 0.22 * 0.929 = 0.796 before allowing for small baseline scaling.

Measured data check:
- Mean readout 1 = 45.900, mean readout 2 = 45.369.
- The observed readout2/readout1 ratios have mean 0.989 and range 0.936 to 1.054.
- The deepest observed normalized depression is therefore only 1 - 0.936 = 6.4%, far smaller than the expected roughly 20% to 22% dip for the active pi-like pulse.
- In raw units, the expected resonant drop near the mean reference is about 10.1 counts, while the largest observed readout2 minus readout1 depression is about 3.1 counts.
- A fixed 22% contrast rectangular-pulse model can only avoid a large mismatch by placing the resonance outside the scan; a free-amplitude fit inside the scan gives only about a 6.5% dip scale, inconsistent with the expected calibrated pi-pulse pODMR response.

Decision:
The active sequence should produce a large readout-2 dip if an NV pODMR resonance is present in this frequency window. The measured differential signal shows only small tracking-scale fluctuations and no physically expected resonance feature, so I decide resonance_absent.
