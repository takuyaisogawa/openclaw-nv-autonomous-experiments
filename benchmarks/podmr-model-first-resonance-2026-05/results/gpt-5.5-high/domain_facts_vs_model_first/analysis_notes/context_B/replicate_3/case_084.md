Case podmr_070_2026-05-17-082720

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the active instructions, full_expt = 0, so the optional m_S = 1 reference block is skipped. The two stored readouts are therefore:

- readout 1: pumped bright m_S = 0 reference, after adj_polarize and immediate detection
- readout 2: detection after the active rabi_pulse_mod_wait_time pulse

Active pulse parameters:

- length_rabi_pulse = 52 ns, exactly 13 samples at 250 MHz
- mod_depth = 1
- relevant Rabi frequency from the supplied setup facts: about 10 MHz at mod_depth = 1

Quantitative expected signal model:

For a square resonant pulse, the transferred population is

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau),

with Omega / 2 pi = 10 MHz and tau = 52 ns. On resonance,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated bright-to-dark contrast scale of 22%, the expected normalized fluorescence loss on resonance is 0.22 * 0.996 = 0.219, so readout2/readout1 should be about 0.781. Using the measured mean readout1 of 50.71 counts, the expected resonant drop is about 11.11 counts, taking readout2 to about 39.60 counts.

The 5 MHz scan grid would not hide this. If the resonance lay halfway between points, the nearest detuning would be 2.5 MHz, for which the same model gives P1 = 0.929 and an expected normalized drop of 0.204. Even at 5 MHz detuning the expected normalized drop is 0.165, or about 8.35 counts from the observed bright reference level.

Observed comparison:

- mean readout1 = 50.71 counts
- mean readout2 = 50.23 counts
- mean readout2 - readout1 = -0.48 counts
- readout2/readout1 mean = 0.9906
- minimum readout2/readout1 = 0.9613, a maximum normalized drop of 0.0387 or about 1.96 counts

The largest observed normalized drop is far smaller than the minimum expected near-grid pODMR response for this 52 ns, mod_depth 1 pulse. The raw readouts also share slow drift over the scan, so the small readout2 deficits are consistent with baseline variation rather than the expected near-pi-pulse resonance. Stored averages are not treated as an independent repeatability test because they can reflect tracking cadence.

Decision: resonance_absent.
