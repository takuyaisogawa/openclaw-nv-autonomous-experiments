pODMR decision analysis for podmr_012_2026-05-16-121601

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual cross-check of the raw data

Sequence and readout roles:
- Active sequence name in the raw export is Rabimodulated.xml, consistent with the provided sequence XML.
- The varied parameter is mw_freq, from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML first applies adj_polarize and then detection. This first detection is the bright m_S = 0 reference/readout.
- full_expt = 0, so the conditional "Acquire 1 level reference" branch is not executed. There is no active independent dark/+1 reference readout in this run.
- The active pODMR readout is the later detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth).
- Provided active variables give length_rabi_pulse = 5.2e-08 s and mod_depth = 1. The pulse is rounded to the sample grid; at 250 MS/s, 52 ns is exactly 13 samples, so the active duration remains 52 ns.

Physical model calculation:
- Given setup Rabi frequency f_Rabi ~= 10 MHz at mod_depth = 1, the resonant rotation angle is
  theta = 2*pi*f_Rabi*t = 2*pi*(10e6)*(52e-9) = 3.267 rad = 1.04*pi.
- The resonant transition probability for a square pulse is sin^2(theta/2) = sin^2(1.6336) = 0.996.
- With a stated bright-to-dark contrast scale of about 22%, a fully resonant 52 ns pulse should reduce the readout by approximately 0.22*0.996 = 21.9% of the bright count.
- The mean first readout is 42.075 counts, so the expected resonant drop is 42.075*0.219 = 9.22 counts, giving an expected on-resonance second readout near 32.86 counts for ideal contrast.

Observed quantitative features:
- The second readout minimum is 33.923 counts at 3.880 GHz.
- At that same point, the first readout is 41.231 counts, so the paired drop is 7.308 counts and the ratio readout2/readout1 is 0.823.
- Nearby points show a localized dip: at 3.870, 3.875, 3.880, and 3.885 GHz the paired drops are 5.54, 5.23, 7.31, and 5.65 counts.
- Away from 3.870-3.885 GHz, the paired readout2-readout1 difference has mean -0.59 counts and standard deviation 1.02 counts. The central minimum is therefore about 6.6 standard deviations below the off-resonant paired-difference level.
- A simple Gaussian-dip least-squares model for readout2 gives best center 3.880 GHz, width 7.5 MHz, and amplitude 7.39 counts. This reduces SSE from 144.17 for a constant model to 35.68, a 75% improvement.

Decision:
The expected near-pi resonant pulse should create a large negative feature in the second readout relative to the first readout. The data show a localized dip of the correct sign, near the expected contrast scale, centered within the scanned microwave-frequency range. Stored averages are not treated as a strong repeatability test, but both averages show the same central depression. I therefore decide that a pODMR resonance is present.
