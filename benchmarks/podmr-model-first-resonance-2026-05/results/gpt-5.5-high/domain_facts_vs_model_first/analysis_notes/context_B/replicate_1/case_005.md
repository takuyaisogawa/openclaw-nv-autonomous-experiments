Sequence interpretation:

The active sequence is Rabimodulated with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence XML and exported variable values give length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, and do_adiabatic_inversion = 1. Because full_expt is zero, the conditional "Acquire 1 level reference" block is skipped, so the adiabatic inversion and the extra 1-level reference are not active. The executed readout order is:

1. adj_polarize followed by detection: this is the bright m_S = 0 reference readout.
2. one rabi_pulse_mod_wait_time pulse followed by detection: this is the signal readout after the microwave pulse.

Thus readout 1 is the m_S = 0 reference and readout 2 is the post-pulse pODMR signal.

Quantitative model:

Using the stated setup calibration, f_Rabi = 10 MHz * mod_depth = 10 MHz. For a square pulse of duration t = 52 ns, the driven transition probability versus detuning Delta is modeled as

P(Delta) = (f_Rabi^2 / (f_Rabi^2 + Delta^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + Delta^2)).

On resonance, P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of 22%, an on-resonance signal readout should be lower than the bright reference by about 0.22 * 0.996 = 0.219, or about 4.4 counts for a 20-count readout level. This is the expected physical signal size for this active pulse.

Data check:

The combined readout means are readout 1 = 20.079 and readout 2 = 19.791. The pointwise signal/reference ratio has mean 0.9878, standard deviation 0.0553, and minimum 0.8815. The largest observed deficit is only about 11.9% or 2.5 counts at 3.840 GHz, much smaller than the modeled 21.9%/4.4-count pi-pulse response, and similar negative excursions appear at separated frequencies rather than as one coherent Rabi lineshape.

I fit the normalized ratio to a linear baseline plus the explicit Rabi response shape above while scanning the resonance center. The best unconstrained resonance-like fit gives amplitude A = 0.070 at 3.840 GHz, about one third of the expected 0.22 contrast. Forcing the physically expected A = 0.22 gives SSE = 0.0736, worse than the linear-only baseline SSE = 0.0550. Therefore the quantitative model expected for the active pulse is not supported by the data.

Decision:

The data do not show the expected pODMR resonance for this sequence. The observed readout differences are too small and too scattered compared with the expected 52 ns, mod_depth 1 pi-pulse contrast response, so I classify this case as resonance_absent.
