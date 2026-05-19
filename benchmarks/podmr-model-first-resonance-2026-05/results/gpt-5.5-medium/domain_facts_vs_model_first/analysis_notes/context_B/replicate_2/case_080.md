<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_080

I used only the provided raw export and sequence XML.

Sequence interpretation:
- Active sequence: Rabimodulated.xml.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional 1-level reference block is skipped.
- Readout 1 role: true m_S = 0 reference after adj_polarize and detection.
- Readout 2 role: signal readout after one rabi_pulse_mod_wait_time pulse and detection.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded duration remains 52 ns.

Physical model calculation:
The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1. I modeled the pulse as a square driven two-level pulse with

P(+1) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

where Omega = 2*pi*10 MHz and t = 52 ns. The expected fluorescence ratio for the signal readout relative to the 0 reference is

signal / reference = 1 - 0.22 * P(+1),

using the stated 22 percent contrast scale.

At exact resonance, 10 MHz * 52 ns = 0.52 Rabi cycles, so P(+1) = sin^2(pi * 0.52) = 0.996. The expected signal/reference ratio is therefore 0.781, a 21.9 percent dip. For a typical reference level near 46 counts, this is about a 10 count reduction in readout 2 relative to readout 1. At +/-5 MHz detuning the model still predicts P = 0.749 and signal/reference = 0.835, about a 7.6 count dip. At +/-10 MHz detuning it predicts P = 0.273 and signal/reference = 0.940, about a 2.8 count dip.

Observed data comparison:
The measured readout2 - readout1 differences range from -3.06 to +2.40 counts, with mean -0.53 counts. The measured readout2/readout1 ratios range from 0.936 to 1.054, with mean 0.989. There is no point or neighboring pair showing the expected 7-10 count suppression from the active 52 ns, mod_depth 1 pulse.

I also compared a fixed-physics resonance model across possible resonance centers in the scanned range. The no-resonance model r2 = r1 has SSE 58.36, and allowing only a constant mean offset gives SSE 52.43. The best fixed-physics resonance model has SSE 160.61, centered near 3.8872 GHz, because it predicts approximately -9.7 count dips at 3.885-3.890 GHz where the observed dips are only about -2 to -3 counts.

Decision:
The expected pODMR resonance signal from the relevant pulse model is much larger and more structured than the observed fluctuations. Stored averages are not treated as an independent repeatability test. I decide resonance_absent.
