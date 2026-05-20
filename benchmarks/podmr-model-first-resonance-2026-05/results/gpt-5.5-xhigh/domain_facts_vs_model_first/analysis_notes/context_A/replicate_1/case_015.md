Sequence XML used: Rabimodulated.xml.

Active sequence branch:
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true.
- The executed detections are therefore:
  1. After adj_polarize: true mS = 0 / bright reference.
  2. After rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth): MW-modulated signal readout.

Pulse settings before decision:
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s = 52 ns, rounded at 250 MHz sample rate.
- With the provided setup scale of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is close to a pi pulse, so an on-resonance drive should transfer population from bright mS = 0 toward darker mS = +1 and reduce the second readout relative to the first.

Readout behavior:
- The combined second readout shows a localized deep loss relative to the first readout near 3.870-3.880 GHz.
- At 3.875 GHz the ratio readout2/readout1 is about 0.783, and at 3.880 GHz it is about 0.754, matching the expected contrast scale for this setup.
- Away from this region the two readouts are mostly much closer, with no comparable broad baseline collapse.
- The two stored averages both show a depression in this frequency region, although stored averages may partly reflect tracking cadence rather than independent repeatability.

Decision:
The active pulse is appropriate for a near-pi pODMR contrast measurement and the signal readout contains a localized contrast-scale dip, so a pODMR resonance is present.
