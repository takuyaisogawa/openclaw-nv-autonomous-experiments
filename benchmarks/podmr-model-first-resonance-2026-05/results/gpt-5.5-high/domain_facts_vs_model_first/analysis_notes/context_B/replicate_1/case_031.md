Case: podmr_016_2026-05-16-131456

I used the provided sequence XML and the raw numeric export, without using labels or sibling cases.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is taken immediately after adj_polarize and is the initialized m_S = 0 fluorescence reference.
- Readout 2 is taken after one rabi_pulse_mod_wait_time pulse, so it is the pODMR signal readout.
- mod_depth = 1 from inputs/sequence.xml.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MS/s, the rounded pulse length is round(52 ns * 250 MS/s) / 250 MS/s = 13 samples / 250 MS/s = 52 ns.

Physical model calculation:

The setup Rabi frequency is about 10 MHz at mod_depth = 1, so I used f_R = 10 MHz. For a rectangular driven two-level pulse, the transition probability versus detuning is

P_1(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * tau * sqrt(f_R^2 + df^2)).

At tau = 52 ns and df = 0:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance normalized readout drop is

0.22 * 0.996 = 0.219, or about 21.9%.

Using readout 1 as the local m_S = 0 reference, the observed normalized contrast 1 - readout2/readout1 has its largest feature at:
- 3.870 GHz: 13.2%
- 3.875 GHz: 17.1%
- 3.880 GHz: 16.9%
- 3.885 GHz: 15.0%

Away from this band the normalized contrast is mostly near zero, with both signs present from readout scatter. The minimum raw readout 2 is 39.615 at 3.880 GHz, while the mean readout 1 is 47.237 and the far-off-resonance readout 2 mean is about 46.716.

I also fitted the fixed-pulse Rabi line-shape model to the normalized contrast. With amplitude fixed to the expected 22% contrast scale and allowing only a small constant offset, the best center is 3.877155 GHz. A free-amplitude fit gives center 3.877160 GHz, amplitude 20.4%, offset -0.025%, and reduces the residual sum of squares by about 84.7% relative to a constant no-resonance model. This fitted amplitude is close to the physically expected 21.9% on-resonance drop for a near-pi pulse.

Decision:

The observed dip has the frequency-localized shape, amplitude, and center consistency expected from a pODMR resonance under this sequence. I therefore classify this case as resonance_present.
