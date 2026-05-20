Case podmr_071_2026-05-17-084118

Inputs used
- Used only inputs/sequence.xml and inputs/raw_export.json numeric readouts.
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed instructions polarize, detect the true m_S=0 level, wait, then because full_expt = 0 skip the optional m_S=1 reference block, apply one rabi_pulse_mod_wait_time pulse, and detect again.
- Readout roles from the sequence are therefore: first detection is the m_S=0 optical reference; second detection is the post-microwave signal after the Rabi pulse. The two exported raw readout traces are both raw photon readouts from this acquisition path, not a full independent 0/1 reference pair because the m_S=1 reference block is disabled.
- Pulse duration: length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.
- mod_depth in the provided sequence XML: 1.

Physical model calculation
- Given setup contrast C = 0.22 between m_S=0 and m_S=+1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, with linear scaling in mod_depth.
- For a square resonant pulse, transferred population is p = sin^2(pi f_R t), where f_R is in cycles/s.
- With f_R = 10 MHz and t = 52 ns, f_R t = 0.52 cycles and p = sin^2(pi * 0.52) = 0.996.
- Expected resonant PL contrast is C * p = 0.22 * 0.996 = 0.219, i.e. about a 21.9% drop from the off-resonant m_S=0 brightness.
- Around the observed 50-count level, that corresponds to an expected dip of about 10.96 counts in the post-microwave readout. Even if the embedded export text value mod_depth = 0.3 were used instead of the provided XML value, the model gives p = sin^2(pi * 3 MHz * 52 ns) = 0.222 and an expected drop of about 4.87%, or about 2.44 counts.

Quantitative comparison to data
- Combined raw readouts:
  - readout 1 ranges from 44.77 to 51.56 counts and has a positive linear trend of about 3.97 counts per 100 MHz.
  - readout 2 ranges from 45.37 to 51.88 counts and has a positive linear trend of about 3.22 counts per 100 MHz.
  - the mean of the two readouts has a positive linear trend of about 3.59 counts per 100 MHz.
- After subtracting a linear baseline from the mean trace, residual standard deviation is about 1.04 counts. The most negative mean residual is -2.59 counts at the lowest scan point, where the whole scan begins low rather than showing a localized resonance. Away from that edge, the residuals are within roughly +/-1.6 counts.
- The expected mod_depth = 1 resonant depletion, about 11 counts, is far larger than the residual scatter and is not present. The data instead rises with scan value and lacks a localized dip or dispersive resonance-sized feature.
- Stored averages differ mainly by slow tracking/brightness drift and do not provide a strong independent repeatability test, so the decision is based on the active sequence and combined raw readout scale.

Decision
- A pODMR resonance is absent. The measured variation is consistent with slow baseline drift and small scatter, not the large resonant PL depletion predicted for the active 52 ns, mod_depth = 1 Rabi pulse.
