Case podmr_048_2026-05-17-002650 analysis

Sequence identification:
- The saved scan sequence is Rabimodulated.xml.
- The active pulse sequence first polarizes, then performs a detection of the initialized m_S = 0 state. This is readout 1, the true 0-level reference.
- The optional m_S = +1 reference block is inside `if abs(full_expt)>1e-12`; `full_expt` is 0, so this block is inactive. There is no active independent 1-level reference.
- The active pODMR measurement pulse is `rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on)`, followed by detection. This is readout 2, the signal readout after the microwave pulse.
- `length_rabi_pulse` is 52 ns, rounded at 250 MHz sample rate to 52 ns.
- `mod_depth` is 1.

Expected-signal calculation:
- Given setup contrast between m_S = 0 and m_S = +1: about 22%.
- Given Rabi frequency: about 10 MHz at mod_depth = 1, scaling linearly with mod_depth.
- Therefore f_R = 10 MHz for this sequence.
- For a resonant rectangular Rabi pulse, the transferred population is
  P = sin^2(pi * f_R * t).
- With f_R = 10e6 Hz and t = 52e-9 s:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fluorescence contrast in the signal readout at resonance:
  0.22 * 0.996 = 0.219, or about 21.9%.
- The measured readout 2 mean is about 49.79 counts, so the expected resonant dip is
  49.79 * 0.219 = 10.91 counts.

Observed data check:
- Readout 1 is the m_S = 0 reference and should not be used as the pODMR signal.
- Readout 2 ranges from 48.17 to 52.04 counts, a full excursion of only 3.87 counts.
- The lowest readout 2 point is at 3.895 GHz, not at a distinct endpoint/center resonance feature, and it is only about 1.62 counts below the readout 2 mean.
- At 3.925 GHz, the final scanned point, readout 2 is 50.98 counts, above its mean rather than showing the roughly 11-count loss expected for an on-resonance pi-like pulse.
- Stored averages are only two and may reflect tracking cadence, so they do not provide a strong independent repeatability test.

Decision:
The active signal readout does not show a dip remotely close to the quantitatively expected 21.9% resonance response. The small fluctuations are inconsistent in location and magnitude with the physical model for this pulse. I therefore classify this case as resonance_absent.
