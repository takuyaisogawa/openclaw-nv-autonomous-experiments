Case: podmr_066_2026-05-17-072831

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML first performs optical polarization and a detection. This is readout 1, the ms=0 reference.
- full_expt is 0, so the optional ms=+1 reference block is skipped.
- The active microwave block is then rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is readout 2, the signal after the Rabi pulse.
- sample_rate = 250 MHz, length_rabi_pulse = 52 ns. The sequence rounds this to 13 samples, still 52 ns.
- mod_depth = 1.

Expected physical signal calculation:
- Given f_Rabi = 10 MHz at mod_depth = 1, the active pulse has f_Rabi = 10 MHz.
- For a square pulse, the transition probability versus detuning is
  P(delta) = f_Rabi^2 / (f_Rabi^2 + delta^2) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2)).
- With t = 52 ns:
  - P(0 MHz) = 0.996, so the pulse is essentially a pi pulse.
  - P(2.5 MHz) = 0.929.
  - P(5 MHz) = 0.749.
  - P(10 MHz) = 0.273.
- With a 22% ms=0 to ms=+1 contrast scale, the normalized readout-2/readout-1 signal should be approximately 1 - 0.22 * P(delta):
  - on resonance: 0.781, a 21.9% drop;
  - 2.5 MHz away: 0.796, a 20.4% drop;
  - 5 MHz away: 0.835, a 16.5% drop.
- Since the scan spacing is 5 MHz, a resonance inside the scanned range should put at least one sampled point within 2.5 MHz of resonance and should therefore produce a roughly 20% normalized dip.

Observed data:
- Mean readout 1 = 45.900; mean readout 2 = 45.369.
- The normalized ratio readout2/readout1 has mean 0.989 and standard deviation 0.035.
- The deepest combined-ratio point is 0.936 at 3.890 GHz, only a 6.4% drop from the local ms=0 reference.
- A square-pulse line-shape fit with free depth gives a best depth of about 6.5% to 7.2%, far below the expected 22% contrast-scale response for this pulse.
- A fixed-22%-contrast model centered on the shallow feature would predict ratios near 0.78 at the center and about 0.84 at adjacent 5 MHz points, much lower than the measured ratios near 0.94 to 0.97.

Decision:
The measured data do not contain the strong, broad dip required by the active 52 ns, mod_depth=1 pODMR pulse model. The shallow variations are not quantitatively consistent with the expected resonance response, so I classify this case as resonance_absent.
