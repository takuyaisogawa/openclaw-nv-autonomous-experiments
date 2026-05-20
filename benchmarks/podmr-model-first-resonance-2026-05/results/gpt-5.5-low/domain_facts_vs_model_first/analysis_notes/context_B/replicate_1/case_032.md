Sequence and active readouts:

The active saved sequence is Rabimodulated.xml. In the instructions, the first detection occurs immediately after adj_polarize, so readout 1 is the polarized m_S = 0 fluorescence reference. The block labelled "Acquire 1 level reference" is guarded by full_expt, and full_expt = 0, so that extra reference is inactive. The second active detection occurs after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so readout 2 is the signal after the microwave pulse.

Relevant parameters from the sequence/export:

- varied parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- length_rabi_pulse: 52 ns
- mod_depth: 1
- full_expt: 0, so only the 0 reference and post-pulse readout are active

Quantitative expected signal model:

For a resonant square microwave pulse, transition probability can be modeled as

P_transfer = sin^2(pi * f_Rabi * t_pulse)

Using the provided calibration, f_Rabi = 10 MHz * mod_depth = 10 MHz. With t_pulse = 52 ns:

pi * f_Rabi * t_pulse = pi * 10e6 * 52e-9 = 0.52*pi
P_transfer = sin^2(0.52*pi) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant readout reduction is

expected fractional dip = 0.22 * 0.996 = 0.219, or 21.9%.

Data check:

Readout 2 has an off-resonance baseline of about 43.656 counts when excluding the central dip region. Its minimum is 34.173 counts at 3.875 GHz. The fractional dip is

(43.656 - 34.173) / 43.656 = 0.217, or 21.7%.

That is essentially the model expectation for a near-pi resonant pulse. The dip is also large compared with the noncentral scatter: using the same off-resonance points, sigma is about 1.016 counts, so the central dip depth is about 9.34 sigma. The readout-2/readout-1 ratio gives the same conclusion, with its minimum at 3.875 GHz and an approximately 23.6% fractional dip from off-resonance ratio baseline.

The two stored averages are not treated as a strong independent repeatability test because averages can reflect tracking cadence, but both averages show the central depression: at index 10, their readout-2 fractional dips are about 25.2% and 18.3% relative to their off-resonance baselines.

Decision:

A pODMR resonance is present. The observed dip is centered in the scan and quantitatively matches the expected contrast for the active 52 ns, mod_depth 1 Rabi-modulated pulse.
