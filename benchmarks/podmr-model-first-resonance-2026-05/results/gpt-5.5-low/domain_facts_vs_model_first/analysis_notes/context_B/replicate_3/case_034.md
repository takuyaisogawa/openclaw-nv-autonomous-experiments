Sequence and roles:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instruction path has full_expt = 0, so the optional +1 reference block is skipped.
- Readout 1 is acquired immediately after adj_polarize and is the bright m_S = 0 reference.
- Readout 2 is acquired after one rabi_pulse_mod_wait_time pulse and is the pODMR signal readout.
- Pulse duration: length_rabi_pulse = 52 ns. The 250 MHz sample-rate rounding leaves this as 52 ns.
- mod_depth: inputs/sequence.xml gives mod_depth = 1. The raw export variable values also list mod_depth = 1, though the embedded saved sequence text has an older default value of 0.3; the active value used here is 1.

Quantitative expected signal:

Given the stated setup Rabi frequency, f_Rabi ~= 10 MHz at mod_depth = 1. For a square pulse, the resonant transition probability is

P = sin^2(pi * f_Rabi * tau)

with tau = 52 ns. This gives f_Rabi * tau = 0.52 cycles and P = sin^2(0.52*pi) = 0.996. With a 22% m_S = 0 to m_S = +1 contrast, the expected resonant readout-2/readout-1 ratio is approximately

1 - 0.22 * 0.996 = 0.781.

Thus a resonance in this scan should produce a deep dip in readout 2 relative to readout 1, roughly 22% below the bright reference at the resonant frequency. For a typical readout 1 level of 47 to 49 counts, this corresponds to a resonant readout 2 near 37 to 38 counts, not near 46 to 48 counts.

I also evaluated the finite-detuning square-pulse response

P(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * tau * sqrt(Omega^2 + Delta^2))

where Omega = 2*pi*10 MHz and Delta = 2*pi*(mw_freq - center). Centered near the nominal 3.8751 GHz, the expected ratio reaches about 0.781 around 3.875 GHz and is still about 0.84 near 3.870 to 3.880 GHz.

Observed data:

- Observed readout-2/readout-1 ratio mean: 0.983.
- Observed ratio standard deviation across scan points: 0.028.
- Observed ratio minimum: 0.929.
- Observed readout 2 minus readout 1 mean: -0.814 counts.
- Largest observed readout-2 deficit: -3.423 counts.

The observed minimum deficit is far smaller than the expected resonant deficit of about 10 to 11 counts. Around the nominal resonance region, ratios are 0.982 at 3.870 GHz, 0.977 at 3.875 GHz, and 0.961 at 3.880 GHz, not the predicted approximately 0.78 to 0.84. A scan-center fit of the square-pulse lineshape gives only about 4% contrast amplitude, much smaller than the expected 22%, and does not form a convincing resonant dip.

Decision:

The relevant physical model predicts a large near-pi-pulse contrast dip if resonance is present. The measured two-readout comparison does not show that dip; the readouts remain close together with only small fluctuations and drift-scale differences. Therefore I decide that a pODMR resonance is absent.
