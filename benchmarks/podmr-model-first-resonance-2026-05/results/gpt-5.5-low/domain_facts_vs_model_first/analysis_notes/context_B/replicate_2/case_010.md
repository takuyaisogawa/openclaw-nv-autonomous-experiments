Case: podmr_017_2026-05-12-134151

I used only the provided inputs in this isolated workspace.

Sequence interpretation:
- The active sequence is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS=1 reference block is inactive.
- Readout 1 is the initial polarized mS=0 fluorescence reference, acquired before the microwave pulse.
- Readout 2 is the fluorescence after the modulated Rabi pulse and is the pODMR signal readout.
- The provided sequence XML has mod_depth = 1 and length_rabi_pulse = 52 ns. The pulse is rounded at 250 MS/s, still 52 ns.

Expected physical signal:
- Given setup Rabi frequency of about 10 MHz at mod_depth = 1, the resonant pulse area for t = 52 ns is:
  theta = 2*pi*(10 MHz)*(52 ns) = 3.267 rad.
- Resonant population transfer probability is sin^2(theta/2), equivalently sin^2(pi*f_R*t):
  P = sin^2(pi*10e6*52e-9) = 0.996.
- With the stated mS=0 to mS=+1 contrast scale of about 22%, the expected resonant fluorescence drop in readout 2 relative to readout 1 is:
  0.22 * 0.996 = 0.219, or about 22%.
- Thus a true resonance should make readout2/readout1 near 0.781 at resonance, aside from noise and baseline effects.

Measured data check:
- Mean readout1 = 22.700, SD = 0.955.
- Mean readout2 = 22.768, SD = 0.723.
- The normalized contrast (readout1 - readout2) / readout1 has mean -0.0045 and SD 0.0497.
- The largest positive contrast point is 0.087 at 3.855 GHz, far below the expected about 0.219 resonant contrast and not accompanied by a coherent resonance-shaped feature.
- Several neighboring and other points have opposite-sign excursions of comparable size, for example -0.087 at 3.860 GHz and -0.103 at 3.825 GHz.
- Stored per-average traces show strong drift/tracking-like variation, so I do not treat the two averages as an independent repeatability confirmation.

Decision:
The pulse parameters predict a large, localized pODMR dip if the scan crosses resonance, but the observed post-pulse signal does not show that feature. The fluctuations are small compared with the expected resonant contrast and are not frequency coherent. I therefore classify this case as resonance_absent.
