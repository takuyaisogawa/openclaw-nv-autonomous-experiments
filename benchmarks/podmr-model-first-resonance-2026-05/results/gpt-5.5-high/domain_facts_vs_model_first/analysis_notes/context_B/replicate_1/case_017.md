Sequence interpretation:

I used inputs/sequence.xml as the sequence source. The active sequence is Rabimodulated.xml. With full_expt = 0, the conditional "Acquire 1 level reference" block is skipped, so the run has two active readouts:

1. readout 1: after adj_polarize, before the swept microwave pulse; this is the bright m_S = 0 reference.
2. readout 2: after a single rabi_pulse_mod_wait_time pulse, then detection; this is the pODMR signal readout.

The relevant active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1. The sample rate rounding leaves 52 ns unchanged because 52 ns is exactly 13 samples at 250 MHz.

Quantitative expected signal model:

Given the setup facts, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a square resonant Rabi pulse, the transferred population is

P_transfer(delta = 0) = sin^2(pi * f_Rabi * t)

Using f_Rabi = 10 MHz and t = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional fluorescence drop in readout 2 relative to the bright reference is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout 1 level is 37.23 counts, so the expected resonant drop is about

37.23 * 0.219 = 8.16 counts,

giving an expected resonant readout 2 level near 29.07 counts if the pulse is on resonance and the contrast calibration applies directly.

Data comparison:

The scan runs from 3.825 GHz to 3.925 GHz in 5 MHz steps. Readout 1 stays in the mid/high 30 count range and does not show a comparably deep local dip. Readout 2 has a localized minimum at 3.880 GHz:

- readout 1 at 3.880 GHz: 38.12
- readout 2 at 3.880 GHz: 26.96
- observed drop: 11.15 counts
- observed ratio readout2/readout1: 0.707

The off-resonant edge mean ratio readout2/readout1 is about 0.979, so the observed localized contrast relative to the off-resonant signal is about 27%. A fixed-contrast Rabi lineshape calculation using f_Rabi = 10 MHz, t = 52 ns, and contrast = 22% gives a best center near 3.8774 GHz. Allowing the contrast amplitude to float gives the same center and an amplitude of about 25.3%, close to the expected 21.9% given the sparse 5 MHz sampling and raw-count noise.

Stored averages should not be treated as a strong independent repeatability test because they can reflect tracking cadence. Still, both stored averages show the same readout-2 depression in the 3.875-3.880 GHz region, while readout 1 remains a reference-like trace.

Decision:

The active pulse is essentially a pi pulse at the stated mod_depth, and the expected pODMR signal is a roughly 22% fluorescence drop in the post-pulse readout. The measured readout 2 contains a localized dip of the expected order and width near 3.88 GHz. I therefore decide that a pODMR resonance is present.
