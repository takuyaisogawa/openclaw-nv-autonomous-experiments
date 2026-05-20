Case: podmr_010_2026-05-16-114624

Sequence and readout roles

The provided XML is Rabimodulated.xml. The active instructions first perform polarization and detection before the microwave pulse:

- adj_polarize(...)
- detection(...)
- wait_for_awg(...)

This first recorded readout is therefore the bright m_S = 0 reference. The block labelled "Acquire 1 level reference" is inside `if abs(full_expt)>1e-12`, but `full_expt = 0`, so that block is inactive and no independent m_S = 1 reference is acquired. The active signal readout is then acquired after:

- rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)
- detection(...)

Thus readout 1 is the m_S = 0 reference and readout 2 is the post-microwave-pulse pODMR signal.

Sequence parameters used for the model

- scan variable: mw_freq
- scan range: 3.825 GHz to 3.925 GHz in 5 MHz steps
- length_rabi_pulse = 5.2e-08 s
- sample_rate = 250 MHz, so the rounded pulse duration remains 52 ns
- mod_depth = 1
- setup Rabi frequency at mod_depth = 1: about 10 MHz
- setup contrast between m_S = 0 and m_S = +1: about 22%

Quantitative physical model

I used the driven two-level Rabi response for transition probability during a square pulse:

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * T * sqrt(f_R^2 + delta^2))

where f_R = 10 MHz, T = 52 ns, and delta is detuning in Hz. The expected normalized optical readout after the pulse is:

R(delta) = S * (1 - C * P1(delta))

with C = 0.22 and S a scale factor for the readout2/readout1 ratio.

On resonance:

- f_R * T = 0.52 cycles
- P1(0) = sin^2(pi * 0.52) = 0.9961
- expected readout drop = 0.22 * 0.9961 = 21.9%

The expected response is broad enough to affect neighboring 5 MHz scan points:

- detuning 0 MHz: P1 = 0.996, drop = 21.9%
- detuning 5 MHz: P1 = 0.749, drop = 16.5%
- detuning 10 MHz: P1 = 0.273, drop = 6.0%
- detuning 15 MHz: P1 = 0.0117, drop = 0.26%

Data comparison

Using the combined readouts, readout2/readout1 is:

- minimum ratio: 0.7626 at 3.875 GHz
- adjacent ratios: 0.8236 at 3.870 GHz and 0.8430 at 3.880 GHz
- off-resonant ratios are mostly near 0.96 to 1.02

Fitting the model above to the readout2/readout1 ratio while allowing only resonance frequency and a scale factor gives:

- best center frequency: 3.8753 GHz
- scale factor: 0.9939
- residual sum of squares: 0.0146
- flat-ratio residual sum of squares: 0.0914
- variance improvement versus flat ratio: about 84%

Stored averages are not treated as a strong repeatability test because they can reflect tracking cadence, but both stored averages have their minimum ratio at 3.875 GHz:

- average 1 minimum ratio: 0.7268 at 3.875 GHz
- average 2 minimum ratio: 0.7880 at 3.875 GHz

Decision

The active sequence applies a near-pi Rabi pulse at mod_depth = 1, for which the expected pODMR resonance is a roughly 22% dip in the post-pulse readout relative to the m_S = 0 reference. The measured normalized signal shows a localized dip of the correct magnitude and width centered at about 3.875 GHz, matching the explicit Rabi model. I therefore decide that a pODMR resonance is present.
