Case: podmr_004_2026-05-10-171142

Sequence interpretation

The provided sequence XML is the Rabimodulated pulse sequence. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction flow is:

1. adj_polarize
2. detection
3. wait_for_awg
4. skip the "Acquire 1 level reference" branch because full_expt = 0
5. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth)
6. detection
7. wait_for_awg

Therefore readout 1 is the true mS = 0 bright reference acquired before the microwave pulse, and readout 2 is the pODMR readout after the modulated Rabi pulse. The active pulse duration is length_rabi_pulse = 52 ns. The exported variable values and the provided sequence.xml both give mod_depth = 1. The embedded saved XML text in raw_export contains a stale-looking default line with mod_depth = 0.3, but the prompt asks to use the provided sequence XML and the exported Variable_values list also reports mod_depth = 1, so I use mod_depth = 1 for the decision.

Quantitative model

For a square resonant Rabi pulse, using the stated setup relation f_Rabi = 10 MHz at mod_depth = 1,

P_transfer(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2*pi*10 MHz, Delta = 2*pi*(f - f0), and t = 52 ns.

At resonance:

Omega*t = 2*pi*10e6*52e-9 = 3.267 rad
P_transfer(0) = sin^2(Omega*t/2) = 0.996

The stated mS = 0 to mS = +1 contrast is about 22%, so a real resonance should make readout 2 darker than readout 1 by approximately

0.22 * 0.996 = 0.219 of the bright reference.

The observed readout 1 mean is 43.68 raw counts, so the expected on-resonance dip in readout 2 relative to readout 1 is about

43.68 * 0.219 = 9.57 counts.

Data comparison

Using readout2 - readout1 across the 21 scan points:

mean = +0.57 counts
standard deviation = 1.74 counts
minimum = -2.46 counts at 3.855 GHz
maximum = +3.96 counts at 3.915 GHz

Thus the largest observed darkening is only about 5.7% of the bright reference, far below the expected about 21.9% darkening for a resonant 52 ns pulse at mod_depth = 1. Most of the trace is not darker after the pulse; readout 2 is slightly brighter on average.

I also compared the observed readout difference to the square-pulse Rabi line shape over possible resonance centers at the sampled frequencies. With the physical amplitude fixed by the 22% contrast and mod_depth = 1, the best model including a constant offset had SSE = 139.85, while a constant no-resonance model had SSE = 60.42. Allowing the model amplitude to float gave the best fit at 3.910 GHz with beta = -0.267, meaning the data preferred the opposite sign of the expected dark resonance there.

Decision

The physically expected pODMR resonance would be a large negative feature in readout 2 relative to the mS = 0 reference. The observed data do not show the expected sign, amplitude, or model fit improvement. Stored averages show baseline/tracking changes and are not a strong independent repeatability test. I decide that a pODMR resonance is absent.
