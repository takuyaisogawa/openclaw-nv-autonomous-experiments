Case: podmr_060_2026-05-17-060259

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json numeric readouts only

Active pulse sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The sequence first polarizes the NV and performs a detection readout before any microwave pulse. This is the m_S = 0 reference readout, corresponding to readout 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive and no separate m_S = +1 reference is acquired.
- The active signal block applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), then performs detection. This is the microwave-pulse signal readout, corresponding to readout 2.
- From the provided XML / variable values: mod_depth = 1, sample_rate = 250 MHz, length_rabi_pulse = 52 ns. Rounding to samples gives round(52 ns * 250 MHz) = 13 samples, so the pulse remains 13 / 250 MHz = 52 ns.

Physical model calculation:
- Setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a square pulse, the excited-state transfer probability versus microwave detuning delta is modeled as:
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- With t = 52 ns and f_R = 10 MHz:
  P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
  Expected on-resonance readout-2 loss relative to readout 1 = C * P(0) = 0.219, about 21.9%.
- Since the scan step is 5 MHz, even if the resonance center fell halfway between sampled points, delta = 2.5 MHz at the nearest point:
  P(2.5 MHz) = 0.929, expected loss = 0.204, about 20.4%.
- At the observed readout-1 mean of 50.94 counts, the expected on-resonance loss is about 11.16 counts, and the worst half-step sampled loss is about 10.41 counts.

Observed quantitative comparison:
- Scan: 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Mean readout 1 = 50.943 counts.
- Mean readout 2 = 50.197 counts.
- Mean readout-2 minus readout-1 difference = -0.746 counts.
- Standard deviation of pointwise differences = 1.507 counts.
- Largest observed readout-2 deficit is -3.635 counts at 3.875 GHz, ratio readout2/readout1 = 0.931, i.e. only a 6.9% normalized drop.
- A resonant point under the active-pulse model should show approximately a 20% to 22% normalized drop, several times larger than the observed maximum deficit and much larger than the overall readout scatter.
- The plotted traces show no readout-2 dip of the modeled magnitude anywhere in the swept range.

Decision:
The expected pODMR signal for the active 52 ns, mod_depth = 1 pulse would be a large readout-2 suppression relative to the m_S = 0 reference. The measured readout differences remain at the few-count drift/noise scale and never approach the modeled approximately 10 to 11 count loss. I therefore decide that a pODMR resonance is absent in this scan.
