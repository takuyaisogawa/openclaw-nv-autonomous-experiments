Case podmr_065_2026-05-17-071421

I used the provided sequence XML and the saved sequence in raw_export.json to identify the active experiment before deciding. The scan sequence is Rabimodulated.xml with vary_prop mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions acquire a true mS=0 fluorescence reference first after adj_polarize and detection. The optional mS=1 reference block is inactive because full_expt = 0. The second measured readout is therefore the signal after one rabi_pulse_mod_wait_time pulse followed by detection.

The relevant active pulse parameters are:
- mod_depth = 1
- length_rabi_pulse = 52 ns, rounded to the 250 MHz sample clock but unchanged because 52 ns is 13 samples
- setup Rabi frequency estimate = 10 MHz at mod_depth 1
- contrast scale between mS=0 and mS=+1 = 22%

Explicit expected-signal calculation:

For a resonant square Rabi pulse, the transferred population is modeled as
P = sin^2(pi * f_R * t / 2).
With f_R = 10 MHz and t = 52 ns,
pi * f_R * t / 2 = pi * 0.52 / 2 = 0.8168 rad,
P = sin^2(0.8168) = 0.531.

The expected fractional fluorescence change at resonance is then approximately
-0.22 * 0.531 = -0.1169, or an 11.7% drop in the post-pulse readout relative to the mS=0 reference. The observed mean mS=0 reference readout is 47.48 counts, so the expected resonant dip is about -5.55 counts in readout 2 relative to readout 1.

Measured comparison:

The measured combined readout-2 minus readout-1 differences across the scan have mean -0.27 counts, minimum -2.27 counts, and maximum +2.00 counts. The most negative raw point is at 3.830 GHz, but it is only -2.27 counts, less than half of the expected resonant response, and the difference trace does not show a localized ODMR-like dip. A linear-trend residual check gives residual standard deviation about 1.17 counts and most negative residual about -2.04 counts, again much smaller than the expected -5.55 count resonant signal.

The per-average traces mainly show offset and tracking drift between the two stored averages, consistent with the warning that stored averages are not a strong repeatability test here. The combined data show broad drift and readout-to-readout fluctuations rather than a physically expected resonance-sized depression in the post-pulse readout.

Decision: resonance_absent.
