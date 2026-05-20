Case podmr_020_2026-05-16-165809

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName/exported sequence: Rabimodulated.xml.
- The provided XML sets full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- The active measurement first polarizes and detects the true m_S = 0 reference, then applies rabi_pulse_mod_wait_time and detects the MW-driven signal.
- Therefore readout 1 is the bright m_S = 0 reference channel and readout 2 is the post-Rabi pODMR signal channel.
- The active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1 from the provided sequence/variable values. With sample_rate = 250 MHz, 52 ns is exactly 13 samples, so rounding does not change it.

Quantitative model:
The stated setup has f_Rabi approximately 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For the active mod_depth = 1 pulse, f_Rabi = 10 MHz. I used the resonant Rabi transition probability

P(+1) = sin^2(pi * f_Rabi * tau)

with tau = 52 ns. This gives P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the setup m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fluorescence drop is about 0.996 * 22% = 21.9% relative to the readout 1 bright reference. For a typical bright count near 45.2, the expected on-resonance absolute drop is about 9.9 raw-count units.

For detuned points using the square-pulse model

P(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * tau * sqrt(f_Rabi^2 + delta^2)),

the expected drops are approximately 21.9% at 0 MHz detuning, 16.5% at 5 MHz, 6.0% at 10 MHz, and about 1.1% at 20 MHz. Since the scan step is 5 MHz, a real resonance inside the scan should create at least one strong localized depression in readout 2/readout 1 unless it lies well outside the scanned range.

Observed data:
- readout 1 mean = 45.19, readout 2 mean = 44.54.
- The normalized signal readout2/readout1 ranges from 0.929 to 1.040.
- The largest observed apparent drop is 1 - readout2/readout1 = 7.1% at 3.825 GHz, corresponding to an absolute drop of 3.21 raw-count units.
- Around the middle of the scan, where a resonance-like feature would be expected if present in range, the ratio is close to unity: examples include 0.990 at 3.875 GHz, 0.994 at 3.880 GHz, 0.987 at 3.885 GHz.
- The scan shows slow drift/crossing behavior between the two readouts rather than a localized dip with the expected 20% scale. The stored two averages also move strongly with scan index, consistent with tracking or drift cadence rather than an independent repeatability test.

Decision:
The active pulse should produce an almost full pi-pulse contrast on resonance, about a 22% drop in the post-Rabi readout relative to the bright reference. The observed maximum normalized depression is only about one third of that and is not localized in a resonance-shaped feature. I therefore classify this case as resonance_absent.
