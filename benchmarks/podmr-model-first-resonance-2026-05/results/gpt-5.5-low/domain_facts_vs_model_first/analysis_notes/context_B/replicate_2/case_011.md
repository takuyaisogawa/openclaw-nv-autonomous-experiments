Case podmr_028_2026-05-13-100213

I used only the provided XML/export data. The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed sequence has full_expt = 0, so the optional "1 level reference" block is skipped. The recorded readouts are therefore:

- readout 1: after adj_polarize, before the swept Rabi pulse; this is the bright m_S = 0 reference/readout for each frequency point.
- readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection; this is the pODMR signal readout.

Important active parameters from the saved sequence/variable values:

- length_rabi_pulse = 52 ns
- mod_depth = 1
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples exactly
- mw_freq is the swept variable
- do_adiabatic_inversion = true in variables, but the adiabatic inversion calls are inside the skipped full_expt reference branch or commented, so it is not part of the active signal path.

Explicit expected-signal calculation:

Given the stated setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant square Rabi pulse, the transferred population is

P_transfer = sin^2(pi * f_Rabi * t_pulse).

With f_Rabi = 10 MHz and t_pulse = 52 ns:

pi * f_Rabi * t = pi * 10e6 * 52e-9 = 1.6336 rad,
P_transfer = sin^2(1.6336) = 0.996.

With a bright-to-dark contrast scale of 22%, the ideal resonant fractional fluorescence drop is therefore

0.22 * 0.996 = 0.219, or about 21.9%.

The measured readout-1 mean is 27.69 counts. The ideal on-resonance post-pulse readout would be approximately

27.69 * (1 - 0.219) = 21.62 counts,

so the ideal expected drop is about 6.07 counts relative to the bright reference. Real pODMR can show a reduced apparent depth due to detuning grid, finite linewidth, imperfect initialization/readout, tracking drift, and MW delivery, but the expected sign is a localized decrease in readout 2 without the same feature in readout 1.

Observed data:

- readout 1 mean = 27.69, standard deviation across scan = 0.90, range = 26.19 to 29.08.
- readout 2 mean = 27.25, standard deviation across scan = 1.46, range = 24.12 to 30.31.
- readout 2 minimum is 24.12 at 3.905 GHz.
- readout 2 median is 27.23, so the observed dip below the median is 3.12 counts, or 11.4%.
- The readout2/readout1 ratio minimum is also at 3.905 GHz, with ratio 0.873.
- Around the feature, readout 2 is 24.85 at 3.900 GHz and 24.12 at 3.905 GHz, while readout 1 is 26.54 and 27.62 at those same points. Thus the dip is not simply a simultaneous loss in the bright reference.

The stored averages are only two averages and should not be treated as a strong repeatability test; they are useful mainly to understand scale and drift. Still, the combined post-pulse readout has a localized depression of the correct sign and in the correct readout role, with an amplitude about half of the ideal 22% contrast prediction. Given the expected near-pi pulse response and the measured ratio minimum, I decide that a pODMR resonance is present.
