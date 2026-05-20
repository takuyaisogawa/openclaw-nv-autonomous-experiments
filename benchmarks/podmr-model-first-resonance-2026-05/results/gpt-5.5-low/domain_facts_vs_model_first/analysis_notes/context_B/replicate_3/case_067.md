Case: podmr_053_2026-05-17-042031

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The scan reports SequenceName = Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

1. adj_polarize(... pumping_time ...)
2. detection(...)
3. wait_for_awg(... wait_time ...)
4. if abs(full_expt)>1e-12: acquire an extra 1-level reference
5. rabi_pulse_mod_wait_time(... length_rabi_pulse, mod_depth ...)
6. detection(...)
7. wait_for_awg(... length_last_wait ...)

The relevant variable values are full_expt = 0, length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us, and length_last_wait = 1 us. Because full_expt is zero, the conditional 1-level reference is inactive. Therefore readout 1 is the polarized m_S = 0 fluorescence reference, and readout 2 is the post-Rabi-pulse fluorescence signal. There is no independent m_S = +1 reference readout in this scan.

Expected physical signal calculation

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse of duration t = 52 ns, the resonant transfer probability is

P_1 = sin^2(pi * f_Rabi * t)
    = sin^2(pi * 10e6 * 52e-9)
    = sin^2(0.52 pi)
    = 0.996.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so a true resonance should reduce the post-pulse readout by approximately

fractional drop = 0.22 * 0.996 = 0.219.

With the observed readout-1 baseline around 45-46 counts, the expected resonant readout-2 value is about

46 * (1 - 0.219) = 35.9 counts,

or a drop of about 10 counts relative to the same-point readout-1 reference. This is the expected signal scale for the active sequence if the sweep crosses the addressed resonance.

Observed scan comparison

The combined readout differences, using readout2 - readout1, have mean -0.18 counts and sample standard deviation 1.53 counts. The largest observed deficit is at 3.880 GHz:

readout1 = 45.8846, readout2 = 42.5962, deficit = 3.2885 counts, ratio = 0.928.

A similar deficit appears at 3.890 GHz:

readout1 = 46.3077, readout2 = 43.0769, deficit = 3.2308 counts, ratio = 0.930.

These deficits are far smaller than the approximately 10 count drop predicted by the resonant 52 ns pi-like pulse model. They also do not form a compelling isolated ODMR feature against the point-to-point noise and tracking-related average variation; stored averages are not treated as a strong repeatability test here.

Decision

The active pulse sequence should produce a large post-pulse fluorescence dip if a pODMR resonance is present in the scanned range. The measured readout-2 signal remains close to the readout-1 reference, with only small scattered deficits. I therefore classify this case as resonance_absent.
