Case: podmr_031_2026-05-16-195907

Sequence interpretation

The provided XML is Rabimodulated.xml. The active sequence first polarizes the NV, then immediately performs a detection call. Because full_expt = 0, the conditional "Acquire 1 level reference" block is skipped, so no independent m_s = +1 reference is acquired. After the first detection, the sequence applies:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on);

and then performs the second detection. Therefore readout 1 is the true m_s = 0 / laser-only reference for each scan point, and readout 2 is the post-Rabi-pulse signal readout. The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, this duration is already on the 4 ns sample grid, so the rounded pulse length remains 52 ns.

Quantitative expected-signal model

Using the stated setup facts, the on-resonance Rabi frequency at mod_depth = 1 is approximately 10 MHz. For a square pulse with detuning Delta, I used the two-level transition probability

P1(Delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau),

where Omega = 2*pi*10 MHz, delta = 2*pi*Delta, and tau = 52 ns. On resonance this gives sin^2(pi * 10 MHz * 52 ns) = 0.996, so the pulse is effectively a pi pulse. The current setup contrast between m_s = 0 and m_s = +1 is about 22%, so a resonance should reduce the post-pulse readout by approximately

0.22 * 52.72 = 11.6 raw readout units

near the resonance center, with a broad finite-pulse line shape spanning several neighboring 5 MHz scan points. For example, if the resonance center were near 3.875 GHz, the expected raw drops at scan points around the center would be approximately 3.2, 8.7, 11.6, 8.7, and 3.2 units over the five central points.

Data comparison

The combined raw readout means are:

- readout 1 mean: 52.721 raw units
- readout 2 mean: 52.728 raw units
- readout 2 - readout 1 mean: 0.007 raw units
- readout 2 - readout 1 standard deviation over frequency: 1.393 raw units

At the nominal central part of the scan near 3.875 GHz, readout 2 - readout 1 is only -0.135 raw units, corresponding to a 0.26% drop, not the expected roughly 22% drop. The largest normalized apparent drop anywhere is 7.1% at 3.920 GHz, but it is isolated: the adjacent points at 3.915 GHz and 3.925 GHz do not show the required broad dip pattern. A model fit constrained to the expected 11.6 raw-unit contrast gives a much worse residual than a flat baseline inside the scan window, while an unconstrained in-window line-shape fit reduces the amplitude to about 1.8 raw units, far below the physically expected signal for this pulse.

The per-average traces mainly show a large baseline offset between the two stored averages, consistent with tracking cadence rather than an independent repeatability test. Averaging those two baselines gives the combined traces above, where the readout difference remains near zero.

Decision

The active sequence should produce a large post-pulse fluorescence dip if a pODMR resonance is present in the scanned window. The observed data do not contain that dip in either amplitude or line shape. I therefore classify this case as resonance absent.
