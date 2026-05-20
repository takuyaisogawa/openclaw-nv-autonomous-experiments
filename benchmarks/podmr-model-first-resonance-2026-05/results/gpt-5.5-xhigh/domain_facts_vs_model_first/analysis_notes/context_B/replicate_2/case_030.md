Case: podmr_015_2026-05-16-130043

Active sequence and readout roles:

The sequence is Rabimodulated.xml. The instructions first run adj_polarize followed by detection, so readout 1 is the optically polarized m_S = 0 fluorescence reference. The `full_expt` variable is 0, so the intermediate "Acquire 1 level reference" block is skipped. The only microwave-prepared readout is therefore the later `rabi_pulse_mod_wait_time(...)` followed by detection; readout 2 is the pODMR signal after the Rabi-modulated microwave pulse, not a separately acquired m_S = +1 reference.

The active pulse values are:

- `mod_depth = 1`
- `length_rabi_pulse = 52 ns`
- `sample_rate = 250 MHz`, so 52 ns is exactly 13 samples and is unchanged by the rounding instruction.
- The scan varies `mw_freq` from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Expected signal model:

Using the provided setup facts, the Rabi frequency is approximately

    f_R = 10 MHz * mod_depth = 10 MHz

For a square pulse of duration t, the driven transition probability versus detuning is

    P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

where f_R and Delta are in cycles/s. The normalized fluorescence model is

    S(Delta) = baseline * (1 - C * P(Delta))

with C = 0.22 for the m_S = 0 to m_S = +1 contrast scale.

On resonance with t = 52 ns:

    pi * f_R * t = pi * 10e6 * 52e-9 = 0.52 pi
    P(0) = sin^2(0.52 pi) = 0.996
    expected fluorescence drop = 0.22 * 0.996 = 0.219

So a true resonance should produce about a 22% fluorescence dip in the microwave-prepared readout relative to the m_S = 0 reference, with a finite-pulse linewidth on the order of the 10 MHz Rabi frequency.

Data comparison:

The combined readout ratio readout2/readout1 has a minimum at 3.875 GHz:

    readout1 = 46.2115
    readout2 = 35.8654
    ratio = 0.7761
    raw contrast relative to readout1 = 1 - ratio = 0.2239

Using points at least 30 MHz from the fitted resonance center as the far-off-resonance reference gives a mean ratio of 0.9713. The dip at 3.875 GHz is therefore lower by 0.1952 in ratio units, or 20.1% of the far-off baseline. This is close to the 21.9% expected contrast from the 52 ns, mod_depth 1 pulse.

I also fit the finite-pulse model to the normalized ratio. With the physical contrast fixed at C = 0.22 and a free baseline scale, the best center is about 3.878 GHz with baseline scale 0.985 and SSE 0.0114, compared with SSE 0.0741 for a constant model and 0.0715 for a linear-baseline-only model. Allowing the dip amplitude to float gives an effective contrast of about 0.200 relative to the fitted baseline, again consistent with the expected scale after baseline drift and finite detuning from the nearest sampled point.

The stored two averages are not a strong independent repeatability test because they may reflect tracking cadence, but both averages contain their deepest normalized point near the same feature: average 1 at 3.875 GHz with ratio 0.758, and average 2 at 3.880 GHz with ratio 0.757.

Decision:

The observed dip is centered within the scan, has the expected finite-pulse width, and has the expected contrast scale for a near-pi pulse at mod_depth 1. A pODMR resonance is present.
