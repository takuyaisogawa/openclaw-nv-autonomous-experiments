Case podmr_081_2026-05-17-110558

I used inputs/sequence.xml as the controlling sequence description. The active sequence is Rabimodulated.xml. The instructions first polarize and detect, then wait. Because full_expt = 0, the optional +1 reference block is skipped. The only microwave-driven measurement block is then:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on);
PSeq = detection(PSeq, sample_rate, delay_wrt_1mus, ch_on);

Therefore readout 1 is the polarized mS = 0 reference and readout 2 is the post-Rabi-pulse signal. The XML values are mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate rounds 52 ns to 52 ns exactly at 250 MS/s.

Quantitative expected signal model:

The provided setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. Thus f_R = 10 MHz for this sequence. For a rectangular resonant pulse, the transition probability is

P(detuning) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz, Delta = 2*pi*detuning, and t = 52 ns. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current mS = 0 to mS = +1 contrast scale is about 22%, so the expected fluorescence drop in readout 2 relative to readout 1 at resonance is

0.22 * 0.996 = 0.219, or about 21.9% of the readout 1 level.

With the observed mean readout 1 of 47.34 counts, this corresponds to an expected on-resonance drop of about 10.37 counts. The scan step is 5 MHz, so if a resonance lies within the scanned interval the nearest sampled point should be within at most 2.5 MHz. The same model gives:

- detuning 0 MHz: P = 0.996, expected drop = 10.37 counts
- detuning 2.5 MHz: P = 0.929, expected drop = 9.68 counts
- detuning 5 MHz: P = 0.749, expected drop = 7.80 counts
- detuning 10 MHz: P = 0.273, expected drop = 2.84 counts
- detuning 20 MHz: P = 0.0479, expected drop = 0.50 counts

Observed data:

The combined readout difference readout2 - readout1 has mean -0.24 counts, standard deviation 1.30 counts, minimum -2.15 counts, and maximum +1.69 counts. The normalized contrast (readout2 - readout1) / readout1 ranges from -4.52% to +3.72%. The largest negative deviations occur at isolated points and are comparable to the point-to-point fluctuations; they are not the approximately 20% broad dip expected from a 52 ns, mod_depth 1 pi pulse. Stored average overlays are not treated as an independent repeatability test because the averages can reflect tracking cadence.

Decision:

Given the active readout roles and the quantitative pulse model, a true pODMR resonance within the scan should have produced a much larger drop in the post-pulse readout than is present. I therefore classify this case as resonance_absent.
