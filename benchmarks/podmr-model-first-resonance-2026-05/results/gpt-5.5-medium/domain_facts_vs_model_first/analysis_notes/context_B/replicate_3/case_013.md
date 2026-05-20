Case: podmr_032_2026-05-14-161051

I used only the provided sequence XML and the raw readout export. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first polarizes and detects the bright m_S = 0 reference, waits, skips the optional m_S = 1 reference because full_expt = 0, then applies one rabi_pulse_mod_wait_time pulse and detects again. Therefore readout 1 is the true 0-level reference and readout 2 is the pulsed pODMR signal readout.

Relevant pulse parameters from the XML:

- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, exactly 13 samples after rounding
- mod_depth = 1
- full_expt = 0, so no active dark-state reference is acquired
- delay_wrt_1mus = 0.2 us
- length_last_wait = 1 us

Quantitative model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular resonant pulse of duration T = 52 ns, the two-level transition probability versus detuning d is

P(d) = (f_R^2 / (f_R^2 + d^2)) * sin^2(pi * T * sqrt(f_R^2 + d^2)).

At d = 0, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fluorescence reduction in the pulsed readout is approximately 0.22 * 0.996 = 21.9% relative to the bright reference. The calculated fractional dips at selected detunings are about 16.5% at +/-5 MHz, 6.0% at +/-10 MHz, and near zero to a few percent by +/-15 to +/-25 MHz, with Rabi side-lobe structure from the finite pulse.

Data check:

The ratio readout2/readout1 shows the strongest narrow depression near 3.875 to 3.880 GHz:

- 3.870 GHz: 0.933
- 3.875 GHz: 0.923
- 3.880 GHz: 0.822
- 3.885 GHz: 1.021

A least-squares fit of a linear baseline minus the explicit finite-pulse Rabi response above gives a best center near 3.877 GHz and a fitted dip amplitude of about 0.113 in ratio units. This is smaller than the ideal 0.219 expected for perfect transfer and full readout contrast, but it has the expected MHz-scale feature at the correct width for the 52 ns, 10 MHz pulse. A no-resonance linear baseline gives SSE 0.0594 on the normalized ratios, while the Rabi-response model gives SSE 0.0385. The stored per-average traces show substantial drift consistent with tracking cadence, so I did not treat the two averages as a strong independent repeatability test.

Decision:

The pulsed readout contains a localized dip with the sign and approximate frequency width expected from the active 52 ns modulated Rabi pulse. The evidence is noisy and the observed amplitude is below the ideal contrast limit, but the quantitative model comparison supports a present pODMR resonance rather than an absent one.
