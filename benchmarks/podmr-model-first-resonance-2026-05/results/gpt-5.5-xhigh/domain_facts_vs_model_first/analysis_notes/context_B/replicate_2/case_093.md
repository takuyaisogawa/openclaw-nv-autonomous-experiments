Case: podmr_079_2026-05-17-103702

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional +1 reference block is disabled.
- Readout 1 is the true m_S = 0 reference acquired immediately after polarization.
- Readout 2 is the post-microwave-pulse signal readout after the Rabi-modulated pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse duration remains 52 ns.

Physical model calculation:
Use the square-pulse two-level transition probability

P(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

where Omega / (2*pi) = 10 MHz at mod_depth = 1 and t = 52 ns. On resonance:

P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The given setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should have normalized post-pulse/reference ratio

1 - 0.22 * P(0) = 0.781.

The mean readout-1 level is 50.718 counts, so the expected on-resonance readout-2 drop is about

0.22 * 0.996 * 50.718 = 11.1 counts.

Because the frequency step is 5 MHz, even if the resonance is halfway between sampled points the nearest point has P(2.5 MHz) = 0.929, giving an expected ratio about 0.796 and a drop of about 10.4 counts.

Observed data:
- mean readout 1 = 50.718 counts
- mean readout 2 = 50.782 counts
- mean readout2/readout1 ratio = 1.0017
- minimum readout2/readout1 ratio = 0.9607 at 3.870 GHz
- largest observed readout2 - readout1 deficit = -2.10 counts

The observed data therefore lacks the expected roughly 20-22% normalized dip. The deepest observed point is only a 3.9% deficit and is far smaller than the 10-11 count deficit expected from the active 52 ns, mod_depth 1 pulse.

Model fit check:
- Flat ratio model SSE = 0.01276.
- Best in-scan square-pulse dip model with free dip amplitude gives amplitude 0.0197 and SSE = 0.01212.
- Forcing the physically expected 22% contrast gives best in-scan SSE = 0.07509, much worse than the flat model.

Decision: resonance_absent. The active pulse should produce a large pODMR dip if a resonance were in this scan window, but the post-pulse readout tracks the reference and stays near unity.
