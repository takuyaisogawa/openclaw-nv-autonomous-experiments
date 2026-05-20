Case: podmr_033_2026-05-16-203113

I used only the supplied XML/export data for this case.

Active sequence and readout roles

- Sequence name: Rabimodulated.xml.
- The XML instructions first polarize and detect immediately; this is the true m_S = 0 reference and corresponds to readout 1.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active experiment pulse is then PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection; this post-pulse detection corresponds to readout 2.
- The adiabatic inversion flag is present but its block is inside the skipped full_expt reference section, so it is not part of the active signal acquisition.

Pulse parameters from the provided sequence XML / variable values

- sample_rate = 250 MHz, so the time grid is 4 ns.
- length_rabi_pulse = 52 ns, which is exactly 13 samples after rounding.
- mod_depth = 1.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected-signal model

The relevant model is a square resonant Rabi pulse. With the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1, the on-resonance spin-transfer probability for a 52 ns pulse is

P_res = sin^2(pi * f_Rabi * t)
      = sin^2(pi * 10e6 * 52e-9)
      = sin^2(1.6336)
      = 0.996.

With the stated optical contrast scale of about 22% between m_S = 0 and m_S = +1, the expected resonant optical change is

contrast_drop = 0.22 * P_res = 0.219, or about 21.9%.

Using the detuned square-pulse expression

P(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

where Omega = 2*pi*10 MHz and Delta = 2*pi*detuning, the expected contrast drops are:

- detuning 0 MHz: P = 0.996, optical drop = 21.9%.
- detuning 2.5 MHz: P = 0.929, optical drop = 20.4%.
- detuning 5 MHz: P = 0.749, optical drop = 16.5%.
- detuning 10 MHz: P = 0.273, optical drop = 6.0%.

Because the frequency grid is 5 MHz, any resonance lying within the scanned range should have a measured point no more than 2.5 MHz from resonance, so it should produce roughly a 20% drop in readout 2 relative to readout 1 at the nearest sampled frequency.

Observed data comparison

The combined readout statistics are:

- mean(readout 1) = 53.899
- mean(readout 2) = 54.309
- readout2 - readout1: mean = +0.409, minimum = -1.442, maximum = +2.519
- readout2/readout1: mean = 1.0076, minimum = 0.9728, maximum = 1.0457

The largest observed deficit of readout 2 relative to readout 1 is therefore only about 2.7%, far below the approximately 20% to 22% deficit required by the pulse model for a resonance inside the scanned frequency range. A fixed-contrast resonance model with mod_depth = 1 is incompatible with the scan; fitting such a resonance inside the range gives a much worse residual than a no-resonance baseline and still requires a large dip not present in the data.

Decision

The expected pODMR resonance from the active 52 ns, mod_depth = 1 pulse would be a large negative feature in readout 2 relative to the m_S = 0 reference. The observed readouts show only small fluctuations and no physically sized dip. I therefore classify this case as resonance_absent.
