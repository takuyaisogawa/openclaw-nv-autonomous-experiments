Case: podmr_019_2026-05-16-164247

Sequence/readout identification

The provided XML is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active sequence has full_expt = 0, so the "Acquire 1 level reference" block is skipped. The active readouts are:

1. After adj_polarize(...) and detection(...): true m_S = 0 level reference. This corresponds to readout 1 in the raw export.
2. After rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...) and detection(...): microwave-pulsed signal readout. This corresponds to readout 2.

The active microwave pulse is not the adiabatic inversion block. It is the modulated Rabi pulse after the skipped full_expt block.

Relevant pulse parameters from XML:

- sample_rate = 250 MHz
- length_rabi_pulse = 5.2e-08 s, rounded to 13 samples = 52 ns
- mod_depth = 1
- do_adiabatic_inversion = 1 is present as a variable, but it is not active because the surrounding full_expt block is skipped

Quantitative physical model

Use a square-pulse Rabi model for the active pulse. The setup Rabi frequency is about 10 MHz at mod_depth = 1. With pulse duration t = 52 ns, the transfer probability versus detuning is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

where f_R and delta are in cycles/s.

At resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected normalized resonant dip in readout 2 relative to readout 1 is

0.22 * 0.9961 = 0.219, or 21.9%.

Because the scan spacing is 5 MHz, any resonance inside the scanned interval should have a measured point within 2.5 MHz. The same model gives:

- detuning 0 MHz: expected dip 21.9%
- detuning 2.5 MHz: expected dip 20.4%
- detuning 5 MHz: expected dip 16.5%
- detuning 10 MHz: expected dip 6.0%

The mean readout 1 level is 46.94 counts, so the expected on-resonance drop is about 10.29 counts.

Data comparison

Using the combined raw export and the sequence-derived readout roles, I computed the normalized pulsed contrast as

y = (readout1 - readout2) / readout1.

Results:

- mean y = 1.70%
- standard deviation across scan points = 2.76%
- maximum y = 7.07% at 3.895 GHz
- minimum y = -5.21%
- largest raw drop readout1 - readout2 = 3.42 counts

The observed maximum normalized drop is much smaller than the >=20.4% expected at some sampled point for an in-range resonance. It is also not a broad/clustered feature with the expected Rabi line shape. A least-squares scan using the square-pulse line shape gives a best positive fitted contrast amplitude of about 4.6%, far below the physical 22% contrast scale. Forcing the physical 22% amplitude leaves large residuals and predicts a dip that is not present.

The two stored averages have different absolute count levels, consistent with tracking/cadence changes, and their largest normalized dips occur at different frequencies. I do not treat them as a strong independent repeatability test.

Decision

No pODMR resonance is present in this scan.
