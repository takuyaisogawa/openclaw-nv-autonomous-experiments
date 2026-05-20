Sequence and readout interpretation:

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects, giving the true m_S = 0 reference readout. The optional m_S = 1 reference block is disabled because full_expt = 0. The second acquired readout follows a single rabi_pulse_mod_wait_time pulse, so readout 2 is the pODMR signal channel. The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. Although do_adiabatic_inversion is true, that block is inside the disabled full_expt branch and is not active for the acquired signal.

Quantitative expected signal:

The provided setup calibration gives a Rabi frequency of about 10 MHz at mod_depth = 1, approximately linear in mod_depth. For a resonant 52 ns pulse, the expected transferred population is

P = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With an m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant pulse should reduce the signal readout by about

0.22 * 0.996 = 0.219,

or about 22% relative to the m_S = 0 reference, ignoring smaller readout drift and normalization errors. Thus an on-resonance signal/reference ratio near 0.78 is physically expected for this pulse, while off resonance the ratio should be near the local baseline.

Observed data:

The combined readout 1 values are mostly flat around 36 to 40 counts and do not show a corresponding narrow dip at the candidate resonance. Readout 2 has a localized trough centered at 3.880 GHz:

- 3.870 GHz: readout1 = 38.21, readout2 = 33.38, ratio = 0.874
- 3.875 GHz: readout1 = 35.94, readout2 = 29.35, ratio = 0.817
- 3.880 GHz: readout1 = 39.98, readout2 = 28.06, ratio = 0.702
- 3.885 GHz: readout1 = 36.63, readout2 = 32.94, ratio = 0.899
- 3.890 GHz: readout1 = 37.23, readout2 = 36.77, ratio = 0.988

Using points outside 3.865 to 3.885 GHz, the median signal/reference ratio is 0.989. The minimum ratio at 3.880 GHz is lower by 0.287 relative to this baseline. This observed dip is somewhat deeper than the simple 22% contrast estimate, but it has the expected sign, is localized in the signal readout rather than the reference, and is centered within the scanned microwave range. The per-average traces both show the same main depression around 3.875 to 3.880 GHz; the stored averages should be treated mainly as tracking cadence, not a strong independent repeatability test.

Decision:

A pODMR resonance is present. The active pulse is essentially a pi pulse at the stated calibration, and the measured signal channel contains a localized drop of the expected physical sign and comparable scale near 3.88 GHz.
