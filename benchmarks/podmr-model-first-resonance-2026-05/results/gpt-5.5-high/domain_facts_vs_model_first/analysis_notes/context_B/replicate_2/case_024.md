Case: podmr_009_2026-05-16-113112

I used the provided sequence XML as the pulse sequence source. The active sequence is Rabimodulated.xml. Its active body first polarizes the NV and records a detection readout before any MW pulse; because full_expt = 0, the optional "1 level reference" block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and records the second detection readout. Therefore readout 1 is the true mS=0/reference readout and readout 2 is the MW-driven pODMR signal readout.

Relevant XML parameters:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- mw_freq is the scanned parameter, 3.825 GHz to 3.925 GHz in 5 MHz steps
- sample_rate = 250 MHz, so the 52 ns pulse is rounded to 13 samples and remains 52 ns

Expected signal model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse of duration t = 52 ns, the transition probability versus detuning df is

P(df) = (fR^2 / (fR^2 + df^2)) * sin^2(pi * t * sqrt(fR^2 + df^2)),

with fR = 10 MHz. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated 22 percent mS=0 to mS=+1 contrast scale, the expected resonant fluorescence drop is

0.22 * 0.996 = 0.219, or about 6.57 raw-count units for a 30-count reference level.

I then compared the data with this explicit model using readout2/readout1 so that the first readout serves as the local reference. A no-resonance constant ratio model has SSE = 0.1187 and RMS residual = 0.0752. A no-resonance linear baseline has SSE = 0.1115 and RMS residual = 0.0729. A fixed-contrast physical Rabi model with a linear baseline, allowing only the resonance center and baseline to fit, gives best center 3.87845 GHz, SSE = 0.02466, and RMS residual = 0.03427. A free-amplitude version gives a fitted dip amplitude of 0.230, close to the expected 0.219.

Near the fitted center the normalized signal falls from near unity to 0.773 at 3.875 GHz and 0.804 at 3.880 GHz. The absolute readout 2 minimum is 24.15 counts while readout 1 at the same point is 30.04 counts, a drop of about 5.9 counts, consistent with the predicted about 6.6-count resonant dip. The dip appears in the MW-driven readout, not as a comparable feature in the reference readout.

Decision: resonance_present.
