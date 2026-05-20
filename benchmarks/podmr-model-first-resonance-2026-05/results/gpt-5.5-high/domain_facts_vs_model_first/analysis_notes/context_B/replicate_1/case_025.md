Case: podmr_010_2026-05-16-114624

Active sequence and readout roles:
- The provided XML is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes the NV and immediately performs detection. This is the true m_S = 0 optical reference, corresponding to readout 1.
- full_expt = 0, so the separate m_S = 1 reference block is skipped.
- The sequence then applies one rabi_pulse_mod_wait_time pulse and performs detection. This is the microwave-pulse readout, corresponding to readout 2.
- The active pulse duration is length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is exactly 13 samples after rounding.
- The provided XML sets mod_depth = 1, and I use mod_depth = 1 for the physical calculation.

Expected signal model:
- Given the stated calibration, the Rabi frequency is approximately 10 MHz at mod_depth = 1.
- For a square resonant pulse, the driven population transfer is P = sin^2(pi*f_R*t) when f_R is the Rabi oscillation frequency in cycles/s.
- With f_R = 10 MHz and t = 52 ns, f_R*t = 0.52 cycles, so P_res = sin^2(pi*0.52) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance optical drop in the pulse readout relative to the m_S = 0 reference is 0.22*0.996 = 0.219, or 21.9%.
- Off resonance I used the square-pulse two-level response:
  P(f) = (Omega^2/(Omega^2 + Delta^2))*sin^2(0.5*sqrt(Omega^2 + Delta^2)*t),
  with Omega = 2*pi*10 MHz, Delta = 2*pi*(f - f0), and t = 52 ns.

Data calculation:
- I normalized the microwave-pulse readout by the m_S = 0 reference using readout2/readout1, because readout 1 has a slow drift across the scan.
- The combined normalized ratio reaches its minimum at 3.875 GHz:
  readout1 = 40.903846, readout2 = 31.192308, ratio = 0.762576.
- This is a local fractional drop of 1 - 0.762576 = 0.237424, close to the 0.219 expected from the calibrated near-pi pulse.
- The neighboring points also form a localized dip: 0.823557 at 3.870 GHz, 0.762576 at 3.875 GHz, and 0.842983 at 3.880 GHz.
- The two stored averages both show their minimum normalized ratio at 3.875 GHz: about 0.7268 for average 1 and 0.7880 for average 2. I treat this only as support, since stored averages often reflect tracking cadence.

Model comparison:
- A no-resonance linear baseline fit to readout2/readout1 gives SSE = 0.09013.
- A fixed-contrast square-pulse resonance model with the calibrated 22% contrast, 10 MHz Rabi frequency, and 52 ns pulse gives best center f0 = 3.8752 GHz and SSE = 0.01342.
- Letting the contrast amplitude float gives A = 0.216, best center f0 = 3.8752 GHz, and SSE = 0.01339.
- The fitted free amplitude of 21.6% matches the independently expected 21.9% signal size.

Decision:
The frequency-localized drop in the pulse readout has the expected magnitude and width for the active 52 ns, mod_depth 1 Rabi pulse, while the reference readout mainly shows slow drift. I therefore decide that a pODMR resonance is present.
