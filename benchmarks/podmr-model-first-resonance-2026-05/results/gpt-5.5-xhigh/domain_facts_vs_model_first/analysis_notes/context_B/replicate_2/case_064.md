Case podmr_050_2026-05-17-005655.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional +1 reference block is skipped.
- Readout 1 is the "true 0 level reference" detection immediately after optical polarization and before the swept Rabi pulse.
- Readout 2 is the detection after rabi_pulse_mod_wait_time, so this is the resonance-sensitive pODMR signal.
- The provided sequence XML and exported variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, 52 ns is exactly 13 samples, so rounding does not change it.

Quantitative model:
Use the square-pulse two-level response for initial mS = 0:

P1(df) = (Omega_R^2 / (Omega_R^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega_R^2 + Delta^2) * t)

where Omega_R / 2pi = 10 MHz * mod_depth = 10 MHz, Delta / 2pi = df, and t = 52 ns. The fluorescence model is

signal/reference = 1 - C * P1(df)

with C = 0.22 for the mS = 0 to mS = +1 contrast scale.

Model values:
- df = 0 MHz: P1 = 0.996, expected fractional drop = 0.219, about 11.6 counts for a 53 count reference.
- df = 2.5 MHz: P1 = 0.929, expected fractional drop = 0.204, about 10.8 counts.
- df = 5 MHz: P1 = 0.749, expected fractional drop = 0.165, about 8.7 counts.

Because the scan step is 5 MHz, any resonance within the swept span should have a point within 2.5 MHz and should therefore produce roughly a 20% dip in readout 2 relative to the readout 1 reference.

Data comparison:
- Mean readout 1 = 53.287 counts; mean readout 2 = 52.929 counts.
- The readout2/readout1 ratio has mean 0.9936, standard deviation 0.0244, and minimum 0.9384.
- The minimum ratio is only about 6.2% below the median, far from the expected ratio near 0.781 for an on-resonance pi pulse.
- The minimum raw readout 2 value is 50.904 counts at 3.910 GHz, only about 2.0 counts below its mean, while the physical model predicts an approximately 9 to 12 count depression at or near resonance.
- A free-amplitude fit of the Rabi line shape to readout2/readout1 gives a best contrast of about 2.4%, not 22%. A forced 22% contrast model fits much worse than a constant-ratio baseline.

Decision:
The active pulse should create a large, broad pODMR dip if a resonance is present in this frequency range. The observed features are small, irregular fluctuations consistent with tracking/noise and are an order of magnitude below the expected pi-pulse contrast. I therefore decide that a pODMR resonance is absent.
