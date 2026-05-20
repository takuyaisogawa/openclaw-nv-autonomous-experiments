Sequence and readout identification

The provided XML is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, wait_time = 2 us, and length_last_wait = 1 us. The instruction block first polarizes and detects immediately; this is the true m_S = 0 bright reference readout. Because full_expt = 0, the intermediate m_S = +1 reference branch is skipped. The active pODMR measurement is then rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) followed by detection, so readout 2 is the microwave-pulse signal readout. The pulse length is unchanged by sample rounding: round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns.

Quantitative expected signal model

Use the supplied setup model: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a rectangular resonant pulse, the population transferred from m_S = 0 to m_S = +1 is

P1(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

where Omega = 2*pi*10 MHz, Delta = 2*pi*delta, and t = 52 ns. At exact resonance, P1 = sin^2(pi * 10 MHz * 52 ns) = 0.996. With the supplied 22% contrast scale, the expected fluorescence suppression is 0.22 * 0.996 = 21.9% of the bright reference. The mean bright reference readout is 48.85, so an exact-resonance point should drop by about 10.7 raw readout units.

Because the scan step is 5 MHz, any resonance lying within the scanned interval should have a sampled point within 2.5 MHz. The same model gives P1 = 0.929 at 2.5 MHz detuning, for a 20.4% fractional suppression, about 10.0 raw units. Even at 5 MHz detuning the expected suppression is 16.5%, about 8.0 raw units.

Observed data comparison

The combined readouts have mean readout 1 = 48.852 and mean readout 2 = 48.767. The paired difference readout2 - readout1 has mean -0.084 raw units, standard deviation 1.039 raw units, minimum -1.827, and maximum +2.404. The largest observed paired suppression, using 1 - readout2/readout1, is 0.0365 or 3.65%, at 3.845 GHz. This is only about 1.83 raw units, far below the 8 to 11 raw units expected from the active pulse model if a resonance were present in the scan. The per-average traces also only reach about 5.4% paired suppression, and those stored averages are treated as tracking-cadence context rather than independent repeatability evidence.

Decision

The active 52 ns, mod_depth 1 pulse should create a large near-pi-pulse pODMR dip on resonance. The measured paired signal lacks any suppression at the expected magnitude or spectral pattern. I therefore classify this case as resonance_absent.
