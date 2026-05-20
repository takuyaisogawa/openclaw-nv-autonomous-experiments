Case: podmr_020_2026-05-16-165809

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml / Rabimodulated pulsed ODMR scan with mw_freq varied from 3.825 GHz to 3.925 GHz.
- full_expt = 0, so the optional "1 level reference" block is inactive.
- Readout 1 role: true m_S = 0 bright reference after adj_polarize followed by detection.
- Readout 2 role: signal readout after the modulated Rabi pulse followed by detection.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding keeps it at 52 ns.

Physical model calculation:
For a square resonant pulse, using the stated setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the population transfer after pulse duration t is

P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t).

At resonance, with t = 52 ns:

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the setup contrast scale of 22%, the expected fractional PL drop in readout 2 relative to the m_S = 0 reference is

0.22 * 0.996 = 0.219,

so a resonant point should have readout2/readout1 near

1 - 0.219 = 0.781.

Because the scan grid is 5 MHz, even a resonance halfway between adjacent scan points would be at 2.5 MHz detuning from a sampled point. The same model gives P_transfer(2.5 MHz) = 0.929 and expected readout2/readout1 = 0.796. At 5 MHz detuning the expected ratio is still about 0.835, and at 10 MHz detuning it is about 0.940.

Observed data comparison:
- Combined readout2/readout1 mean: 0.986.
- Minimum combined readout2/readout1: 0.929 at 3.825 GHz.
- At 3.875 GHz the ratio is 0.990.
- The largest ratios exceed 1 near 3.905-3.910 GHz, showing baseline/readout drift rather than stable contrast-normalized behavior.
- The two stored averages have broad opposite trends and ratio scatter of about 0.036-0.047, consistent with tracking cadence or drift rather than independent confirmation of a reproducible resonance.

Decision:
The expected resonant signal for this 52 ns, mod_depth 1 pulse is a large localized reduction of readout 2 to about 0.78-0.80 of readout 1 at the nearest scan point. The observed combined ratio never approaches this value and lacks a localized ODMR dip. The shallow low points are comparable to drift and occur without the expected resonance shape. Therefore the pODMR resonance is absent.
