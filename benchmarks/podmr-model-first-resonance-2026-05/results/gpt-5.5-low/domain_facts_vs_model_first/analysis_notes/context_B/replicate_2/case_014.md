Case podmr_033_2026-05-15-233800

I used the supplied sequence XML and raw export only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS=1 reference block is not active.
- The active detections are therefore:
  - readout 1: after adj_polarize, the true mS=0 bright reference.
  - readout 2: after the modulated Rabi microwave pulse, the signal readout.
- Active pulse parameters from Variable_values and sequence logic:
  - mod_depth = 1.
  - length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate to 52 ns.
  - microwave pulse call is rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...).

Physical model calculation:
- Given setup Rabi frequency at mod_depth 1 is about 10 MHz, and mod_depth is 1, use f_R = 10 MHz.
- Resonant Rabi transfer probability for a pulse of duration t is P = sin^2(pi f_R t).
- With t = 52 ns: P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between mS=0 and mS=+1 is about 22%, so the expected resonant fractional fluorescence drop is 0.22 * 0.996 = 0.219.
- Thus the expected resonant post-pulse/reference ratio is about 1 - 0.219 = 0.781.

Including detuning, I used:
P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * t),
with Omega = 10 MHz, t = 52 ns, and contrast C = 0.22, so model ratio = 1 - C * P(delta).

Near a center of 3.875 GHz, observed readout2/readout1 ratios and model ratios are:
- 3.860 GHz: observed 1.001, model 0.997
- 3.865 GHz: observed 0.943, model 0.940
- 3.870 GHz: observed 0.897, model 0.835
- 3.875 GHz: observed 0.749, model 0.781
- 3.880 GHz: observed 0.820, model 0.835
- 3.885 GHz: observed 0.911, model 0.940
- 3.890 GHz: observed 0.944, model 0.997

The combined readout 1 channel is comparatively flat around 38-40 counts, while readout 2 has a localized dip centered near 3.875 GHz. The minimum ratio, 0.749, corresponds to a 25.1% drop relative to readout 1, close to the expected 21.9% drop for a resonant near-pi pulse at this setup contrast. The two stored averages both show a depressed readout 2 point in the same resonance region, although the averages should mainly be treated as tracking cadence rather than independent repeatability.

Decision: resonance_present.
