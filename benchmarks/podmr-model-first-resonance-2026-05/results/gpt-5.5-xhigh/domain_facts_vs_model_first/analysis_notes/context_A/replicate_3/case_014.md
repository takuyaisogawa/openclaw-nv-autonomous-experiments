Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence XML has mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. Therefore, on resonance it should drive population out of m_S = 0 and lower the post-pulse fluorescence by roughly the setup contrast scale.

Readout roles from the sequence:
- Readout 1 follows optical polarization and detection before the microwave pulse, so it is the bright m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout 2 follows the 52 ns modulated microwave pulse and is the resonance-sensitive signal.

The combined readout 1 trace is fairly flat near 38-40 counts, while readout 2 shows a pronounced dip centered at 3.875 GHz: readout 1 is 38.5 and readout 2 is 28.83, a drop of about 25%. The adjacent 3.880 GHz point remains suppressed by about 18%, so this is not just a weak isolated mismatch. The size is close to the expected 22% contrast scale for an approximately pi pulse at this modulation depth.

The stored averages have tracking-scale offsets, so I do not treat them as a strong independent repeatability test. Even so, the resonance-sensitive readout is lower than its reference at the same central frequency in both stored averages. I conclude that a pODMR resonance is present.
