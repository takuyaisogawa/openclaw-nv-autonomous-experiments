I used inputs/sequence.xml for the pulse-sequence parameters.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Active readout 1 is the detection immediately after adj_polarize, labeled in the XML as the true mS = 0 level reference.
- Active readout 2 is the detection after rabi_pulse_mod_wait_time, so it is the pODMR signal readout after the microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounded pulse duration remains 52 ns (13 samples).

Physical model calculation:
For a square resonant Rabi pulse starting in mS = 0, I used

P1(delta) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * sqrt(fR^2 + delta^2) * tau)

where fR = 10 MHz * mod_depth = 10 MHz and tau = 52 ns. The fluorescence drop expected from transfer to mS = +1 is approximately contrast * P1, with contrast = 0.22.

This gives:
- delta = 0 MHz: P1 = 0.996, expected fractional PL drop = 0.219, about 10.1 counts for a 46-count readout.
- delta = 2.5 MHz: P1 = 0.929, expected drop = 0.204.
- delta = 5 MHz: P1 = 0.749, expected drop = 0.165.
- delta = 10 MHz: P1 = 0.273, expected drop = 0.060.
- delta = 15 MHz: P1 = 0.0117, expected drop = 0.0026.

Because the scan step is 5 MHz, any resonance lying within the scanned range should put at least one point within 2.5 MHz of resonance, where the expected readout-2 suppression is about 20%.

Data comparison:
I formed the normalized pODMR contrast y = (readout1 - readout2) / readout1, using readout1 as the mS = 0 reference and readout2 as the post-pulse signal. Across the 21 points, y has mean -0.0020, standard deviation 0.0315, minimum -0.0497, and maximum 0.0688. The largest observed positive drop is 6.9%, far below the approximately 20% minimum near-resonant drop expected from the pulse model at this scan spacing. Several points have readout2 brighter than readout1, which is inconsistent with a robust resonant transfer feature.

I also fit y to the calculated Rabi lineshape as A * P1(freq - center) + offset while scanning possible resonance centers. A free-amplitude fit gave A = 0.032 at 3.82825 GHz with R^2 = 0.087, much smaller than the expected A = 0.22 and with little explanatory power. Forcing A = 0.22 gave a poor fit with negative R^2; the best center was at the scan edge and would predict about a 19% drop at 3.825 GHz, while the observed contrast there is -0.13%.

The per-average overlays show tracking-like drift between stored averages, so I did not treat them as a strong independent repeatability test. They do not rescue the model comparison: the combined signal lacks the large, narrow post-pulse suppression required by the active 52 ns, mod_depth 1 Rabi sequence.

Decision: resonance_absent.
