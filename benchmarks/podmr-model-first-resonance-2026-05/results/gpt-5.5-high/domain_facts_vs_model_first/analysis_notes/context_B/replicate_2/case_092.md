Case: podmr_078_2026-05-17-102220
Timestamp: 2026-05-17-102220

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual cross-check of the same raw readout arrays

Active sequence interpretation

The provided XML is Rabimodulated.xml. The active instruction flow is:

1. adj_polarize(...)
2. detection(...)
3. wait_for_awg(...)
4. The optional "Acquire 1 level reference" block is skipped because full_expt = 0.
5. rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)
6. detection(...)
7. wait_for_awg(...)

Therefore readout 1 is the polarized m_S = 0 reference before the microwave pulse, and readout 2 is the signal after one modulated Rabi pulse. There is no separate m_S = +1 reference in the active sequence.

Relevant active parameters from the XML / exported variable values:
- vary_prop: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- length_rabi_pulse = 52 ns after sample-rate rounding
- mod_depth = 1
- full_expt = 0
- do_adiabatic_inversion is true in variables, but the adiabatic inversion calls are inside the skipped reference block or commented, so it is not active for the measured signal.

Physical model calculation

The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For this case, mod_depth = 1, so f_Rabi ~= 10 MHz.

For a rectangular resonant Rabi pulse, the transferred population is:

P_1(delta = 0) = sin^2(pi * f_Rabi * tau)

With tau = 52 ns and f_Rabi = 10 MHz:

P_1(0) = sin^2(pi * 10e6 * 52e-9)
       = sin^2(1.6336)
       ~= 0.996

The expected fluorescence depletion at resonance is therefore:

expected depletion ~= 0.22 * 0.996 = 0.219, or about 21.9%

At a baseline readout near 52 counts, an on-resonance point should put the post-pulse readout about 11.4 counts below the pre-pulse reference, before considering smaller detuned sidelobes from the finite pulse.

Data calculation

Using the two combined raw readout arrays from raw_export.json:

- mean(readout1) = 51.831 counts
- mean(readout2) = 51.760 counts
- mean(readout2 - readout1) = -0.071 counts
- standard deviation of readout2 - readout1 across frequency = 1.174 counts
- normalized depletion (readout1 - readout2) / readout1 ranges from -4.05% to +3.10%

The largest observed post-pulse depletion is at 3.905 GHz:

readout1 = 51.481
readout2 = 49.885
difference = -1.596 counts
normalized depletion = 3.10%

This is far below the approximately 21.9% depletion expected for a resonant 52 ns pulse at mod_depth = 1. The final scan point at 3.925 GHz, where a resonance at the scan edge would still be expected to produce about a 21.9% depletion under the on-resonance model, instead has readout2 higher than readout1 by about 3.0%.

Decision

The active measurement should show a large readout-2 dip relative to readout 1 at resonance. The observed readout differences are small, sign-changing, and compatible with drift/noise at the few-percent level rather than the expected approximately 22% resonant depletion. I therefore decide that a pODMR resonance is absent.
