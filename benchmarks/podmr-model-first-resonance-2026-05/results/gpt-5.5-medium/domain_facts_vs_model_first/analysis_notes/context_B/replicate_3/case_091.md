<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_091

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml / Rabi-modulated pODMR while sweeping mw_freq.
- Scan: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional +1 reference block is skipped.
- Readout roles:
  - readout 1 is the true m_S = 0 reference after polarization and before the microwave pulse.
  - readout 2 is the signal after a modulated Rabi microwave pulse and before the final wait.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth: 1 from the provided sequence XML and exported variable values.

Physical model calculation:

The provided setup facts say the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Therefore this sequence uses f_R = 10 MHz. For a resonant rectangular pulse, the transfer probability is

P_1 = sin^2(pi f_R t).

With t = 52 ns,

P_1 = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

Using the current m_S = 0 to m_S = +1 contrast scale of about 22%, a true resonance should reduce the signal readout by

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout 1 value is 50.936 counts, so the expected resonant signal readout is approximately

50.936 * (1 - 0.219) = 39.77 counts,

an expected drop of about 11.16 counts at resonance. A detuned rectangular-pulse model over the scan,

P_1(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz, also predicts an approximately 11.16 count maximum dip if the swept range crosses resonance.

Observed data:

- Mean readout 1: 50.936 counts.
- Mean readout 2: 50.769 counts.
- Mean signal-reference difference, readout2 - readout1: -0.167 counts.
- Standard deviation of readout2 - readout1 across scan points: 1.192 counts.
- Most negative observed readout2 - readout1 value: -2.192 counts, only a 4.2% drop.
- The largest apparent fractional drop is about 4.2%, far below the expected 21.9% resonant dip.
- The readout2 - readout1 differences change sign repeatedly and do not form the expected large ODMR-like depletion feature.

Stored averages are only two averages and may reflect tracking cadence, so I do not treat average-to-average consistency as a strong repeatability test. The combined readouts themselves are sufficient for this decision because the expected resonant signal is much larger than the observed deviations.

Decision: resonance absent.
