<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_079

Sequence and roles

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The saved sequence/instructions show full_expt = 0, so the optional "1 level reference" block is inactive. The two acquired readouts are therefore:

- readout 1: immediately after optical polarization/detection, a bright m_S = 0 reference.
- readout 2: after one rabi_pulse_mod_wait_time pulse followed by detection, the actual pODMR signal channel.

The relevant pulse settings from the active run are mod_depth = 1 and length_rabi_pulse = 52 ns. The setup fact gives a Rabi frequency of about 10 MHz at mod_depth = 1, approximately linear with mod_depth, so this pulse is close to a pi pulse on resonance.

Quantitative expected-signal model

Use a two-level resonant Rabi model for the MW pulse. On resonance, the transfer probability from m_S = 0 to m_S = +1 is

P_transfer = sin^2(pi * f_R * tau)

with f_R = 10 MHz * mod_depth = 10 MHz and tau = 52 ns. This gives

pi * f_R * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P_transfer = sin^2(1.6336) = 0.996

The current setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance readout-2 dip relative to the bright readout should be approximately

fractional dip = 0.22 * 0.996 = 0.219

The measured readout-1 mean is 47.48 raw counts, so the expected resonant depletion is about

47.48 * 0.219 = 10.4 raw counts

Thus a real resonance in this scan should produce an obvious localized reduction of readout 2 versus readout 1, with readout 2 near roughly 37 counts at the resonant point if the bright reference is around 47.5 counts, before allowing for modest drift/noise.

Observed data

Combined readout statistics:

- readout 1 mean 47.48, standard deviation 1.26, range 45.46 to 49.90
- readout 2 mean 47.21, standard deviation 1.50, range 44.33 to 50.08
- readout2 - readout1 mean -0.27, standard deviation 1.23, range -2.27 to +2.00
- readout2/readout1 mean 0.994, range 0.952 to 1.043

The largest readout-2 deficit relative to readout 1 is 2.27 counts at 3.830 GHz, only about 4.8% of the bright level and about 22% of the expected 10.4-count resonant dip. Several points have readout 2 above readout 1. Around the nominal high-frequency part of the scan there is no sharp 22% depletion; the curves largely track each other with slow drift and small point-to-point noise.

Decision

Given the active physical model, this pulse should create a near-maximum pODMR contrast if it hits resonance. The expected signal is large compared with the observed differences, and the observed data do not show a localized depletion of the signal readout. Stored averages are not treated as independent repeatability evidence because they can reflect tracking cadence. I therefore classify this case as resonance_absent.
