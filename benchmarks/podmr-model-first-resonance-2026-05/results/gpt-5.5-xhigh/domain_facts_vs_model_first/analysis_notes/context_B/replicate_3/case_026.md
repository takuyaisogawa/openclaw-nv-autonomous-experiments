Case: podmr_011_2026-05-16-120107

Active sequence identification

The active sequence is Rabimodulated.xml. The instruction flow is:

1. adj_polarize
2. detection
3. wait_for_awg
4. optional 1-level reference block, but full_expt = 0 so this block is skipped
5. rabi_pulse_mod_wait_time
6. detection
7. wait_for_awg

Thus the two stored readouts have these roles:

- readout 1: bright mS = 0 reference, acquired immediately after optical polarization and before the microwave pulse.
- readout 2: pODMR signal readout, acquired after the microwave Rabi pulse.

The active microwave pulse is a square Rabi pulse with length_rabi_pulse = 52 ns and mod_depth = 1. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns. The full-expt mS = 1 reference is not active, so there is no separate dark reference readout in this scan.

Physical model calculation

Use a two-level square-pulse Rabi model for the mS = 0 to mS = +1 transition. The setup gives a Rabi frequency of about 10 MHz at mod_depth = 1, so f_R = 10 MHz. With detuning Delta in Hz and pulse duration tau = 52 ns, the transfer probability is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).

On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current setup contrast scale between mS = 0 and mS = +1 is about 22%, so the expected resonant readout-2 dip relative to the bright reference is

0.22 * 0.996 = 0.219, or about 21.9%.

For the same model, the expected dips around the resonance are:

- Delta = 0 MHz: 21.9%
- Delta = +/-5 MHz: 16.5%
- Delta = +/-10 MHz: 6.0%
- Delta = +/-15 MHz: 0.26%

Observed data check

The scan runs from 3.825 GHz to 3.925 GHz in 5 MHz steps. The strongest normalized dip occurs in readout 2 at 3.880 GHz:

- readout 1 = 41.404
- readout 2 = 33.096
- readout2/readout1 = 0.799
- observed dip = 20.1%

Neighboring points also follow the expected broad square-pulse resonance scale:

- 3.870 GHz: 12.4% dip
- 3.875 GHz: 17.9% dip
- 3.880 GHz: 20.1% dip
- 3.885 GHz: 10.9% dip
- 3.890 GHz: 2.45% dip

The readout 1 reference remains near the low-40-count level through the feature, so the localized reduction is in the post-microwave signal readout rather than a shared optical/reference artifact.

I also fit the normalized ratio readout2/readout1 to the fixed-contrast Rabi model ratio = a * (1 - 0.22 * P(Delta)), fitting only the multiplicative readout scale and resonance center. The best center is 3.87735 GHz with scale a = 0.9909. The RMSE is 0.0268, compared with 0.0612 for a flat no-resonance ratio. Allowing the contrast amplitude to float gives an effective contrast of about 20.0%, close to the 22% setup scale.

Decision

A pODMR resonance is present. The observed localized post-pulse fluorescence dip has the expected sign, frequency-localized shape, and magnitude for a 52 ns near-pi pulse at mod_depth = 1.
