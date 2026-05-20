Case: podmr_069_2026-05-17-081236

I used inputs/sequence.xml for the active sequence. The sequence is Rabimodulated with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

- polarize, then detection: this is the true m_S = 0 reference readout, corresponding to raw readout 1.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- apply rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection: this is the microwave-dependent signal readout, corresponding to raw readout 2.

Sequence parameters from the XML:

- sample_rate = 250 MHz
- length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns
- mod_depth = 1
- expected Rabi frequency at this mod_depth = about 10 MHz
- setup contrast between m_S = 0 and m_S = +1 = about 22%

Quantitative physical model:

For a square microwave pulse, the excited-state population after a pulse of duration t at detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

using frequencies in cycles/s. With f_R = 10 MHz and t = 52 ns, the on-resonance transfer is

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

The expected resonant fluorescence ratio is therefore

signal/reference = 1 - 0.22 * 0.9961 = 0.7809,

so a real on-grid resonance should produce about a 21.9% drop. With the measured reference baseline near 46.7 raw counts, that is an expected resonant drop of about 10.2 raw-count units.

Data check:

The measured readout2/readout1 ratios have mean 0.9980 and standard deviation 0.0293. The lowest ratio is 0.9111 at 3.845 GHz, an 8.9% drop, or 4.29 raw counts below the same-point reference. Neighboring points do not show the required near-pi-pulse line shape: a fixed mod_depth = 1 Rabi model centered near 3.848 GHz would predict ratios around 0.80 at 3.845 GHz and 0.79 at 3.850 GHz, but the observed ratios are 0.911 and 0.971.

I also compared the reference-normalized ratios against the detuned square-pulse model over possible center frequencies. The fixed-amplitude model required by mod_depth = 1 and 22% contrast fit worse than a flat no-resonance model: SSE 0.0769 versus flat SSE 0.0172. If the amplitude is allowed to float, the best fit gives only about 6.5% effective contrast, far below the expected 21.9% resonant contrast for the active XML parameters.

Decision:

The observed deviations are too small and too inconsistent with the required mod_depth = 1, 52 ns near-pi-pulse pODMR response. I decide resonance_absent.
