Case: podmr_055_2026-05-17-045046

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence name in the data is Rabimodulated.xml.
- The provided XML executes adj_polarize, detection, wait, then a rabi_pulse_mod_wait_time pulse, then detection.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive. do_adiabatic_inversion is defined true but is not reached in the active branch.
- readout 1 is therefore the bright m_S = 0 reference immediately after optical polarization.
- readout 2 is the signal after the microwave Rabi-modulated pulse.
- mod_depth = 1 from the provided XML/variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding leaves 52 ns exactly because 52 ns is 13 samples.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling, use f_R = 10 MHz.
- For a square pulse, the transition probability at detuning Delta is
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau),
  with tau = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the setup contrast scale of 22%, the expected fractional fluorescence dip in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, so r2/r1 should be about 0.781 at resonance.
- The mean readout 1 level is 43.81, so the expected raw drop at resonance is about 9.60 readout units.
- At 5 MHz detuning the same model still predicts a fractional dip of about 16.5%; at 10 MHz detuning it predicts about 6.0%, so a real resonance should create a clear multi-point dip on this 5 MHz grid.

Observed data check:
- Combined readout 1 mean = 43.81, readout 2 mean = 43.45.
- The normalized ratio r2/r1 has mean 0.992, standard deviation 0.036, minimum 0.941.
- Thus the largest observed combined fractional drop is only about 5.9%, or about 2.6 raw units, far below the expected 21.9% / 9.6-unit on-resonance signal.
- The dips are not centered in a way that follows the expected square-pulse detuning response. A grid fit of the expected lineshape with free resonance frequency inside the scan and fixed 22% contrast gives worse residuals than a no-resonance baseline; allowing the amplitude to float gives only about 3.6% fitted contrast, far below the physical expectation for this pulse.
- The two stored averages show different largest dips, consistent with tracking/cadence drift rather than repeatable resonance structure.

Decision: resonance_absent. The active 52 ns, mod_depth 1 pulse should be essentially a pi pulse on resonance, producing a large dark signal in readout 2 relative to the m_S = 0 reference, and that signal is not present in the data.
