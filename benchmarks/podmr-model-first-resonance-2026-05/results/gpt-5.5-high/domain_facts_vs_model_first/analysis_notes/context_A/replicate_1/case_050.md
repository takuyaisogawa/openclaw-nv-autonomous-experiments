The active sequence is Rabimodulated.xml. The instructions first polarize the NV and take a detection readout, then wait. Because full_expt = 0, the optional "1 level reference" block is skipped. The active swept measurement is then a modulated Rabi pulse followed by detection while varying mw_freq from 3.825 GHz to 3.925 GHz.

Readout roles:
- readout 1: polarized mS = 0 reference after adj_polarize and detection.
- readout 2: signal readout after the swept-frequency Rabi pulse.

Pulse parameters from the provided XML/raw export are length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse, so an on-resonance transition should drive substantial population into mS = +1 and lower readout 2 relative to the mS = 0 reference by a contrast-scale amount, order tens of percent for this setup.

The combined readouts are noisy and jagged, with readout 2 sometimes above and sometimes below readout 1. The largest apparent negative deviations are only a few percent, not near the expected about 22% contrast scale, and they occur without a clean resonance-shaped feature. The stored averages also show broad tracking-like offsets and do not provide strong independent repeatability. I therefore do not see a convincing pODMR resonance in this measurement.
