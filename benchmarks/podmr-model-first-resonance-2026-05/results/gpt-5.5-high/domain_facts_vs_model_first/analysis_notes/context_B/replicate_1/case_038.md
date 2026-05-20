Case podmr_023_2026-05-16-174219.

Sequence interpretation from inputs/sequence.xml and the exported variable table:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_s = +1 reference block is inactive.
- readout 1 role: after adj_polarize only, a bright m_s = 0 reference for the current scan point.
- readout 2 role: after adj_polarize, a single modulated Rabi microwave pulse, then detection; this is the pODMR signal readout.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse duration remains 52 ns.
- mod_depth = 1 from the provided sequence XML and variable values. The raw export also embeds an older sequence text containing mod_depth = 0.3, but the standalone XML and exported variable table are the requested controlling inputs.

Physical model calculation:
Use a driven two-level square-pulse model for population transfer from m_s = 0 to m_s = +1:

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

where Omega is the resonant Rabi frequency in cycles/s, Delta = f - f0 in cycles/s, and t = 52 ns. The setup gives Omega about 10 MHz at mod_depth = 1. On resonance:

P0 = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The setup contrast scale between m_s = 0 and m_s = +1 is about 22%, so an on-resonance pODMR point should reduce readout 2 relative to the bright readout 1 by:

0.22 * 0.996 = 0.219, or about 21.9%.

At the measured reference level mean(readout 1) = 47.55, the expected resonant signal readout would be roughly:

47.55 * (1 - 0.219) = 37.13,

an expected drop of about 10.42 raw units. The frequency step is 5 MHz, and the pulse is broad enough that even a resonance halfway between sample points should still produce a large nearest-point reduction. At Delta = 2.5 MHz, the same model gives P about 0.929, i.e. about a 20.4% fluorescence reduction. At Delta = 5 MHz, P is about 0.751, i.e. about a 16.5% reduction.

Data comparison:
- mean(readout 1) = 47.55, standard deviation across scan points = 1.02.
- mean(readout 2) = 47.69, standard deviation across scan points = 0.98.
- readout2/readout1 mean = 1.003.
- minimum readout2/readout1 = 0.949 at 3.835 GHz, only a 5.1% relative dip and not accompanied by the broad line shape expected for the 52 ns, mod_depth 1 pulse.
- maximum readout2 - readout1 occurs at 3.875 GHz, so the nominal central region is brighter, not darker, in the signal readout.

I also compared the fixed-amplitude two-level model against the normalized ratios while allowing the resonance center to vary over the scanned interval. The best fixed model still requires a minimum ratio of about 0.781 and has RMSE about 0.0605, while a flat model at the observed mean ratio has RMSE about 0.0301. Thus the expected resonance signal is not present in the raw readouts.

Decision: resonance_absent.
