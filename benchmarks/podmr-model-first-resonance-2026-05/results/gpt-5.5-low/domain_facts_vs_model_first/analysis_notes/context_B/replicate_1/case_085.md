Case podmr_071_2026-05-17-084118 analysis

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS=+1 reference block is inactive.
- Readout 1 role: the first detection after optical polarization, a true mS=0 bright reference.
- Readout 2 role: detection after a microwave rabi_pulse_mod_wait_time block.
- Active microwave pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s still 52 ns.
- mod_depth: the provided XML file and exported Variable_values give mod_depth = 1.

Physical model calculation:
For a square resonant Rabi pulse, the driven transition probability is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * tau)

using frequency units in Hz. The setup facts give Omega = 10 MHz at mod_depth = 1, and tau = 52 ns.

At resonance:
- pi * Omega * tau = pi * 10e6 * 52e-9 = 1.6336 rad
- P(0) = sin^2(1.6336) = 0.996

With the stated 22% mS=0 to mS=+1 contrast, an on-resonance pulse should reduce the post-pulse readout by about

0.22 * P(0) = 0.219

or approximately 21.9% relative to the bright reference. With readout levels near 50 counts, the expected resonant dip is about 10.8 counts.

Observed data:
- Mean readout2/readout1 ratio = 1.0004.
- Standard deviation of readout2/readout1 ratio across scan points = 0.0304.
- Lowest readout2/readout1 ratio is 0.9457 at 3.860 GHz, a 5.4% depression.
- Largest readout2 - readout1 negative difference is -2.79 counts, also at 3.860 GHz.

Model comparison:
- A fixed 22% contrast Rabi-response model with center scanned over the measurement range gives residual sum of squares about 0.0857 in readout2/readout1.
- A flat no-resonance model gives residual sum of squares about 0.0184.
- A linear baseline gives residual sum of squares about 0.0179.

Decision:
The active pulse should produce an almost full population transfer at resonance and therefore a large approximately 22% pODMR dip in readout 2 relative to the mS=0 reference. The measured readout ratio stays near unity with only small scatter-level fluctuations and no feature of the expected magnitude or line shape. Stored averages are not treated as independent confirmation because they can reflect tracking cadence. I therefore classify this case as resonance_absent.
