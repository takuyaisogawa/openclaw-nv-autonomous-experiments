Case: podmr_054_2026-05-17-043636

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The active scan sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the active instruction path, full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The two stored readouts therefore correspond to:

- readout 1: polarized mS = 0 fluorescence reference, acquired immediately after adj_polarize and detection.
- readout 2: fluorescence after the single rabi_pulse_mod_wait_time pulse and subsequent detection.

The pulse settings from the sequence variables are:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- sample_rate = 250 MHz, so the 52 ns pulse rounds to 13 samples and remains 52 ns

Quantitative expected signal model

The supplied setup facts give a contrast scale of about 22 percent between mS = 0 and mS = +1, and a Rabi frequency of about 10 MHz at mod_depth = 1. With the usual resonant Rabi population transfer model,

    P_transfer = sin^2(pi * f_Rabi * tau)

For f_Rabi = 10 MHz and tau = 52 ns:

    P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996057

The expected resonant fractional fluorescence change in readout 2 relative to the mS = 0 reference is therefore approximately:

    -0.22 * 0.996057 = -0.219133

The mean readout 1 level is 42.5174 counts, so a resonant point should show an expected depletion of:

    -0.219133 * 42.5174 = -9.3169 counts

Observed data calculation

Using the combined raw readouts, readout2 - readout1 has:

- mean difference: -0.2518 counts
- standard deviation across scan points: 1.1768 counts
- most negative point: -2.3269 counts at 3.840 GHz
- largest positive point: +2.3077 counts at 3.880 GHz
- mean fractional difference: -0.55 percent
- most negative fractional difference: -5.32 percent

This is far smaller than the expected near-resonant depletion of about -21.9 percent, or -9.3 counts at the observed reference level. Even under the weaker alternative implied by a mod_depth = 0.3 text value in the saved sequence string, the expected depletion would be about -4.87 percent, or -2.07 counts at the mean reference level; the combined data do not show a consistent resonance-shaped dip at that scale either, and stored averages mainly reflect tracking drift rather than independent repeatability.

Decision

No pODMR resonance is present. The post-pulse readout does not show the quantitatively expected resonant depletion for the active Rabimodulated pulse sequence.
