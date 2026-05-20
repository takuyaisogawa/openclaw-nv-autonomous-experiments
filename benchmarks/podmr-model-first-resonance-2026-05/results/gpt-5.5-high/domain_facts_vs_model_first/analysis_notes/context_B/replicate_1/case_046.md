Case podmr_032_2026-05-16-201700.

Sequence inspection:
- Active sequence: Rabimodulated.xml / Rabimodulated.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped.
- Readout 1 role: bright mS = 0 reference acquired after adj_polarize and before the microwave Rabi pulse.
- Readout 2 role: signal acquired after the microwave Rabi pulse.
- mod_depth = 1 from the provided sequence XML and scan variable values.
- Rabi pulse duration: length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s, still 52 ns.

Quantitative physical expectation:
The setup Rabi frequency is about 10 MHz at mod_depth = 1, with approximately linear scaling, so this sequence should have f_R = 10 MHz. For a resonant rectangular Rabi pulse, the transfer probability is

P = sin^2(pi * f_R * t).

With t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

Using the stated mS = 0 to mS = +1 contrast scale of 22%, an on-resonance signal readout should be

signal/reference = 1 - 0.22 * 0.996 = 0.7809.

The mean reference readout is 55.255 counts, so the expected resonant drop is about

55.255 * (1 - 0.7809) = 12.1 counts.

Data comparison:
- Mean readout 1: 55.255 counts.
- Mean readout 2: 55.262 counts.
- Mean signal-reference difference: +0.006 counts.
- Signal/reference ratio: mean 1.0004, standard deviation 0.0275, minimum 0.9582, maximum 1.0729.

The largest observed negative excursion is only about 4.2% below the reference, far smaller than the approximately 21.9% drop expected for a real resonance under this near-pi pulse. A detuned Rabi-response model with the fixed 10 MHz Rabi frequency and 22% contrast, allowing the resonance center to move over the scanned range and allowing a multiplicative baseline factor, gives a worse squared residual than a flat ratio baseline. The data therefore do not show the expected pODMR dip.

Decision: resonance_absent.
