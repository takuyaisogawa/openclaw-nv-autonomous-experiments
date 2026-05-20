Case: podmr_011_2026-05-11-181506

Active sequence and readout roles:

The sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to
3.925 GHz in 5 MHz steps. The active instruction flow is:

1. adj_polarize
2. detection
3. wait
4. optional mS=+1 reference block, but this is skipped because full_expt = 0
5. rabi_pulse_mod_wait_time
6. detection
7. final wait

Therefore readout 1 is the post-polarization bright mS=0 reference, and readout
2 is the signal after the microwave Rabi pulse. The optional independent mS=+1
reference is inactive. Stored averages are not treated as independent
repeatability because they can reflect tracking cadence.

Sequence parameters used for the physical expectation:

- length_rabi_pulse = 52 ns
- mod_depth = 1 from inputs/sequence.xml
- contrast scale between mS=0 and mS=+1 = about 22 percent
- Rabi frequency at mod_depth = 1 = about 10 MHz

Quantitative model:

I used the standard rectangular-pulse two-level transition probability

P(+1) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * tau * sqrt(fR^2 + delta^2))

with fR = 10 MHz, tau = 52 ns, and delta = mw_freq - f0. The predicted
fluorescence ratio is

readout2/readout1 = scale * (1 - 0.22 * P(+1)).

On resonance, fR * tau = 0.52, so P(+1) = sin^2(pi * 0.52) = about 0.996.
The expected on-resonance fluorescence drop is therefore about 0.22 * 0.996 =
21.9 percent, relative to the bright reference.

Observed quantitative comparison:

The combined readout2/readout1 ratio reaches its minimum at 3.880 GHz:

- readout 1 = 21.346
- readout 2 = 16.981
- ratio = 0.7955
- fractional drop = 20.45 percent

This is close to the 21.9 percent expected from the sequence parameters and
setup contrast. A grid fit of the fixed-contrast Rabi model to the normalized
readout2/readout1 data gives a best center near 3.877 GHz, scale about 1.003,
SSE 0.0182 versus 0.0824 for a constant-ratio null model, corresponding to
R^2 about 0.78. Fitting the effective contrast depth gives about 22.9 percent,
also consistent with the stated contrast scale.

Decision:

The readout-2 dip is centered in frequency, has the expected magnitude for a
near-pi pulse at mod_depth = 1, and is quantitatively better described by the
Rabi resonance model than by a constant response. A pODMR resonance is present.
