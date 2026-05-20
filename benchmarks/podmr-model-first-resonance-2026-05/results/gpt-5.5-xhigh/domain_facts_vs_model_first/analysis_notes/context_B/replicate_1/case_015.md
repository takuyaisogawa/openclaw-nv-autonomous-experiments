Case: podmr_034_2026-05-15-235221

Sequence/readout identification:
- The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active experiment has full_expt = 0, so the optional mS = +1 reference block is not executed.
- Readout 1 is the true mS = 0 bright reference: adj_polarize, detection, then wait.
- Readout 2 is the pODMR signal after the active rabi_pulse_mod_wait_time pulse, then detection.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse length remains 52 ns.
- mod_depth = 1. With the supplied setup relation, the Rabi frequency is about 10 MHz.

Physical model calculation:
I modeled the active microwave pulse as a square two-level Rabi pulse from mS = 0 to mS = +1. For detuning d in Hz, Rabi frequency f_R = 10 MHz, and pulse duration t = 52 ns,

P1(d) = (f_R^2 / (f_R^2 + d^2)) * sin(pi * t * sqrt(f_R^2 + d^2))^2.

The fluorescence model for readout 2 relative to the bright readout is

ratio(d) = a * (1 - C * P1(d)),

with C = 0.22 from the stated mS = 0 to mS = +1 contrast scale and a fitted constant scale factor for readout-role offsets.

On resonance, P1(0) = sin(pi * 10e6 * 52e-9)^2 = 0.996. The expected relative fluorescence is therefore 1 - 0.22 * 0.996 = 0.7809, corresponding to about a 7.6 count drop for a local bright readout near 34.6 counts.

Observed quantitative comparison:
- The readout-2/readout-1 ratio reaches its minimum at 3.880 GHz: 26.2885 / 34.8846 = 0.7536.
- At 3.875 GHz the ratio is 26.8077 / 34.2308 = 0.7831.
- The off-dip normalized ratio mean outside 3.865-3.885 GHz is 0.9774 with standard deviation 0.0377, so the deepest point is about 5.9 off-region standard deviations below the off-dip level.
- Fitting the fixed-contrast finite-pulse model over resonance center and scale gives best center 3.87575 GHz, scale a = 0.9863, SSE = 0.02747.
- A flat no-resonance ratio model gives SSE = 0.11996, about 4.37 times worse.
- Allowing the contrast to fit gives best center 3.87575 GHz and contrast 0.240, close to the expected 0.22.
- The two stored averages both contain the dip near the same frequency region, although I do not treat the two averages as a strong independent repeatability test because they may reflect tracking cadence.

Decision:
The active pulse is essentially a pi pulse at mod_depth = 1, so a real pODMR resonance should produce a near-full contrast dip. The measured second readout has a frequency-localized dip of the expected magnitude and width near 3.876 GHz while the first readout remains a bright reference. The model comparison and observed depth support resonance_present.
