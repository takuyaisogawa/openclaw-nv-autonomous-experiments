Active sequence and readout roles:

- The active sequence is Rabimodulated.xml / Rabimodulated, with the scan varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The saved run variables show mod_depth = 1 and length_rabi_pulse = 52 ns.
- full_expt = 0, so the optional "1 level reference" block is skipped. The two stored readouts are therefore:
  - readout 1: detection immediately after optical polarization, the bright ms=0 reference.
  - readout 2: detection after the modulated microwave Rabi pulse, the pODMR signal readout.

Pulse interpretation:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1, so a 52 ns pulse is close to a pi pulse. If the microwave frequency were resonant with the NV transition, readout 2 should show a substantial fluorescence reduction relative to readout 1, on the order of the setup contrast scale between ms=0 and ms=+1, about 22% in the strongest case.

Data assessment:

The combined readouts are both centered near 50 counts. The pointwise readout2/readout1 ratio has mean about 1.002 and ranges from about 0.961 to 1.048. The largest apparent dips are only around 4% and occur as isolated alternating fluctuations rather than as a coherent resonance feature. The per-average traces show substantial tracking/cadence offsets between stored averages, so the averages should not be treated as a strong repeatability test. There is no consistent darkening of the post-pulse readout over the scan comparable to the expected contrast for a near-pi pulse.

Decision:

No convincing pODMR resonance is present in this scan.
