Case: podmr_063_2026-05-17-064555

I used the provided sequence XML as the controlling sequence description. The active sequence is Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence has full_expt = 0, so the optional +1 reference block is inactive. The first detection is the initialized/polarized m_S = 0 reference readout, and the second detection is the pODMR readout after the active microwave Rabi pulse. The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns. The stored averages are only two averages and are treated mainly as tracking-cadence information, not as a strong repeatability test.

Quantitative expected-signal model:

The stated setup has about 22% contrast between m_S = 0 and m_S = +1. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so the active pulse has f_R = 10 MHz. For a square resonant pulse of duration t = 52 ns, the transferred +1 population is:

P(+1) = sin^2(pi * f_R * t)
      = sin^2(pi * 10e6 * 52e-9)
      = 0.996.

Thus an on-resonance point should reduce the post-pulse readout relative to the m_S = 0 reference by approximately:

0.22 * 0.996 = 0.219, or 21.9%.

The mean reference readout is 51.82 counts, so the expected resonant dip is about:

51.82 * 0.219 = 11.36 counts.

Observed data comparison:

The combined readout-1 mean is 51.82 counts and the combined post-pulse readout mean is 51.40 counts. The pointwise post-pulse minus reference difference has mean -0.42 counts, standard deviation 1.36 counts, and minimum -2.73 counts. The post-pulse/reference ratio has mean 0.992, standard deviation 0.026, and minimum 0.950. The largest observed fractional loss is therefore about 5.0%, far below the approximately 21.9% loss expected for a resonant near-pi pulse.

I also fit the normalized post-pulse/reference ratios to a square-pulse Rabi response versus detuning,

g(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t),

with a free linear baseline and candidate resonance centers on the measured frequency grid. The fitted contrast amplitudes were small, with the largest positive amplitudes around 0.05, not near the physically expected 0.22. Several candidate centers even gave negative fitted amplitudes. This is consistent with noise/drift and not with a resolved pODMR resonance.

Decision: resonance_absent.
