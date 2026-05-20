Sequence and readout interpretation

The provided sequence is Rabimodulated.xml. The active instruction path first performs optical polarization and detection, giving the true m_S = 0 reference readout. The conditional "Acquire 1 level reference" block is inactive because full_expt = 0, so no independent m_S = +1 reference is acquired. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. Therefore readout 1 is the m_S = 0 optical reference and readout 2 is the signal after the MW pulse.

Relevant active pulse parameters from the provided XML / exported variable values:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1.
- scan variable = mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so stored averages mainly show tracking/cadence behavior, not a strong repeatability test.

Quantitative model

Using the stated setup calibration, the resonant Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular resonant pulse, the transition probability is

P = sin^2(pi * f_R * t).

With f_R = 10 MHz and t = 52 ns:

pi * f_R * t = pi * 0.52 = 1.6336 rad
P = sin^2(1.6336) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a real on-resonance pODMR feature should reduce the MW readout relative to the m_S = 0 reference by

0.22 * 0.996 = 0.219, or about 21.9%.

The mean reference level is 46.76 raw counts, so the expected resonant signal drop is approximately

46.76 * 0.219 = 10.25 raw counts.

I also evaluated the detuned rectangular-pulse model

P(detuning) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz. If a resonance lay within the scanned range, this pulse should produce a broad negative readout2 - readout1 feature with peak scale near -10 counts, sampled by several 5 MHz scan points.

Data comparison

The combined readout difference readout2 - readout1 has:
- mean = +0.07 counts,
- standard deviation across scan points = 1.48 counts,
- minimum = -3.27 counts at 3.890 GHz,
- maximum = +2.21 counts.

There is no broad negative feature near the expected -10 count scale. The most negative point is isolated and only about one third of the expected resonant amplitude, with neighboring points returning near zero or positive. A least-squares scan of the rectangular-pulse line shape with resonance constrained inside the scan gives a fitted dip amplitude of only about 1.5 counts, far below the expected 10.25 counts and comparable to point-to-point scatter.

Decision

Given the active sequence, readout roles, mod_depth = 1, and 52 ns pulse, the expected resonant pODMR contrast is large enough that it should be obvious in readout2 relative to readout1. The measured data do not show that signature. I therefore decide that a pODMR resonance is absent.
