Sequence/readout interpretation:

The active sequence is Rabimodulated.xml while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect, then, because full_expt = 0, skip the optional m_S = +1 reference block. The remaining active microwave operation is a single rabi_pulse_mod_wait_time followed by detection. Thus readout 1 is the polarized m_S = 0 reference and readout 2 is the post-pulse signal readout.

Relevant pulse settings from the provided XML/export values are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns. With the stated setup Rabi rate of about 10 MHz at mod_depth = 1, this is approximately a pi pulse. If a pODMR resonance were present and the pulse drove the m_S = 0 to m_S = +1 transition efficiently, readout 2 should show a clear fluorescence depression relative to readout 1, with a scale approaching the stated 22% contrast.

The combined raw data show only scattered signal/reference depressions. The largest normalized drops are around 6-7%, with similarly sized positive excursions elsewhere, and the apparent low points do not form a single clean resonance-shaped feature. The two stored averages also show large baseline/tracking shifts, so they are not strong independent repeatability evidence. Given the pi-scale pulse and expected contrast, the observed structure is too small and irregular to call a pODMR resonance.

Decision: resonance_absent.
