Case podmr_042_2026-05-16-225623

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The active sequence is Rabimodulated.xml. In the instructions, the sequence first polarizes the NV and performs detection before any microwave pulse; this is the "true 0 level reference", so readout 1 is the bright m_S = 0 reference for tracking/normalization. The full_expt variable is 0, so the optional separate m_S = 1 reference block is disabled. The active measurement pulse is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

followed by detection, so readout 2 is the signal after the microwave pulse. The active parameters from the saved export are length_rabi_pulse = 52 ns and mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant square Rabi pulse, the transferred population is modeled as:

P_transfer = sin^2(pi * f_Rabi * t)

With f_Rabi = 10 MHz and t = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.9961.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so a resonant pODMR response in readout 2 normalized by the bright readout 1 reference should be approximately:

R_res = 1 - 0.22 * P_transfer = 0.7809.

Thus a real resonance should produce about a 21.9% normalized fluorescence reduction relative to the m_S = 0 reference. At the central scan point, readout 1 is 45.365, so the expected resonant readout 2 would be:

45.365 * 0.7809 = 35.42.

Observed data calculation

The observed central point at 3.875 GHz is readout 1 = 45.365 and readout 2 = 43.538, giving:

R_obs = 43.538 / 45.365 = 0.9597.

Using all noncentral scan points as an off-resonance ratio baseline gives mean(readout2/readout1) = 1.0057 with sample standard deviation 0.0292. The observed normalized center drop relative to that baseline is:

1.0057 - 0.9597 = 0.0460.

This is far smaller than the model-predicted resonant drop of about 0.2249 relative to the same baseline. Equivalently, the observed center readout 2 is 8.11 counts higher than the resonant model prediction of 35.42 counts. The small depression near the middle is also visible in both readouts, which is consistent with tracking/background variation rather than a strong independent spin-dependent fluorescence loss.

Decision

Because the active pulse should produce nearly full population transfer on resonance and therefore a large approximately 22% normalized fluorescence dip, while the observed normalized dip is only about 4.6% and close to baseline scatter, I decide that a pODMR resonance is absent.
