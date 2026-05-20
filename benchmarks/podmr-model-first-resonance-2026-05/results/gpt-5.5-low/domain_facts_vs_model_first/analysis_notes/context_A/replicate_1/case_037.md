Active sequence decision:

The provided XML is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to
3.925 GHz. The instructions first polarize and detect, producing the true
m_s = 0 bright reference readout. Because full_expt is 0, the optional
m_s = +1 reference block is skipped. The active experimental contrast channel
is therefore the second detection after the Rabi-modulated microwave pulse.

Pulse settings:

mod_depth is 1 in the provided sequence XML and length_rabi_pulse is 52 ns.
With the stated setup calibration of about 10 MHz Rabi frequency at
mod_depth = 1, this is approximately a pi pulse. If the swept microwave
frequency crossed a real single-NV pODMR resonance, the post-pulse readout
should show a clear reduction relative to the pre-pulse m_s = 0 reference on
the order of the available contrast scale, not merely small point-to-point
scatter.

Data assessment:

The two combined raw readouts track each other closely across the sweep, with
no narrow or broad feature where the post-pulse readout consistently drops
relative to the bright reference. The largest excursions are isolated and are
not reproducible between the two stored averages; the per-average traces also
show substantial drifting baseline behavior consistent with tracking cadence.
Since stored averages are not a strong independent repeatability test here,
the relevant observation is that the active post-pulse readout lacks a
coherent resonance-shaped contrast feature against the reference.

Decision: resonance absent.
