Case: podmr_050_2026-05-17-005655

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:

The active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the XML, detuning is 0, full_expt is 0, mod_depth is 1, and length_rabi_pulse is 5.2e-08 s. The sample rate is 250 MHz, so the rounded pulse is 13 samples, still 52 ns.

The first detection occurs immediately after adj_polarize and is labeled in the XML as "Acquiring true 0 level reference"; this is the bright m_S = 0 reference readout. The optional "Acquire 1 level reference" block is skipped because full_expt = 0. The second active detection occurs after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on); this is the pODMR MW-pulse readout.

Quantitative physical model:

For a square resonant pulse, using the provided setup scale, the Rabi frequency is approximately 10 MHz at mod_depth = 1. The transition probability at detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t),

with f_R = 10 MHz and t = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, an in-window resonance should therefore cause a fractional fluorescence drop of about

0.22 * 0.996 = 0.219, or 21.9%.

The mean reference readout is 53.29 counts, so the expected on-resonance drop is about 11.68 counts. Even if the true resonance lies halfway between two 5 MHz-spaced scan points, the model gives a minimum sampled transition probability of 0.929 over all possible in-window centers, so at least one sampled point should show about 20.4% contrast.

Data comparison:

Combined readout means:

- reference readout mean: 53.2866
- MW readout mean: 52.9295
- MW/reference ratio mean: 0.9936

The largest combined reference-minus-MW difference is 3.4231 counts at 3.865 GHz, which is a 6.16% normalized drop. The lowest MW readout value is 50.9038 counts at 3.910 GHz, but relative to its local reference this is only a 4.61% drop. These are far smaller than the roughly 11.7-count / 21.9% dip expected for the active 52 ns, mod_depth = 1 pulse.

I also compared the normalized ratio to the fixed-contrast Rabi model. A constant-ratio model gives SSE = 0.01194. A fixed 22% contrast resonance constrained inside the scan gives best SSE = 0.06514, substantially worse than the constant model, with a predicted minimum ratio around 0.794 that is not present in the data. If the line amplitude is allowed to float freely, the best equivalent contrast is only about 2.4%, not the expected setup contrast for this pulse.

Decision:

The active pulse should make a strong pODMR dip if a resonance is present in the scanned frequency range. The observed fluctuations are much smaller and do not follow the expected fixed-contrast Rabi response. I therefore classify this case as resonance_absent.
