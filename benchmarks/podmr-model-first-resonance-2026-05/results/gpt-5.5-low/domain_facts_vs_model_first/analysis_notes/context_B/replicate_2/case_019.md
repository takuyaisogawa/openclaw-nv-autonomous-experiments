Active sequence and readout roles

The provided XML is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize and detect, giving readout 1 as the true m_S = 0 reference. full_expt is 0, so the optional m_S = +1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection, giving readout 2 as the signal after the microwave pulse.

Relevant pulse parameters from the XML / exported variable values:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1.
- pulse is the scanned microwave Rabi-modulated pulse before readout 2.

Explicit physical model calculation

Use the given setup model: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Thus f_Rabi = 10 MHz. For a resonant square pulse of duration t = 52 ns, the spin-transfer probability is

P(m_S=+1) = sin^2(theta/2), theta = 2*pi*f_Rabi*t.

theta = 2*pi*(10e6)*(52e-9) = 3.267 rad, slightly above pi.
P(m_S=+1) = sin^2(3.267/2) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant readout-2/readout-1 ratio is

ratio_res = 1 - 0.22*0.996 = 0.7809,

equivalent to a 21.9% dip relative to readout 1.

Data comparison

The combined readouts show the minimum normalized readout 2 at 3.875 GHz:
- readout 1 = 41.2885
- readout 2 = 32.4231
- ratio = 0.7853
- fractional dip = 21.47%

The next point, 3.880 GHz, is similar:
- readout 1 = 40.4231
- readout 2 = 31.8077
- ratio = 0.7869
- fractional dip = 21.31%

This measured dip amplitude is essentially the predicted near-pi-pulse pODMR contrast. Away from the dip, excluding points within 10 MHz of the minimum, the mean readout-2/readout-1 ratio is about 0.980 with standard deviation about 0.035, so the minimum is lower by about 0.195 in ratio units, or about 5.5 baseline standard deviations. The stored two averages both show the same central suppression, though the averages are treated mainly as tracking-cadence information rather than a strong independent repeatability test.

Decision

A pODMR resonance is present. The decision is based on the active sequence roles and on the quantitative resonant-pulse model: the expected 21.9% dip for a 52 ns, mod_depth 1 pulse matches the observed approximately 21.4% normalized dip near 3.875-3.880 GHz.
