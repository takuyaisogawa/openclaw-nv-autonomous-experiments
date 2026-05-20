Case podmr_003_2026-05-16-003531 analysis

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- Sequence: Rabimodulated.xml / Rabimodulated active instructions.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- readout 1 is the immediately polarized m_S = 0 reference, acquired after adj_polarize and before the swept Rabi pulse.
- readout 2 is the pODMR measurement readout after rabi_pulse_mod_wait_time with length_rabi_pulse.
- mod_depth = 1 from the provided sequence variable values.
- length_rabi_pulse = 5.2e-08 s = 52 ns. With sample_rate = 250 MHz, the rounded duration remains 52 ns.

Quantitative physical model:

The relevant signal is the PL decrease in readout 2 from microwave-driven transfer out of m_S = 0. For a square pulse, the excited population on a transition is modeled as

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2)),

where Omega is the on-resonance Rabi frequency in cycles/s, Delta is detuning in Hz, and t is the pulse duration. The supplied domain facts give Omega about 10 MHz at mod_depth = 1. For t = 52 ns:

Omega * t = 10e6 * 52e-9 = 0.52 cycles
P_on = sin^2(pi * 0.52) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional PL drop in readout 2 is

0.22 * 0.996 = 0.219, or about 21.9%.

From the exported combined readout 2 data, excluding the central 3.870-3.885 GHz dip region, the off-resonant baseline is 36.81 counts. The model therefore predicts an on-resonance drop of

36.81 * 0.219 = 8.07 counts,

giving an expected minimum near 28.74 counts.

Observed readout 2 minimum:

- Minimum at 3.880 GHz: 28.06 counts.
- Observed drop from the off-resonant baseline: (36.81 - 28.06) / 36.81 = 23.8%.

This is close to the expected 21.9% pODMR contrast for a near-pi 52 ns pulse at mod_depth = 1. A simple detuned Rabi model centered at 3.880 GHz gives a central-dip RMS residual of about 1.74 counts over 3.855-3.895 GHz, with the strongest modeled and observed suppression both at 3.880 GHz. The stored per-average traces show the same central suppression but only two averages, so I treat them mainly as tracking-cadence context rather than independent repeatability proof.

Decision: resonance_present. The active post-Rabi readout has a frequency-localized dip with the expected amplitude and approximate width for the pulse parameters and contrast scale.
