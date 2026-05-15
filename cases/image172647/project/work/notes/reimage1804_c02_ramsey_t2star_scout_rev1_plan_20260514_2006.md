# reimage1804_c02 Ramsey/T2star scout revised plan

Created: 2026-05-14T20:06:00-04:00

The initial 51-point / 4x100000 plan was not executed because the MATLAB advisory estimated a 742.3 s per-average tracking window, above the 600 s daytime cap.

Revised scout:

- sequence: `auto__ramsey` / `ramsey.xml`
- scan: `tau = 0..8 us`, 43 points
- mw_freq: 3876461010.481 Hz from terminal pODMR fit
- det: 1.5 MHz
- acquisition: 8 averages x 50000 repetitions (400k total shots, even averages for snake order)

Model: B = 35.91 mT and expected 13C Larmor = 384.6 kHz. Tau step = 190.5 ns, Nyquist = 2.625 MHz, FFT bin = 125 kHz. Nominal sidebands are 1.115 and 1.885 MHz; the high sideband has 740429 Hz nominal margin and 52408 Hz margin after adding the pODMR center covariance uncertainty.

Execute only if the revised verifier/advisory passes and the queue remains idle.
