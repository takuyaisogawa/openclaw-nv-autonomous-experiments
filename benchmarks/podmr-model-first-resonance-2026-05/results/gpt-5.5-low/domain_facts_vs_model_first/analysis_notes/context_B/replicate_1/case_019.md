Case podmr_004_2026-05-16-005019

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, previous outputs, sibling cases, or external context.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions first polarize the NV and perform detection before the microwave pulse. This first readout is the m_S = 0 optical reference.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped; there is no independent m_S = +1 reference in this run.
- The active driven measurement is a single rabi_pulse_mod_wait_time call followed by detection. This second readout is the post-microwave-pulse signal readout.
- The scanned variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Pulse parameters:
- length_rabi_pulse = 52 ns.
- mod_depth = 1.
- The provided setup relation gives Rabi frequency about 10 MHz at mod_depth = 1.

Quantitative expected-signal model:
- For a resonant square pulse, the population transferred from m_S = 0 to m_S = +1 is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence drop is 0.22 * 0.996 = 0.219, or about 21.9%.
- The median first-readout level is about 40.79 counts, so the expected resonant drop is about 8.94 counts.

Observed data comparison:
- The second readout has an off-resonant median of about 40.66 counts outside the central dip region.
- Its minimum is 31.81 counts at 3.880 GHz, giving an observed drop of 8.86 counts from the off-resonant median.
- Fractionally, this is 8.86 / 40.66 = 0.218, or about 21.8%.
- The first readout remains near 40-42 counts through the same region, so the central drop is specific to the post-pulse readout.
- Both stored averages show the same central post-pulse dip around 3.875-3.880 GHz, but I treat that mainly as consistency with tracking cadence rather than a strong independent repeatability test.

Decision:
The active pulse should produce an almost full pi-pulse response at resonance, and the observed post-pulse fluorescence drop has the expected magnitude and frequency-localized shape. I therefore decide that a pODMR resonance is present.
