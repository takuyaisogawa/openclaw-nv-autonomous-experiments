Case podmr_062_2026-05-17-063134

Sequence identification:
- The provided XML is Rabimodulated.xml / Rabimodulated.
- The active scan variable is mw_freq, from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- Readout 1 is therefore the initial detection after adj_polarize, i.e. the bright m_S = 0 reference.
- Readout 2 is the detection after one rabi_pulse_mod_wait_time pulse, i.e. the pODMR signal readout.
- The active Rabi pulse duration is length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding keeps it at 13 samples = 52 ns.
- The provided XML and exported variable values give mod_depth = 1.

Quantitative expected-signal model:
- Use a square-pulse two-level model for the driven m_S = 0 to m_S = +1 transition:
  P_transfer(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * t),
  with Omega and delta in cycles/s.
- The setup facts give Omega = 10 MHz * mod_depth = 10 MHz.
- For t = 52 ns and mod_depth = 1, the resonant pulse area is Omega*t = 0.52 cycles, so
  P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated bright/dark contrast scale of 22%, the expected resonant fractional drop in readout 2 relative to readout 1 is
  0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout level is about 49.4 counts, so a resonant point should drop by about
  49.4 * 0.219 = 10.8 counts.
- Because the scan step is 5 MHz, a resonance centered halfway between sampled points would still put the nearest sampled point at |delta| <= 2.5 MHz. For Omega = 10 MHz, the model remains near full transfer there, so an on-scan resonance should still cause roughly a 20% dip, not a small isolated fluctuation.

Observed data comparison:
- Combined readout 1 mean = 49.41 counts, standard deviation across scan points = 1.18 counts.
- Combined readout 2 mean = 49.44 counts, standard deviation across scan points = 0.89 counts.
- The pointwise difference readout2 - readout1 has mean +0.033 counts and standard deviation 1.25 counts.
- The largest observed positive contrast estimate (readout1 - readout2) / readout1 is 0.0626 at 3.920 GHz, corresponding to a 3.15 count drop.
- That largest drop is only about 29% of the mod_depth=1 expected resonant drop and is not accompanied by the broad neighboring suppression expected from a 10 MHz Rabi frequency square-pulse response.
- Most scan points have readout 2 equal to or higher than readout 1 within the observed scatter, so the data do not show the expected pODMR dip.

Decision:
The active sequence should produce a large, easily visible reduction in the second readout on resonance. The measured readout difference is centered near zero and never approaches the modeled resonance-sized signal. Therefore I decide that a pODMR resonance is absent.
