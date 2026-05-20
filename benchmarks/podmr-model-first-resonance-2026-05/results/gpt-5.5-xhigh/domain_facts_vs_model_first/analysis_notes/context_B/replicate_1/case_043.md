Case podmr_029_2026-05-16-193002 analysis note

Active sequence and readout roles

The provided XML is the Rabimodulated pulse sequence with mw_freq swept from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active exported variable values
give length_rabi_pulse = 52 ns, sample_rate = 250 MHz, and mod_depth = 1.
Rounding the pulse length to the AWG sample grid gives round(52 ns * 250 MHz)
= 13 samples, so the active pulse remains 52 ns.

The instruction block first polarizes and detects before any microwave pulse:
that first detection is the true m_S = 0 reference, corresponding to readout 1.
The optional 1-level reference block is skipped because full_expt = 0, even
though do_adiabatic_inversion is true. After that, the sequence applies
rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth,
switch_delay, ch_on), then detects again. That second detection is the active
pODMR signal readout, corresponding to readout 2.

Physical model calculation

Using the given setup facts, the Rabi frequency at mod_depth = 1 is about
f_R = 10 MHz. I modeled the microwave step as a rectangular two-level pulse:

P_1(delta) = Omega^2 / (Omega^2 + Delta^2) *
             sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2*pi*10 MHz and t = 52 ns. On resonance,
P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated 22 percent
m_S = 0 to m_S = +1 readout contrast, a resonance should therefore make
readout 2 approximately 1 - 0.22 * 0.996 = 0.781 times readout 1. At the
observed reference level of about 45 counts, this is an expected drop of about
9.9 counts. Because the scan step is 5 MHz, any resonance inside the scan
window is at most 2.5 MHz from one sampled point; the same model gives
P_1(2.5 MHz) = 0.929, still an expected drop of about 9.2 counts. Even at
5 MHz detuning the expected drop is about 7.4 counts.

Observed data check

The combined readout 1 mean is 44.93 counts and the combined readout 2 mean is
44.91 counts. The pointwise readout2 - readout1 difference has mean -0.02
counts, standard deviation 1.27 counts, minimum -2.56 counts, and maximum
+3.23 counts. The active/reference ratio has mean 0.9999 and minimum 0.944.
The observed minimum ratio corresponds to only a 5.6 percent drop, far smaller
than the about 20 to 22 percent drop expected for an in-window resonance sampled
by this scan.

I also fit the observed readout2/readout1 ratio to the calculated pulse
line-shape plus a linear baseline. The best free-amplitude fit prefers a
positive line-shape amplitude (+0.138 in ratio units), while the physical
pODMR signal should have a negative amplitude of about -0.22. Forcing the
expected -0.22 amplitude gives a worse residual than a baseline-only fit.
The stored two averages are not used as a strong independent repeatability
test, since they can reflect tracking cadence, but neither average contains
an approximately 22 percent active-readout dip.

Decision

The active pulse should produce a large negative readout-2 contrast if a
pODMR resonance is present in the scan window. The measured signal stays near
unity relative to the 0-level reference and lacks the model-predicted dip.
I therefore decide that a pODMR resonance is absent.
