Active sequence and readout roles

The provided XML is Rabimodulated.xml. The instructions first polarize the NV and call detection, then wait. Because full_expt = 0, the optional "Acquire 1 level reference" block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by a second detection. Therefore readout 1 is the direct polarized m_S = 0 reference, and readout 2 is the post-Rabi-pulse signal readout. The active pulse is a rectangular modulated Rabi pulse, not the adiabatic inversion path. From the XML variable values, length_rabi_pulse = 52 ns and mod_depth = 1.

Expected signal model

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse, the resonant transfer probability is

P(Delta = 0) = sin^2(pi * f_Rabi * tau).

With f_Rabi = 10 MHz and tau = 52 ns, f_Rabi * tau = 0.52 cycles, so P(0) = sin^2(pi * 0.52) = 0.996. The contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance transition should reduce the post-pulse fluorescence by approximately 0.22 * 0.996 = 0.219, or about 21.9% of the polarized reference. The mean readout 1 level is 48.33 counts, so the expected resonant dip in readout 2 is about 10.59 counts.

For finite detuning I used the standard driven two-level rectangular-pulse model:

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * tau * sqrt(Omega^2 + Delta^2)),

where Omega is the 10 MHz Rabi frequency in cycles/s and Delta is the microwave detuning in Hz. The expected normalized fluorescence is then proportional to 1 - 0.22 * P(Delta).

Data comparison

The scan covers 3.825 to 3.925 GHz in 5 MHz steps. The mean readout 1 is 48.33 counts and the mean readout 2 is 47.86 counts. The normalized readout2/readout1 ratio ranges from 0.908 to 1.041 with mean 0.991 and standard deviation 0.031. The largest apparent normalized dip is about 9.2%, much smaller than the approximately 21.9% dip expected for this pulse if a resonance is in the scan range, and it is not shaped like the driven-pulse response.

I also fit the explicit resonance model above over possible resonance centers in the scanned frequency range, allowing only an overall scale factor. The flat normalized model has RSS = 0.0204, while the best resonance-shaped model has RSS = 0.0636, so imposing the expected physical resonance worsens the fit. In count units, the flat scaled-reference residual RMS is about 1.52 counts, while the best resonance model residual RMS is about 2.69 counts. Stored averages are only two and should not be treated as a strong repeatability test; the decision is based on the physical signal size expected from the pulse and the absence of that large, model-shaped dip.

Decision: resonance_absent.
