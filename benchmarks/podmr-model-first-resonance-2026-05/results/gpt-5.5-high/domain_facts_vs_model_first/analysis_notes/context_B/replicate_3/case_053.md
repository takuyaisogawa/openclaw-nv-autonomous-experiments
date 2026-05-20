Case podmr_039_2026-05-16-221215

I used only the provided sequence XML and raw export in this workspace.

Active sequence and readout roles:

- The sequence is Rabimodulated.xml / Rabimodulated.
- The active microwave pulse is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)`.
- `full_expt = 0`, so the optional separate m_S=+1 reference block is skipped.
- Readout 1 is the first detection immediately after optical polarization, so it is the m_S=0 fluorescence reference.
- Readout 2 is the detection after the Rabi-modulated microwave pulse, so it is the pODMR signal readout.
- The relevant pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. The sample-rate rounding at 250 MHz leaves 52 ns unchanged.

Quantitative expected-signal model:

For a square pulse with Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant transfer probability is

P_res = sin^2(pi f_R tau)
      = sin^2(pi * 10e6 * 52e-9)
      = 0.996.

Using the given fluorescence contrast scale C = 0.22 between m_S=0 and m_S=+1, the expected normalized signal on resonance is

readout2 / readout1 = 1 - C * P_res
                   = 1 - 0.22 * 0.996
                   = 0.781.

So a real on-resonance pODMR response for this pulse should be an approximately 21.9% dip of readout 2 relative to the m_S=0 reference, roughly an 11 count drop for a 50 count reference. Off resonance the two readouts should be much closer, apart from drift and noise.

I also used the detuned Rabi formula

P(delta) = Omega^2/(Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),

with Omega = 2*pi*10 MHz and Delta = 2*pi*(scan_frequency - center), to check whether a finite-width resonance line could explain the normalized data.

Observed data:

- Mean readout 1: 49.35.
- Mean readout 2: 49.19.
- Mean readout2/readout1: 0.997.
- Minimum readout2/readout1: 0.951, only about a 4.7% dip from unity and about a 4.65% dip from the observed mean ratio.
- The largest raw readout2-readout1 depression is about -2.54 counts, far smaller than the approximately -10.8 counts expected for a near-pi pulse with 22% contrast.
- A linear-baseline fit to readout2/readout1 gives RSS = 0.02154.
- A resonance-line fit with free amplitude gives best RSS = 0.01645, but the fitted resonance amplitude is +0.056, i.e. a peak rather than the expected negative dip.
- Forcing the physical -22% contrast resonance gives RSS = 0.03784, worse than the no-resonance linear baseline.

Decision:

The physically expected signal for the active 52 ns, mod_depth = 1 pulse is a large negative pODMR dip in readout 2 relative to readout 1. The measured normalized signal has only small percent-level excursions, no approximately 22% dip, and the fitted finite-pulse resonance shape prefers the wrong sign unless the physical contrast is forced. I therefore decide that a pODMR resonance is absent.
