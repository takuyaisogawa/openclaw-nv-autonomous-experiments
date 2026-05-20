Case: podmr_014_2026-05-16-124559

Inputs used: inputs/sequence.xml and inputs/raw_export.json.

Sequence interpretation

The active sequence is Rabimodulated. The relevant active path is:

1. adj_polarize(...)
2. detection(...)
3. wait_for_awg(...)
4. the "Acquire 1 level reference" block is skipped because full_expt = 0
5. rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)
6. detection(...)

Therefore readout 1 is the bright m_S = 0 reference acquired immediately after optical polarization. Readout 2 is the signal after the microwave Rabi pulse. It is not an independent m_S = +1 reference in this run.

The provided sequence XML sets:

- length_rabi_pulse = 5.2e-08 s
- sample_rate = 250000000 samples/s, so the rounded pulse length remains 13 samples / 250 MHz = 52 ns
- mod_depth = 1
- full_expt = 0

Physical model calculation

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For this sequence, f_R = 10 MHz and t = 52 ns.

For a resonant square pulse, the transferred population is:

P(m_S = +1) = sin^2(pi f_R t)

With f_R t = 10e6 * 52e-9 = 0.52 cycles:

P = sin^2(pi * 0.52) = 0.996

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected fluorescence drop on resonance is:

0.22 * 0.996 = 0.219, or about 21.9%.

Using the finite-duration square-pulse detuning model,

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2 pi * 10 MHz, the observed contrast shape is also consistent with a resonance centered near 3.878 GHz. A fixed-amplitude model with 22% full contrast gives predicted drops of about 19.3% at 3.875 GHz, 21.3% at 3.880 GHz, and 13.2% at 3.885 GHz for a best center near 3.8784 GHz.

Data comparison

I normalized the signal as (readout1 - readout2) / readout1. The largest observed drop is 19.4% at 3.875 GHz. Neighboring points are also depressed: 15.9% at 3.880 GHz and 11.7% at 3.885 GHz. Away from 3.870-3.890 GHz, the normalized difference is centered near 0.02% with about 2.5% standard deviation.

The two stored averages are not treated as a strong independent repeatability test, but both show the same central suppression region: average 1 has a 21.1% maximum at 3.875 GHz, and average 2 has a strong central maximum with 17.7% at 3.875 GHz, 13.6% at 3.880 GHz, and 18.6% at 3.885 GHz.

Decision

The readout roles, pulse duration, and mod_depth imply an expected resonant pODMR drop of about 22%. The measured readout-2 suppression is localized in frequency and reaches 19.4%, close to the expected physical signal and far above the off-resonance scatter. I decide that a pODMR resonance is present.
