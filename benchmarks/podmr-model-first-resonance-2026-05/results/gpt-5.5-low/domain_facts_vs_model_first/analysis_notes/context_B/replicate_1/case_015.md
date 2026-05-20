Active sequence identification:

The saved export identifies the sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active parameter values in the exported scan are the values used for the run: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us, and pumping_time = 1 us.

Because full_expt = 0, the conditional "Acquire 1 level reference" block is skipped. The two stored readout roles are therefore:

- readout 1: true m_S = 0 reference after optical polarization and detection, before the microwave test pulse.
- readout 2: detection after the Rabi-modulated microwave pulse.

Quantitative model:

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%. The given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so this run has f_R = 10 MHz. For a resonant square pulse, the transferred population is modeled as

P_transfer = sin^2(pi * f_R * tau)

with tau = 52 ns. This gives

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected fluorescence contrast on resonance is therefore about

0.22 * 0.996 = 0.219, or 21.9%.

Using the combined readout 2 points outside the central dip region as the local off-resonant baseline gives about 35.26 counts. The expected resonant minimum is then

35.26 * (1 - 0.219) = 27.53 counts.

Observed data:

The combined readout 2 minimum is 26.29 counts at 3.880 GHz. Relative to the same off-resonant readout 2 baseline, this is a 25.4% drop. This is close to the quantitative expectation for a resonant near-pi pulse. The neighboring readout 2 points also form a clear trough around the same frequency, while readout 1 remains near its baseline and does not show a matching fluorescence loss.

Decision:

A pODMR resonance is present. The observed readout 2 dip has the correct role, frequency-localized shape, and expected magnitude for the active pulse sequence.
