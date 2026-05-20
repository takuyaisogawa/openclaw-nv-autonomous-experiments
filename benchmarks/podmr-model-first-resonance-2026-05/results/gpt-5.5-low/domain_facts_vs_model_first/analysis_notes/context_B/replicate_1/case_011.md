Case podmr_028_2026-05-13-100213

Active sequence and readout roles

The provided sequence is Rabimodulated.xml / Rabimodulated. The instructions first polarize and detect, then conditionally acquire a 1-level reference only if full_expt is nonzero. Here full_expt = 0, so that conditional block is inactive. The two acquired readouts are therefore:

- readout 1: true m_S = 0 optical reference after adj_polarize and detection, without the Rabi microwave pulse.
- readout 2: signal readout after the active rabi_pulse_mod_wait_time pulse.

The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), with length_rabi_pulse = 52 ns, mod_depth = 1, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps, and sample_rate = 250 MHz. The pulse length rounds to 52 ns at this sample rate.

Quantitative expected signal model

Using the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the transferred population is

P(delta=0) = sin^2(pi * f_Rabi * t)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

With the current m_S = 0 to m_S = +1 fluorescence contrast scale of about 22%, an on-resonance pulse should reduce the signal readout by about 0.22 * 0.996 = 0.219, i.e. about 21.9% of the local bright-state reference. The observed mean readout 1 level is 27.69 counts, giving a nominal full expected dip of about 6.07 counts if the measured contrast is fully expressed in this sequence.

I also used the detuned square-pulse transition probability

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * t)

with Omega = 10 MHz and t = 52 ns. Fitting readout 2 to a linear baseline plus a negative scaled P(delta) feature over possible resonance centers gave the best center near 3.9035 GHz. The fitted dip scale was about 2.90 counts, smaller than the nominal 6.09-count contrast expectation but in the same sign and localized frequency range. A smooth baseline-only fit had SSE 35.98, while the square-pulse resonance model had SSE 25.09, an improvement of 10.89 SSE units.

Data check

readout 1 mean = 27.69 counts, standard deviation across scan points = 0.88 counts.
readout 2 mean = 27.25 counts, standard deviation across scan points = 1.43 counts.
The largest readout2-readout1 deficit is -3.50 counts at 3.905 GHz, and the smallest readout2/readout1 ratio is 0.873 at 3.905 GHz. The adjacent points around 3.900 to 3.910 GHz are also depressed relative to the high-frequency and low-frequency baseline behavior, consistent with a resonance-like feature broadened/sampled by the 52 ns pulse model.

Decision

A pODMR resonance is present. The contrast is weaker than the simple 22% full-transfer estimate, so the confidence should not be treated as high, but the active sequence readout roles and the quantitative square-pulse calculation support a real resonance-like dip near 3.904-3.905 GHz rather than a purely qualitative or label-based decision.
