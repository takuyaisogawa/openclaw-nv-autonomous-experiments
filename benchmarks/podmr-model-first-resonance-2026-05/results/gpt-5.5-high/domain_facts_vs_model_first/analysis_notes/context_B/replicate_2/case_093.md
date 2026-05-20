Case podmr_079_2026-05-17-103702

I used only the supplied sequence XML and raw export in this workspace.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active pulse sequence first polarizes the NV, then performs detection immediately. This is the true m_S = 0 fluorescence reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. There is no active independent m_S = +1 reference readout in this run.
- The active microwave operation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so the second readout is the post-Rabi-pulse signal.
- The supplied sequence settings give length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Given the provided setup fact, f_Rabi = 10 MHz at mod_depth = 1.
- The pulse duration is t = 52 ns.
- For a square resonant pulse, the transfer probability is P = sin^2(pi f_Rabi t).
- P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance post-pulse readout should be lower than the m_S = 0 reference by C * P = 0.22 * 0.996 = 0.219, about a 21.9% drop.
- The observed mean m_S = 0 reference readout is 50.718, so the expected on-resonance count drop is about 11.11 raw-readout units, giving an expected post-pulse/readout-reference ratio near 0.781 at resonance.

Frequency-grid check:
- With the same Rabi model including detuning, P(detuning) = (Omega^2/(Omega^2 + Delta^2)) * sin^2(pi t sqrt(Omega^2 + Delta^2)).
- At 0 MHz detuning the expected fractional drop is 0.219.
- At 2.5 MHz detuning, which is the worst case for a resonance halfway between 5 MHz-spaced scan points, the expected fractional drop is still 0.204.
- At 5 MHz detuning the expected fractional drop is 0.165.
- Therefore a resonance lying inside the scanned band should produce a broad, strong dip in the second readout relative to the first, not just a single-point weak fluctuation.

Data comparison:
- Combined readout 1 mean: 50.718.
- Combined readout 2 mean: 50.782.
- The readout2/readout1 ratio has mean 1.0017, minimum 0.9607, and maximum 1.0476.
- The largest observed negative difference readout2 - readout1 is -2.096 raw-readout units, far smaller than the roughly -11.11 units expected for an in-scan resonance.
- The two stored averages have different absolute levels, consistent with tracking or drift cadence, but neither shows a stable 20% class post-pulse dip.

Decision:
The active sequence would produce an easily visible pODMR dip if the scanned microwave frequency crossed the addressed NV transition. The observed readout ratio stays near unity and never approaches the modeled resonant contrast. I therefore decide that a pODMR resonance is absent in this scan.
