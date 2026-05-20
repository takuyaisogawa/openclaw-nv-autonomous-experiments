Sequence inspection:

- Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout role 1: after adj_polarize and before the swept Rabi pulse, so this is the true m_S = 0 reference.
- Readout role 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so this is the pODMR signal readout after the microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s but unchanged at 13 samples.

Physics/context check:

The provided setup has about 10 MHz Rabi frequency at mod_depth = 1, so a 52 ns pulse is close to a pi pulse. If the sweep crosses a real pODMR resonance, the second readout should move substantially toward the m_S = +1 brightness, with a contrast scale set by the roughly 22% m_S = 0 to m_S = +1 separation.

Data assessment:

The combined readouts differ by only a few raw-count units and cross smoothly over the scan. The largest separation is far below the expected near-pi-pulse contrast for this setup. The per-average overlay shows strong broad drift between the two stored averages: one average trends downward/upward while the other trends upward, and the stored averages are not a strong independent repeatability test because they often reflect tracking cadence. The apparent shape is therefore better explained by drift/cadence effects than by a localized resonance feature.

Decision: resonance absent.
