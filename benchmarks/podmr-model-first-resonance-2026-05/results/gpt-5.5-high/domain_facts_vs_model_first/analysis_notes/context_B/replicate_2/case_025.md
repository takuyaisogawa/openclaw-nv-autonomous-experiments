Case: podmr_010_2026-05-16-114624

Sequence interpretation:
- The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the optional mS=+1 reference block is skipped.
- Readout 1 is the detection immediately after optical polarization, i.e. the mS=0 fluorescence reference.
- Readout 2 is the detection after the modulated Rabi microwave pulse, i.e. the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already on the 4 ns timing grid.

Quantitative expected-signal model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the 52 ns pulse is near a pi pulse.
- Using a square-pulse two-level model,
  P_transfer(df) = (Omega^2/(Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),
  where Omega = 2*pi*10 MHz, Delta = 2*pi*df, and t = 52 ns.
- On resonance this gives P_transfer(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of 22%, the expected on-resonance post-pulse fluorescence ratio is
  readout2/readout1 = 1 - 0.22 * 0.996 = 0.781, i.e. a 21.9% drop.
- The same model predicts ratios of about 0.835 at 5 MHz detuning and 0.940 at 10 MHz detuning, so a several-point dip is expected on this scan grid.

Observed data:
- The normalized readout2/readout1 ratio has a clear minimum at 3.875 GHz:
  3.865 GHz: 0.969
  3.870 GHz: 0.824
  3.875 GHz: 0.763
  3.880 GHz: 0.843
  3.885 GHz: 0.931
- The observed center drop is 1 - 0.763 = 23.7%, very close to the 21.9% expected from the near-pi-pulse model.
- Stored average 1 and average 2 both have their minimum ratio at 3.875 GHz, with ratios 0.727 and 0.788 respectively. These averages are not treated as a strong independent repeatability test, but they are consistent with the same feature.

Decision:
The dip in the post-pulse signal readout relative to the mS=0 reference has the expected amplitude and width for the active 52 ns, mod_depth 1 Rabi pulse. A pODMR resonance is present.
