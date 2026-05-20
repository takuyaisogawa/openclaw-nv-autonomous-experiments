Case: podmr_008_2026-05-16-014743

Sequence inspection:
- Provided sequence file: Rabimodulated.xml.
- Active scan variable: mw_freq, from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active detections are:
  1. Readout 1: after optical polarization, before the scanned microwave pulse. This is the m_S = 0 bright reference / common-mode monitor.
  2. Readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection. This is the pODMR-sensitive readout.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.

Quantitative physical model:
The stated setup gives a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. Therefore this sequence applies approximately a 10 MHz, 52 ns pulse at each scanned microwave frequency. On resonance, the driven two-level transfer probability is

P = sin^2(theta/2), with theta = 2*pi*f_R*tau.

Using f_R = 10 MHz and tau = 52 ns:

theta = 2*pi*10e6*52e-9 = 3.267 rad.
P = sin^2(3.267/2) = 0.996.

Thus the active pulse is effectively a pi pulse on resonance. With the given m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence dip in readout 2 is approximately 0.22*0.996 = 21.9% of the local bright level. Using the observed off-resonance readout-2 mean outside +/-15 MHz of the dip center, 40.92 counts, the expected dip depth is:

0.22 * 0.996 * 40.92 = 8.97 counts.

Observed data:
- Minimum readout 2 occurs at 3.875 GHz: 31.31 counts.
- Off-resonance readout-2 mean outside +/-15 MHz of 3.875 GHz: 40.92 counts.
- Observed drop: 40.92 - 31.31 = 9.61 counts, or 23.5%.
- Readout 1 at the same point is 42.46 counts and does not show a matching common-mode collapse.

The measured dip amplitude and width are consistent with the expected near-pi-pulse pODMR signal for this sequence. The per-average overlays show the same feature, but I treat that only as a tracking-cadence consistency check rather than strong independent repeatability evidence.

Decision: resonance_present.
