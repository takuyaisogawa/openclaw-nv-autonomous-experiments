Case: podmr_006_2026-05-16-011837

Input restrictions followed: I used only inputs/raw_export.json, inputs/raw_readouts.png as a visual check, and inputs/sequence.xml / the stored sequence text in the raw export. I did not use labels, previous outputs, sibling cases, or external context.

Active sequence and readout roles:

The saved scan reports SequenceName = Rabimodulated.xml and vary_prop = mw_freq, scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence is the Rabimodulated pODMR sequence. It first runs adj_polarize followed by detection, then wait_for_awg. This is the "true 0 level reference" readout, so readout 1 is the m_S = 0 optical reference without the scanned microwave pulse. The block labelled "Acquire 1 level reference" is guarded by if abs(full_expt)>1e-12; full_expt is 0, so that block is inactive. The active experiment pulse is then:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

followed by detection. Therefore readout 2 is the pODMR readout after the scanned microwave Rabi pulse.

Sequence parameters used for the model:

- length_rabi_pulse = 52 ns
- mod_depth = 1
- sample_rate = 250 MHz, which leaves 52 ns exactly on the 4 ns sample grid
- mw_freq is scanned; detuning variable is 0
- full_expt = 0, so no active m_S = +1 reference readout is present

Physical model calculation:

The supplied setup facts say the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Thus f_Rabi = 10 MHz for this scan. For a resonantly driven two-level transition with rectangular pulse duration t, the transferred population is

P_res = sin^2(pi * f_Rabi * t).

Using t = 52 ns:

P_res = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.

The current setup contrast scale between m_S = 0 and m_S = +1 is about 22 percent. Using the off-resonance readout 2 baseline estimated by excluding the five points centered on the observed dip gives baseline = 38.435 raw units. The expected resonant drop is therefore:

expected_drop = baseline * 0.22 * P_res = 38.435 * 0.22 * 0.996 = 8.42 raw units.

This predicts an on-resonance readout of about 30.01 raw units.

Observed data comparison:

Readout 2 has its minimum at 3.880 GHz with value 30.788. Using the same off-resonance baseline of 38.435 raw units, the observed drop is 7.65 raw units, or 19.9 percent of the baseline. Normalizing readout 2 by readout 1 gives an off-resonance ratio baseline of 0.981 and a minimum ratio of 0.766, a 21.9 percent fractional drop, matching the stated 22 percent contrast scale.

I also fit the readout 2 data to the rectangular-pulse Rabi detuning model:

P(detuning) = (f_Rabi^2 / (f_Rabi^2 + detuning^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + detuning^2))

with f_Rabi fixed at 10 MHz and t fixed at 52 ns, fitting only center frequency, baseline, and amplitude. A grid fit gave best center about 3.8785 GHz, baseline 38.84, amplitude 8.00 raw units, maximum sampled transfer 0.972, and predicted minimum 31.07. The constant-baseline null RSS was 124.42, while the driven-transition model RSS was 18.78, an improvement of 105.63 raw-unit-squared.

Stored averages are not treated as a strong independent repeatability test because they often reflect tracking cadence. Still, both stored averages show the same readout 2 central depression around indices 10 to 11, while readout 1 lacks a comparable dip. This is consistent with a pODMR resonance rather than common-mode brightness drift.

Decision:

The active pulse is a near-pi microwave pulse at the stated Rabi scale, and the observed readout 2 contrast, line center, and width quantitatively match the expected pODMR signal. A pODMR resonance is present.
