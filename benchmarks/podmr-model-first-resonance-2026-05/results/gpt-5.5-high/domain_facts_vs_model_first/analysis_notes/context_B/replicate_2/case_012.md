Case podmr_030_2026-05-13-160024

I used inputs/sequence.xml to identify the active sequence. The sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first performs adj_polarize followed by detection, so readout 1 is the true m_S = 0 fluorescence reference. Because full_expt = 0, the optional m_S = 1 reference block is inactive. The active pODMR measurement is then a rabi_pulse_mod_wait_time pulse followed by detection, so readout 2 is the microwave-pulsed signal readout. The active pulse has length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:
- Setup contrast scale between m_S = 0 and m_S = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: tau = 52 ns.
- On-resonance transfer probability for a square Rabi pulse:
  P_e(0) = sin^2(pi f_R tau)
         = sin^2(pi * 10e6 * 52e-9)
         = 0.996.
- Expected resonant signal/reference ratio:
  R_res = 1 - C * P_e(0)
        = 1 - 0.22 * 0.996
        = 0.781.

The measured mean readout 1 reference is 27.37 counts, so the expected on-resonance readout 2 level is about 27.37 * 0.781 = 21.37 counts, a dip of about 6.0 counts from the local reference. A detuned square-pulse model using
P_e(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi tau sqrt(f_R^2 + delta^2))
therefore expects a strong, localized dip in readout 2 relative to readout 1 at the resonance frequency.

Measured paired comparison:
- Mean readout 1: 27.37 counts.
- Mean readout 2: 27.73 counts.
- Mean readout 2/readout 1 ratio: 1.015, not a net decrease.
- Minimum readout 2/readout 1 ratio: 0.918 at 3.860 GHz, corresponding to only an 8.2% drop or 2.26 counts.
- The expected resonant ratio is 0.781, about a 21.9% drop or 6.0 counts.

I also compared the observed contrast values, 1 - readout2/readout1, to the fixed square-pulse response with known contrast 0.22 and f_R = 10 MHz while scanning the possible center frequency across the measured range. The best fixed known-model sum of squared residuals was 0.173, worse than a flat-baseline contrast model at 0.067. Allowing the model amplitude to float gave a best fitted contrast amplitude of only about 0.005, far below the expected 0.22. The stored two averages show substantial drift/tracking behavior, so I did not treat the average overlay as a strong repeatability test.

Decision: resonance_absent. The data do not contain the large, physically expected pulsed-ODMR fluorescence dip for the active 52 ns, mod_depth 1 sequence.
