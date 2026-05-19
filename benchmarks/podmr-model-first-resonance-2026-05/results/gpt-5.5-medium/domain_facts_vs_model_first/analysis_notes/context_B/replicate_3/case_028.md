<!-- Model-generated analysis note. Not a ground-truth label. -->

Sequence inspection

The provided sequence is Rabimodulated.xml / SequenceName Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence polarizes into the bright m_S = 0 state, takes a first detection readout, waits, applies one modulated Rabi pulse, then takes the second detection readout. full_expt = 0, so the conditional m_S = +1 reference branch is not executed. Therefore readout 1 is the bright m_S = 0 reference and readout 2 is the pODMR signal after the microwave pulse.

The relevant pulse parameters are:

- mod_depth = 1
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns
- setup Rabi frequency at mod_depth = 1 is about 10 MHz
- setup contrast between m_S = 0 and m_S = +1 is about 22%

Quantitative model calculation

For resonant drive, use the two-level Rabi transfer probability

P_transfer = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10 MHz and tau = 52 ns. This gives:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996

The expected fractional fluorescence dip on resonance is therefore approximately:

contrast * P_transfer = 0.22 * 0.996 = 0.219

Using the observed readout 2 off-resonance baseline excluding the dip window, about 42.96 raw units, the expected resonant dip is:

0.219 * 42.96 = 9.41 raw units

Data comparison

Readout 2 has a baseline near 42.96 raw units and reaches a minimum of 34.08 raw units at 3.880 GHz, an observed dip of 8.88 raw units or 20.7%. This is very close to the 21.9% expected from the physical model for a near-pi pulse at mod_depth = 1.

Readout 1, the m_S = 0 reference, does not show the corresponding dip in the same frequency window; its values there remain around 43.06 to 44.48 raw units. The per-average traces show the same qualitative feature in readout 2, but the averages are not treated as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision

The observed readout 2 dip matches the predicted resonant transfer amplitude for the active 52 ns, mod_depth = 1 pODMR pulse, while the reference readout remains flat. I decide that a pODMR resonance is present.
