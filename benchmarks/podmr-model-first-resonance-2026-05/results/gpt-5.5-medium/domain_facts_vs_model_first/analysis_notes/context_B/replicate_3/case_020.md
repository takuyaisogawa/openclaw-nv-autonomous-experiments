Case podmr_005_2026-05-16-010352 analysis note

Sequence interpretation

The provided sequence is Rabimodulated.xml. The active branch first polarizes the NV and performs a detection readout, then waits. The "Acquire 1 level reference" branch is guarded by full_expt, and full_expt is 0, so that branch is inactive. The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 1 is the polarized m_S = 0 reference, while readout 2 is the signal after the microwave/Rabi pulse.

Relevant parameters used for the decision

- Pulse duration: 52 ns.
- mod_depth: 1 from the provided sequence XML/variable values.
- Rabi frequency scale: about 10 MHz at mod_depth = 1.
- Setup contrast between m_S = 0 and m_S = +1: about 22%.
- Scan: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model

For a square resonant pulse, the population transferred from m_S = 0 to m_S = +1 is modeled as

P_transfer(delta = 0) = sin^2(pi * f_Rabi * t_pulse).

With f_Rabi = 10 MHz and t_pulse = 52 ns:

f_Rabi * t_pulse = 0.52 cycles
P_transfer = sin^2(pi * 0.52) = 0.996

The expected fractional fluorescence drop on resonance is therefore

contrast * P_transfer = 0.22 * 0.996 = 0.219, or about 21.9%.

At a readout baseline near 37.83 counts, this predicts an on-resonance drop of about 8.29 counts.

Observed signal calculation

The pulsed signal readout has its minimum at scan index 11, frequency 3.880 GHz, with readout 2 = 30.327 counts. Excluding the +/-2 points around the dip, the median off-resonance readout 2 level is 37.827 counts. The observed drop is therefore

37.827 - 30.327 = 7.50 counts,

or 19.8% of the off-resonance pulsed-readout level.

Using the local readout 1 reference near the dip gives a drop of

(39.192 - 30.327) / 39.192 = 22.6%.

The off-resonance median absolute deviation of readout 2 is about 0.663 counts, so the 7.50 count dip is about 11.3 MADs. The low points at 3.875 and 3.880 GHz also appear in both stored averages, though the stored averages should mainly be treated as tracking-cadence information rather than a strong independent repeatability test.

Decision

The observed dip magnitude matches the expected signal scale for a near-pi pulse at mod_depth 1 and is far larger than the off-resonance variation. This is consistent with a pODMR resonance being present.
