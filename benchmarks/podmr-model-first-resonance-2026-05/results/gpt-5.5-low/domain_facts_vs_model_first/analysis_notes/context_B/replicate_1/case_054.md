Case: podmr_040_2026-05-16-222642

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided XML has full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active measurement is: polarize, detect the true m_S = 0 reference, wait, apply a modulated Rabi pulse, detect the post-pulse signal, wait.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-Rabi-pulse signal. A pODMR resonance should appear as readout 2 dropping below readout 1 at the resonant frequency.
- The active pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the pulse length rounds to 52 ns exactly.

Quantitative model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant rotation angle for a 52 ns pulse is theta = 2*pi*f_R*t = 2*pi*10e6*52e-9 = 3.267 rad.
- The resonant population transferred to m_S = +1 is P = sin^2(theta/2) = sin^2(1.6336) = 0.996.
- The stated setup contrast between m_S = 0 and m_S = +1 is about 22%.
- The measured readout-1 baseline is mean(readout1) = 47.188 raw-count units.
- Expected on-resonance fluorescence drop in readout 2 relative to readout 1 is 0.22 * 47.188 * 0.996 = 10.34 raw-count units.
- Equivalently, a resonant point should have readout2 - readout1 near -10.3 counts, up to tracking/noise and line-shape effects. Off resonance the detuned Rabi response follows P(Delta) = Omega^2/(Omega^2 + Delta^2) * sin^2(pi*t*sqrt(Omega^2 + Delta^2)), so the strong negative feature should be localized on the scale of the Rabi/spectral width rather than a small global offset.

Observed data:
- Mean readout1 = 47.188, mean readout2 = 46.660, so mean(readout2 - readout1) = -0.527 counts.
- The most negative readout2 - readout1 point is -3.692 counts at 3.885 GHz.
- The point-to-point standard deviation of readout2 - readout1 is 1.345 counts.
- The stored averages show large tracking-scale offsets between averages, so they are not a strong independent repeatability test; still, the combined data do not show the approximately 10-count resonant drop expected from a near-pi pulse.

Decision:
The measured readout difference is far smaller than the explicit resonant Rabi/contrast model predicts and lacks a convincing localized pODMR dip. I classify this case as resonance_absent.
