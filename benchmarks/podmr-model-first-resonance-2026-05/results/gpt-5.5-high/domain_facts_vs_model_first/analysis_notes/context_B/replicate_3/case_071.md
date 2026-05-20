Case: podmr_057_2026-05-17-051839

Input used:
- Provided sequence XML and raw_export.json only.
- No labels, sibling cases, previous outputs, or external context used.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active microwave operation after initialization is:
  PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)
  followed by detection.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Therefore readout 1 is the bright m_S = 0 reference immediately after optical polarization and before the Rabi pulse.
- Readout 2 is the post-Rabi-pulse signal readout.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is exactly 13 samples, so rounding does not change it.
- mod_depth = 1 from the variable values/provided XML.

Physical model:
- Given Rabi frequency at mod_depth = 1 is about 10 MHz and scales linearly with mod_depth, the active pulse has f_R = 10 MHz.
- Rectangular pulse transition probability versus detuning was modeled as:
  P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)
  with Omega = 2*pi*10 MHz and t = 52 ns.
- On resonance this is equivalently sin^2(pi*f_R*t) = sin^2(pi*10e6*52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected normalized fluorescence dip on resonance is 0.22*0.996 = 0.219, so the post-pulse signal/reference ratio should be about 0.781.
- The scan step is 5 MHz. If the resonance is halfway between sampled points, detuning is 2.5 MHz and the model still predicts P = 0.929, dip = 0.204, ratio = 0.796.
- At 5 MHz detuning the predicted ratio is 0.835. Thus a resonance in the scan range should make readout 2 far below readout 1 over at least one nearby point.

Data check:
- Scan range: 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Combined readout 1 mean = 45.455, readout 2 mean = 45.420.
- Mean readout2-readout1 difference = -0.035 counts, with no broad negative feature.
- Signal/reference ratio mean = 0.9993.
- Minimum observed signal/reference ratio is 0.955 at 3.925 GHz, corresponding to only a 4.5% dip.
- This is about one fifth of the expected on-resonance dip and much smaller than even the halfway-between-points expectation.
- Stored averages are only two averages and may reflect tracking cadence, so I used them only as a noise/consistency view, not as a strong repeatability test.

Decision:
- The active 52 ns, mod_depth 1 Rabi pulse should create an approximately 20-22% post-pulse fluorescence decrease at a pODMR resonance in this scan.
- The observed readout 2 trace stays essentially at the bright reference level with only small fluctuations.
- Therefore a pODMR resonance is absent in this measurement.
