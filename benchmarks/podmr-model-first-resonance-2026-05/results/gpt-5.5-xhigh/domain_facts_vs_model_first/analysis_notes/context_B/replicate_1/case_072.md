Case: podmr_058_2026-05-17-053345

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles

The active sequence is Rabimodulated.xml. The sequence first runs adj_polarize, then detection; the comment says this is the true 0 level reference. The optional 1 level reference block is inside "if abs(full_expt)>1e-12", but full_expt is 0, so that block is skipped. The second recorded readout is after:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);
PSeq = detection(PSeq,sample_rate,delay_wrt_1mus,ch_on);

Therefore readout 1 is the m_S=0 reference and readout 2 is the signal after the Rabi pulse. The pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse length is still 52 ns.

Quantitative expected-signal model

For a square resonant Rabi pulse, using the provided setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz. I modeled the driven transition probability versus detuning as

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),

where Omega = 10 MHz, delta is microwave detuning in Hz, and t = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the given contrast scale between m_S = 0 and m_S = +1 of 22%, a true resonance should lower readout 2 relative to readout 1 by about

0.22 * 0.996 = 0.219, or 21.9%.

The mean readout 1 level is 45.68 raw units, so the expected resonant drop is about 10.0 raw units. The scan step is 5 MHz, so even if the resonance lies halfway between two scan points, the nearest sampled detuning is 2.5 MHz and the model still predicts P = 0.929, or a 20.4% drop. At 5 MHz detuning the expected drop is still 16.5%.

Measured comparison

The measured combined traces give:

- readout 1 mean = 45.68, standard deviation = 0.96
- readout 2 mean = 45.58, standard deviation = 1.40
- readout 2 minus readout 1: mean = -0.10, minimum = -3.23, maximum = 3.04 raw units
- readout 2 / readout 1: mean = 0.998, standard deviation = 0.040, minimum = 0.931

Thus the largest observed normalized dip is only 6.9%, about 3.23 raw units, much smaller than the expected approximately 21.9% or 10 raw unit resonant drop. A least-squares fit of the finite-pulse Rabi line shape to readout2/readout1, allowing a linear baseline and arbitrary center frequency over the scanned range, gives a best-fit dip amplitude of 0.054, far below the expected 0.219. The baseline-only SSE is 0.0270; the free-amplitude finite-pulse model SSE is 0.0224; forcing the physically expected 0.219 dip amplitude worsens the SSE to 0.0660.

The per-average data show large vertical offsets consistent with tracking/cadence changes, so I did not treat the two stored averages as a strong independent repeatability test.

Decision

Given the active readout roles and the 52 ns, mod_depth 1 pulse, a real pODMR resonance should produce a large, broad negative feature in readout 2 relative to readout 1. The measured signal is near unity ratio with only small fluctuations and does not support the expected resonant response. I decide resonance_absent.
