Case: podmr_066_2026-05-17-072831

Input restrictions followed: I used only inputs/sequence.xml and inputs/raw_export.json in this isolated workspace, not labels or external cases.

Sequence and roles:
- Active sequence: Rabimodulated.xml.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S=+1 reference block is inactive.
- Readout 1 is acquired immediately after optical polarization and is the m_S=0 bright reference.
- Readout 2 is acquired after the modulated microwave Rabi pulse and is the signal readout.
- length_rabi_pulse = 52 ns.
- mod_depth = 1 from the provided sequence XML and exported variable values.

Quantitative physical expectation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, the resonant Rabi frequency is f_R = 10 MHz.
- For a square resonant pulse of duration t = 52 ns, the transition probability is:
  P = sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S=0 to m_S=+1 contrast scale of 22%, the expected resonant fluorescence loss in readout 2 relative to readout 1 is:
  0.22 * 0.996 = 0.219, or about 21.9%.
- Around the measured mean readout level of about 45.9 counts, this corresponds to an expected resonant drop of about 10.1 counts if a fully driven pODMR resonance is sampled.

Observed data check:
- Mean readout 1 = 45.900.
- Mean readout 2 = 45.369.
- Mean difference readout2 - readout1 = -0.531 counts, about -1.2%.
- The strongest raw ratio dip is readout2/readout1 = 0.9358 at 3.890 GHz, a 6.4% decrease, much smaller than the expected 21.9% resonant contrast.
- Neighboring points do not form a convincing resonance: 3.875 GHz has readout2 above readout1 by 2.404 counts, while the apparent negative differences near 3.880-3.910 GHz are irregular and comparable to tracking/average offsets.
- Stored averages are not a strong independent repeatability test here; the two averages mainly show baseline shifts consistent with tracking cadence.

Decision:
The expected on-resonance signal for the active sequence is a large near-pi-pulse dip in the post-microwave readout relative to the m_S=0 reference. The measured scan does not show that scale or a coherent pODMR line shape, so I classify this case as resonance_absent.
