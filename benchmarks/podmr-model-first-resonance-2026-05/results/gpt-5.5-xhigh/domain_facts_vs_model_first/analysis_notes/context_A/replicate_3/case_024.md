Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The instructions first polarize and detect without a microwave pulse, so readout 1 is the bright mS = 0 reference. The optional mS = +1 reference block is skipped because full_expt = 0. The active measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the microwave-pulse signal.

At mod_depth = 1 the stated Rabi frequency is about 10 MHz, giving a pi-pulse time of about 50 ns. The 52 ns pulse is therefore expected to produce near-maximal mS = 0 to mS = +1 transfer when the microwave frequency is on resonance. With the stated setup contrast scale of about 22%, a real resonance should look like an approximately 20% dip in readout 2 relative to readout 1.

The combined data show exactly that localized feature. Away from the center, readout 2 is usually close to readout 1, but around 3.875 to 3.885 GHz the normalized readout 2 / readout 1 ratio drops strongly: 0.773 at 3.875 GHz, 0.804 at 3.880 GHz, and 0.813 at 3.885 GHz. The deepest point corresponds to about 22.7% contrast, matching the expected contrast for this setup and pulse length.

The per-average raw traces have large opposite baseline drifts, consistent with tracking cadence rather than independent repeatability. Normalizing within each stored average still leaves the dip in both averages near the same frequencies, with ratios around 0.76 to 0.84 through the central feature. This makes the feature more consistent with a pODMR resonance than with a simple tracking or averaging artifact.

Decision: resonance_present.
