<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_021

Sequence identification:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML executes an initial polarization followed by detection. This is the true mS = 0 reference readout.
- full_expt = 0, so the conditional 1-level reference block is not executed.
- The active driven signal is a single rabi_pulse_mod_wait_time call followed by detection. This is the post-microwave signal readout.
- The active pulse duration is length_rabi_pulse = 52 ns.
- The active mod_depth is 1.

Physical model calculation:
For a square resonant Rabi pulse, using the stated setup calibration f_R = 10 MHz at mod_depth = 1, the driven population transfer is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),

with Omega = 10 MHz and t = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated mS = 0 to mS = +1 contrast scale is about 22%, so the expected resonant signal reduction is

0.22 * 0.996 = 0.219, or about 21.9%.

Data check:
The sequence readout roles mean readout 1 should be treated as the mS = 0 reference and readout 2 as the driven signal. Using readout2/readout1, the off-resonance baseline ratio away from the central dip is about 0.974. The minimum ratio is about 0.762 at 3.875 GHz, giving a normalized depletion

1 - 0.762 / 0.974 = 0.218, or about 21.8%.

A direct square-pulse model fit over trial centers from 3.865 GHz to 3.895 GHz gives the best center at about 3.880 GHz, baseline ratio about 0.993, and fitted contrast about 0.223. The dip is also visible in both stored averages, but the stored averages are not treated as a strong independent repeatability test because averages can reflect tracking cadence.

Decision:
The measured depletion magnitude and frequency-localized shape match the expected response for a near-pi pulse at mod_depth = 1. A pODMR resonance is present.
