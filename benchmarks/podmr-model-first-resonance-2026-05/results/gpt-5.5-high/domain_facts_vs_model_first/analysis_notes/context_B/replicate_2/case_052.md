Case: podmr_038_2026-05-16-214551

Sequence inspection

The provided XML is Rabimodulated.xml. The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant active instruction block is:

1. adj_polarize, then detection: this is the bright m_S = 0 reference readout.
2. The "Acquire 1 level reference" block is skipped because full_expt = 0.
3. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detection: this is the pODMR signal readout after the microwave pulse.

The relevant pulse parameters from the provided sequence values are:

- mod_depth = 1
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns
- expected Rabi frequency = 10 MHz at mod_depth = 1

Physical model calculation

For a resonant square pulse, the population transferred from m_S = 0 to m_S = +1 is

P = sin^2(pi * f_Rabi * tau).

With f_Rabi = 10 MHz and tau = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the setup contrast scale of 22%, an on-resonance pODMR point should reduce the signal readout relative to the m_S = 0 reference by

0.22 * 0.996 = 0.219, or about 22%.

The mean reference readout is 46.57 counts, so the expected resonant drop is about 10.2 counts, giving an expected signal/reference ratio near 0.781 at exact resonance.

Because the scan step is 5 MHz, any resonance inside the scanned range should be within at most 2.5 MHz of one sampled point. Using the detuned square-pulse model

P(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),

with Omega = 2*pi*10 MHz and Delta = 2*pi*delta, the worst nearest-grid case at delta = 2.5 MHz still gives P = 0.929 and an expected signal/reference ratio of 1 - 0.22*0.929 = 0.796.

Data comparison

The combined readouts give:

- mean reference readout: 46.57
- mean post-pulse signal readout: 46.23
- mean signal/reference ratio: 0.993
- minimum signal/reference ratio: 0.940 at 3.845 GHz
- minimum signal-reference difference: -2.79 counts

The deepest observed reduction is only about 6.0%, or 2.79 counts, much smaller than the expected near-resonant reduction of about 20-22%, or about 10 counts. The two stored averages show drift and tracking-like offsets, so I do not treat them as a strong independent repeatability test. The normalized combined data do not contain the large dip required by the active pODMR pulse model.

Decision: resonance_absent.
