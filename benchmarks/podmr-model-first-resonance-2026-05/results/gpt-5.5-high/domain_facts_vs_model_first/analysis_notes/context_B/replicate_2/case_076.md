Case: podmr_062_2026-05-17-063134

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is not active.
- Readout role 1: detection after adj_polarize, the true m_S = 0 fluorescence reference.
- Readout role 2: detection after a single rabi_pulse_mod_wait_time pulse, the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s, still 52 ns.

Physical model calculation:
The supplied setup has Rabi frequency about 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so the active pulse has f_R = 10 MHz. For a square resonant pulse, transition probability is

P(Delta=0) = sin^2(pi * f_R * t)
           = sin^2(pi * 10e6 * 52e-9)
           = sin^2(1.6336)
           = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance readout-2 dip relative to the readout-1 reference is

0.22 * 0.996 = 0.219, or about 21.9%.

At a typical 50-count raw readout level this corresponds to about 11 counts. Even if the resonance center fell halfway between the 5 MHz scan points, the detuned Rabi formula

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

gives P(2.5 MHz) = 0.929 and an expected dip of about 20.4%. At 5 MHz detuning it is still about 16.5%.

Observed data calculation:
- readout 1 mean = 49.411, population standard deviation across scan points = 1.147.
- readout 2 mean = 49.444, population standard deviation across scan points = 0.868.
- readout2 - readout1 mean = +0.033 counts, paired t about 0.12.
- readout2/readout1 mean = 1.001.
- Largest observed positive dip of readout 2 relative to readout 1 is 6.26% at 3.920 GHz, about 3.15 counts.
- This largest single-point dip is far below the 16-22% dip expected for a near-pi pulse sampled within one 5 MHz step of a resonance, and the readout difference has no consistent negative excursion around a resonance-shaped feature.

Decision:
The active sequence should produce a large pODMR dip if a resonance is present, but the measured signal readout remains statistically consistent with the 0-state reference and lacks the expected contrast scale. I therefore decide resonance_absent.
