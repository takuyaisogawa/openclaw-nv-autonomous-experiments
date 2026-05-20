Sequence and readout interpretation

The provided XML is Rabimodulated.xml. The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first runs adj_polarize and detection, so the first stored readout is the bright m_S = 0 reference. The branch labelled "Acquire 1 level reference" is inactive because full_expt = 0, so it does not create an independent dark reference. The active signal operation is then rabi_pulse_mod_wait_time followed by detection, so the second stored readout is the post-microwave-pulse signal. The active pulse uses mod_depth = 1 and length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns. The do_adiabatic_inversion flag is not used by the active instructions.

Quantitative expected-signal model

Using the stated setup calibration, the Rabi frequency at mod_depth = 1 is about f_R = 10 MHz. For a square resonant pulse of duration t = 52 ns, the transition probability as a function of detuning is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of about 22 percent, the expected maximum pODMR contrast is 0.22 * 0.996 = 0.219, or about 21.9 percent. Around a bright reference level near 46.9 raw units, this corresponds to an expected drop of roughly 10.3 raw units for a near-pi pulse on resonance.

Measured comparison

I used the paired contrast (readout1 - readout2) / readout1 because readout1 is the m_S = 0 reference and readout2 is the post-pulse signal. The strongest local feature is:

- 3.875 GHz: readout1 = 48.538, readout2 = 39.115, contrast = 19.41 percent
- 3.880 GHz: readout1 = 47.038, readout2 = 39.558, contrast = 15.90 percent
- 3.885 GHz: readout1 = 48.712, readout2 = 43.038, contrast = 11.65 percent

Away from the 3.865-3.890 GHz feature, the contrast mean is about -0.10 percent with standard deviation about 2.55 percent. The 3.875 and 3.880 GHz points are therefore about 7.7 and 6.3 off-resonance standard deviations above the off-resonance contrast level. Fitting the square-pulse response above with center frequency, amplitude, and offset free gives a best center near 3.8784 GHz, fitted amplitude 19.75 percent, offset -0.81 percent, and contrast RMSE 2.33 percent. A fixed 22 percent physical contrast model also has its best match near 3.8775 GHz.

Decision

The observed localized decrease appears only in the post-pulse readout, has the correct sign, has the expected magnitude for a 52 ns near-pi pulse at mod_depth = 1, and is much larger than the off-resonance paired-readout scatter. The stored averages are not treated as a strong independent repeatability test, but they are compatible with the same dip region. I therefore decide that a pODMR resonance is present.
