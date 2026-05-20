Active sequence and readout roles

The provided sequence is Rabimodulated.xml. The active microwave manipulation is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

The readout block before this pulse is the true 0 level reference: polarize, detect, wait. Because full_expt = 0, the optional 1 level reference block is skipped. Therefore the two stored readouts are:

- readout 1: polarized m_S = 0 reference fluorescence.
- readout 2: fluorescence after the modulated Rabi pulse.

Sequence parameters used for the physical model:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s; 52 ns is already an integer number of samples.
- mod_depth = 1.
- setup Rabi frequency at mod_depth = 1: about 10 MHz.
- m_S = 0 to m_S = +1 contrast scale: about 22%.

Expected signal calculation

For a square resonant Rabi pulse starting in m_S = 0, using Rabi frequency f_R in cycles per second,

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

At resonance with f_R = 10 MHz and t = 52 ns:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected normalized fluorescence is therefore

F_signal / F_0 = 1 - 0.22 * 0.996 = 0.781,

or an expected contrast dip of 0.219 relative to readout 1.

The detuning-dependent model also gives a narrow feature on the scan scale:

- delta = 0 MHz: P_1 = 0.996, relative fluorescence = 0.781.
- delta = +/-5 MHz: P_1 = 0.749, relative fluorescence = 0.835.
- delta = +/-10 MHz: P_1 = 0.273, relative fluorescence = 0.940.
- delta = +/-15 MHz: P_1 = 0.012, relative fluorescence = 0.997.

Observed data calculation

Using readout 1 as the 0 reference, the normalized contrast 1 - readout2/readout1 has its maximum at scan value 3.875 GHz:

- readout 1 = 46.2115
- readout 2 = 35.8654
- readout2/readout1 = 0.776
- observed contrast = 0.224

This is essentially the expected 0.219 dip from a resonant near-pi pulse. Neighboring points also follow the expected broadened Rabi response: the contrast is 0.097 at 3.870 GHz, 0.180 at 3.880 GHz, and 0.126 at 3.885 GHz, then mostly returns toward the off-resonant level. A grid fit of the fixed 10 MHz, 52 ns, 22% contrast Rabi model to readout2 relative to readout1 gives best center about 3.8778 GHz and reduces squared error from 154.5 for a no-resonance proportional-reference model to 23.9.

The two stored averages both show the same central loss feature in readout 2, but I do not treat that as a strong independent repeatability test because stored averages can track cadence and drift. The primary decision is from the physical expected signal and the combined readout contrast.

Decision

A pODMR resonance is present. The measured central fluorescence loss has the amplitude and frequency-localized shape expected for a 52 ns near-pi pulse at mod_depth = 1 with a 22% contrast scale.
