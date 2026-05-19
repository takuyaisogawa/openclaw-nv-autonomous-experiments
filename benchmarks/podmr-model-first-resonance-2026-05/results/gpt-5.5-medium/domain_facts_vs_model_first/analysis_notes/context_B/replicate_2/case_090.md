<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_090

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- readout 1 role: detection immediately after optical polarization, the true m_S = 0 reference.
- readout 2 role: detection after a modulated Rabi pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.

Physical model calculation:
For the relevant two-level driven transition, use
P_exc(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * t),
with Omega = 10 MHz at mod_depth = 1 and t = 52 ns. On resonance, Omega * t = 0.52 cycles, so
P_exc(0) = sin^2(pi * 0.52) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance normalized signal for readout 2 relative to readout 1 is
1 - 0.22 * 0.996 = 0.781.
At a typical reference level near 51 counts, that corresponds to a drop of about 11.2 counts.

The scan spacing is 5 MHz. Even if the resonance falls halfway between sampled frequencies, Delta = 2.5 MHz gives P_exc = 0.929 and an expected normalized signal of 0.796. At Delta = 5 MHz, P_exc = 0.749 and the expected normalized signal is 0.835. Thus a real resonance in this scanned window should produce a broad, large depression in readout 2 relative to the m_S = 0 reference, not just a one-point fluctuation.

Observed quantitative comparison:
- Mean readout 1: 51.03 counts.
- Mean readout 2: 50.82 counts.
- Mean readout2/readout1 ratio: 0.996, standard deviation 0.0277.
- Minimum readout2/readout1 ratio: 0.948 at 3.905 GHz, equivalent to only a 5.2% depression.
- Largest combined readout2 - readout1 drop: about -2.7 counts, far smaller than the expected roughly -11 count resonant pi-pulse response.
- A constrained fit of the fixed Rabi response shape over possible resonance centers gives an amplitude of about 0.023 in normalized contrast, versus the physically expected 0.22.

Stored per-average traces do not provide a strong independent repeatability test here because the averages can reflect tracking cadence. They also do not show a stable, expected-amplitude resonant depression.

Decision:
The expected pODMR resonance for this pulse should be large and broad on the 5 MHz scan grid. The observed readout difference is near zero on average and any dips are much smaller than the modeled resonant response, so I decide that a pODMR resonance is absent.
