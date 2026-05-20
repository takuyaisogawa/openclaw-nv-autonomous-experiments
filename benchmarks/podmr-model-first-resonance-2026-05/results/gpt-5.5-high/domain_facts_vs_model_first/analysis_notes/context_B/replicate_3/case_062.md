Case: podmr_048_2026-05-17-002650

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The scan reports SequenceName = Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided XML, full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- The first active detection is after adj_polarize and is the true m_S = 0 optical reference. This corresponds to readout 1.
- The second active detection is after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay). This corresponds to readout 2, the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, the pulse is already exactly 13 samples, so rounding leaves it at 52 ns.

Quantitative expected-signal model:
- Given the stated setup calibration, f_Rabi = 10 MHz * mod_depth = 10 MHz.
- For a rectangular microwave pulse of duration tau = 52 ns, the driven transition probability versus detuning is
  P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),
  with Omega = 2*pi*10 MHz and Delta = 2*pi*(f - f0).
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- With an m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance readout-2 drop relative to readout 1 is 0.22 * 0.996 = 0.219, about 21.9%.
- With the observed reference level near 50.5 raw units, that model predicts an on-resonance readout-2 deficit of about 11.1 raw units.
- The expected contrast is still large on nearby scan points: for a resonance on a sampled point, the model gives about 16.5% contrast at +/-5 MHz and about 6.0% at +/-10 MHz.

Observed data comparison:
- Observed contrast was computed as (readout1 - readout2) / readout1 at each scan point.
- The observed contrast has mean 1.34%, standard deviation 2.65%, minimum -3.52%, and maximum 7.35%.
- The largest apparent deficit is at 3.850 GHz, where readout1 = 52.577 and readout2 = 48.712, giving 7.35% contrast. This is far below the expected 21.9% on-resonance contrast and does not have the expected neighboring detuned Rabi shape.
- At the final scan point, 3.925 GHz, readout1 = 52.731 and readout2 = 50.981, giving only 3.32% contrast.
- A least-squares comparison of the measured contrast to the physical detuned-Rabi shape with fixed 22% amplitude is worse than a constant baseline fit by a factor of 4.86 in SSE.
- If the amplitude is allowed to float but constrained positive, the best fit amplitude is only 3.31%, much smaller than the 21.9% physically expected for this pulse.
- If the amplitude is allowed to become unphysical, the best fit prefers a negative resonance feature, which is not a pODMR dip.

Decision:
The active sequence should have produced a large readout-2 dip if a resonance were present in the scanned range. The measured signal contains only small fluctuations and no physical detuned-Rabi line shape at the expected scale. I therefore classify this case as resonance_absent.
