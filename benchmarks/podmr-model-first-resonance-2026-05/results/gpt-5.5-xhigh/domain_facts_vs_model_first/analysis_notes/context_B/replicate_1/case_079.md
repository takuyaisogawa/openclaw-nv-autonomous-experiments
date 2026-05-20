Case podmr_065_2026-05-17-071421

Sequence inspection:
- Sequence file: Rabimodulated.xml.
- Active branch: full_expt = 0, so the optional m_s = +1 reference branch is skipped even though do_adiabatic_inversion = 1.
- Readout roles:
  - readout 1 is the true m_s = 0 reference after optical polarization and before the microwave pulse.
  - readout 2 is the signal readout after the modulated Rabi microwave pulse.
- Scanned variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- mod_depth = 1.
- Rabi pulse duration = round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Quantitative model:
- Given the setup fact, the Rabi frequency at mod_depth = 1 is about 10 MHz.
- For a resonant square pulse, transition probability is
  P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The m_s = 0 to m_s = +1 fluorescence contrast scale is about 22%, so an on-resonance pODMR dip should be approximately
  0.22 * 0.996 = 0.219, or 21.9% of the reference readout.
- Therefore, at resonance readout 2 should be about 1 - 0.219 = 0.781 times readout 1. With the combined reference mean of 47.48 counts, the expected resonant signal is about 37.07 counts, a drop of about 10.4 counts.

Data comparison:
- Combined readout 2 / readout 1 ranges from 0.952 to 1.043, with mean 0.994.
- The largest combined fractional drop is only 0.0477 at 3.830 GHz, far below the expected 0.219.
- Per stored average, the largest same-average fractional drops are 0.0776 and 0.0729, still far below the expected 0.219 and occurring at different scan frequencies. The stored averages also show a large absolute tracking offset, so they are not a strong independent repeatability test.
- Fitting the combined fractional drop to the expected detuned Rabi response while allowing the resonance center to vary gives a best-fit amplitude of about 0.049, not the expected 0.22.

Decision:
The active pulse would produce a large, easily visible dip if a resonance were within the scan window. The normalized data show only small fluctuations and no dip near the expected 22% contrast scale. I therefore decide that a pODMR resonance is absent.
