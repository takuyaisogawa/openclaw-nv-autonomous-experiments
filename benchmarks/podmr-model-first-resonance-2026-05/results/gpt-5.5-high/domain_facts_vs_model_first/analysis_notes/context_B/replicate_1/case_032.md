Free-form analysis note for podmr_017_2026-05-16-132945

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and roles

The saved scan sequence is Rabimodulated.xml with vary_prop = mw_freq, 21 points from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence polarizes the NV,
performs a detection immediately after polarization, waits, then applies a modulated
Rabi pulse and performs a second detection. full_expt = 0, so the optional mS = +1
reference branch is inactive.

Therefore readout 1 is the bright mS = 0 reference acquired before the microwave
pulse. Readout 2 is the post-microwave signal readout. A pODMR resonance should
appear as a dip in readout 2 relative to readout 1/baseline, not as a dip in both
readouts.

Relevant active parameters from the exported variable values:
- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MS/s, so the pulse duration is already on the 4 ns grid
- mw scan = 3.825 to 3.925 GHz
- pumping_time = 1 us
- delay_wrt_1mus = 0.2 us

Quantitative model calculation

Given the provided setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1.
For a square pulse, the resonant spin-transfer probability is

    P(+1) = sin^2(pi * f_Rabi * tau)

Using f_Rabi = 10 MHz and tau = 52 ns:

    pi * f_Rabi * tau = pi * 0.52
    P(+1) = sin^2(pi * 0.52) = 0.9961

The expected fluorescence contrast for full mS = 0 to mS = +1 transfer is about
22%, so the expected on-resonance readout-2 dip is

    expected fractional dip = 0.22 * 0.9961 = 0.2191, or 21.9%

I also evaluated the standard detuned square-pulse response

    P(+1, delta) = f_Rabi^2 / (f_Rabi^2 + delta^2)
                  * sin^2(pi * sqrt(f_Rabi^2 + delta^2) * tau)

with the resonance center set at the observed minimum. This gives a central
normalized readout of 0.7809 relative to the off-resonant bright level, matching
the expected 21.9% dip.

Observed data check

Readout 2 has an off-resonant baseline mean of 43.656 counts/readout when excluding
the central dip region. Its minimum is 34.173 counts/readout at 3.875 GHz.

    observed fractional dip = (43.656 - 34.173) / 43.656 = 0.2172, or 21.7%

The two stored averages both show the central readout-2 suppression at the same
frequency, with values 32.731 and 35.615 at 3.875 GHz. I do not treat this as a
strong independent repeatability test because stored averages can reflect tracking
cadence, but it is consistent with the combined data.

Readout 1, the bright reference, has no comparable central dip: its value at
3.875 GHz is 45.404, close to its off-resonant baseline mean of 44.309. This
separates a microwave-dependent post-pulse resonance from common-mode fluorescence
or tracking variation.

Decision

The active sequence, readout roles, and pulse parameters predict a near-full
population-transfer pODMR dip of about 22% in readout 2 for an on-resonance NV
transition. The observed dip is 21.7%, centered at 3.875 GHz, with the expected
detuned-pulse shape over neighboring scan points and no corresponding dip in the
bright reference. I therefore decide that a pODMR resonance is present.
