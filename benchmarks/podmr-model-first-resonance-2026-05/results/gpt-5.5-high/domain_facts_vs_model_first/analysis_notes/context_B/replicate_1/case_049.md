Case podmr_035_2026-05-16-210045

I used the provided sequence XML and the raw export only for the measured scan values. The active sequence is Rabimodulated.xml. The executable instructions first polarize and detect the bright m_S = 0 reference, skip the optional m_S = 1 reference because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and detect again. Therefore readout 1 is the polarized reference and readout 2 is the post-microwave pODMR signal readout.

Active pulse settings from the sequence are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With the stated setup calibration, f_Rabi = 10 MHz at mod_depth 1. The expected resonant population transfer for a square Rabi pulse is:

P_transfer = sin^2(pi * f_Rabi * tau)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, a true resonance under these pulse settings should reduce the normalized post-pulse readout by approximately:

0.22 * 0.996 = 0.219, or 21.9%.

Thus the expected readout2/readout1 ratio at resonance is about 0.781. For a typical reference level near 50 raw-count units, this corresponds to a dip of about 11 raw-count units.

Measured combined readouts:
- readout2/readout1 ratio range: 0.943 to 1.022
- mean ratio: 0.983
- ratio standard deviation across scan points: 0.0205
- raw readout2 - readout1 range: -2.81 to +1.06

The deepest observed normalized point is at 3.830 GHz with ratio 0.943, only a 5.7% decrease. A simple Lorentzian dip fit constrained to the expected 21.9% resonant depth gives a worse fit than a nearly flat normalized trace. Letting the dip depth float gives a best depth of about 3.4%, only about 16% of the physically expected resonant signal for the active pulse.

The stored two averages show similar scatter and tracking-scale variations rather than a repeated strong resonance feature. Since the physically expected pODMR dip for these active pulse settings is much larger than the observed normalized deviations, I decide that a pODMR resonance is absent in this scan.
