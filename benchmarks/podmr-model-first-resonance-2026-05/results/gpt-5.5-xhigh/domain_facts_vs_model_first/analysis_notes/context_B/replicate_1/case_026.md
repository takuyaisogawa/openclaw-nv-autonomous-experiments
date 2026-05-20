Case: podmr_011_2026-05-16-120107

Inputs used: inputs/sequence.xml and inputs/raw_export.json in this isolated workspace.

Sequence identification:
- Active sequence: Rabimodulated.xml.
- The scan varies mw_freq from 3825 MHz to 3925 MHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Active readout 1 is the detection immediately after adj_polarize; this is the true m_S = 0 reference.
- Active readout 2 is the detection after rabi_pulse_mod_wait_time; this is the microwave-pulsed signal readout.
- Active pulse duration: length_rabi_pulse = 5.2e-08 s = 52 ns.
- Active mod_depth from the provided XML: 1.

Physical model calculation:

For a square resonant pulse, the transition probability is

P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

using frequencies in cycles/s. The setup facts give f_R = 10 MHz * mod_depth = 10 MHz. With tau = 52 ns,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The readout contrast between m_S = 0 and m_S = +1 is about C = 0.22, so the expected resonant signal ratio is

S2 / S1 = 1 - C * P1(0) = 1 - 0.22 * 0.996 = 0.781.

The mean readout 1 level is 42.20 counts, giving an expected resonant readout 2 level of about 32.95 counts and an expected drop of about 9.25 counts.

Observed data:
- The deepest readout 2 point is at 3880 MHz: readout 1 = 41.404, readout 2 = 33.096.
- The observed ratio there is 33.096 / 41.404 = 0.799, a 20.1% drop relative to readout 1.
- This is close to the expected resonant ratio of 0.781 for a near-pi pulse with 22% contrast.
- Excluding the five points centered on the dip, the off-dip readout 2/readout 1 ratio has mean 0.977 and standard deviation 0.033; the 3880 MHz point is lower by about 5.3 standard deviations.
- A fixed-contrast square-pulse line-shape calculation gives the best center near 3877.25 MHz and reproduces the trough spanning about 3870-3885 MHz.

Decision:

The pulsed readout shows a frequency-localized reduction with the expected sign, amplitude, and approximate width for the active 52 ns, mod_depth 1 Rabi pulse. A pODMR resonance is present.
