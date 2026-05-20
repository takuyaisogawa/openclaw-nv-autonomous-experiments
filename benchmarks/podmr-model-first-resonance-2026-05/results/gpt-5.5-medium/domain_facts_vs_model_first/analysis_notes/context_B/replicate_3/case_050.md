Case: podmr_036_2026-05-16-211536

Sequence interpretation:
- The provided sequence XML is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active microwave pulse before the signal readout is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)`.
- `length_rabi_pulse = 52 ns` after sample-rate rounding at 250 MHz.
- `mod_depth = 1`.
- `full_expt = 0`, so the optional `m_S = +1` reference block is inactive.
- Readout 1 is the polarized `m_S = 0` reference detection immediately after `adj_polarize`.
- Readout 2 is the detection after the 52 ns modulated Rabi pulse.

Physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the expected on-resonance Rabi frequency here is 10 MHz.
- For a rectangular resonant pulse, the transferred population is
  `P = sin^2(pi * f_Rabi * t)`.
- With `f_Rabi = 10 MHz` and `t = 52 ns`, `P = sin^2(pi * 10e6 * 52e-9) = 0.996`.
- The expected fluorescence contrast between `m_S = 0` and `m_S = +1` is about 22%, so a real resonance should produce an on-resonance readout-2 reduction of approximately `0.22 * 0.996 = 21.9%` of the `m_S = 0` reference.
- The mean readout-1 level is 50.985, so the expected resonant drop is about `50.985 * 0.219 = 11.17` raw readout units.

Observed data:
- Mean readout 1: 50.985.
- Mean readout 2: 50.476.
- Mean difference readout2 - readout1: -0.509.
- Standard deviation of pointwise differences: 1.360.
- Largest observed negative difference is -2.788 at 3.920 GHz, only about 25% of the expected near-pi-pulse resonant drop.
- The largest positive difference is +3.481 at 3.840 GHz, comparable in magnitude to the largest negative excursion.
- Stored averages show broad tracking-level offsets and point scatter; they do not provide a strong independent repeatability test here.

Decision:
The active pulse should create a large, near-complete spin transfer at resonance and therefore an approximately 11-count drop in readout 2 relative to the `m_S = 0` reference. The measured scan only shows small, sign-changing fluctuations of a few counts without a resonance-shaped readout-2 dip of the expected size. I therefore decide that a pODMR resonance is absent.
