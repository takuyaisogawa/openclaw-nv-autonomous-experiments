Case: podmr_073_2026-05-17-090948

Sequence identification

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

1. Polarize the NV.
2. Detect once.
3. Wait.
4. Apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
5. Detect again.

The conditional "Acquire 1 level reference" block is inactive because full_expt = 0. Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-microwave signal readout. The microwave test pulse has length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding leaves 52 ns unchanged because 52 ns is exactly 13 samples at 250 MS/s.

Expected signal model

Given the stated setup, Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant square Rabi pulse with Rabi frequency f_R and duration t, the transferred population is:

P_transfer = sin^2(pi * f_R * t)

Using f_R = 10 MHz and t = 52 ns:

f_R * t = 10e6 * 52e-9 = 0.52 cycles
P_transfer = sin^2(pi * 0.52) = 0.996

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected fractional fluorescence drop in the post-pulse readout at resonance is:

drop_fraction = 0.22 * 0.996 = 0.219

Thus the expected resonant readout ratio is:

readout2 / readout1 = 1 - 0.219 = 0.781

The mean readout level is about 50.17 counts, so the expected resonant dip is about:

50.17 * 0.219 = 10.99 counts

Data check

The combined readouts have mean readout 1 = 50.17 and mean readout 2 = 50.04. The mean ratio readout2/readout1 is 0.998. The lowest observed ratio is 0.950 at 3.855 GHz, corresponding to only a 2.52 count drop. Other local drops are similarly small, for example ratio 0.954 at 3.910 GHz. These are far smaller than the expected ratio near 0.781 and roughly 11 count drop for a resonant near-pi pulse.

The two stored averages do not provide a strong independent repeatability test here, and their strongest ratio dips occur at different frequencies or remain small compared with the physical expectation. This is consistent with tracking/noise-scale variation rather than a pODMR resonance.

Decision

No pODMR resonance is present. The sequence should produce a large readout-2 suppression at resonance, but the observed readout-2/readout-1 variations are only a few percent and do not approach the expected approximately 22% contrast-scale dip.
