Case podmr_011_2026-05-16-120107

I used only the provided XML and raw export. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed variables are length_rabi_pulse = 52 ns and mod_depth = 1. full_expt = 0, so the optional "1 level reference" block is skipped. The acquired roles are therefore:

- readout 1: true mS = 0 bright reference after adj_polarize and detection.
- readout 2: measurement after a rabi_pulse_mod_wait_time pulse, then detection.

Quantitative physical model:

The stated setup has Rabi frequency about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For this case mod_depth = 1, so f_R = 10 MHz. For a resonant square Rabi pulse, the transferred population is modeled as P = sin^2(pi f_R t). With t = 52 ns,

P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The stated mS = 0 to mS = +1 contrast scale is about 22%, so the expected resonant fractional PL reduction in the post-pulse readout is 0.22 * 0.996 = 0.219, or 21.9%. Using the non-dip readout-2 baseline from the raw export as about 41.21 counts, the expected resonant readout-2 minimum is:

41.21 * (1 - 0.219) = 32.18 counts,

for an expected drop of about 9.03 counts.

Observed comparison:

The combined readout-2 trace has its minimum at 3.880 GHz with 33.096 counts. Relative to the same baseline estimate of 41.21 counts, the observed drop is 8.11 counts, or 19.7%. This is close to the calculated 21.9% resonant drop for the active 52 ns pulse. The per-average overlay shows the same central readout-2 depression in both stored averages; those averages are treated mainly as tracking cadence, not as a strong repeatability test. Readout 1 remains comparatively flat near about 42 counts and does not show a matching deep dip, consistent with readout 1 acting as a bright reference rather than the driven signal channel.

Decision: a pODMR resonance is present.
