Case: podmr_050_2026-05-17-005655

I used inputs/sequence.xml as the sequence source. The active sequence is Rabimodulated. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables include sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, delay_wrt_1mus = 0.2 us, and length_last_wait = 1 us.

Readout roles from the active instruction flow:
- First detection: after adj_polarize and before any microwave pulse. This is the m_S = 0 bright reference readout.
- The optional 1-level reference branch is skipped because full_expt = 0.
- Second detection: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay). This is the pODMR signal readout after the microwave pulse.

Physical model calculation:
For a resonant square Rabi pulse, the transferred population is
P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin(pi * t * sqrt(f_R^2 + delta^2))^2,
using frequencies in Hz. With f_R = 10 MHz at mod_depth = 1 and t = 52 ns,
P1(0) = sin(pi * 10e6 * 52e-9)^2 = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional fluorescence drop is
0.22 * 0.996 = 0.219, or about 21.9%.

The mean bright reference readout is 53.29 counts, so a true sampled resonance should put the signal readout near
53.29 * (1 - 0.219) = 41.61 counts,
an expected drop of about 11.68 counts from the reference. The finite-detuning model is also broad on the 5 MHz grid: even a point 5 MHz from resonance would still be expected to show roughly a 16% drop, so a real resonance in this scan window should not appear as only a tiny single-point fluctuation.

Observed data comparison:
- readout1 mean = 53.29 counts, standard deviation = 0.90.
- readout2 mean = 52.93 counts, standard deviation = 0.93.
- Mean normalized deficit 1 - readout2/readout1 = 0.0064.
- Largest normalized deficit is 0.0616 at 3.865 GHz, corresponding to a 3.42 count drop, much smaller than the approximately 11.68 count drop expected for a resonant pi pulse.
- A least-squares fit of the detuned Rabi lineshape to the normalized deficits gives a best fitted dip coefficient of about 0.024, while the physical expectation is about 0.22. Forcing the 0.22 contrast produces a worse fit than a flat no-resonance model.

Decision:
The active pulse should produce an approximately 22% pODMR dip if a resonance is present in the scanned range. The measured paired readouts show only small, non-Rabi-shaped percent-level deficits and no feature at the expected physical scale, so I classify this case as resonance_absent.
