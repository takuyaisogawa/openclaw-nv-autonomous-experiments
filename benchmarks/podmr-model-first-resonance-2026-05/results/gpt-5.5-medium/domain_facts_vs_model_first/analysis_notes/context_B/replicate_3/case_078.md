Case: podmr_064_2026-05-17-065956

Sequence interpretation

The provided sequence is Rabimodulated.xml. The active instructions first polarize the NV and acquire a detection immediately afterward; this is readout 1, the true mS = 0 fluorescence reference. The block labelled "Acquire 1 level reference" is inside `if abs(full_expt)>1e-12`; with full_expt = 0 it is inactive, so there is no explicit mS = +1 reference in the acquired two-readout data. The active microwave manipulation is then:

`rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)`

followed by detection; this is readout 2, the post-Rabi-pulse signal. The relevant values are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and the scanned variable is mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Expected physical signal

The given calibration says the Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For the active mod_depth = 1 and a 52 ns pulse, the on-resonance population transfer for a rectangular Rabi pulse is:

P1 = sin^2(pi * f_Rabi * t)
   = sin^2(pi * 10e6 * 52e-9)
   = 0.996.

With the stated mS = 0 to mS = +1 contrast scale of about 22%, the expected resonant fluorescence loss in readout 2 relative to readout 1 is:

contrast_expected = 0.22 * 0.996 = 0.219, about 21.9%.

The readout 1 mean is 50.97 counts, so the expected resonant dip is about:

50.97 * 0.219 = 11.17 counts.

Quantitative comparison to data

Using contrast y = 1 - readout2/readout1, the observed points have:

- mean contrast: 0.00068
- standard deviation: 0.02675
- minimum: -0.0610
- maximum: 0.0538

The largest observed positive dip is only 5.4%, roughly one quarter of the expected resonant contrast, and the largest excursion is actually an anti-dip of -6.1%. The readout-2 minus readout-1 differences have mean -0.052 counts and standard deviation 1.38 counts, far below the expected about 11-count resonant drop.

I also compared the observed contrast to a rectangular-pulse detuned Rabi model:

P1(detuning) = (f_Rabi^2 / (f_Rabi^2 + detuning^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + detuning^2))
model contrast = 0.22 * P1(detuning)

Sweeping the unknown resonance center across the measured frequency range, the best fixed-contrast model has SSE = 0.0918, while the no-resonance baseline y = 0 has SSE = 0.0143. Allowing the model amplitude to float nonnegative gives a best amplitude of only 0.023, not the expected 0.22.

Decision

The active pulse is essentially a pi pulse at the stated calibration, so a true pODMR resonance in this scan should produce a broad, order-22% dip in readout 2 relative to readout 1. The measured contrast remains near zero with small tracking-like fluctuations and no fixed-calibration resonance signature. I decide resonance_absent.
