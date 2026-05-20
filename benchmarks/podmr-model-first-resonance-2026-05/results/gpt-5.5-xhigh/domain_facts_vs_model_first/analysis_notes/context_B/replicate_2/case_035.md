Case: podmr_020_2026-05-16-165809

I used only the provided sequence XML and the raw exported readouts.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. The do_adiabatic_inversion setting is therefore not part of the active measurement path.
- Readout 1 is the detection immediately after adj_polarize, so it is the polarized mS = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so it is the pODMR driven readout.
- The active pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. At the given setup calibration this gives f_Rabi about 10 MHz.

Explicit quantitative model:

For a square microwave pulse, I used the two-level transition probability

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),

where f_R = 10 MHz and t = 52 ns. The optical readout model is

I_driven = I_0 * (1 - C * P(Delta)),

with C = 0.22 from the stated mS = 0 to mS = +1 contrast scale and I_0 represented by readout 1.

At exact resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. The expected normalized contrast is therefore 0.22 * 0.996 = 0.219, so the driven readout should be about 0.781 of readout 1. With the measured mean readout 1 of 45.19, the expected on-resonance drop is about 9.90 raw units.

The expected neighboring-point contrasts are also large on this 5 MHz frequency grid: about 20.4% at 2.5 MHz detuning, 16.5% at 5 MHz detuning, and 6.0% at 10 MHz detuning. Thus a resonance inside the scanned range should create at least one deep dip, and if it lies between grid points it should create two adjacent large dips.

Observed data:
- The largest observed normalized drop, 1 - readout2/readout1, is 0.0706 at 3.825 GHz.
- The minimum observed readout2/readout1 ratio is 0.929, far above the expected resonant ratio of about 0.781.
- Several points have negative contrast, with readout 2 brighter than readout 1, which is not the expected sign for resonant transfer into the darker mS = +1 state.
- A fixed-contrast in-scan fit of the above model chooses the scan edge, 3.825 GHz, but still predicts a 9.97 raw-unit drop at that point and a 7.35 raw-unit drop at the next point, while the observed drops are only 3.21 and 1.33 raw units. Allowing the best fixed model to move outside the scan shifts the apparent center below the scanned band, which is not evidence for a resonance present in this pODMR scan.

Decision:

The active pulse would produce a large, localized loss of fluorescence if an mS = 0 to mS = +1 resonance were present in the scan. The measured second readout lacks the required depth, sign consistency, and adjacent-point structure. I therefore classify this case as resonance_absent.
