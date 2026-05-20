Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the intermediate "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. The active detections are therefore:
- readout 1: the initial polarized mS = 0 reference after adj_polarize.
- readout 2: the signal after rabi_pulse_mod_wait_time using length_rabi_pulse.

Key pulse settings from the provided XML/export values are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, the pulse is approximately a half-period/pi pulse on resonance. A real pODMR resonance should therefore produce a sizeable decrease of the driven readout relative to the mS = 0 reference, potentially on the order of the 22% contrast scale, localized near the resonance frequency.

The combined raw readouts do not show that behavior. The driven readout is sometimes below the reference and sometimes above it, with small differences compared with the expected contrast scale. There is a shallow low point near 3.855 GHz, but it is not a clean resonant dip: the surrounding points do not form a strong line shape, the difference is only a few percent of the baseline, and the high-frequency side trends upward rather than showing a clear isolated ODMR feature. The per-average overlay mainly shows large tracking/cadence offsets between stored averages, which should not be interpreted as strong repeatability evidence.

Decision: resonance_absent.
