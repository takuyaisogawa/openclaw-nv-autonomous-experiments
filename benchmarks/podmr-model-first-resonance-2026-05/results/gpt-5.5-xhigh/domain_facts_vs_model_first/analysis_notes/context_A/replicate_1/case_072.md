Sequence inspection:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional +1 reference block is inactive.
- The first active detection follows adj_polarize and is the polarized mS=0 reference.
- The second active detection follows rabi_pulse_mod_wait_time and is the post-microwave-pulse pODMR signal.
- mod_depth = 1 and length_rabi_pulse = 52 ns. At the provided 10 MHz Rabi scale, this is essentially a pi pulse.

Data judgment:

For a single NV with the stated setup contrast scale, an on-resonance 52 ns pulse at mod_depth 1 should produce a clear post-pulse readout reduction close to the 22% contrast scale at or near one of the 5 MHz-spaced scan points. The combined post-pulse deficits relative to the mS=0 reference are small and sign-changing, with the largest combined deficit only about 7%. The stored averages show similar-size excursions, but those averages mainly reflect tracking cadence and are not a strong independent repeatability test.

Decision: resonance absent.
