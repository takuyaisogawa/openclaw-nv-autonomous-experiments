Case: podmr_021_2026-05-16-171244

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. do_adiabatic_inversion is not used in the active path because that block is gated off.
- Readout 1 role: true m_S = 0 reference, taken immediately after adj_polarize and before the microwave pulse.
- Readout 2 role: signal readout after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- Pulse parameters used for the active signal readout: length_rabi_pulse = 52 ns, mod_depth = 1.

Physical model calculation:

For a rectangular resonant microwave pulse, use the two-level transition probability

P_transfer(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * tau * sqrt(f_R^2 + df^2))

with f_R = 10 MHz at mod_depth = 1, tau = 52 ns, and fluorescence contrast between m_S = 0 and m_S = +1 of 22 percent. At zero detuning, f_R * tau = 0.52 cycles, so

P_transfer(0) = sin^2(pi * 0.52) = 0.996

Expected normalized fluorescence drop at resonance:

0.22 * 0.996 = 0.219, or about 21.9 percent.

Expected normalized drops at scan-step detunings:

- 0 MHz: 21.9 percent
- 5 MHz: 16.5 percent
- 10 MHz: 6.0 percent
- 15 MHz: 0.3 percent
- 20 MHz: 1.1 percent

The predicted feature from a real resonance should therefore include a large readout-2 decrease relative to the m_S = 0 reference at one scan point and usually the adjacent 5 MHz point as well, unless the resonance falls between points.

Data comparison:

Combined readout means:

- readout 1 mean = 46.49 counts
- readout 2 mean = 46.41 counts

Pointwise normalized drop (readout1 - readout2) / readout1:

- mean = 0.14 percent
- standard deviation = 2.59 percent
- range = -3.98 percent to +4.72 percent

The largest observed drop is 4.72 percent at 3.830 GHz, and nearby points do not show the expected broad pulse-response pattern. Around 3.880 to 3.885 GHz there is only a 2.4 to 2.6 percent dip, far below the 16 to 22 percent expected for this pulse strength and duration. Several points have readout 2 above readout 1, inconsistent with a driven transition to the dimmer m_S = +1 state.

Decision:

The physically expected pODMR signal for this active pulse sequence is much larger than the observed readout-2/reference differences. The scan shows tracking-scale fluctuations and no quantitatively compatible resonance dip. I decide resonance_absent.
