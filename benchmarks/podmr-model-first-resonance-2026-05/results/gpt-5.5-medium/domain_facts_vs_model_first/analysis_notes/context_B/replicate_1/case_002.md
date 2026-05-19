<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The active microwave operation in the measurement body is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

followed by detection. The earlier detection after adj_polarize is the true m_S = 0 reference. The "Acquire 1 level reference" block is inactive because full_expt = 0, so there is no separate +1 reference in this run. Therefore readout 1 is the pre-pulse 0-level reference, and readout 2 is the post-Rabi-pulse pODMR signal readout.

Sequence parameters from inputs/sequence.xml:

- sample_rate = 250 MHz
- varied parameter = mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- length_rabi_pulse = 5.2e-08 s = 52 ns
- mod_depth = 1
- full_expt = 0

Physical model calculation

Using the supplied setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square pulse, the transition probability versus detuning is:

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

with Omega = 10 MHz, t = 52 ns, and Delta = f - f0 in Hz. On resonance:

P0 = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant pulse should produce an approximate fractional fluorescence drop of:

0.22 * 0.996 = 0.219

relative to the 0-state reference, before allowing for imperfect initialization/readout, drift, and finite linewidth.

Observed quantitative comparison

I used the normalized contrast y = 1 - readout2/readout1. The largest contiguous positive contrast feature is centered near 3.875-3.880 GHz:

- 3.870 GHz: 0.118
- 3.875 GHz: 0.163
- 3.880 GHz: 0.167
- 3.885 GHz: 0.132

The deepest absolute post-pulse drop is readout2 - readout1 = -6.96 counts at 3.880 GHz, from a reference near 41.69 counts, i.e. a 16.7% normalized drop. This is smaller than the ideal 21.9% but close enough for a real single-NV pODMR trace with only two stored averages and tracking-related average structure.

Fitting the square-pulse detuning model over f0 with fixed 22% contrast plus a constant offset gave best f0 = 3.8778 GHz and reduced SSE from 0.10356 for a flat baseline to 0.05234, a 49.5% improvement. Allowing the effective contrast amplitude to fit gave f0 = 3.8778 GHz, amplitude = 0.1806, baseline = 0.0079, and SSE = 0.04978, a 51.9% improvement.

Decision

The active sequence is a single post-polarization Rabi pulse followed by detection, and the expected resonant effect is a dip in readout 2 relative to readout 1. The observed contrast dip has the expected sign, magnitude, and detuning width for the 52 ns, mod_depth 1 pulse. I therefore decide that a pODMR resonance is present.
