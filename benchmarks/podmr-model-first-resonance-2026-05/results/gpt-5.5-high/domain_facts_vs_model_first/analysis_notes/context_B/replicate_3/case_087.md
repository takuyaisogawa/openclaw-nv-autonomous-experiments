Case podmr_073_2026-05-17-090948

I used the provided sequence XML to identify the active experiment. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence has two active detections because full_expt = 0 disables the optional m_S=+1 reference block. Readout 1 is the detection immediately after optical pumping, so it is the m_S=0 reference. Readout 2 is the detection after the modulated Rabi pulse and is the pODMR signal channel.

Relevant sequence parameters from the provided XML:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns
- mod_depth = 1
- expected Rabi frequency from the stated setup scaling = 10 MHz
- contrast scale between m_S=0 and m_S=+1 = about 22%

Quantitative model:

For a driven two-level transition, using frequency units in Hz,

P(+1 | detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * t * sqrt(f_R^2 + detuning^2)).

With f_R = 10 MHz and t = 52 ns, the on-resonance transfer probability is

sin^2(pi * 10e6 * 52e-9) = 0.996.

Thus the expected fluorescence suppression at resonance is approximately

0.22 * 0.996 = 0.219, or 21.9% of the m_S=0 reference level.

The observed reference level is about 50.17 raw counts, so the expected on-resonance drop in readout 2 relative to readout 1 is about

50.17 * 0.219 = 10.99 raw counts.

The modeled half-width is about 7.6 MHz. Since the scan step is 5 MHz, any resonance inside the scan range should put at least one sampled point within 2.5 MHz of resonance and should therefore produce a drop close to the full ~11-count scale, far larger than point-to-point scatter.

Observed data check:

- mean readout 1 = 50.17
- mean readout 2 = 50.04
- mean(readout 2 - readout 1) = -0.12 counts
- std(readout 2 - readout 1) = 1.09 counts
- most negative readout 2 - readout 1 point = -2.52 counts at 3.855 GHz
- smallest readout2/readout1 ratio = 0.950, corresponding to only about a 5.0% drop

A free-amplitude fit of the expected Rabi lineshape to readout2-readout1 gives a best drop amplitude of about 1.8 counts, much smaller than the approximately 11 counts required by the physical model. Forcing the expected 11-count amplitude gives a poor match and would require a conspicuous dip that is not present in the raw readouts. The two stored averages are consistent with tracking-scale scatter rather than an independent repeatability test, so I did not treat them as strong confirmation of any narrow feature.

Decision: resonance_absent. The expected pODMR signal from the active 52 ns, mod_depth 1 near-pi pulse is much larger than the observed readout difference structure, and no physically sized resonance dip is present.
