Case: podmr_027_2026-05-16-184117

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and roles:
- SequenceName is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active readouts are therefore:
  - readout 1: detection immediately after optical polarization, a true mS = 0 reference.
  - readout 2: detection after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth.
- length_rabi_pulse = 52 ns.
- mod_depth = 1.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a resonant rectangular Rabi pulse, the transferred population is
  P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given the setup contrast scale between mS = 0 and mS = +1 is about 22%, the expected on-resonance fluorescence drop in the post-pulse readout is approximately
  mean(readout 1) * 0.22 * P.
- mean(readout 1) = 53.794 counts, so the expected drop is 53.794 * 0.22 * 0.996 = 11.79 counts.

Observed quantitative comparison:
- mean(readout 1) = 53.794 counts, SD across scan points = 1.043 counts.
- mean(readout 2) = 52.947 counts, SD across scan points = 1.094 counts.
- readout1 - readout2 has mean 0.847 counts, SD 1.468 counts, and maximum 3.462 counts.
- The largest observed separation is far below the approximately 11.8 count on-resonance signal expected from the pulse model.
- A simple positive-amplitude Rabi-detuning line-shape fit over possible center frequencies gave best fitted amplitude about 2.83 counts, still much smaller than the expected 11.83 count contrast-scale amplitude and not independently stable across the two stored averages.

Decision:
The active pulse is effectively a pi pulse at the stated Rabi frequency and modulation depth, so a true pODMR resonance should create a large dip in readout 2 relative to the mS = 0 reference. The data show only small scan-scale fluctuations and no feature near the expected signal size. I decide resonance_absent.
