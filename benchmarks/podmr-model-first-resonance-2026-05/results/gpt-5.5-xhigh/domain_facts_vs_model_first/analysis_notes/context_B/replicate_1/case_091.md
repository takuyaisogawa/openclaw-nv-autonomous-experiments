Case podmr_077_2026-05-17-100811

I used inputs/sequence.xml to identify the active Rabimodulated sequence. The active instructions first polarize and detect a true mS=0 reference, then wait. Because full_expt = 0, the optional mS=+1 reference block is skipped even though do_adiabatic_inversion is true. The final active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

followed by detection. Therefore readout 1 is the bright mS=0 reference and readout 2 is the post-Rabi-pulse pODMR signal. The sequence values are sample_rate = 250 MHz, length_rabi_pulse = 52 ns after rounding to 13 samples, mod_depth = 1, and the scan varies mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Quantitative model:

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1. I modeled the rectangular pulse transition probability as

P1(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2*pi*10 MHz, Delta = 2*pi*(f - f0), and t = 52 ns. On resonance, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated mS=0 to mS=+1 contrast scale of about 22%, the expected normalized post-pulse readout at resonance is

S2/S1 = 1 - 0.22 * 0.996 = 0.781

or a dip of about 11.16 raw-count units for the observed mean readout-1 level of 50.94.

I also simulated the scan sampling explicitly over all possible resonance centers inside the scanned 3.825-3.925 GHz interval. Because the frequency step is 5 MHz, every resonance center would be within 2.5 MHz of a sampled point. The rectangular-pulse model predicts the nearest sampled point should have max P1 between 0.929 and 0.996, so the minimum normalized readout should fall between 0.796 and 0.781 if a resonance is present in the scan.

Observed data:

The combined readout-2/readout-1 ratios are centered near 0.997, with min = 0.958 and max = 1.053. No sampled point is below 0.90, 0.85, or 0.80. The raw readout-2 minus readout-1 differences range from -2.19 to +2.63 counts, far smaller than the roughly -11 count resonant dip expected for the active pulse. Stored averages differ mostly as tracking offsets and do not supply an independent repeatability test.

Decision:

The active physical model predicts a large, easily visible negative-going post-pulse readout feature for any resonance in the scanned band. The observed normalized trace lacks that feature and is consistent with baseline scatter/tracking variation rather than pODMR contrast. I decide resonance_absent.
