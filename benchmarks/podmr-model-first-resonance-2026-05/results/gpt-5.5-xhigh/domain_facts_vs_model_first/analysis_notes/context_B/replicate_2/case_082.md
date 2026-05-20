Case podmr_068_2026-05-17-075825

I used the provided sequence XML and the raw export only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- do_adiabatic_inversion is inside that skipped block and is not active.
- The first active detection follows adj_polarize and is the true m_S = 0 bright reference. This corresponds to readout 1.
- The second active detection follows rabi_pulse_mod_wait_time and is the pODMR signal readout. This corresponds to readout 2.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.
- mod_depth = 1.

Quantitative model:
Given the supplied setup facts, f_Rabi = 10 MHz * mod_depth = 10 MHz. For a square pulse, the transfer probability versus detuning df is

P(df) = f_Rabi^2 / (f_Rabi^2 + df^2) * sin^2(pi * t * sqrt(f_Rabi^2 + df^2)).

With t = 52 ns and f_Rabi = 10 MHz, the on-resonance transfer is

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the setup contrast scale of 22%, the expected relative fluorescence drop for a resonance at a scan point is

0.22 * 0.996 = 0.219, or about 10.96 counts for a 50-count bright reference.

At detunings from resonance, the expected drops are:
- 0 MHz: 21.9%
- 2.5 MHz: 20.4%
- 5 MHz: 16.5%
- 10 MHz: 6.0%
- 15 MHz: 0.26%

Measured normalization:
I normalized the signal readout by the same-point bright reference as readout2/readout1. The observed relative contrast, 1 - readout2/readout1, ranges from -4.0% to +4.5%, with mean 0.78%. The largest positive contrast is at 3.855 GHz:

readout1 = 51.192, readout2 = 48.904, contrast = 4.47%.

That is far below the approximately 21.9% drop expected from the pulse model. The high-frequency downward trend is common-mode because readout 1 and readout 2 both decrease together; for example at 3.925 GHz the normalized contrast is only 3.42%, not a pi-pulse spin-contrast dip.

Model comparison:
Using readout1 as the local bright reference and the fixed 22% square-pulse pODMR model, the best resonance-center fit over the scan gives RMSE = 2.67 counts. A no-resonance scaled-reference model gives RMSE = 0.96 counts. If the contrast amplitude is fit freely with the same pulse lineshape, the best-fit contrast is only 2.8%, far below the expected 22% for a real pODMR response under these pulse settings.

Decision:
The expected resonant signal for a 52 ns, mod_depth 1 pulse is a large, localized reduction of readout 2 relative to readout 1. The measured data show only small readout ratio fluctuations and common-mode drift, so a pODMR resonance is absent in this scan.
