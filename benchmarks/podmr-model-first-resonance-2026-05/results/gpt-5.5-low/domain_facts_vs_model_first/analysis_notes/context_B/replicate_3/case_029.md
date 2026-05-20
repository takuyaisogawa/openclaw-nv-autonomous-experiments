Active sequence and readout roles

The active pulse sequence is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first performs
polarization and detection, giving readout 1 as the true m_S = 0 reference.
The optional m_S = 1 reference block is skipped because full_expt = 0. The
sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and
mod_depth, followed by detection, giving readout 2 as the microwave-driven
pODMR readout.

Pulse parameters used for the decision

From the exported variable values and provided sequence XML, the relevant pulse
has length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup fact
that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly
with mod_depth, the expected on-resonance transfer probability for a square
Rabi pulse is:

P_transfer = sin^2(pi * f_Rabi * t)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance
drive should reduce the driven readout by approximately:

0.22 * 0.996 = 0.219, or about 22% of the off-resonant readout level.

Quantitative comparison to the data

Using readout 2 off-resonance points outside the central dip as a baseline gives
an off-resonant level of 46.73 counts. The minimum driven readout is 39.12 counts
at 3.875 GHz, a raw drop of 7.62 counts or 16.3%. Normalizing readout 2 by
readout 1 gives an off-resonant ratio of 0.999 and a minimum ratio of 0.806 at
3.875 GHz, a normalized drop of 19.3%. This is close to the expected 21.9%
signal from the Rabi-pulse model, allowing for finite linewidth, scan sampling,
and experimental noise.

The reference readout does not show the same central dip; its values remain in
the 45.27 to 48.71 count range with no comparable resonance feature. The two
stored averages are not treated as a strong independent repeatability test, but
both include a central driven-readout suppression near 3.875 to 3.880 GHz.

Decision

A pODMR resonance is present. The observed centered suppression in the driven
readout has the correct readout role, frequency location within the scan, and
quantitative scale expected from a 52 ns, mod_depth = 1 Rabi pulse with the
given 22% contrast.
