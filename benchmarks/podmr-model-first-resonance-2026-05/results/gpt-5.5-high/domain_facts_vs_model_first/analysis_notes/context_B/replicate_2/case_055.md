Case: podmr_041_2026-05-16-224136

Sequence and readout roles

The active sequence is Rabimodulated.xml. It first polarizes and detects immediately, which is the m_S = 0 reference readout. Since full_expt = 0, the conditional 1-level reference block is skipped. The only driven measurement readout is after:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

followed by detection. Therefore readout 1 is the 0-state reference and readout 2 is the signal after the Rabi-modulated microwave pulse.

The provided sequence XML and saved Variable_values give:

- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, rounded to 13 samples at 250 MHz, still 52 ns
- mod_depth = 1
- mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps

There is an embedded sequence-text default in raw_export.json that shows mod_depth = 0.3, but the provided XML file and saved active Variable_values both give mod_depth = 1, so the model calculation uses mod_depth = 1.

Physical model calculation

Using the supplied setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a rectangular resonant pulse of duration tau = 52 ns, the two-level transition probability versus detuning is:

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau)

where Omega and Delta are in cycles per second. The expected normalized fluorescence is:

S/R0 = 1 - C * P(Delta)

with contrast scale C = 0.22.

Numerical values:

- Delta = 0 MHz: P = 0.996, expected contrast = 0.219, expected dip at reference 46 counts = 10.1 counts
- Delta = 2.5 MHz: P = 0.929, expected contrast = 0.204, expected dip = 9.4 counts
- Delta = 5 MHz: P = 0.749, expected contrast = 0.165, expected dip = 7.6 counts
- Delta = 10 MHz: P = 0.273, expected contrast = 0.060, expected dip = 2.8 counts

Thus a resonance inside the scanned band should produce a large, broad feature across adjacent 5 MHz sample points, with a near-resonance readout 2 value around 36 counts for a 46-count reference.

Data check

For the combined data, the normalized contrast 1 - readout2/readout1 has:

- mean = 0.0045
- standard deviation = 0.0303
- maximum observed contrast = 0.0563 at 3.895 GHz
- minimum observed contrast = -0.0484

The deepest observed point is only about a 2.6-count drop from its same-point reference, far below the approximately 10-count drop expected for the active 52 ns, mod_depth 1 pulse on resonance. A least-squares fit of the Rabi lineshape with free baseline and free amplitude chooses an amplitude of only about 0.053, not the expected 0.22. Holding the physical amplitude fixed at 0.22 does not produce a compelling fit; the best center shifts outside the scanned band to avoid imposing the large missing dip.

Decision

Under the active pulse sequence parameters, the expected pODMR resonance signal is much larger than the observed fluctuations. The small trough near 3.89-3.90 GHz is quantitatively consistent with noise or a much smaller effective pulse depth, not with the provided active mod_depth = 1 and 52 ns pulse. Therefore I decide that a pODMR resonance is absent.
