Case: podmr_065_2026-05-17-071421

Sequence interpretation

The active sequence is Rabimodulated.xml / Rabimodulated: optical polarization, detection, wait, then a single modulated Rabi pulse followed by detection. The optional mS=+1 reference block is inactive because full_expt = 0, so the two stored raw readouts are:

- readout 1: the initial no-microwave / mS=0 fluorescence reference after polarization.
- readout 2: fluorescence after the Rabi pulse.

The relevant pulse parameters from the provided XML/exported active variables are:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s, so still 52 ns.
- mod_depth = 1.
- mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation

For a square Rabi pulse, the driven population transfer versus detuning is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),

with Omega in cycles/s. The provided setup facts give Omega = 10 MHz at mod_depth = 1. With t = 52 ns,

Omega * t = 10e6 * 52e-9 = 0.52 cycles
P(0) = sin^2(pi * 0.52) = 0.996.

The stated contrast scale between mS=0 and mS=+1 is about 22%, so an on-resonance pi-like pulse should reduce the post-pulse readout by

0.22 * 0.996 = 0.219,

i.e. readout2/readout1 should be near 0.781 at resonance, before allowing for modest baseline drift. This would be a large, localized dip over the pulse bandwidth.

Observed data check

Normalizing the microwave readout by the no-microwave reference gives readout2/readout1 values with:

- minimum ratio = 0.9523, a 4.77% dip, at 3.830 GHz;
- another local dip near 3.890 to 3.895 GHz of about 3.4% to 4.3%;
- mean ratio = 0.9945 and standard deviation = 0.0259.

The largest observed dip is roughly 5 times smaller than the 21.9% expected on resonance for the active mod_depth = 1, 52 ns pulse. A detuned square-pulse fit with the physically expected 22% contrast gives substantially worse residuals than a simple drifting baseline, because it predicts readout2/readout1 around 0.87 to 0.88 near the best edge candidate while the observations remain around 0.95 to 0.96. Allowing the dip amplitude to float only finds small apparent dips of about 2% to 6%, comparable to baseline/tracking variation and much below the expected pi-pulse response.

Decision

The data do not show the expected pODMR resonance for this sequence and pulse strength. The small ratio fluctuations are not consistent with the required physical signal size, and the stored averages are not a strong independent repeatability test because they can reflect tracking cadence.
