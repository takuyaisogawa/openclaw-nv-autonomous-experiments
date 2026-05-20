I used the provided sequence XML and the raw export values for the scan and readouts.

Active pulse sequence: Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave pulse is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on)

with length_rabi_pulse = 52 ns and mod_depth = 1. The sample rate is 250 MHz, so the 52 ns pulse is already exactly 13 samples after rounding. full_expt = 0, so the optional m_S = +1 reference block is skipped.

Readout roles from the instruction order:

1. readout 1 is the true m_S = 0 bright reference, acquired immediately after optical polarization and before the microwave Rabi pulse.
2. readout 2 is the post-Rabi signal readout, acquired after the 52 ns modulated microwave pulse.

Thus a pODMR resonance should appear as readout 2 dropping below readout 1 at the resonant scan frequency.

Quantitative physical model:

The given setup has Rabi frequency about 10 MHz at mod_depth = 1, approximately linear with mod_depth. Therefore f_R = 10 MHz here. For a square resonant pulse, the transferred population is

P(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

At delta = 0 and t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.9961.

Using the stated optical contrast scale C = 0.22, the expected normalized resonant signal is

readout2/readout1 = 1 - C * P(0) = 1 - 0.22 * 0.9961 = 0.7809.

So an on-resonance point should show about a 21.9% drop in readout 2 relative to readout 1, roughly 11 raw-count units for a 50-count reference. The off-resonant pulse-response model still predicts large nearby dips: at detunings of 5 MHz and 10 MHz, the expected drops are about 16.5% and 6.0%, respectively.

Observed normalized readout2/readout1 ratios across the 21 scan points:

mean = 0.9975
standard deviation = 0.0236
minimum = 0.9509 at 3.830 GHz
maximum = 1.0480

The largest observed drop is only 4.9%, about one quarter of the expected resonant drop and not close to the 0.7809 resonant ratio. At 3.875 GHz, the normalized ratio is 0.9740, only a 2.6% drop.

I also simulated the pulse-response line shape over possible resonance centers and fit readout2/readout1 with a linear baseline plus a nonnegative dip amplitude. The best nonnegative fitted dip amplitude was about 0.038, while the expected amplitude from the physical model is 0.219. A fixed-amplitude 0.219 model does not match the measured trace; it would require a much deeper and more coherent dip than is present.

The per-average overlays are not treated as a strong independent repeatability test because stored averages can reflect tracking cadence, but they also do not show a stable, model-sized dip at one frequency. The data are dominated by common drift and shallow point-to-point fluctuations rather than the expected post-Rabi pODMR contrast.

Decision: resonance_absent.
