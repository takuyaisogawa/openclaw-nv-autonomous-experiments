Case: podmr_026_2026-05-16-182622

Sequence interpretation

The supplied sequence is Rabimodulated.xml with scan variable mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

1. adj_polarize
2. detection
3. wait_for_awg
4. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth)
5. detection
6. wait_for_awg

The full_expt variable is 0, so the "Acquire 1 level reference" branch is inactive. Therefore readout 1 is the true m_S = 0 reference after optical polarization and before the microwave pulse. Readout 2 is the signal readout after the modulated Rabi pulse. do_adiabatic_inversion is not active because it is only inside the skipped branch.

Relevant pulse parameters from the provided XML / variable table:

- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so the rounded pulse duration remains 52 ns
- mod_depth = 1
- expected Rabi frequency at this mod_depth = 10 MHz
- setup contrast between m_S = 0 and m_S = +1 = 22%

Quantitative model

For a rectangular resonant Rabi pulse, using the Rabi frequency in cycles/s,

P_+1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

With f_R = 10 MHz and t = 52 ns:

P_+1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The mean first readout is 49.6108 counts. A resonant point should therefore reduce the second readout by

0.22 * 49.6108 * 0.996 = 10.87 counts.

Even if the resonance lies halfway between two 5 MHz-spaced scan points, the nearest sampled detuning is 2.5 MHz:

P_+1(2.5 MHz) = 0.929, expected drop = 10.14 counts.

At 5 MHz detuning the expected drop is still 8.17 counts. Thus, if a pODMR resonance were inside this scan, the second readout should show a large negative feature relative to the first readout over at least the nearest sampled point(s).

Measured readout comparison

Using the combined raw readouts, readout2 - readout1 has:

- mean = -0.0275 counts
- standard deviation across scan points = 1.471 counts
- most negative point = -3.096 counts at 3.835 GHz
- most positive point = +3.173 counts at 3.830 GHz
- fractional range = -5.94% to +6.54%

The expected resonant fractional drop is 21.91%, far larger than the observed excursions. The largest observed drop is only about 28% of the expected on-resonance drop and is adjacent to an equally large opposite-sign excursion, not a Rabi-limited resonance dip.

Model comparison

I compared the measured difference trace d_i = readout2_i - readout1_i against:

- no-resonance model: d_i = constant offset
- fixed-physics resonance model: d_i = offset - 0.22 * mean(readout1) * P_+1(mw_freq_i - f0), scanning f0 across the acquired frequency span

The best no-resonance constant-offset model has RSS = 43.29. The best fixed-physics resonance model has RSS = 162.72, because it must predict an approximately 9 to 11 count negative dip that is not present in the data.

A free-amplitude fit to the same resonance shape gives a best dip amplitude of only 2.17 counts, about 20% of the physically expected amplitude for the stated contrast and pulse calibration. This is not compatible with the expected pODMR response from a 52 ns, mod_depth = 1 near-pi pulse.

Decision

No pODMR resonance is present in this scan.
