Case podmr_075_2026-05-17-093901

Sequence identification:
- Active sequence: Rabimodulated.xml.
- Scan axis: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout roles from the instruction order:
  - readout 1 is the "true 0 level reference": optical polarization followed immediately by detection.
  - readout 2 is the measurement after the modulated Rabi pulse. The optional separate 1-level reference is skipped because full_expt = 0.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to the same 52 ns.

Physical expectation:
The provided setup gives Rabi frequency about 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so this sequence has f_R = 10 MHz. For a resonant square pulse, the transferred population is approximately sin^2(pi f_R tau). With tau = 52 ns:

sin^2(pi * 10e6 * 52e-9) = 0.996.

Thus the pulse is essentially a pi pulse on resonance. With the stated m_S=0 to m_S=+1 contrast scale of about 22%, the expected resonant fluorescence ratio for the post-pulse signal relative to the pre-pulse 0 reference is:

1 - 0.22 * 0.996 = 0.7809.

The mean readout 1 level is 50.523 counts, so the expected resonant drop is about 11.07 counts, with readout 2 near 39.45 counts at resonance if the transition is driven strongly.

Observed quantitative comparison:
- Mean readout 1 = 50.523.
- Mean readout 2 = 50.390.
- Mean difference readout2 - readout1 = -0.133 counts.
- Standard deviation of pointwise differences = 1.187 counts.
- Deepest pointwise difference is -2.442 counts at 3.830 GHz.
- Deepest pointwise ratio readout2/readout1 is 0.9509, far above the expected resonant ratio of 0.7809.
- Near the nominal center region, ratios are also close to unity, for example 0.9740 at 3.875 GHz, 1.0019 at 3.880 GHz, and 1.0480 at 3.885 GHz.

Decision:
The active readout should show a large approximately 22% dip if a pODMR resonance were present under these pulse settings. Instead, readout 2 tracks readout 1 with only small percent-level fluctuations and drift. The stored two averages are mainly a tracking-cadence view and do not change the conclusion. No pODMR resonance is present in this scan.
