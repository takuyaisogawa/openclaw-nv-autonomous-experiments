Case: podmr_044_2026-05-16-232730

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual check of the same raw readouts

Active sequence and readout roles:
- SequenceName in the export is Rabimodulated.xml.
- The provided sequence XML enables channels [1 1 1 0 0 0], sets the microwave, polarizes, then detects once before the microwave pulse. This is the true m_S = 0 reference readout.
- full_expt = 0, so the "Acquire 1 level reference" branch is inactive and no independent m_S = +1 reference is acquired.
- The active measurement pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second detection is the pODMR readout after the microwave pulse.
- The provided sequence XML has length_rabi_pulse = 5.2e-08 s, sample_rate = 250 MHz, mod_depth = 1, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The 52 ns pulse is already exactly on the 4 ns sample grid.

Quantitative physical model:
- Given setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so f_R = 10 MHz here.
- For a rectangular pulse, the transferred population at detuning Delta is modeled as:
  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau)
  with tau = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected fluorescence drop is 0.22 * 0.996 = 21.9%.
- The mean reference readout is 48.56 counts, so the expected on-resonance count drop is about 48.56 * 0.219 = 10.6 counts.
- At detunings of 2.5, 5, and 10 MHz, the expected drops are still about 20.4%, 16.5%, and 6.0%, respectively. With 5 MHz scan spacing, a real resonance should therefore produce at least one large negative point and usually a multi-point dip.

Measured data check:
- Mean readout 1: 48.56 counts.
- Mean readout 2: 48.69 counts.
- Mean readout2 - readout1: +0.13 counts.
- Standard deviation of readout2 - readout1 across the sweep: 1.09 counts.
- Most negative readout2 - readout1 point: -2.42 counts at 3.865 GHz, which is -4.8% relative to readout 1.
- The best nonnegative dip fit using the above Rabi lineshape has an amplitude of about 2.1 counts, far below the expected 10.6 counts for mod_depth = 1, and the surrounding points do not show the expected large Rabi lineshape.

Decision:
Under the active Rabimodulated pulse sequence in the provided XML, a resonance should create an approximately 22% pulsed-readout drop. The observed differential readout has only percent-level fluctuations and no large, coherent dip. I therefore classify this case as resonance_absent.
