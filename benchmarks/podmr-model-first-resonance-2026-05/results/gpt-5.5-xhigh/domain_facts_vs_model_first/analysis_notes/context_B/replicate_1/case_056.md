case_id: podmr_042_2026-05-16-225623
timestamp: 2026-05-16-225623

Sequence and readout roles

The provided XML is Rabimodulated.xml. The active scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse branch is:

1. adj_polarize
2. detection
3. wait_for_awg
4. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth)
5. detection
6. wait_for_awg

full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. Therefore readout 1 is the true m_S = 0 optical reference after polarization, and readout 2 is the signal readout after the microwave Rabi pulse. The relevant microwave pulse has mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the pulse duration is already an integer number of 4 ns samples, so the rounded duration remains 52 ns.

Expected signal model

Using the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. I used the two-level detuned Rabi model:

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

where f_R = 10 MHz, t = 52 ns, and delta is the microwave detuning in Hz. The optical readout ratio expected for the post-pulse readout relative to the m_S = 0 reference is:

R_signal / R_ref = 1 - C * P_1(delta)

with contrast C = 0.22 for m_S = 0 versus m_S = +1.

At exact resonance, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.9961. The expected normalized readout ratio is therefore 1 - 0.22 * 0.9961 = 0.7809, an expected dip of about 21.9 percent. On the 5 MHz scan grid, a resonance centered on a scan point would also give neighboring ratios near 0.835 at +/-5 MHz and near 0.94 at +/-10 MHz.

Observed quantitative comparison

The combined readout2/readout1 ratios are:

3.825 GHz 1.0625
3.830 GHz 0.9575
3.835 GHz 1.0276
3.840 GHz 0.9479
3.845 GHz 0.9795
3.850 GHz 1.0369
3.855 GHz 1.0312
3.860 GHz 0.9674
3.865 GHz 0.9976
3.870 GHz 1.0057
3.875 GHz 0.9597
3.880 GHz 0.9811
3.885 GHz 1.0381
3.890 GHz 1.0080
3.895 GHz 0.9996
3.900 GHz 1.0143
3.905 GHz 1.0247
3.910 GHz 0.9983
3.915 GHz 1.0271
3.920 GHz 1.0176
3.925 GHz 0.9920

The ratio mean is 1.0035 with standard deviation 0.0302. The minimum combined ratio is 0.9479 at 3.840 GHz, a 5.2 percent dip, and the next-lowest obvious dip is 0.9597 at 3.875 GHz. These are far smaller than the 21.9 percent on-resonance dip expected from the active pulse.

A direct least-squares comparison also disfavors the resonance model. A constant-ratio null model has SSE = 0.0182. The best resonance-shaped model over centers in the scanned range has SSE = 0.0804 and requires a predicted minimum ratio of about 0.813 at 3.840 GHz, much lower than observed. Stored per-average traces are not a strong repeatability test here, but they also do not show a consistent 20 percent class normalized dip.

Decision

The active 52 ns, mod_depth 1 pulse should be nearly a pi pulse and should produce a large normalized pODMR dip if a resonance is in the scan. The measured second readout remains close to the m_S = 0 reference across the scan, with only small tracking-scale fluctuations. I therefore classify this case as resonance_absent.
