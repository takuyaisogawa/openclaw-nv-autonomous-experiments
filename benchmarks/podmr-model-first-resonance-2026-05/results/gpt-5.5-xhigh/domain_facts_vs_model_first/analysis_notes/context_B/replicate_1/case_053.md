Case: podmr_039_2026-05-16-221215

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification

The active sequence is Rabimodulated.xml, swept over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The supplied sequence XML sets sample_rate = 250 MHz, mod_depth = 1, length_rabi_pulse = 52 ns, full_expt = 0, and do_adiabatic_inversion = 1, but the adiabatic path is inside the skipped full_expt block.

Readout roles from the instructions:

1. adj_polarize, then detection: readout 1 is the true m_S = 0 reference.
2. The optional m_S = +1 reference block is skipped because full_expt = 0.
3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection: readout 2 is the signal after the microwave pulse.

The pulse is rounded to the 250 MHz sample clock. 52 ns is 13 samples, so the active pulse duration remains 52 ns.

Quantitative model

Use a two-level square-pulse model for the driven m_S = 0 to m_S = +1 transition. With detuning delta in Hz and Rabi frequency f_R in cycles/s,

P_transfer(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

The setup facts give f_R = 10 MHz * mod_depth = 10 MHz. With t = 52 ns:

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected normalized paired readout signal at resonance is

(readout2 - readout1) / readout1 = -0.22 * 0.996 = -0.219.

The mean readout 1 level is 49.348 raw counts, so an on-resonance point should drop by about 10.814 counts. Even 5 MHz off resonance, the model gives P_transfer = 0.749, or a predicted drop of about 8.130 counts.

Data comparison

Observed paired normalized differences (readout2 - readout1) / readout1 have mean -0.0026. The most negative point is -0.0491 at 3.850 GHz, corresponding to only -2.538 raw counts. No scan point shows the approximately -0.219 normalized contrast or approximately -10.8 raw-count drop expected for the active pulse.

I also swept the fixed-amplitude square-pulse model over possible resonance centers using a constant baseline offset. For mod_depth = 1, the best fixed 22% contrast resonance fit had SSE = 0.0669, while a baseline-only model had SSE = 0.0219. Thus the physically expected resonance worsens the fit by about a factor of 3.1. An unconstrained-amplitude fit preferred a positive amplitude rather than the required negative ODMR dip.

Conclusion

Given the active mod_depth = 1, 52 ns near-pi pulse and the 22% setup contrast, a real pODMR resonance in this scan would produce a large paired readout dip. The observed differences are small, inconsistent in sign, and not consistent with the expected square-pulse response. I decide resonance_absent.
