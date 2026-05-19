<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_041

Sequence interpretation

The provided XML is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence is:

1. adj_polarize for 1 us.
2. detection: this is the true ms=0 optical reference, corresponding to readout 1.
3. wait_for_awg for 2 us.
4. The full_expt branch is inactive because full_expt = 0, so no separate ms=+1 reference is acquired.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
6. detection: this is the post-microwave-pulse signal, corresponding to readout 2.
7. final wait.

Thus the relevant pODMR signal is a dip of readout 2 relative to readout 1 when the microwave pulse is resonant with the NV transition.

Expected quantitative signal

Given domain facts, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For the active pulse:

    f_R = 10 MHz
    tau = 52 ns
    contrast C = 0.22

For a rectangular Rabi pulse, the resonant transfer probability is:

    P0 = sin^2(pi f_R tau)

Using f_R tau = 10e6 * 52e-9 = 0.52 cycles:

    P0 = sin^2(pi * 0.52) = 0.996

The expected fractional readout drop at resonance is therefore:

    C * P0 = 0.22 * 0.996 = 0.219

On the observed baseline near 54 raw counts, this predicts an on-resonance dip of about:

    54 * 0.219 = 11.8 counts

For finite detuning, I used:

    P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) *
               sin^2(pi tau sqrt(f_R^2 + Delta^2))

This still predicts large dips near resonance. Even if the true resonance falls halfway between 5 MHz-spaced scan points, at Delta = 2.5 MHz the expected transfer is 0.929 and the expected drop is about 11.0 counts. At Delta = 5 MHz the expected drop is still about 8.9 counts.

Observed data

Combined readout statistics:

    mean(readout 1) = 53.794, sd = 1.018
    mean(readout 2) = 52.947, sd = 1.067
    mean(readout2 - readout1) = -0.847 counts
    sd(readout2 - readout1) = 1.432 counts
    min(readout2/readout1) = 0.9368
    mean(readout2/readout1) = 0.9846

The largest observed readout-2 deficit relative to readout 1 is 3.46 counts at 3.835 GHz, only about 6.3 percent of the local readout level. The visually suggestive deficits near 3.88-3.90 GHz are also only about 2.3 to 3.0 counts, much smaller than the approximately 12 count resonant dip expected from the active 52 ns, mod_depth 1 pulse.

I also fit the normalized ratio readout2/readout1 to a rectangular-pulse pODMR model y = baseline - A * P(Delta) over candidate resonance centers. The best in-window fit gives:

    center = 3.87975 GHz
    fitted A = 0.03795
    expected A = 0.22
    fitted/expected = 0.172

This fitted contrast is far below the physical expectation for this setup and pulse, and the improvement over a flat-ratio model is small. Stored averages are not a strong independent repeatability test here because they may reflect tracking cadence.

Decision

The active sequence should produce a large, narrow readout-2 dip if a pODMR resonance is present in the scanned range. The measured data contain only small percent-level fluctuations and no feature remotely matching the expected approximately 22 percent signal. I decide resonance_absent.
