<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_029

Sequence and readout roles

The provided sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV and detects immediately; this is the true m_S = 0 reference and corresponds to readout 1. Because full_expt = 0, the optional separate m_S = 1 reference block is inactive. The active signal block is a single rabi_pulse_mod_wait_time pulse followed by detection; this is readout 2. Thus the pODMR contrast should be assessed by comparing readout 2 against readout 1 at each microwave frequency.

Relevant sequence parameters

- active pulse sequence: Rabimodulated.xml
- mod_depth: 1
- microwave pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s, still 52 ns
- readout 1: post-polarization m_S = 0 fluorescence reference
- readout 2: fluorescence after the scanned microwave Rabi pulse

Physical model calculation

Using the stated setup calibration, the resonant Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular resonant pulse,

theta = 2*pi*f_R*t = 2*pi*(10e6 Hz)*(52e-9 s) = 3.267 rad = 187.2 degrees.

The expected spin transfer probability on resonance is

P = sin^2(theta/2) = sin^2(1.6336) = 0.996.

With a setup m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence drop is therefore

0.22 * 0.996 = 0.219, or about 21.9%.

Using the detuned rectangular-pulse model

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi*t*sqrt(f_R^2 + delta^2)),

the expected contrast drops around resonance for detunings of 0, +/-5 MHz, and +/-10 MHz are approximately 21.9%, 16.5%, and 6.0%, respectively. This predicts a resolved dip spanning several 5 MHz scan points.

Data comparison

The combined readouts show readout 1 approximately flat near 46-49 counts. Readout 2 has a strong localized dip:

- at 3.875 GHz: readout 1 = 48.538, readout 2 = 39.115, fractional drop = 19.4%
- at 3.880 GHz: readout 1 = 47.038, readout 2 = 39.558, fractional drop = 15.9%
- at 3.885 GHz: readout 1 = 48.712, readout 2 = 43.038, fractional drop = 11.6%

Using off-resonance points outside 3.870-3.885 GHz, the readout2/readout1 ratio baseline is 0.998 with standard deviation 0.025. The 3.875 GHz point has a ratio z-score of about -7.6 relative to this off-resonance baseline, and the difference readout2-readout1 has a z-score of about -7.9. The two stored averages both show the same central depression, but I treat that mainly as support for the combined trace because stored averages can reflect tracking cadence rather than a strong independent repeatability test.

Decision

The active sequence and pulse duration predict a large pODMR dip if a resonance is hit. The observed localized readout-2 suppression is quantitatively consistent with that prediction in amplitude and width. A pODMR resonance is present.
