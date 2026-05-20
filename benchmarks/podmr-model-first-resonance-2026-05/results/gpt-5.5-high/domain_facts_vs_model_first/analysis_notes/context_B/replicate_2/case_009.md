Case: podmr_016_2026-05-12-120649

Inputs used: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles

The active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant XML instruction path is:

1. adj_polarize
2. detection
3. wait_for_awg
4. optional one-level reference block, skipped because full_expt = 0
5. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay)
6. detection

Therefore readout 1 is the bright m_S = 0 reference after optical polarization and before the swept Rabi pulse. Readout 2 is the signal after the swept microwave Rabi pulse. The stored averages are treated mainly as tracking-cadence views, not as a strong independent repeatability test.

Pulse parameters

sample_rate = 250 MHz. The pulse duration is length_rabi_pulse = 5.2e-8 s = 52 ns, which is exactly 13 samples after rounding. The active modulation depth is mod_depth = 1. With the supplied setup fact, the Rabi frequency is about 10 MHz at mod_depth = 1.

Quantitative physical expectation

For a square pulse on a two-level transition, I used the standard driven response

P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

where f_R = 10 MHz, tau = 52 ns, and delta is detuning in cycles/s. The optical readout model is

readout2 / readout1 = 1 - C * P_transfer(delta)

with contrast scale C = 0.22 between m_S = 0 and m_S = +1.

At resonance:

P_transfer(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996
expected depletion = 0.22 * 0.996 = 0.219
expected normalized resonant ratio = 0.781

Representative expected ratios:

delta = 0 MHz: 0.781
delta = 5 MHz: 0.835
delta = 10 MHz: 0.940
delta = 15 MHz: 0.997
delta = 20 MHz: 0.989

Data comparison

The combined readouts give:

mean readout1 = 25.734
mean readout2 = 26.168
mean readout2/readout1 = 1.017
minimum readout2/readout1 = 0.947 at 3.915 GHz

Thus the largest observed depletion relative to the local reference is only 5.3 percent. Relative to the mean normalized ratio, the largest negative excursion is about 7.0 percent. A true near-pi-pulse resonance in this sequence should produce about a 21.9 percent depletion, with the resonant point near readout2/readout1 = 0.78 after reference correction. The data never approach that level.

A least-squares scan over possible resonance centers using the fixed physical pulse model also fails qualitatively: the best model center would still require predicted normalized minima near 0.82, far below the observed minimum of 0.947. The visible variations are small compared with the expected resonant contrast and are entangled with readout drift/tracking.

Decision

No pODMR resonance is present in this scan.
