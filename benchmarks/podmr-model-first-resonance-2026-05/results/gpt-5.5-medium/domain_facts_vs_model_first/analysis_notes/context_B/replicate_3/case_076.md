<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_076

Input basis:
- Used only inputs/sequence.xml and inputs/raw_export.json from this workspace.
- SequenceName in the raw export is Rabimodulated.xml; the supplied XML instructions implement the Rabimodulated pulse sequence.

Active pulse sequence and readout roles:
- The sequence first performs optical polarization with adj_polarize(...), then immediately calls detection(...). This first stored readout is therefore the bright m_S = 0 reference/readout.
- full_expt = 0, so the optional explicit m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection(...). This second stored readout is the pODMR signal after the microwave pulse.

Pulse parameters from the supplied XML:
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- swept variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model:
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore Omega_R = 10 MHz for this sequence.
- For a square resonant pulse, the transferred population is modeled as P(Delta) = Omega_R^2/(Omega_R^2 + Delta^2) * sin^2(pi * t * sqrt(Omega_R^2 + Delta^2)), using Hz units for Omega_R and detuning.
- At Delta = 0 and t = 52 ns: P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pulse should reduce the signal readout by about 0.22 * 0.996 = 21.9% of the bright level.
- The measured bright/reference readout mean is 49.41 counts, so the expected on-resonance drop is about 10.83 counts.
- Model drops at representative detunings using the same parameters:
  - 0 MHz: 10.83 counts
  - 2.5 MHz: 10.10 counts
  - 5 MHz: 8.14 counts
  - 10 MHz: 2.97 counts
  - 20 MHz: 0.52 counts
  - 50 MHz: 0.33 counts

Observed data comparison:
- Combined readout 1 mean/std/min/max: 49.41 / 1.15 / 46.98 / 51.23 counts.
- Combined readout 2 mean/std/min/max: 49.44 / 0.87 / 47.25 / 50.87 counts.
- Signal minus reference, readout2 - readout1, mean/std/min/max: 0.033 / 1.22 / -3.15 / 2.33 counts.
- The strongest negative signal-reference point is -3.15 counts, far smaller than the approximately -10.8 count on-resonance expectation and not part of a broad resonance-shaped suppression.
- Stored averages differ substantially in baseline and shape, consistent with the warning that averages often track cadence rather than independent repeatability; they do not show a robust 22% microwave-induced contrast feature.

Decision:
- A true pODMR resonance under this sequence should be a large signal-readout suppression relative to the preceding m_S = 0 reference, because the 52 ns mod_depth 1 pulse is essentially a pi pulse on resonance.
- The observed two-readout comparison remains near zero and within small tracking/noise variations across the sweep.
- Prediction: resonance_absent.
