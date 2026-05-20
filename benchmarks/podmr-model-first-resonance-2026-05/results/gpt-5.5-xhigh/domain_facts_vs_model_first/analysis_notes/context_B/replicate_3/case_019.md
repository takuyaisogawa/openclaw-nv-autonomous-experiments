Case: podmr_004_2026-05-16-005019

I used the provided inputs/sequence.xml and the exported variable values. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The branch controlled by full_expt is inactive because full_expt = 0, so the optional mS = +1 reference readout is not acquired. The actual readout roles are:

- readout 1: true mS = 0 reference after adj_polarize and detection, before the microwave pulse.
- readout 2: signal readout after one rabi_pulse_mod_wait_time pulse.

The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so the rounded duration remains 52 ns. The setup fact gives f_Rabi about 10 MHz at mod_depth = 1.

Quantitative expectation:

For a rectangular driven two-level pulse, using cyclic frequencies,

P_transfer(delta) = f_Rabi^2 / (f_Rabi^2 + delta^2) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2)).

On resonance, with f_Rabi = 10 MHz and t = 52 ns:

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated contrast scale of 22 percent between mS = 0 and mS = +1, the expected resonant readout ratio is:

R_signal / R_0 = 1 - 0.22 * 0.996 = 0.781.

The measured combined readout ratios R2/R1 are minimized at:

- 3.875 GHz: 32.423 / 41.288 = 0.785
- 3.880 GHz: 31.808 / 40.423 = 0.787

These are essentially the expected full-transfer pODMR contrast. Away from the dip, the readout ratios are mostly near 0.95 to 1.03, aside from ordinary baseline scatter.

I also evaluated the full detuned Rabi-pulse model as R2 = s * R1 * (1 - 0.22 * P_transfer(freq - f0)). A grid fit over f0 gave best f0 = 3.8776 GHz and scale s = 0.9909 with SSE = 31.75. The no-resonance null model R2 = s * R1 gave s = 0.9522 with SSE = 168.29. Letting the contrast vary gave best contrast = 0.224, also centered at 3.8776 GHz, matching the expected 22 percent scale.

Stored averages both show the same central dip region, but I treat that only as consistency with the combined readout because the stored average count can reflect tracking cadence.

Decision: resonance_present.
