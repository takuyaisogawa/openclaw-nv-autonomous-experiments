Case: podmr_040_2026-05-16-222642

Input files used: inputs/sequence.xml and inputs/raw_export.json.

Active sequence/readouts

The provided XML is Rabimodulated.xml. The active path is:

1. adj_polarize with pumping_time = 1 us.
2. detection: this is the true m_S = 0 reference readout.
3. wait_for_awg for 2 us.
4. The optional +1 reference block is skipped because full_expt = 0, even though do_adiabatic_inversion is true.
5. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
6. detection: this is the post-microwave-pulse signal readout.

Thus readout 1 is the zero-state reference, and readout 2 is the pODMR signal after the modulated Rabi pulse.

Pulse parameters from the provided XML:

- mod_depth = 1
- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, rounded by the sequence to round(52 ns * 250 MHz) / 250 MHz = 52 ns
- scan parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps

Physical model calculation

Using the supplied setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square pulse, the resonant transition probability is

P_1(0) = sin^2(pi * f_Rabi * t).

With f_Rabi = 10 MHz and t = 52 ns:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonance should produce a fractional fluorescence drop of

0.22 * 0.996 = 0.219.

The mean zero-reference readout is 47.188 raw units, so the expected on-resonance drop in readout 2 relative to readout 1 is about

47.188 * 0.219 = 10.34 raw units.

I also used the off-resonant two-level Rabi model

P_1(delta) = Omega^2 / (Omega^2 + delta^2) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * t),

with Omega / (2 pi) = 10 MHz and t = 52 ns, and compared the scan to a baseline plus this expected dip shape.

Data comparison

The measured combined readouts have:

- mean readout 1 = 47.188
- mean readout 2 = 46.660
- mean difference readout2 - readout1 = -0.527 raw units
- standard deviation of pointwise differences = 1.312 raw units

The observed normalized contrast 1 - readout2/readout1 ranges from -0.042 to 0.076, with mean 0.0108. The largest apparent drop is at 3.885 GHz:

- readout 1 = 48.365
- readout 2 = 44.673
- drop = 3.692 raw units
- normalized contrast = 0.076

This largest single-point drop is much smaller than the approximately 10.34 raw-unit, 21.9% drop expected for a resonance under the active pulse parameters.

The explicit line-shape fit does not support the expected resonance either. Fitting normalized contrast as baseline + A * P_1(delta) over possible centers gives a best amplitude A = -0.058, i.e. the best model feature is inverted relative to the expected positive contrast dip. Forcing the physically expected A = 0.22 drives the best center outside the scan edge and does not identify a credible in-window resonance. In count units, fitting readout2 - readout1 as baseline - A * P_1(delta) similarly gives A = -2.72 raw units, again opposite in sign to the expected drop.

Decision

Given the active 52 ns, mod_depth 1 pulse, a real pODMR resonance should be large and dip-like in the second readout relative to the zero reference. The measured variation is small, inconsistent in sign/shape, and not supported by the quantitative Rabi line-shape model. I therefore classify this case as resonance_absent.
