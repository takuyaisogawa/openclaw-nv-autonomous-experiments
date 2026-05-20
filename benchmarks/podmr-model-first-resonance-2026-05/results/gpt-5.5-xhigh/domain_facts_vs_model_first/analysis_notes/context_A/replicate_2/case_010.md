The provided sequence is Rabimodulated.xml with the active measurement path:
polarize, detect, wait; skip the optional 1-level reference because full_expt = 0;
apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1;
then detect again.

Thus readout 1 is the bright m_S = 0 reference taken before the microwave pulse,
and readout 2 is the signal after the scanned microwave pulse. At mod_depth = 1
the stated Rabi frequency is about 10 MHz, so a 52 ns pulse is essentially a pi
pulse. If the scan crosses a real pODMR resonance, readout 2 should show a
large drop relative to readout 1 on the order of the setup contrast scale
(about 22%), with a feature broader than a single isolated 5 MHz step.

The observed combined signal-reference contrast is small and irregular. The
largest negative value is about -8.7% near 3.855 GHz, but it is a single-point
excursion flanked by positive contrast at adjacent scan points. Other negative
points are similarly modest and not organized into a clear resonance-shaped
dip. The stored averages show strong tracking-like drift, so I do not treat
their apparent agreement as strong independent repeatability.

Decision: resonance_absent. The scan does not show a reliable pODMR resonance
for this near-pi-pulse sequence.
