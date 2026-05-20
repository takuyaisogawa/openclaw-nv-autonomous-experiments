Case: podmr_014_2026-05-12-081841

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:

The active sequence is Rabimodulated.xml. The instructions first polarize the NV, then perform a detection before any microwave pulse. This first detection is the true m_s = 0 reference readout. The optional "Acquire 1 level reference" block is guarded by full_expt, and full_expt = 0, so that block is skipped and there is no active m_s = +1 reference readout. The active pulsed-ODMR measurement is then a rabi_pulse_mod_wait_time pulse followed by detection. Therefore readout 1 is the bright reference and readout 2 is the post-microwave signal readout.

The provided sequence XML and exported Variable_values give:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so rounding to sample clock leaves the pulse at 13 samples = 52 ns
- swept mw_freq range = 3.825 to 3.925 GHz in 5 MHz steps

There is an internal inconsistency in raw_export.json: the embedded Sequence text contains a default line with mod_depth = 0.3, while the standalone provided XML and exported Variable_values contain mod_depth = 1. I used mod_depth = 1 as the active value and also checked mod_depth = 0.3 as a sensitivity case.

Physical model calculation:

For a pulsed ODMR scan starting from m_s = 0, the microwave pulse transfers population according to the Rabi formula

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

using frequencies in cycles/s. The expected normalized fluorescence is approximately

readout2 / readout1 = 1 - C * P_1(delta)

with contrast C = 0.22. The setup gives f_R = 10 MHz * mod_depth.

For the active mod_depth = 1:

- f_R = 10 MHz
- tau = 52 ns
- on-resonance P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996
- expected on-resonance fluorescence drop = 0.22 * 0.996 = 0.219, or about 22%
- at the observed readout scale near 46.8 counts, this is about 10.3 counts

Observed data:

- mean readout 1 = 46.624 counts
- mean readout 2 = 46.315 counts
- readout2 - readout1 mean = -0.309 counts, point-to-point SD = 1.299 counts
- most negative readout2 - readout1 point = -3.135 counts at 3.865 GHz, a 6.3% drop
- at 3.875 GHz, readout2 - readout1 = +0.269 counts, so the signal readout is slightly higher than the reference

I fit the Rabi lineshape over possible resonance centers in the scanned range using readout2/readout1 = baseline - A * P_1(delta). For mod_depth = 1, the best free-amplitude fit gives A = 0.0378 +/- 0.0204, with a maximum fitted dip of only 3.5% or 1.7 counts. That is far below the physical A = 0.22 expected from the setup contrast. Forcing the physical A = 0.22 gives RSS = 0.0746, much worse than the flat no-resonance model RSS = 0.0160.

Sensitivity check for the inconsistent mod_depth = 0.3 line:

- f_R = 3 MHz
- on-resonance P_1(0) = 0.222
- expected maximum fluorescence drop = 4.9%, or about 2.3 counts
- the best free-amplitude fit has only a weak apparent dip, A = 0.136 +/- 0.089, and a maximum fitted drop of about 2.9%
- the fixed physical model improves RSS over flat by only 0.0011, which is not strong evidence

The stored two averages have different strongest negative points, one near 3.865 GHz and one near 3.905 GHz. Since stored averages can reflect tracking cadence, I did not treat that as an independent repeatability test, but it is consistent with the absence of a stable resonance feature.

Decision:

The active pulse should produce an unmistakable near-pi-pulse pODMR dip if a resonance is present. The measured readout ratio does not show the expected 22% dip anywhere in the sweep, and the best quantitative lineshape fit is small and weak. I decide resonance_absent.
