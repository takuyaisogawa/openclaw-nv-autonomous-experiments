Case: podmr_007_2026-05-11-064944

Inputs used: inputs/sequence.xml and the numeric data in inputs/raw_export.json. I did not use labels, previous outputs, sibling cases, or external context.

Active sequence and readout roles:

- The sequence is Rabimodulated.xml. The active instruction flow is: polarize, detect, wait, skip the optional 1-level reference block because full_expt = 0, apply rabi_pulse_mod_wait_time, then detect.
- Readout 1 is therefore the true m_S = 0 reference after optical polarization.
- Readout 2 is the post-Rabi-pulse readout.
- do_adiabatic_inversion = 1 is not active in this run, because the adiabatic-inversion calls are in the disabled full_expt block.
- The active Rabi pulse uses mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already an integer 13 samples, so the rounded pulse length remains 52 ns.

Quantitative physical model:

Use a rectangular driven two-level Rabi model. With the supplied setup facts, the Rabi frequency is approximately

f_R = 10 MHz * mod_depth = 10 MHz.

For detuning df in Hz, the transition probability after pulse duration t is

P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)).

On resonance with t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

The expected normalized fluorescence drop in the post-pulse readout relative to the m_S = 0 reference is then

C * P(0) = 0.22 * 0.9961 = 0.2191,

so a resonance should give readout2/readout1 near 0.7809 at the closest scan point. Since the scan step is 5 MHz and the pulse is near a pi pulse, a real resonance should also have a multi-point central lobe. If centered at the strongest observed dip frequency, 3.855 GHz, the expected normalized drops would be about 0.1647 at 3.850 and 3.860 GHz, and 0.0600 at 3.845 and 3.865 GHz.

Data comparison:

- Mean readout1 = 31.7216, mean readout2 = 31.5458.
- Mean normalized drop (readout1 - readout2) / readout1 = 0.00446, much smaller than 0.2191.
- The largest observed positive normalized drop is 0.1128 at 3.855 GHz, only about half the expected resonant drop.
- The adjacent points do not match the rectangular-pulse line shape: at 3.850 GHz the observed drop is 0.0454 instead of about 0.1647, and at 3.860 GHz the observed value is -0.0203 instead of about 0.1647.
- The minimum observed readout2/readout1 ratio is 0.8872, never close to the expected 0.7809 resonant ratio.
- A fixed-amplitude model with C = 0.22 fit over possible resonance centers from 20 MHz below to 20 MHz above the scan range gives its best center at 3.807121 GHz, outside the scan, with RSS 0.05168 versus a flat-baseline RSS 0.05576. A free-amplitude fit gives amplitude 0.07154 with baseline -0.00819, far below the expected 0.22 contrast scale.

The stored averages were not treated as a strong independent repeatability test because they can reflect tracking cadence. The main decision comes from the active pulse model and the combined raw readouts.

Decision: resonance_absent. The data do not contain the expected near-22% resonant fluorescence drop or the required adjacent-point Rabi line shape; the largest dip-like point is too small and isolated.
