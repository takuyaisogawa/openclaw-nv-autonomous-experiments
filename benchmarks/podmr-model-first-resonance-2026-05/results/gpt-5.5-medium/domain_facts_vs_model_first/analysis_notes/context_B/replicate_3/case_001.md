Case: podmr_004_2026-05-10-171142

Sequence and readout roles

The provided sequence is Rabimodulated.xml / Rabimodulated. It scans mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize the
NV and immediately detect, then wait, then apply a modulated Rabi microwave pulse,
then detect again. Because full_expt = 0, the optional "Acquire 1 level reference"
block is inactive. Therefore readout 1 is the bright m_S = 0 reference after
polarization, and readout 2 is the post-microwave pODMR signal. It is not a
separate dark-state reference.

The standalone sequence.xml values are:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s; 52 ns is already on the 4 ns grid.
- mod_depth = 1.
- microwave pulse call: rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...).

The raw export also contains an embedded saved sequence string with mod_depth =
0.3, while the exported Variable_values list and the standalone sequence.xml say
mod_depth = 1. Since the instruction is to use the provided sequence XML, I use
mod_depth = 1 for the primary physical model, and I also check the weaker 0.3 case
as a sensitivity check.

Physical model calculation

For resonant Rabi driving, the population transferred from m_S = 0 to m_S = +1 is

    P_+1 = sin^2(pi * f_R * tau)

where f_R is the Rabi frequency in cycles/s and tau is the pulse length. The setup
facts give f_R approximately 10 MHz at mod_depth = 1, scaling linearly with
mod_depth. The readout contrast between m_S = 0 and m_S = +1 is about 22%, so the
expected fractional fluorescence drop in readout 2 on resonance is

    drop_fraction = 0.22 * P_+1.

For the provided XML:

    f_R = 10 MHz
    tau = 52 ns
    P_+1 = sin^2(pi * 10e6 * 52e-9) = 0.996
    expected drop_fraction = 0.219

At the observed count level near 44 counts, this is an expected on-resonance drop
of about 9.6 counts in the post-pulse readout relative to the bright reference.

For the embedded-sequence sensitivity case with mod_depth = 0.3:

    f_R = 3 MHz
    P_+1 = sin^2(pi * 3e6 * 52e-9) = 0.222
    expected drop_fraction = 0.0487

That would still be about a 2.1 count post-pulse dip at a 44 count baseline.

Observed data

The combined readouts have:

- readout 1 mean = 43.68 counts, standard deviation over scan points = 0.85 counts.
- readout 2 mean = 44.25 counts, standard deviation over scan points = 1.62 counts.
- readout2 - readout1 mean = +0.57 counts.
- readout2/readout1 mean = 1.013.
- readout2/readout1 minimum = 0.943, maximum = 1.092.

Thus the post-pulse readout is, on average, slightly higher than the bright
reference, not lower. The largest local negative differences are about -2.46 counts
near 3.855 GHz and -2.31 counts near 3.830 GHz, far smaller than the 9.6 count dip
expected from the provided XML model and not organized as a clear resonance line.

I also fitted a simple frequency-domain Rabi response

    ratio(f) = offset - A * [f_R^2/(f_R^2 + detuning^2)]
               * sin^2(pi * sqrt(f_R^2 + detuning^2) * tau)

using the measured readout2/readout1 ratio and allowing the resonance center and
offset to vary. A physical pODMR dip requires A > 0 and should be around 0.22 for
mod_depth = 1. The best least-squares fit for mod_depth = 1 instead gives
A = -0.061, i.e. a weak brightening feature rather than a dip. Repeating the fit
for the embedded 0.3 sensitivity case also gives the opposite sign, A = -0.237.

Decision

The relevant model predicts a sizable post-pulse fluorescence dip for the provided
52 ns, mod_depth = 1 pulse. The measured readout 2 does not show that dip; it is
mostly equal to or above the reference, and the best quantitative response fit has
the wrong sign. The stored two averages are not treated as a strong independent
repeatability test because they can reflect tracking cadence. Based on the active
sequence, readout roles, and quantitative expected-signal calculation, I decide
that a pODMR resonance is absent.
