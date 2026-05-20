Case podmr_037_2026-05-16-213011

Inputs used only from this isolated workspace: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles

The exported scan identifies SequenceName = Rabimodulated.xml and the scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence instructions are:

1. adj_polarize for optical initialization.
2. detection immediately after initialization: this is the true m_S = 0 reference readout.
3. wait_for_awg.
4. The optional "Acquire 1 level reference" block is skipped because full_expt = 0.
5. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
6. detection after the microwave pulse: this is the pODMR signal readout.

The relevant active parameters are:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so the 52 ns pulse is rounded to 13 samples and remains 52 ns
- readout 1 = m_S = 0 reference
- readout 2 = post-microwave pODMR signal

Quantitative expected-signal model

The provided domain facts say the Rabi frequency is about 10 MHz at mod_depth = 1 and scales approximately linearly with mod_depth. For a resonant square pulse, the transferred population is:

P_1 = sin^2(pi * f_Rabi * tau)

With f_Rabi = 10 MHz and tau = 52 ns:

pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 0.52*pi
P_1 = sin^2(0.52*pi) = 0.996

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance microwave transition should reduce the post-pulse signal readout relative to the m_S = 0 reference by approximately:

0.996 * 22% = 21.9%

Thus, if a pODMR resonance is present at one of the scan points, readout 2 should show an about 22% dip relative to readout 1 near resonance. Since the reference level is about 47.6 counts, the expected resonant drop is roughly 10.4 counts. Even allowing substantial experimental scatter, the signature should be a large negative signal-reference contrast, not a few percent fluctuation.

Observed data

Combined readout means:

- readout 1 reference mean = 47.629
- readout 2 signal mean = 47.929
- mean(readout1 - readout2) = -0.299 counts
- standard deviation of readout1 - readout2 across scan points = 1.323 counts
- largest absolute pointwise readout1 - readout2 difference = 2.808 counts

Fractional contrast, computed as (readout1 - readout2) / average(readout1, readout2):

- mean = -0.0064
- standard deviation = 0.0278
- minimum = -0.0601
- maximum = 0.0447

The expected resonance sign for this sequence is readout2 below readout1, i.e. positive (readout1 - readout2), with about 0.219 fractional contrast. The observed positive contrasts never exceed 0.045, about one fifth of the expected resonant contrast. The largest deviations are of the opposite sign, where readout2 is higher than the reference. Stored averages are not treated as strong independent repeatability evidence because the prompt notes that they often reflect tracking cadence.

Decision

The active pulse is essentially a pi pulse at mod_depth = 1, so a real pODMR resonance should produce a strong approximately 22% signal dip in readout 2 relative to the readout 1 reference. The observed signal-reference contrast is small, inconsistent in sign, and far below the expected physical response. I therefore decide that a pODMR resonance is absent.
