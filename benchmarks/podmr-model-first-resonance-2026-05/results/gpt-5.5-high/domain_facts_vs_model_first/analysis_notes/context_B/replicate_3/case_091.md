Case podmr_077_2026-05-17-100811

I used the provided sequence XML and raw export only.

Active sequence and readout roles:

- Sequence name in the export: Rabimodulated.xml.
- The instructions first polarize with the laser and immediately call detection. This is the active mS = 0 reference readout.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The sequence then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second active readout is the pODMR signal after the Rabi-modulated microwave pulse.
- Therefore readout 1 is the polarized mS = 0 reference and readout 2 is the post-pulse signal.

Relevant pulse parameters:

- mod_depth = 1 from inputs/sequence.xml and Variable_values in raw_export.json.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- sample_rate = 250 MHz, so the 52 ns pulse is rounded to 13 samples / 250 MHz = 52 ns.
- The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model:

The given setup has a Rabi frequency of about 10 MHz at mod_depth = 1. For a square resonant pulse, the transition probability is

P = sin^2(pi * f_R * t)

with f_R in cycles/s. With f_R = 10 MHz and t = 52 ns,

P_on = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated 22% mS = 0 to mS = +1 contrast and the measured reference level of about 50.94 raw counts, the expected on-resonance post-pulse readout change is

50.94 * 0.22 * 0.996 = 11.16 raw counts.

Thus a true resonance in this scan should make the post-pulse readout about 11 counts lower than the mS = 0 reference near resonance, modulo line-shape broadening. This is a large effect compared with the observed scatter.

Observed data check:

- Mean readout 1 = 50.936.
- Mean readout 2 = 50.769.
- Mean readout2 - readout1 = -0.167 raw counts.
- Standard deviation of readout2 - readout1 across scan points = 1.164 raw counts.
- Most negative readout2 - readout1 point = -2.192 raw counts.
- The readout2/readout1 ratio ranges from 0.958 to 1.053, so the largest observed relative drop is only about 4.2%, not the expected about 22%.
- A simple least-squares resonance-shaped dip model using the fixed 10 MHz, 52 ns pulse improves the post-pulse trace only with a best-fit amplitude of about 2.4 raw counts, far below the expected 11.2 raw counts and comparable to ordinary trace variation.

Decision:

The pulse should be almost a pi pulse at resonance, so the expected pODMR signal is much larger than the observed variations. The data do not show the required post-pulse depletion relative to the mS = 0 reference or a quantitatively consistent resonance-shaped dip. I therefore decide that a pODMR resonance is absent.
