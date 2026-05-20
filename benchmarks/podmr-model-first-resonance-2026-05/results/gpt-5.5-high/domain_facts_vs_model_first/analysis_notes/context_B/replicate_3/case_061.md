Case podmr_047_2026-05-17-001223

Input use and active sequence:
- SequenceName in the export is Rabimodulated.xml and the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The standalone sequence XML and exported active variable table give length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, and delay_wrt_1mus = 0.2 us.
- Since full_expt = 0, the "Acquire 1 level reference" branch is inactive. The two acquired readouts are therefore:
  1. detection immediately after adj_polarize: true m_S = 0 reference,
  2. detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth): pODMR signal readout.

Quantitative physical model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and tau = 52 ns, the rectangular-pulse transition probability versus detuning is
  P(df) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),
  where Omega = 2*pi*10 MHz and Delta = 2*pi*df.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup m_S = 0 to m_S = +1 contrast scale of 22%, the expected normalized final readout at resonance is approximately 1 - 0.22 * 0.996 = 0.781 of the 0-reference.
- The raw reference level is about 50 counts, so an on-resonance pi-pulse pODMR feature should be a drop of about 0.219 * 50 = 11 counts in the final readout relative to the 0-reference.
- The same model predicts normalized final/reference values of about 0.835 at 5 MHz detuning, 0.940 at 10 MHz detuning, and near baseline beyond roughly 15 MHz aside from weak pulse sidelobes.

Data comparison:
- The combined final/reference ratios across the scan have mean 0.994, standard deviation 0.028, minimum 0.947 at 3.905 GHz, and maximum 1.051 at 3.925 GHz.
- The largest measured final-readout suppression relative to the reference is about 2.73 counts, far smaller than the approximately 11 count resonant drop expected for the active 52 ns, mod_depth 1 pulse.
- A least-squares fit of the measured normalized ratio to a constant-plus-linear baseline gives RSS 0.01545. Forcing the expected 22% contrast Rabi lineshape and scanning the center frequency gives best RSS 0.03546, worse than the baseline-only model.
- Allowing the resonance amplitude to float gives a much smaller best amplitude, about 6.5%, which is inconsistent with the expected near-pi pulse signal from the active sequence and is comparable to baseline/tracking variation in these two stored averages.

Decision:
The relevant physical model predicts a broad, large pODMR dip that is not present in the final readout relative to the 0-reference. The observed few-percent fluctuations and weak trend are not quantitatively compatible with the active pulse sequence expectation, so I classify this case as resonance_absent.
