Case: podmr_022_2026-05-16-172725

I used only the provided inputs for this case. The sequence is Rabimodulated.xml. The active instruction path has full_expt = 0, so the optional mS = +1 reference block is skipped. The two active detections are therefore:

1. Readout 1: after optical polarization, before the microwave pulse; this is the mS = 0 bright reference.
2. Readout 2: after one modulated Rabi microwave pulse; this is the pODMR signal readout.

Active pulse parameters from sequence.xml and the exported variable values:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- mw_freq scan = 3.825 GHz to 3.925 GHz in 5 MHz steps
- current setup Rabi frequency at mod_depth = 1 is about 10 MHz
- setup contrast between mS = 0 and mS = +1 is about 22%

Quantitative expected-signal model:

For a square resonant Rabi pulse, the transferred population is

P(+1) = sin^2(pi * f_Rabi * t).

With f_Rabi = 10 MHz and t = 52 ns,

f_Rabi * t = 0.52 cycles
P(+1) = sin^2(pi * 0.52) = 0.996.

The expected fractional fluorescence drop on resonance is therefore

contrast * P(+1) = 0.22 * 0.996 = 0.219.

The mean readout-1 level is 46.76 raw-count units, so an on-resonance point should produce approximately

46.76 * 0.219 = 10.25 raw-count units

of negative contrast in readout2 - readout1. Using the detuned square-pulse response,

P(detuning) = (f_Rabi^2 / (f_Rabi^2 + df^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + df^2)),

and sampling on the actual 5 MHz grid, a resonance whose center lies anywhere in the scanned range should still give a maximum sampled drop of about 9.56 to 10.25 raw-count units.

Observed paired data:

The combined readout2 - readout1 differences have mean +0.07, standard deviation 1.48, minimum -3.27, and maximum +2.21 raw-count units. The most negative fractional point is about -6.9%, far smaller than the approximately -21.9% signal expected for this pulse. The two stored averages do not show a repeatable large negative feature either; their difference traces have minima of -3.85 and -3.04 counts, consistent with tracking/noise-scale variation rather than the expected near-pi-pulse pODMR dip.

Conclusion:

The physically expected resonance signature for this pulse would be a large post-pulse readout decrease relative to the bright reference, of order 10 raw-count units at one or more scan points. The observed paired readout differences never approach that size and do not show a repeatable resonance-shaped negative feature. I therefore decide that a pODMR resonance is absent in this scan.
