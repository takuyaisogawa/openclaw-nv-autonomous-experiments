Case: podmr_068_2026-05-17-075825

I used only the files in this workspace. The provided sequence XML is Rabimodulated.xml. In the active instruction path, the sequence first polarizes the NV and takes a detection readout, then waits. The conditional "Acquire 1 level reference" block is skipped because full_expt = 0. The sequence then applies one rabi_pulse_mod_wait_time pulse and takes the final detection readout. Thus readout 1 is the optically polarized m_S = 0 reference/readout before the microwave pulse, and readout 2 is the pODMR signal readout after the microwave pulse. The active microwave pulse has length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence XML.

Quantitative model check:

- Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, the resonant Rabi frequency for the XML pulse is 10 MHz.
- For a square pulse of duration t = 52 ns, the resonant transition probability is sin^2(pi*f_R*t) = sin^2(pi*10e6*52e-9) = 0.996.
- With the setup contrast scale of about 22% between m_S = 0 and m_S = +1, a true resonance should therefore reduce the fluorescence by about 0.996*22% = 21.9%.
- The observed baseline readouts are around 50 counts, so the expected resonant pODMR dip is approximately 50*0.219 = 11 counts.

The measured readout 2 values do not show an isolated dip of this scale anywhere in the 3.825 to 3.925 GHz scan. Readout 2 mostly tracks readout 1, with point-to-point readout-2-minus-readout-1 differences typically within about +/-2 counts. The largest low values occur at the high-frequency end, where readout 1 also drops strongly, indicating shared drift/tracking behavior rather than a microwave-specific pODMR contrast feature. The per-average traces also reflect the same broad drift and scatter; with only two stored averages, these averages mainly reflect the tracking cadence rather than a strong independent repeatability test.

Decision: resonance_absent.
