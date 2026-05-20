Case podmr_023_2026-05-16-174219

I used only the provided sequence XML and raw export data in this isolated workspace.

Sequence identification:
- SequenceName in the raw export is Rabimodulated.xml.
- The active instruction path has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The executed readouts are therefore:
  - readout 1: post-polarization/detection true m_S = 0 reference.
  - readout 2: detection after one rabi_pulse_mod_wait_time pulse.
- The relevant pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is already on a 4 ns sample grid.
- The variable values list gives mod_depth = 1. The provided sequence file also has mod_depth = 1, while the embedded Sequence text contains an older-looking mod_depth default of 0.3. I use the explicit provided XML and Variable_values for the active run.

Physical model calculation:
- Setup contrast scale between m_S = 0 and m_S = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: tau = 52 ns.
- On-resonance transition probability for a square pulse:
  P = sin^2(pi * f_R * tau)
    = sin^2(pi * 10e6 * 52e-9)
    = 0.996.
- Expected on-resonance relative readout change:
  Delta S / S0 = -C * P = -0.219.
- At the observed baseline near 48 raw counts, the expected resonant readout 2 value would be about:
  48 * (1 - 0.219) = 37.5 counts,
  a drop of about 10.5 counts relative to readout 1.

Observed data check:
- readout 1 mean = 47.551.
- readout 2 mean = 47.690.
- Mean relative difference (readout2 - readout1) / readout1 = +0.0034.
- Most negative relative difference is -0.0506 at 3.835 GHz.
- Largest absolute negative difference is -2.48 counts, far smaller than the approximately -10.5 count drop expected from the active pi-pulse model.
- Several scan points have readout 2 above readout 1 by comparable or larger amounts, including +6.78% at 3.875 GHz.
- The two stored averages separate mostly as slow baseline/tracking changes, and the prompt notes these averages often reflect tracking cadence rather than independent repeatability.

Decision:
The active pulse sequence should produce a large, direct readout-2 suppression at resonance. The observed scan has only small, sign-changing readout differences and no feature near the expected 22% contrast scale. I therefore classify this case as resonance_absent.
