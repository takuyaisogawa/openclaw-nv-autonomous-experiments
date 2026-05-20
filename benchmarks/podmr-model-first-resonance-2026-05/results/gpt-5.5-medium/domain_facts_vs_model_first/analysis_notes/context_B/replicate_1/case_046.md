Case: podmr_032_2026-05-16-201700

Input files used only from this isolated workspace:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png

Active pulse sequence and readout roles
--------------------------------------
The active sequence is Rabimodulated.xml. The instructions first polarize the NV and run a detection event labelled in the XML as "Acquiring true 0 level reference". Because full_expt = 0, the optional "Acquire 1 level reference" branch is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and performs the final detection. Therefore:
- readout 1 is the polarized m_S = 0 reference readout.
- readout 2 is the signal readout after the modulated Rabi pulse.

The relevant pulse parameters are:
- length_rabi_pulse = 52 ns, rounded by the 250 MHz sample clock to 52 ns.
- mod_depth = 1 from the provided XML / exported variable values.
- mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected signal model
----------------------------------
Use the supplied setup facts:
- Contrast between m_S = 0 and m_S = +1 is about C = 0.22.
- Rabi frequency at mod_depth = 1 is f_R = 10 MHz and scales linearly with mod_depth.

For a square resonant Rabi pulse, the transferred population is

P_1(delta = 0) = sin^2(pi * f_R * tau).

With f_R = 10 MHz and tau = 52 ns:

f_R * tau = 10e6 * 52e-9 = 0.52
P_1(0) = sin^2(pi * 0.52) = 0.996

The expected signal/reference ratio on resonance is then

R_expected = 1 - C * P_1 = 1 - 0.22 * 0.996 = 0.781.

So an on-resonance point should be about 21.9% below the polarized reference readout. Equivalently, with readout 1 around 55 counts, the signal readout should be near 43 counts at resonance, not near 55 counts.

I also checked the detuned Rabi model form

P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

which would produce a localized contrast feature on the scale of the 10 MHz Rabi rate and 52 ns pulse width somewhere in the 100 MHz frequency sweep if a resonance were present.

Observed quantitative comparison
--------------------------------
From raw_export.json:
- readout 1 mean = 55.255, population standard deviation across scan = 1.093.
- readout 2 mean = 55.262, population standard deviation across scan = 1.210.
- readout2/readout1 mean = 1.0004.
- readout2/readout1 minimum = 0.9582 at 3.830 GHz.
- readout2/readout1 maximum = 1.0729 at 3.875 GHz.

The deepest observed normalized dip is only 4.2% below unity, far smaller than the approximately 21.9% dip predicted for a resonant pi-like pulse at mod_depth = 1. The largest feature is actually an upward signal/reference excursion near 3.875 GHz. The per-average overlays show the two averages mainly offset by tracking cadence, so the stored averages are not a strong independent repeatability test.

Decision
--------
The active sequence should have generated a large negative readout-2 feature if the scanned microwave frequency crossed an NV resonance under these pulse parameters. The measured signal readout does not show that feature, and the observed fluctuations are inconsistent with the expected resonant contrast and line shape. I therefore decide that a pODMR resonance is absent.
