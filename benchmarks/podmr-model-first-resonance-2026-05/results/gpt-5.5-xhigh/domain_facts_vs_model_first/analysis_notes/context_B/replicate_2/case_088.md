Case podmr_074_2026-05-17-092418.

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sequence is Rabimodulated. The active parameters are mod_depth = 1 and length_rabi_pulse = 52 ns.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive. The do_adiabatic_inversion flag is therefore not used in the active path.
- Readout 1 is the detection immediately after optical polarization and before the microwave pulse, so it is the bright m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the pODMR signal readout after the 52 ns microwave pulse.

Quantitative expected-signal model:

The setup gives a Rabi frequency of about 10 MHz at mod_depth = 1. With pulse duration t = 52 ns, the resonant population transfer for a square pulse is

P(Delta=0) = sin^2(pi * f_Rabi * t)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

Using the setup contrast scale of 22%, the expected resonant fluorescence contrast is

C_expected = 0.22 * 0.996 = 0.219, or about 21.9%.

For detuning Delta in Hz, I used

P(Delta) = f_Rabi^2 / (f_Rabi^2 + Delta^2)
           * sin^2(pi * t * sqrt(f_Rabi^2 + Delta^2)).

This gives expected contrast values of about 21.9% at line center, 16.5% at +/-5 MHz, and 6.0% at +/-10 MHz. Since the scan step is 5 MHz, a real resonance in this scan should be a large multi-point dip in readout 2 relative to readout 1.

Measured comparison:

I normalized the combined readouts as contrast = (readout1 - readout2) / readout1. The measured contrast ranges from -4.7% to +7.7%, with mean +0.56%. The largest positive point is at 3.900 GHz:

readout1 = 50.981, readout2 = 47.058, contrast = 7.70%.

This is far below the 21.9% center contrast expected from the active 52 ns, mod_depth = 1 pulse. It also lacks the expected broad/symmetric neighboring structure: for a 3.900 GHz centered resonance, the 3.895 and 3.905 GHz points should both still show about 16.5% contrast, but the measured contrasts are only +5.8% and -3.2%.

I also compared least-squares models on the 21 combined contrast points:

- Constant-baseline null model SSE: 0.0241.
- Fixed physical Rabi line with the expected 21.9% amplitude and center constrained inside the scanned band, allowing a constant offset: best SSE 0.0687, worse than null by 0.0446.
- Free positive-amplitude Rabi line inside the scanned band: best peak contrast only 4.5%, with SSE 0.0202, a small improvement over null and about one fifth of the expected physical amplitude.

The stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence. As a diagnostic, the 3.900 GHz dip is also not stable across the two averages: average 1 has 13.3% contrast there, while average 2 has only 1.9%.

Decision:

The active sequence should produce a large, multi-point pODMR dip if a resonance is present in the scanned band. The measured normalized readout difference is small, inconsistent in shape, and quantitatively incompatible with the expected fixed-amplitude Rabi response. I therefore decide resonance_absent.
