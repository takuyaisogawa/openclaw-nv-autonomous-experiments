Case podmr_009_2026-05-16-113112

Inputs used only from this isolated workspace: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles:
- The saved scan reports SequenceName = Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize the NV and perform detection. This is the true m_S = 0 level reference, corresponding to readout 1.
- full_expt = 0, so the optional explicit m_S = 1 reference branch is not active.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is the MW-affected pODMR readout, corresponding to readout 2.

Pulse settings:
- length_rabi_pulse = 52 ns.
- mod_depth = 1.
- The setup Rabi frequency is approximately 10 MHz at mod_depth = 1, so the active pulse has f_Rabi approximately 10 MHz.

Explicit quantitative model:
- For a square resonant Rabi pulse, the population transferred from m_S = 0 to m_S = +1 is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The current setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant PL change is 0.22 * 0.996 = 0.219, or about 21.9%.
- The mean raw count level across the two combined readouts is about 28.7 counts, so the expected resonant signal scale is about 28.7 * 0.219 = 6.3 counts.

Observed data comparison:
- readout 1 is roughly flat around 29 to 31 counts across the central region.
- readout 2 shows a localized depression at 3.870 to 3.885 GHz: 26.21, 24.29, 24.15, and 25.00 counts.
- The readout1 - readout2 separation reaches 7.13 counts at 3.875 GHz and remains 5.88 to 5.75 counts at 3.880 to 3.885 GHz.
- This observed separation is close to the explicitly modeled 6.3 count expectation for a resonant nearly-pi pulse.
- Stored per-average traces show strong slow drift/tracking behavior, so I do not treat the two averages as a strong independent repeatability test; the decision is based on the active readout roles and the expected signal scale versus the combined readout feature.

Decision:
The data are consistent with a pODMR resonance being present. The active MW readout has a localized dip of the expected magnitude relative to the m_S = 0 reference near the scan center.
