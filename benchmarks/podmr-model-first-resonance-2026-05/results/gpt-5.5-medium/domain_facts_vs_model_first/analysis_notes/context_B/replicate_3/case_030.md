Case: podmr_015_2026-05-16-130043

I used the provided sequence XML and raw export values, not labels or external cases.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- Readout 1 is the fluorescence detection immediately after optical polarization, i.e. the true m_S = 0 reference.
- Readout 2 is the detection after one modulated Rabi microwave pulse, so this is the pODMR-sensitive readout.
- length_rabi_pulse = 52 ns.
- mod_depth = 1.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the driven on-resonance transition probability after pulse duration t is
  P = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional fluorescence drop in the post-pulse readout is
  0.22 * 0.996 = 0.219, or 21.9%.

Observed quantitative comparison:
- Away from the central feature, readout 2 baseline is about 44.59 counts.
- The model therefore predicts an on-resonance drop of about 44.59 * 0.219 = 9.77 counts.
- The observed readout 2 minimum is 35.87 counts at 3.875 GHz, a drop of 8.73 counts from the off-feature baseline, or 19.6%.
- Readout 1 is the m_S = 0 reference and does not show a comparable central drop; its minimum deviation from its off-feature baseline is about 5.3%, much smaller and not centered in the same way.
- The readout-1 minus readout-2 difference peaks around the central dip: 10.35 counts at 3.875 GHz and 8.15 counts at 3.880 GHz.

Decision:
The measured pODMR-sensitive readout shows a central fluorescence dip with the correct sign, location within the scan, and magnitude expected from a near-pi pulse under the stated Rabi model. A pODMR resonance is present.
