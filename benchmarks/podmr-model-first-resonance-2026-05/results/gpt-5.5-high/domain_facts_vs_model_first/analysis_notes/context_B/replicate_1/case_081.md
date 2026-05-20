Case podmr_067_2026-05-17-074342

Sequence interpretation

The provided XML is Rabimodulated.xml. The active experimental block is:

1. adj_polarize followed by detection: this is the true mS = 0 optical reference, so readout 1 is the bright reference.
2. full_expt = 0, so the optional explicit mS = 1 reference block is disabled.
3. A single rabi_pulse_mod_wait_time pulse followed by detection: readout 2 is the signal readout after the microwave/Rabi pulse.

The standalone sequence.xml and exported Variable_values give length_rabi_pulse = 52 ns and mod_depth = 1. The pulse is rounded to the 250 MHz sample clock; 52 ns is exactly 13 samples, so the active pulse duration remains 52 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Expected physical signal

Using the given setup facts:

- Contrast scale between mS = 0 and mS = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: tau = 52 ns.

For a resonant rectangular Rabi pulse, the transferred population is

P_res = sin^2(pi f_R tau)
      = sin^2(pi * 10e6 * 52e-9)
      = 0.996.

The expected fractional bright-readout depletion on resonance is therefore

C * P_res = 0.22 * 0.996 = 0.219, about 21.9%.

With a typical readout level of about 49 counts, this corresponds to a dip of about

49 * 0.219 = 10.7 counts

in readout 2 relative to the mS = 0 reference readout. Because the scan step is 5 MHz and the Rabi frequency is 10 MHz, even a resonance halfway between sampled frequencies should still give an order-20% depletion at the nearest sampled point under the same rectangular-pulse model, not a sub-5% fluctuation.

Data comparison

The combined means are:

- readout 1 mean: 48.920
- readout 2 mean: 48.757
- readout 2 minus readout 1 mean: -0.163 counts

Pointwise readout-2/readout-1 contrast ranges from -4.77% to +6.28%, with no feature close to the expected -21.9% resonant depletion. The most negative points are small, irregular fluctuations, and positive excursions of comparable or larger size are also present. Stored averages are only two and can reflect tracking cadence, so I do not treat average-to-average variation as a strong repeatability test.

Decision

Given the active pulse is effectively a pi pulse at mod_depth = 1, a real pODMR resonance in the scanned range should produce a large readout-2 dip relative to the readout-1 bright reference. The observed data lack any depletion on the expected scale. I therefore classify this case as resonance_absent.
