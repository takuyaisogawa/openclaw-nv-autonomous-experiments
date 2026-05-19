<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_058

Sequence interpretation

The active sequence is Rabimodulated.xml. The instruction block first polarizes the NV and performs detection, so readout 1 is the bright m_S = 0 reference. The block labelled "Acquire 1 level reference" is inside "if abs(full_expt)>1e-12"; full_expt is 0, so that block is skipped. The only microwave manipulation before the second detection is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

Thus readout 2 is the post-Rabi pODMR signal, not an independent m_S = +1 reference. The provided XML variables give length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps, and the stored export reports the same scan range with 21 points.

Expected-signal model calculation

Using the provided setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a rectangular pulse, the driven transition probability versus detuning is

P_1(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau),

where Omega and Delta are in cycles/s and tau = 52 ns. On resonance:

pi * Omega * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P_1(0) = sin^2(1.6336) = 0.9961

With a bright-to-dark contrast scale of 22%, the expected normalized readout-2 signal on resonance is

S_res / S_off = 1 - 0.22 * 0.9961 = 0.7809.

At the observed readout level, readout 1 averages 48.56 counts, so a true resonant pi-like response should produce an approximately 48.56 * 0.22 * 0.9961 = 10.64 count drop in readout 2 near the resonance frequency, ignoring smaller baseline drift.

Data comparison

The measured readout 1 mean is 48.56 counts with population standard deviation 1.13. The measured readout 2 mean is 48.69 counts with population standard deviation 1.17. The pointwise readout-2/readout-1 ratio has mean 1.0029, standard deviation 0.0217, minimum 0.9522, and maximum 1.0437. The largest pointwise deficit of readout 2 relative to readout 1 is -2.42 counts at 3.865 GHz, far smaller than the approximately -10.6 count dip expected for a resonant 52 ns, mod_depth 1 pulse. At the nominal center around 3.875 GHz, readout 2 is slightly higher than readout 1 rather than suppressed.

Stored averages show two separated baseline levels, which is consistent with tracking or cadence effects; I therefore do not treat the two averages as a strong repeatability test. The combined signal lacks the quantitatively expected resonant depletion in the post-Rabi readout.

Decision: resonance absent.
