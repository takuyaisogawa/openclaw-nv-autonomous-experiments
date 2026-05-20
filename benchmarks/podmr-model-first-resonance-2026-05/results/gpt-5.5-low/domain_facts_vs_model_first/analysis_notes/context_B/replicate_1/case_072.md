Case: podmr_058_2026-05-17-053345

Inputs used only from this isolated workspace: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles

The scan export identifies SequenceName = Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The exported variable values are the active values for the saved experiment:

- length_rabi_pulse = 5.2e-08 s = 52 ns
- mod_depth = 1
- full_expt = 0
- sample_rate = 250 MHz, so the 52 ns pulse is rounded to 52 ns because 52 ns * 250 MHz = 13 samples

In the instructions, the sequence first polarizes and detects the true mS = 0 reference. The optional mS = 1 reference block is guarded by if abs(full_expt)>1e-12, and full_expt is 0, so that block is inactive. After the reference, the sequence applies one rabi_pulse_mod_wait_time pulse with length_rabi_pulse and mod_depth, then detects again. Therefore readout 1 is the polarized bright reference and readout 2 is the post-microwave signal readout.

Quantitative physical expectation

Given the domain facts, the Rabi frequency at mod_depth = 1 is about 10 MHz and scales linearly with mod_depth. Thus for this case Omega_R = 10 MHz. For a rectangular driven two-level pulse, the transition probability versus detuning is

P1(Delta) = (Omega_R^2 / (Omega_R^2 + Delta^2)) * sin^2(pi * sqrt(Omega_R^2 + Delta^2) * tau)

using frequencies in cycles/s. With tau = 52 ns and Omega_R = 10 MHz:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The contrast scale between mS = 0 and mS = +1 is about 22%, so a true on-resonance pi-like pODMR response should reduce the post-pulse fluorescence by about

0.22 * 0.996 = 0.219, or 21.9%

relative to the bright reference. At the observed count level near 45.7 raw counts, this corresponds to an expected dip of roughly 10.0 raw counts in readout 2 relative to readout 1 at resonance. The same model gives only small off-resonant transfer away from the center: at +/-25 MHz, P1 = 0.125 and the expected contrast effect is about 2.7%; at +/-50 MHz, P1 = 0.030 and the expected effect is about 0.7%.

Observed data check

The combined readout means are:

- mean(readout 1) = 45.6813
- mean(readout 2) = 45.5842
- mean(readout 2 - readout 1) = -0.0971

Pointwise readout2/readout1 fractional differences range from about -6.9% to +6.9%, much smaller than the expected -21.9% on-resonance contrast and with both signs present. The largest negative differences occur at 3.885, 3.890, 3.910, and 3.925 GHz, but they are only about -2.85 to -3.23 raw counts, not the expected approximately -10 raw-count dip. The nearby points do not form a clear single resonance lineshape of the quantitative model; positive excursions of similar size also occur elsewhere.

Decision

Because the active pulse should produce a near-maximal pi-pulse response at resonance, the expected signal is large compared with the observed fluctuations. The data do not show the required readout-2 suppression relative to the readout-1 bright reference. I therefore decide that a pODMR resonance is absent.
