Case: podmr_072_2026-05-17-085551

Input basis: I used the supplied sequence XML and the raw_export data only. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction flow is:

1. adj_polarize followed by detection: readout 1 is the polarized m_S = 0 fluorescence reference.
2. full_expt = 0, so the optional m_S = 1 reference block is skipped.
3. rabi_pulse_mod_wait_time followed by detection: readout 2 is the signal after the microwave pulse.

Sequence parameters used for the physical model:

- mod_depth = 1
- length_rabi_pulse = 52 ns, rounded at 250 MS/s remains 52 ns
- setup Rabi frequency at mod_depth = 1: about 10 MHz
- setup fluorescence contrast between m_S = 0 and m_S = +1: about 22%

Quantitative model:

For a resonant square Rabi pulse, the transferred population is

P(+1) = sin^2(pi * f_Rabi * t).

With f_Rabi = 10 MHz and t = 52 ns:

P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected signal readout ratio at resonance is therefore

readout2 / readout1 = 1 - 0.22 * 0.996 = 0.781.

The mean readout 1 level is 50.17 raw counts, so the expected resonant drop is

50.17 * 0.22 * 0.996 = 10.99 raw counts.

Including detuning with

P(+1, delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * sqrt(f_Rabi^2 + delta^2) * t),

the expected drop is still about 10.26 counts at 2.5 MHz detuning and 8.27 counts at 5 MHz detuning. Since the scan step is 5 MHz, a resonance within the scan range should produce a large local suppression in readout 2 relative to readout 1.

Observed data:

- mean(readout1) = 50.17
- mean(readout2) = 49.54
- mean(readout2 - readout1) = -0.63
- standard deviation of pointwise differences = 1.20
- largest observed suppression = -2.44 counts
- minimum observed readout2/readout1 ratio = 0.952

The observed suppression is far smaller than the modeled resonant response. The two stored averages show broad tracking-like offsets and fluctuations, so I do not treat them as a strong independent repeatability test. Based on the active sequence and quantitative expected signal, no pODMR resonance is present in this scan.
