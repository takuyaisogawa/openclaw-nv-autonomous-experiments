Active sequence and roles

The provided sequence XML is Rabimodulated.xml. The active variables are:

- length_rabi_pulse = 5.2e-08 s, rounded at 250 MHz sample rate to 52 ns.
- mod_depth = 1.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.

Therefore the two active detections are:

1. Readout 1: after optical polarization only, the bright m_S = 0 reference.
2. Readout 2: after the modulated microwave Rabi pulse, the pODMR signal readout.

Physical model calculation

Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the resonant Rabi frequency here is 10 MHz. For a square resonant pulse, the transferred population is

P = sin^2(pi * f_Rabi * tau).

With tau = 52 ns and f_Rabi = 10 MHz:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%. The observed readout 1 mean is 37.23 counts, so the expected resonant signal loss is approximately:

0.22 * 37.23 * 0.996 = 8.16 counts.

Using the detuned square-pulse model,

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau),

with Omega = 2*pi*10 MHz, the expected profile is a localized dip centered at resonance with strongest response over only a few 5 MHz scan points. This is the relevant model because the active sequence applies a fixed-length microwave pulse and sweeps mw_freq.

Data comparison

The minimum of readout 2 is 26.96 counts at 3.880 GHz. At that same scan point, readout 1 is 38.12 counts, giving a direct readout difference of 11.15 counts. Estimating the off-resonant differential baseline from points more than two scan steps away from the minimum gives 1.04 counts with a standard deviation of 1.76 counts. The excess dip is therefore 10.11 counts, about 5.8 standard deviations by this rough comparison.

The expected resonant loss from the model is about 8.2 counts, and the observed localized loss is about 10.1 counts relative to the off-resonant readout difference. This is compatible with a pODMR resonance. The per-average traces both show the same central suppression in readout 2, but I do not treat the two stored averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision: resonance_present.
