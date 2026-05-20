Case: podmr_039_2026-05-16-221215

I used only the files in this workspace. The provided sequence XML is Rabimodulated.xml. The active experiment polarizes the NV, performs a first detection as the true m_S = 0 reference, waits, skips the optional m_S = 1 reference because full_expt = 0, applies one rabi_pulse_mod_wait_time pulse, then performs the second detection. Thus readout 1 is the local 0-state reference and readout 2 is the post-microwave-pulse signal. The active microwave pulse has length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:

The given setup has about 22% optical contrast between m_S = 0 and m_S = +1. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so the active pulse has f_Rabi = 10 MHz. For a resonant rectangular pulse, the transferred population is

P_transfer = sin^2(pi * f_Rabi * tau)

with tau = 52 ns. This gives P_transfer = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996. A pODMR resonance at the driven transition should therefore reduce the post-pulse readout by approximately 0.22 * 0.996 = 0.219, or 21.9%, relative to the 0-state reference. Around the observed 50-count baseline, the expected resonant dip is about 10.96 raw-count units.

Observed comparison:

The paired combined readout differences readout2 - readout1 over the 21 frequency points have mean -0.154 counts, corresponding to -0.257% relative change. The largest negative relative change is -4.91% at 3.850 GHz, or -2.54 counts. Nearby and adjacent points are not a clean resonance feature; for example 3.855 GHz is +8.74% relative change. The all-point standard deviation of the relative paired changes is about 3.31%, and the stored averages differ substantially enough that they are better treated as tracking-cadence views rather than a strong repeatability test.

Decision:

The physically expected resonant signal for the active 52 ns, mod_depth 1 pulse is an approximately 22% readout drop, but the data show only small, irregular paired changes with no dip of the expected magnitude or coherent resonance shape. I therefore decide that a pODMR resonance is absent.
