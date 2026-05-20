Case: podmr_039_2026-05-16-221215

Inputs inspected: inputs/sequence.xml and inputs/raw_export.json.

Active pulse sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active sequence first polarizes and detects the true m_S = 0 reference, then applies one rabi_pulse_mod_wait_time pulse and detects again.
- Therefore readout 1 is the pre-microwave m_S = 0 reference, and readout 2 is the post-microwave signal readout. It is not an independently acquired m_S = +1 reference.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 from the provided sequence XML and exported variable values.

Quantitative expected-signal model:
- Given f_Rabi ~= 10 MHz at mod_depth = 1, the square-pulse rotation angle on resonance is theta = 2*pi*f_Rabi*t = 2*pi*10e6*52e-9 = 3.27 rad, close to a pi pulse.
- Excited-state transfer probability on resonance is P = sin^2(theta/2) = sin^2(pi*10e6*52e-9) = 0.996.
- The mean pre-pulse readout is 49.35 counts. With the stated setup contrast of 22%, a full m_S = 0 to m_S = +1 transfer should reduce the post-pulse readout by 0.22 * 49.35 * 0.996 = 10.81 counts at resonance.
- More generally I used the square-pulse detuning response
  P(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi*t*sqrt(f_R^2 + delta^2))
  and fit readout2 = offset - A*P(mw_freq - f0) over resonance centers across the scan range.
- The best fit gives f0 = 3.915 GHz, A = 2.97 counts, offset = 49.69 counts, with max P = 0.996. The fitted depth is only 27% of the expected physical amplitude of 0.22 * 49.35 = 10.86 counts.

Data check:
- readout1 mean = 49.35 counts, population SD = 1.33 counts.
- readout2 mean = 49.19 counts, population SD = 1.25 counts.
- The largest local readout2 deficits relative to readout1 are about 2.3 to 2.5 counts, much smaller than the expected approximately 10.8 count near-pi-pulse resonance signature.
- The two stored averages show noticeable tracking-scale variation, so I did not treat the averages as a strong independent repeatability test.

Decision:
The observed post-pulse readout does not show the expected near-pi-pulse pODMR contrast. Any shallow downward trend near the high-frequency edge is too small compared with the quantitative physical expectation. I classify this case as resonance_absent.
