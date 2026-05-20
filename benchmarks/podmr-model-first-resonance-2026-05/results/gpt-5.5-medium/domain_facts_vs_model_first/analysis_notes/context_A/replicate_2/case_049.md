Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence roles:
- full_expt is 0, so the optional m_S=+1 reference block is inactive.
- Readout 1 is the first detection after optical polarization, serving as the m_S=0 / bright reference.
- Readout 2 is the detection after a modulated Rabi microwave pulse, serving as the pODMR signal readout.

Pulse parameters from the provided sequence XML:
- mod_depth = 1
- length_rabi_pulse = 52 ns
- With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is very close to a pi pulse because 1/(2*10 MHz) is 50 ns.

Expected behavior:
A true on-resonance near-pi pulse should transfer a large fraction of population from m_S=0 toward m_S=+1, giving a localized signal readout decrease on the order of the setup contrast scale, about 22%, relative to the m_S=0 reference, allowing for practical imperfections.

Observed behavior:
Both readouts mainly show a shared upward drift with scan value. The second readout is sometimes below the first, but the largest localized differences are only a few percent of the reference level and are not a clean, strong resonance-shaped contrast. The two stored averages are not treated as strong independent repeatability evidence because they can reflect tracking cadence.

Decision:
The data do not show a convincing pODMR resonance under the active near-pi-pulse sequence. I classify this case as resonance_absent.
