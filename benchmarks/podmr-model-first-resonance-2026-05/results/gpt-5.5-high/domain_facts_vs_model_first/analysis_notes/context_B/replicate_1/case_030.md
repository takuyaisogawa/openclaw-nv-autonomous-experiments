Case podmr_015_2026-05-16-130043

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout 1 is the true m_S = 0 level reference acquired immediately after optical polarization.
- Readout 2 is acquired after the active Rabi-modulated microwave pulse and is the pODMR-sensitive readout.
- Active pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns.
- mod_depth = 1 from the provided sequence variable values, giving an expected Rabi frequency near 10 MHz.

Quantitative model:
Use the square-pulse two-level Rabi model for the microwave-prepared readout:

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

with Omega = 10 MHz * mod_depth = 10 MHz and t = 52 ns. On resonance,

P1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional PL reduction in readout 2 relative to readout 1 is

0.22 * 0.996 = 0.219,

corresponding to an expected readout2/readout1 ratio of about 0.781 on resonance.

Data comparison:
- The minimum measured combined readout2/readout1 ratio is 35.865 / 46.212 = 0.776 at 3.875 GHz.
- This is a 22.4% drop relative to the same-point readout 1, matching the 21.9% expected drop for a near-pi pulse at mod_depth = 1.
- Away from the central dip, excluding points within +/-10 MHz of 3.875 GHz, the mean readout2/readout1 ratio is 0.970 with standard deviation 0.027.
- The central dip therefore lies about 0.194 below the off-resonant mean ratio, far larger than the point-to-point off-resonant scatter.
- A square-pulse detuning model centered at 3.875 GHz predicts ratios of about 0.781 at resonance, about 0.835 at +/-5 MHz, and about 0.940 at +/-10 MHz, consistent with the observed broad central depression from 3.870 to 3.885 GHz.

Decision:
The observed microwave-prepared readout has the amplitude and frequency-localized shape expected from the relevant Rabi pulse model. The resonance is present.
