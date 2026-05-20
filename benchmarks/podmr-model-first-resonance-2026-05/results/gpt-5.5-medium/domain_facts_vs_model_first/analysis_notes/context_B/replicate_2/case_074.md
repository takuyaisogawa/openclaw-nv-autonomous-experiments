Case: podmr_060_2026-05-17-060259

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml / Rabi-modulated pODMR with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction flow is:

1. adj_polarize
2. detection: readout 1, the polarized m_S = 0 reference
3. wait
4. the optional m_S = +1 reference block is skipped because full_expt = 0
5. rabi_pulse_mod_wait_time
6. detection: readout 2, the signal after the microwave pulse

The relevant pulse parameters are length_rabi_pulse = 52 ns and mod_depth = 1 from the provided sequence XML and the exported active Variable_values. The embedded saved sequence text contains an older/default-looking mod_depth = 0.3, but the explicit active values and the standalone provided XML both give mod_depth = 1, so I use mod_depth = 1.

Physical signal model:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular resonant pulse of duration t, the population transferred out of m_S = 0 is

P_1(delta=0) = sin^2(pi * f_Rabi * t).

With f_Rabi = 10 MHz and t = 52 ns:

P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant readout drop is

0.22 * 0.996 = 0.219, or 21.9% of the m_S = 0 fluorescence.

The observed readout 1 baseline is about 50.94 raw-count units, so a resonance near the scan range should produce a readout 2 value around

50.94 * (1 - 0.219) = 39.78,

that is a readout2 - readout1 dip of about -11.16 raw-count units at resonance.

I also evaluated the detuned rectangular-pulse model across the scanned points:

P_1(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2)).

For any resonance center landing on one of the scanned frequency points, the model predicts the same approximately -11.16 count resonant dip, with off-resonant values returning near the readout 1 baseline.

Observed data:

Combined readout 1 mean = 50.94.
Combined readout 2 mean = 50.20.
Mean readout2 - readout1 = -0.75 counts.
Standard deviation of readout2 - readout1 across scan points = 1.51 counts.
Most negative combined difference = -3.63 counts at 3.875 GHz.

Per-average checks are not treated as a strong repeatability test because stored averages can reflect tracking cadence. Still, the two averages have mean readout2 - readout1 values of -0.78 and -0.71 counts, and their most negative differences occur at different/weakly useful points. The combined trace does not show the approximately 11-count resonant depletion expected from a near-pi pulse at mod_depth = 1.

Decision: resonance_absent. The observed contrast is far below the quantitative expected pODMR signal from the active pulse parameters, and the apparent variations are consistent with small raw readout fluctuations rather than the required resonant dip.
