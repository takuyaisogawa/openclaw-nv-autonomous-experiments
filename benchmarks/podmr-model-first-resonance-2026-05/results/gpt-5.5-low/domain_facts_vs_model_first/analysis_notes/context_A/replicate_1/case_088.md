Sequence review:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence XML sets mod_depth = 1 and length_rabi_pulse = 52 ns, rounded on a 250 MHz sample clock. With the stated setup calibration, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance.

Readout roles:

The instructions first polarize and detect before any microwave pulse, giving the true m_S = 0 bright reference. The full_expt flag is 0, so the separate m_S = +1 reference block is skipped. The sequence then applies the 52 ns modulated Rabi pulse and performs the second detection. Thus readout 1 is the bright reference and readout 2 is the microwave-pulse-affected signal.

Resonance assessment:

For a single NV with about 22% contrast between m_S = 0 and m_S = +1, an on-resonance pi pulse should create a substantial reduction of the second readout relative to the first, much larger than the point-to-point scatter. The combined traces do not show a clear localized post-pulse dip of that scale. The second readout is sometimes lower and sometimes higher than the reference, with variations of only a few raw-count units and no stable resonance-shaped feature. The per-average overlay also looks dominated by tracking/cadence drift rather than an independently repeated resonance.

Decision: resonance_absent.
