Case: podmr_002_2026-05-16-002114

Sequence interpretation from inputs/sequence.xml:

- Active sequence name from the export is Rabimodulated.xml, and the provided XML instructions implement the Rabimodulated pulse sequence.
- The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is the true mS = 0 reference: optical polarization, then detection, with no microwave pulse before it.
- Readout 2 is the pODMR signal readout: optical polarization has occurred earlier in the cycle, then a modulated Rabi microwave pulse is applied, then detection.
- mod_depth = 1 from the provided XML variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this rounds to 13 samples, so the effective pulse duration remains 52 ns.

Physical model calculation:

For a driven two-level transition, the population transferred by a rectangular pulse at detuning Delta is

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

where Omega = 2*pi*f_Rabi and Delta is angular detuning. The supplied setup facts give f_Rabi = 10 MHz at mod_depth = 1. With t = 52 ns,

Omega*t = 2*pi*10e6*52e-9 = 3.267 rad = 1.04*pi.

Thus the on-resonance transfer is sin^2(Omega*t/2) = 0.996. With a 22 percent mS=0 to mS=+1 contrast scale, the expected on-resonance fluorescence reduction is

0.22 * 0.996 = 0.219, or about 8.1 counts for a 37-count reference level.

Data comparison:

- Mean readout 1 is 37.23 counts.
- Readout 2 edge baseline, using the first and last five scan points, is 36.55 counts.
- Minimum readout 2 is 26.96 counts at 3.880 GHz.
- The observed dip from the edge baseline is 9.58 counts, a 26.2 percent reduction relative to the readout 2 edge baseline. This is close to the expected 8.1-count, 21.9 percent dip given calibration uncertainty and raw-count noise.
- Readout 1 does not show a corresponding dip at the same frequency; it stays in the mid/high 30s, consistent with a reference channel rather than common-mode tracking loss.

I also fit the two-level lineshape with f_Rabi fixed at 10 MHz, t fixed at 52 ns, and contrast fixed at 22 percent, allowing only the baseline scale and resonance center to vary. The best center is about 3.87725 GHz. The model sum of squared residuals for readout 2 is 26.2, versus 193.5 for a constant readout-2 null model and 209.1 for a model using only a constant ratio to readout 1. The largest residuals are at the scan edges and the deepest point, but the resonance-shaped dip is much closer to the data than the no-resonance alternatives.

Decision:

A pODMR resonance is present. The expected signal from the pulse sequence is a large near-pi-pulse fluorescence dip in readout 2 only, and the observed feature has the right channel, amplitude, and approximate width/center behavior.
