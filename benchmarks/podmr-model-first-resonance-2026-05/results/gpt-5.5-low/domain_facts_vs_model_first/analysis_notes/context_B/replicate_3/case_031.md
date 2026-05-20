Case podmr_016_2026-05-16-131456

Sequence identification:
- SequenceName from raw export: Rabimodulated.xml.
- Active path in the XML: adj_polarize, detection for the true mS=0/bright reference, wait, then rabi_pulse_mod_wait_time, then detection for the pulsed readout.
- The "Acquire 1 level reference" branch is inactive because full_expt = 0, even though do_adiabatic_inversion is true. Therefore readout 1 is the mS=0 reference and readout 2 is the signal after the microwave Rabi pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.

Explicit signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling with mod_depth, f_R = 10 MHz here.
- For a resonant square pulse, the transferred population is P(+1) = sin^2(pi * f_R * t).
- With t = 52 ns, P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between mS=0 and mS=+1 is about 22%, so a resonant pulse should reduce fluorescence by about 0.22 * 0.996 = 0.219 of the bright reference.
- With a readout-1 median of 47.46 counts, the expected on-resonance dip is about 10.4 counts for an ideal isolated pi response. Detuning, linewidth, finite scan spacing, and nonideal pulse calibration can reduce the observed depth, but a several-count dip in readout 2 relative to the flat reference is expected.

Observed quantitative comparison:
- Scan axis: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout 1 ranges from 45.40 to 48.71 counts and has no comparable narrow central dip.
- Readout 2 has a broad dip centered near 3.875-3.880 GHz: 42.17 at 3.870 GHz, 39.65 at 3.875 GHz, 39.62 at 3.880 GHz, and 41.15 at 3.885 GHz.
- A robust off-dip baseline for readout 2 is about 46.72 counts, giving an observed minimum dip of about 7.11 counts, or 15.2%.
- This observed dip is of the same sign, location, and order of magnitude as the model expectation for a near-pi resonant pulse. The two stored averages both show the same central depression in the pulsed readout, but I treat that only as consistency with the tracking cadence rather than a strong independent repeatability test.

Decision:
The active pulse sequence and quantitative contrast/Rabi model predict a fluorescence dip in readout 2 at resonance, and the data show a pronounced central dip of the expected scale while readout 1 remains comparatively flat. I decide that a pODMR resonance is present.
