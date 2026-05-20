Sequence review:

- Active sequence: Rabimodulated-style pODMR sweep of mw_freq.
- full_expt is 0, so the optional mS=+1 reference block is skipped.
- Active readouts:
  - readout 1 is the true mS=0 level reference after optical polarization.
  - readout 2 is the signal after a modulated Rabi pulse and detection.
- mod_depth is 1 from the provided sequence XML / exported variable values.
- Rabi pulse duration is 52 ns, rounded at 250 MS/s but unchanged in practice.

Decision:

At mod_depth = 1, the setup Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse. If the microwave frequency crossed a real pODMR resonance, the post-pulse signal readout should show a substantial contrast change relative to the mS=0 reference, on the order of the known 22% scale for this setup. Instead, the two combined raw readouts differ by only a few counts at most on a roughly 49 count baseline, with sign changes and no stable resonance-like dip in the signal readout. The per-average traces also show large baseline offsets between averages, consistent with tracking cadence rather than independent repeatability of a spectral feature.

Conclusion: resonance_absent.
