Case: podmr_006_2026-05-16-011837

I used only inputs/raw_export.json, inputs/raw_readouts.png, and inputs/sequence.xml. The active sequence is Rabimodulated.xml with vary_prop = mw_freq over 3.825 to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. The active detections are therefore:

- readout 1: after adj_polarize and before the microwave pulse, a true m_S = 0 fluorescence reference.
- readout 2: after rabi_pulse_mod_wait_time and detection, the pODMR signal readout.

The active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

with length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and switch_delay = 100 ns. The 52 ns pulse is already an integer number of 250 MHz samples after rounding: 52 ns * 250 MHz = 13 samples.

Quantitative expected-signal model:

The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For this case mod_depth = 1, so f_R = 10 MHz. For a rectangular driven two-level pulse at detuning df, the transition probability is

P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * tau * sqrt(f_R^2 + df^2))

where tau = 52 ns and frequencies are in cycles/s. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated fluorescence contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance readout-2 drop relative to the readout-1 reference is

0.22 * 0.996 = 0.219, or 21.9%.

Observed normalized signal:

Using the combined raw data as readout2/readout1, the minimum occurs at 3.875 GHz:

readout1 = 41.8077
readout2 = 31.8654
readout2/readout1 = 0.7622
observed drop = 1 - 0.7622 = 0.2378, or 23.8%.

The neighboring 3.880 GHz point is also strongly depressed:

readout1 = 40.1923
readout2 = 30.7885
readout2/readout1 = 0.7660
observed drop = 23.4%.

The off-resonance median readout2/readout1 ratio, excluding the dip region, is about 0.9794, so the dip is not just a global offset between the two readouts.

I also fit the rectangular-pulse model over the scan with fixed contrast amplitude C = 0.22 and f_R = 10 MHz, allowing only the resonance center and baseline ratio to vary. The best center was 3.878 GHz with baseline ratio 0.9926. The sum of squared residuals was 0.0163, compared with 0.1049 for a no-resonance constant-ratio model, a factor of 6.4 improvement. Letting the contrast amplitude float gave center 3.878 GHz and amplitude 0.232, close to the expected 0.22.

Stored averages are not treated as a strong independent repeatability test, but both averages show their deepest normalized drop in the same 3.875 to 3.880 GHz region:

- average 1: minimum at 3.875 GHz, drop 25.3%.
- average 2: minimum at 3.880 GHz, drop 26.5%.

Decision: resonance_present. The observed dip magnitude and width match the expected near-pi-pulse pODMR response for the active 52 ns, mod_depth 1 pulse.
