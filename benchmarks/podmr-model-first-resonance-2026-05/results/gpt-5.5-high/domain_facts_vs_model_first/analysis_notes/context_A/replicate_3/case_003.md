Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instruction block first polarizes and detects, which is the true mS=0 fluorescence reference. Because full_expt = 0, the optional mS=1 reference block is skipped. The second active detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so readout 2 is the microwave-pulse signal readout while readout 1 is the pre-pulse reference.

Pulse settings from the provided XML/variable values: mod_depth = 1 and length_rabi_pulse = 52 ns. With the given setup scale of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is essentially a pi pulse on resonance, so a real resonance should reduce the post-pulse fluorescence toward the mS=+1 level. The setup contrast scale is about 22%, so a dip smaller than that can still be physical.

The combined data show a localized dip in readout 2 relative to readout 1 near 3.880-3.885 GHz. At 3.880 GHz the ratio readout2/readout1 is about 0.846, and at 3.885 GHz it is about 0.870, corresponding to a roughly 13-15% reduction. Readout 1 also has tracking/noise variation, but the post-pulse depression is concentrated in the expected signal readout and is compatible with the near-pi pulse contrast. The stored averages are only two tracking-cadence averages, so I do not treat them as a strong independent repeatability test, but both show the same region as low in the signal readout.

Decision: a pODMR resonance is present.
