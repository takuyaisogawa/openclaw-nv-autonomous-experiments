Case podmr_028_2026-05-13-100213

Inputs used
- Used only inputs/sequence.xml and inputs/raw_export.json in this isolated workspace.
- The active sequence in the saved export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The saved variable table gives mod_depth = 1, length_rabi_pulse = 52 ns, full_expt = 0, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us, and length_last_wait = 1 us.

Pulse sequence and readout roles
- The instructions first call adj_polarize and detection. With full_expt = 0, the optional "Acquire 1 level reference" block is skipped.
- The only active microwave manipulation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- Therefore readout 1 is the bright m_S = 0 reference after polarization, and readout 2 is the signal readout after the Rabi-modulated microwave pulse.

Quantitative expected signal model
- Domain fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Here f_R = 10 MHz and pulse duration t = 52 ns.
- Resonant transfer probability for a square Rabi pulse is P = sin^2(pi f_R t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup m_S = 0 to m_S = +1 contrast scale of about 22%, the maximum expected resonant fluorescence drop is 0.22 * 0.996 = 0.219, or about 21.9% of the bright reference signal.
- At the observed readout scale near 27.7 counts, this corresponds to an ideal on-resonance decrease of about 6.1 counts in the post-pulse readout. A smaller observed dip is plausible if the resonance is between sampled frequencies, broadened, detuned from the exact scan point, or affected by imperfect initialization/readout.

Data comparison
- Mean readout 1 = 27.69 counts, standard deviation across scan points = 0.90.
- Mean readout 2 = 27.25 counts, standard deviation across scan points = 1.46.
- The clearest feature is in readout 2 at 3.900-3.905 GHz: readout 2 falls to 24.85 and then 24.12 counts.
- At 3.905 GHz, readout 1 = 27.62 and readout 2 = 24.12, so readout 2/readout 1 = 0.873 and the paired drop is 3.50 counts, about 12.7% of readout 1.
- Excluding the two dip points at 3.900 and 3.905 GHz, readout 2 has a baseline mean of 27.55 counts and standard deviation of 1.19 counts. The 3.905 GHz point is 3.43 counts below that baseline, about 2.9 baseline standard deviations.
- The stored per-average traces mainly show tracking offsets between the two averages, so I did not treat the two averages as a strong independent repeatability test. The combined readout role, dip location, and dip magnitude relative to the explicit Rabi/contrast model are the main evidence.

Decision
- A pODMR resonance is present. The observed post-pulse readout dip is smaller than the ideal 21.9% model expectation but has the correct sign, appears in the active signal readout rather than the bright reference readout, and is quantitatively compatible with a resonance sampled near 3.900-3.905 GHz under nonideal experimental conditions.
