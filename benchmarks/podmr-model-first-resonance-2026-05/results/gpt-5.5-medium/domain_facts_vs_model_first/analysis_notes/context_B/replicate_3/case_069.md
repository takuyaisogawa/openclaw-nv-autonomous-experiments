Case: podmr_055_2026-05-17-045046

Sequence/readout identification:
- The provided sequence is Rabimodulated.xml.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Active detections are:
  1. readout 1: after adj_polarize, before microwave pulse; this is the bright m_S = 0 reference.
  2. readout 2: after rabi_pulse_mod_wait_time; this is the microwave-sensitive pODMR signal.
- Active microwave pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns.
- mod_depth = 1 in the provided sequence XML and variable values.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Rabi frequency scales linearly with mod_depth, so f_R = 10 MHz here.
- For a resonant square Rabi pulse, transition probability is:
  P_1 = sin^2(pi * f_R * t)
- With t = 52 ns:
  pi * f_R * t = pi * 10e6 * 52e-9 = 1.6336 rad
  P_1 = sin^2(1.6336) = 0.996
- With an m_S=0 to m_S=+1 contrast scale of about 22%, the expected on-resonance fluorescence drop in readout 2 relative to readout 1 is:
  0.22 * 0.996 = 0.219, or about 21.9%.
- At the observed mean readout 1 level of 43.81 counts, this corresponds to an expected on-resonance readout-2 decrease of about 9.60 counts.

Observed data comparison:
- Scan range: 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Mean readout 1: 43.81.
- Mean readout 2: 43.45.
- Mean readout 2 - readout 1: -0.365 counts, or -0.77%.
- Most negative relative point: -5.89% at 3.850 GHz.
- Combined difference standard deviation across scan points: 1.61 counts.
- The expected resonant dip for the active pulse is about -9.60 counts, much larger than any observed local drop.

Decision:
The active pulse should produce a large, near-pi-pulse pODMR dip if the resonance is in the scanned range. The data do not show a readout-2 suppression remotely close to the expected approximately 22% contrast-scale drop, and the small readout differences are comparable to point-to-point noise/tracking variation. Therefore, no pODMR resonance is present.
