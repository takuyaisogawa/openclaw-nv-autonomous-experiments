Case: podmr_026_2026-05-16-182622

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. The active sequence is Rabimodulated.xml / Rabimodulated with vary_prop = mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The saved export contains the active run values: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us, pumping_time = 1 us, and length_last_wait = 1 us.

Readout roles from the sequence:

- First detection occurs immediately after adj_polarize and is the true m_S = 0 level reference.
- The optional m_S = 1 reference block is disabled because full_expt = 0.
- The second detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the signal readout after the microwave pulse.

Physical model calculation:

The setup Rabi frequency is about 10 MHz at mod_depth = 1, and the active mod_depth is 1, so f_Rabi ~= 10 MHz. For a resonant square Rabi pulse of duration t = 52 ns, the driven transition probability is

P = sin^2(pi * f_Rabi * t)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pODMR response should reduce the signal readout relative to the m_S = 0 reference by approximately

0.22 * 0.996 = 0.219, or 21.9%.

The mean readout-1 reference in the combined data is 49.61 counts, so the expected on-resonance drop is about 10.87 counts, giving a signal readout near 38.7 counts at resonance if the pulse is resonant and the contrast applies.

Observed quantitative comparison:

- Mean readout 1 = 49.61.
- Mean readout 2 = 49.58.
- Mean readout2 - readout1 = -0.027 counts.
- Standard deviation of pointwise differences = 1.47 counts.
- The largest negative pointwise difference is -3.10 counts at 3.835 GHz, only about 6% of the reference, and it is not part of a convincing resonance profile.
- The minimum readout2/readout1 ratio is 0.9406, far from the expected resonant ratio near 0.781.

The per-average traces show comparable scatter and tracking-like offsets; the stored two averages are not strong independent repeatability evidence. Because the active pulse should produce an approximately 22% signal loss on resonance but no such feature appears anywhere in the sweep, the data do not support a pODMR resonance.

Decision: resonance_absent.
