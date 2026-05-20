Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects the bright mS=0 reference. Because full_expt is 0, the optional mS=+1 reference block is inactive even though the adiabatic inversion boolean is set. The only microwave manipulation used for the measurement is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection readout. Thus readout 1 is the pre-microwave bright reference and readout 2 is the post-pulse signal.

Decision reasoning:

At mod_depth = 1 the setup Rabi frequency is about 10 MHz, so a 52 ns pulse is approximately a pi pulse. If the microwave frequency were resonant, the post-pulse signal should show a substantial reduction relative to the mS=0 reference, on the order of the stated 22% setup contrast scale. The observed paired differences between readout 2 and readout 1 are much smaller, generally only a few percent, change sign repeatedly, and do not form a consistent resonance-shaped dip. The per-average overlay is dominated by tracking-scale drift between stored averages rather than an independently repeated spectral feature. The largest local negative deviation near 3.900 GHz is isolated and not supported by adjacent points or the second readout structure.

Conclusion:

No reliable pODMR resonance is present in this scan.
