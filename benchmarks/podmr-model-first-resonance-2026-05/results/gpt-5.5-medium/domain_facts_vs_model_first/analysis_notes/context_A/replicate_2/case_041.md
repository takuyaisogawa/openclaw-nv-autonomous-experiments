<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- The first detection occurs immediately after adj_polarize, so readout 1 is the true mS = 0 bright reference.
- full_expt is 0, so the optional mS = +1 reference block is skipped.
- The second detection occurs after rabi_pulse_mod_wait_time, so readout 2 is the signal after the microwave pulse.

Pulse settings used for the decision:
- mod_depth = 1 from the provided sequence and exported variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- With an estimated Rabi frequency of about 10 MHz at mod_depth = 1, a pi pulse is about 50 ns, so this pulse should strongly transfer population when on resonance.

Data interpretation:
The setup contrast scale between mS = 0 and mS = +1 is about 22%, so an on-resonance near-pi pulse should make readout 2 substantially lower than readout 1 at the resonance frequency. Instead, the combined readouts differ by only about 0.85 counts on a 54-count baseline on average, roughly 1.6%, with the deepest individual ratio drop around 6% and no stable localized dip. The per-average traces are jagged and the stored averages mostly reflect tracking cadence rather than strong independent repeatability. Several neighboring points alternate between readout 2 being below and above readout 1, which is more consistent with noise/tracking variation than a pODMR resonance.

Decision: resonance_absent.
