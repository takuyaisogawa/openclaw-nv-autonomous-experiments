Active sequence and readout roles:

The provided XML is the Rabimodulated sequence. It first runs adj_polarize followed by detection, giving the true m_S=0 reference readout. The conditional "Acquire 1 level reference" block is disabled because full_expt = 0, so there is no separate m_S=1 reference readout in this run. The active signal readout is therefore the later detection after:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

The active pulse duration is length_rabi_pulse = 52 ns. The provided sequence XML and exported variable values give mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative model:

Use the given setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a square pulse of duration t = 52 ns, the excitation probability versus detuning is

P_exc(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

with Omega = 10 MHz in cycles/s units and Delta in Hz. On resonance:

P_exc(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

The current setup contrast scale between m_S=0 and m_S=+1 is about 22%, so the expected on-resonance fractional fluorescence decrease in the post-pulse readout relative to the m_S=0 reference is about:

0.22 * 0.996 = 0.219

For a typical reference readout of about 38 counts, this predicts an on-resonance drop of about 8.3 counts. The expected resonance should be a localized dip in readout 2, not in readout 1, because readout 1 is collected before the microwave pulse.

Data comparison:

The combined m_S=0 reference readout is mostly around 36 to 40 counts. The signal readout after the microwave pulse shows a localized drop centered near 3.880 GHz:

- At 3.875 GHz, reference = 35.94 and signal = 29.35, drop = 6.60 counts.
- At 3.880 GHz, reference = 39.98 and signal = 28.06, drop = 11.92 counts.
- At 3.885 GHz, reference = 36.63 and signal = 32.94, drop = 3.69 counts.

Using the median off-feature signal/reference ratio as a baseline, the largest fractional dip is about 29% at 3.880 GHz. This is somewhat larger than the nominal 22% contrast expectation but is the correct sign, localized in frequency, and of the right order for a near-pi pulse. A least-squares comparison to the square-pulse line shape places the best center near 3.8777 GHz.

The stored per-average data should not be overinterpreted as independent repeatability because stored averages can reflect tracking cadence. Still, both stored averages have their maximum reference-minus-signal drop at 3.880 GHz: about 9.35 counts in average 1 and 14.5 counts in average 2.

There is also a lower signal point at the high-frequency edge, 3.925 GHz, with a 5.77 count drop. Because it is at the scan boundary and does not form the dominant localized feature, I do not treat it as the main resonance. The central 3.875 to 3.885 GHz feature matches the active pulse model and expected contrast scale.

Decision: resonance_present.
