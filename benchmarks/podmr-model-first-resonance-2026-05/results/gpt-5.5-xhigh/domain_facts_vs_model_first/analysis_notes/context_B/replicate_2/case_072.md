Case podmr_058_2026-05-17-053345

I used only the provided files in this workspace. The active sequence is Rabimodulated.xml. In the active path, full_expt = 0, so the optional m_S = +1 reference block is skipped. The executed readouts are:

1. Readout 1: after adj_polarize and detection, before the microwave pulse. This is the bright m_S = 0 reference.
2. Readout 2: after a rabi_pulse_mod_wait_time pulse and detection. This is the pODMR signal readout.

Pulse parameters from inputs/sequence.xml and the exported variable values:

- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, rounded to 13 samples at 250 MHz, still 52 ns
- mod_depth = 1
- nominal Rabi frequency at this mod_depth = 10 MHz
- current setup bright/dark contrast scale = 22%

There is one textual sequence copy inside raw_export.json that shows a default mod_depth of 0.3 in the variable definition, but the standalone sequence XML and exported active Variable_values both give mod_depth = 1. I treated mod_depth = 1 as the active setting.

Quantitative expected-signal model:

For a two-level microwave transition driven by a rectangular pulse, with Rabi frequency f_R = 10 MHz and detuning Delta in Hz, the transition probability after pulse duration t is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t).

The readout model relative to the bright reference is

S_pulse / S_ref = 1 - C * P(Delta),

with C = 0.22 and t = 52 ns.

On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996
S_pulse / S_ref = 1 - 0.22 * 0.996 = 0.781

Because the scan step is 5 MHz, any resonance inside the scan range should be within 2.5 MHz of a sampled point. At 2.5 MHz detuning this model still predicts about P = 0.93 and S_pulse / S_ref = about 0.80. With the observed bright reference near 45.7 counts, the expected resonant pulse readout would be near 35.7 to 36.4 counts, a deficit of roughly 9 to 10 counts from the reference.

Observed data:

- Combined readout 1 mean = 45.68 counts.
- Combined readout 2 mean = 45.58 counts.
- Combined pulse/reference ratio mean = 0.998.
- Minimum combined pulse/reference ratio = 0.931, at 3.890 GHz.
- Largest combined deficit readout2 - readout1 = -3.23 counts.
- Per-average ratios fluctuate strongly with tracking level; the stored averages are not a strong independent repeatability test here. Even so, the largest per-average deficit is about 4.92 counts, still far below the expected near-pi-pulse resonant deficit.

I also compared the measured combined ratio to the fixed-contrast physical model. A constant-ratio null model has lower squared error than a model forced to contain the expected 22% Rabi-pulse dip. An unconstrained dip-shaped fit only wants an apparent amplitude of about 6%, not the expected 22%, and the low points are comparable to the scan noise and tracking fluctuations.

Decision: resonance_absent. The active 52 ns, mod_depth = 1 pulse should produce a large, near-pi-pulse pODMR dip if a resonance were present in the scanned range, but the measured readout2/readout1 ratios never approach the predicted about 0.8 level.
