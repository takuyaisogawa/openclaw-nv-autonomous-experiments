Active sequence and readout roles

The provided sequence is Rabimodulated.xml. The executed logic first performs optical polarization, then detection; because full_expt = 0, the conditional "Acquire 1 level reference" block is skipped. The final active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

followed by detection. Therefore readout 1 is the polarized m_S = 0 bright reference, and readout 2 is the signal after the fixed Rabi pulse while scanning mw_freq.

Relevant pulse parameters

sample_rate = 250 MHz, so the 52 ns pulse is exactly 13 samples and is not altered by rounding. mod_depth = 1. The pulse duration is length_rabi_pulse = 52 ns. The scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative signal model

Using the given calibration, the on-resonance Rabi frequency at mod_depth = 1 is approximately 10 MHz. For a square pulse, the population transferred to the darker m_S = +1 state is:

P(detuning) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau)

with Omega = 2*pi*10 MHz, delta = 2*pi*(mw_freq - f0), and tau = 52 ns.

On resonance:

P(0) = sin^2(pi * 10 MHz * 52 ns) = sin^2(1.6336) = 0.996.

With the setup contrast scale of about 22%, the expected on-resonance fluorescence reduction is:

0.22 * 0.996 = 0.219, or about 21.9%.

For a bright reference around 45 counts, the expected resonant readout is:

45 * (1 - 0.219) = 35.1 counts.

Comparison to the data

At 3.875 GHz, readout 1 is 45.404 and readout 2 is 34.173, a reduction of 11.231 counts, or 24.7% relative to readout 1. The off-resonant readout 2 baseline excluding points within +/-15 MHz of 3.875 GHz is about 43.706 counts. The dip is centered at 3.875 GHz and appears in both stored averages, though those averages mainly reflect tracking cadence rather than a strong independent repeatability test.

The explicit square-pulse model predicts a pronounced dip centered at 3.875 GHz with expected values near the observed shape: at zero detuning the model gives roughly 35.45 counts using the local readout-1 baseline, versus the observed 34.17 counts. A fixed-contrast model centered at 3.875 GHz gives a much smaller squared residual than a flat readout-2 model in this scan.

Decision

The observed centered fluorescence dip has the size and approximate lineshape expected from the active 52 ns, mod_depth = 1 Rabi pulse. A pODMR resonance is present.
