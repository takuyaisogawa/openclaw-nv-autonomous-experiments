Case: podmr_032_2026-05-16-201700

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The provided XML is Rabimodulated.xml. The active instruction path is:

1. adj_polarize(... pumping_time ...)
2. detection(...): this is the true m_S = 0 fluorescence reference, corresponding to readout 1.
3. wait_for_awg(... wait_time ...)
4. The "Acquire 1 level reference" block is skipped because full_expt = 0.
5. rabi_pulse_mod_wait_time(... length_rabi_pulse, mod_depth, ...)
6. detection(...): this is the microwave-driven pODMR signal, corresponding to readout 2.

The active microwave pulse settings from the provided XML are:

- length_rabi_pulse = 5.2e-08 s = 52 ns.
- sample_rate = 250 MHz, so the rounded pulse is 13 samples = 52 ns.
- mod_depth = 1.
- mw_freq is the scanned parameter, 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected signal model

Using the supplied setup facts:

- Rabi frequency at mod_depth = 1 is approximately 10 MHz.
- Contrast scale between m_S = 0 and m_S = +1 is approximately 22%.

For a rectangular resonant Rabi pulse, the transferred population is

P_1(0) = sin^2(pi * f_R * t).

With f_R = 10 MHz and t = 52 ns:

pi * f_R * t = pi * 0.52 = 1.6336 rad
P_1(0) = sin^2(1.6336) = 0.9961.

The expected fractional fluorescence dip on resonance is therefore:

0.22 * 0.9961 = 0.2191, or about 21.9%.

The mean readout 1 level is 55.2555 counts, so the expected on-resonance driven readout is approximately:

55.2555 * (1 - 0.2191) = 43.1472 counts.

Equivalently, an on-resonance point should be lower than the readout 1 reference by about:

55.2555 * 0.2191 = 12.1083 counts.

Data comparison

From the combined raw readouts:

- readout 1 mean = 55.2555 counts, standard deviation across scan = 1.1199.
- readout 2 mean = 55.2619 counts, standard deviation across scan = 1.2395.
- readout 2 - readout 1 mean = +0.0064 counts.
- readout 2 - readout 1 range = -2.3462 to +3.9423 counts.
- normalized dip, defined as 1 - readout2/readout1, has mean = -0.00043.
- largest observed positive dip = 0.04181, or 4.18%.
- largest observed negative dip/peak = -0.07285, or -7.29%.

The largest observed driven-readout suppression is only about 4.2%, far below the approximately 21.9% expected for the active 52 ns, mod_depth 1 pulse if the scan crossed a pODMR resonance. The point near 3.875 GHz is instead a positive excursion in readout 2 relative to readout 1, opposite the expected fluorescence dip.

I also fit the normalized dip to the rectangular-pulse two-level response

P(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz and t = 52 ns, allowing the resonance center to vary. The best unconstrained fit wants a negative amplitude, -0.063, near 3.8754 GHz, which is opposite the expected pODMR sign. With the physically allowed positive dip amplitude constrained between 0 and 0.22, the best amplitude is only 0.0365, and the improvement over a flat baseline is small.

Conclusion

The active pulse should have produced a large, broad negative fluorescence dip if a resonance were present. The measured driven/reference contrast is near zero on average, lacks the expected 22% scale, and has its strongest fitted feature with the wrong sign. I therefore decide that a pODMR resonance is absent.
