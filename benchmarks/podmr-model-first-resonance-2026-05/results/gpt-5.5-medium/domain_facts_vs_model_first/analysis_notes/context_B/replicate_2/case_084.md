<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_084

Inputs used:
- sequence.xml and raw_export.json from this isolated workspace only.
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Pulse sequence roles from the XML instructions:
  - readout 1 is acquired immediately after adj_polarize and is the bright m_S = 0 reference.
  - full_expt = 0, so the optional m_S = +1 reference block is skipped.
  - readout 2 is acquired after rabi_pulse_mod_wait_time and is the pODMR signal readout.
- Relevant pulse settings:
  - length_rabi_pulse = 52 ns, rounded at 250 MS/s remains 52 ns.
  - mod_depth = 1 in the provided sequence XML and exported variable values.

Quantitative model:
- Given the supplied calibration, f_Rabi ~= 10 MHz at mod_depth = 1.
- For a rectangular resonant Rabi pulse, transferred population is
  P(detuning) = (f_Rabi^2 / (f_Rabi^2 + detuning^2)) *
                sin^2(pi * t * sqrt(f_Rabi^2 + detuning^2)).
- On resonance with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant normalized readout suppression is
  0.22 * 0.996 = 0.219, about 21.9%.
- The scan step is 5 MHz. Even if the true resonance were halfway between sampled points, the nearest sampled detuning would be 2.5 MHz, for which the model still predicts a suppression close to 20%, so a real resonance in the scanned range should be obvious across one or more adjacent points.

Observed data:
- Mean readout 1 = 50.710 counts, population standard deviation across scan points = 1.320.
- Mean readout 2 = 50.229 counts, population standard deviation across scan points = 1.649.
- The normalized suppression 1 - readout2/readout1 has mean 0.0094 and maximum 0.0387 at 3.885 GHz.
- The largest observed normalized suppression is therefore about 3.9%, roughly 18% of the expected 21.9% resonant contrast.
- Both readouts drift downward across the high-frequency end of the scan, indicating a common-mode/tracking trend rather than a strong selective microwave-induced dip.

Model comparison:
- A simple linear baseline for readout2/readout1 gives RMSE about 0.0213.
- A fixed-contrast physical Rabi-detuning model using the expected 22% contrast gives RMSE about 0.0398, worse than the baseline.
- Allowing the resonance amplitude to float gives a best amplitude of only about 0.0466, far below the expected 0.219 and consistent with small drift/noise-scale structure rather than a pODMR resonance.

Decision:
The expected physical signal for the active 52 ns, mod_depth 1 Rabi pulse is a roughly 22% suppression in readout 2 relative to the m_S = 0 reference. The measured normalized contrast never approaches that scale and is not better explained by the fixed expected resonance model than by baseline drift. I therefore classify this case as resonance_absent.
