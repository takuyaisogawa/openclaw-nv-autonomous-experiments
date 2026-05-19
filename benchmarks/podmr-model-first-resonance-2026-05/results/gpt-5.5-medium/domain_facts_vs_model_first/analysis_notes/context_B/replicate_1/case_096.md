<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_096

Input used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name in export: Rabimodulated.xml.
- The XML sets full_expt = 0, so the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion = 1.
- Active operations are: polarize, detection, wait, one rabi_pulse_mod_wait_time, detection, wait.
- Therefore readout 1 is the true mS=0 bright reference after polarization.
- readout 2 is the measurement readout after the microwave Rabi pulse.
- Pulse duration length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already an integer 13 samples, so rounding leaves 52 ns.
- mod_depth = 1 from inputs/sequence.xml and the exported Variable_values.

Physical model calculation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling, f_R = 10 MHz.
- For a square resonant Rabi pulse, transition probability P(+1) = sin^2(pi f_R t).
- With t = 52 ns, P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given the setup contrast between mS=0 and mS=+1 is about 22%, the expected resonant readout drop is 0.22 * 0.996 = 0.219 of the bright level.
- The measured bright reference is about 50.38 raw counts, giving an expected on-resonance drop of about 11.04 raw counts in readout 2 relative to readout 1.

Explicit comparison to data:
- The observed readout2 - readout1 differences have mean -0.35 counts and standard deviation 1.53 counts.
- The most negative observed point is -3.46 counts at 3.850 GHz, only about 31% of the expected resonant drop.
- A constrained dip model using the finite-pulse transition probability,
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  scanned over resonance centers near the sweep, gives best-fit dip amplitude about 1.91 counts near 3.90975 GHz.
- That fitted amplitude is far below the expected approximately 11 count resonant signal. If the expected-amplitude resonance were present, the minimum readout2 - readout1 would be near -11 counts, not the observed -3.46 counts.
- Stored averages are only two and may reflect tracking cadence, so I do not treat the per-average overlay as a strong repeatability test.

Decision:
No pODMR resonance is present. The active pulse should produce an almost full population transfer and a large raw-count dip on resonance, but the measured traces show only small fluctuations with no quantitatively compatible resonant contrast.
