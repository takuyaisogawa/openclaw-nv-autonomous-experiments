Case: podmr_005_2026-05-10-173726

Inputs used:
- sequence.xml and raw_export.json only.
- Active sequence: Rabimodulated.xml / rabi_pulse_mod_wait_time followed by detection.
- full_expt = 0, so the optional "1 level reference" branch is inactive.
- Readout roles: readout 1 is the bright m_S = 0 reference after polarization and direct detection; readout 2 is the signal after the microwave Rabi-modulated pulse and detection.
- mod_depth = 1 from the provided sequence XML and variable values.
- Microwave pulse duration: length_rabi_pulse = 52 ns. At 250 MS/s this remains 13 samples = 52 ns after rounding.

Quantitative physical expectation:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the resonant rotation angle is:
  theta = 2*pi*(10 MHz)*(52 ns) = 3.267 rad.
- Resonant population transfer for a rectangular pulse is sin^2(theta/2) = 0.996, essentially a pi pulse.
- With the stated 0 to +1 contrast scale of about 22%, an on-resonance signal readout should drop by approximately:
  0.22 * 0.996 = 0.219 of the bright baseline.
- Using the off-dip readout-2 baseline from the data, 41.69 counts, the expected on-resonance drop is about 9.13 counts.

Observed data model check:
- readout 2 baseline excluding the central dip region is about 41.69 counts.
- readout 2 minimum is 34.73 counts at 3.880 GHz, a drop of 6.95 counts or 16.7% of baseline.
- A simple linear-baseline plus negative Gaussian dip fit to readout 2 gives a dip amplitude of about 7.04 counts, centered near 3.877 GHz with sigma about 6.75 MHz.
- The null linear-baseline SSE for readout 2 is about 136.3, while the dip model SSE is about 44.8.
- The ratio readout2/readout1 reaches 0.833 at the dip, versus an edge median ratio of about 0.986.

Decision:
The observed dip is smaller than the ideal 22% contrast-scale prediction but has the expected sign, approximate magnitude, and frequency-localized shape for a near-pi pODMR resonance. Stored averages are not treated as independent confirmation, but the combined readouts are quantitatively consistent with resonance.
