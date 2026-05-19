<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_007

Inputs inspected:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png

Active pulse sequence and readout roles:
- Sequence name from export: Rabimodulated.xml.
- The active instructions are:
  1. set microwave using mw_freq + detuning
  2. polarize
  3. detect the true m_S = 0 bright reference
  4. wait
  5. skip the "Acquire 1 level reference" branch because full_expt = 0
  6. apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth
  7. detect the pulsed readout
  8. wait length_last_wait
- Therefore readout 1 is the bright m_S = 0 reference before the microwave pulse, and readout 2 is the signal after the microwave Rabi pulse. The two readouts are not independent averages of the same observable and are not the skipped m_S = +1 reference.

Relevant XML parameters:
- vary_prop: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz.
- length_rabi_pulse = 52 ns. Rounding to the 250 MHz sample grid gives 13 samples, still 52 ns.
- mod_depth = 1 from the provided XML and the exported variable table.
- full_expt = 0, so the explicit 1-level reference branch is inactive.
- do_adiabatic_inversion is true, but the adiabatic inversion code is inside the inactive full_expt branch and commented alternatives; it is not active for the measured pulsed readout.

Quantitative model:
- Given domain fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- With mod_depth = 1, f_Rabi = 10 MHz.
- For a resonant square Rabi pulse, the transferred population is:
  P_1 = sin^2(pi * f_Rabi * t)
- For t = 52 ns:
  P_1 = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fractional drop in readout 2 relative to readout 1 is:
  0.22 * 0.9961 = 0.2191, or 21.9%.

Observed data calculation:
- The combined readouts have the deepest pulsed-readout dip at mw_freq = 3.880 GHz.
- At 3.880 GHz:
  readout 1 = 21.3462
  readout 2 = 16.9808
  fractional drop = 1 - 16.9808 / 21.3462 = 0.2045, or 20.5%.
- The model expectation at that paired reference level is:
  expected readout 2 = 21.3462 * (1 - 0.2191) = 16.6685.
- This is close to the observed 16.9808, within the level expected for this raw measurement.
- Off-resonance baseline points near the scan edges have readout 1 about 21.97 and readout 2 about 22.06, so the dip is not simply a global readout offset.

Decision:
The active pulse is approximately a pi pulse on resonance at the stated mod_depth, so a real resonance should produce a roughly 22% dip in readout 2 only. The data show a localized readout-2 dip of about 20.5% near 3.880 GHz while readout 1 remains comparatively near the bright reference level. Stored per-average traces show large tracking-like drift, so I do not treat them as strong independent repeatability evidence, but the combined paired-readout signal matches the quantitative Rabi/contrast model. I therefore decide that a pODMR resonance is present.
