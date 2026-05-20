Case: podmr_006_2026-05-11-020739

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- SequenceName is Rabimodulated.xml.
- The active path is polarize -> detection -> wait -> Rabi pulse -> detection -> final wait.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the detection immediately after optical polarization, so it is the bright m_S = 0 reference.
- Readout 2 is the detection after the modulated Rabi pulse, so it is the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz this is 13 samples, so the rounded duration remains 52 ns.

Quantitative model:
For this setup, f_Rabi is about 10 MHz at mod_depth = 1. I used the square-pulse two-level response

P_transfer(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

with Omega = 2*pi*10 MHz, Delta = 2*pi*delta, and t = 52 ns. On resonance this gives

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance fluorescence reduction for the post-pulse signal readout is approximately

0.22 * 0.996 = 0.219,

so a clean on-resonance point should be roughly 21.9% dimmer than the bright-state reference, before allowing for technical drift or reduced effective contrast.

Data comparison:
I normalized the signal readout by the immediate bright reference, readout2/readout1. The minimum normalized point is at 3.880 GHz:

- 3.875 GHz: readout2/readout1 = 0.9108
- 3.880 GHz: readout2/readout1 = 0.8459
- 3.885 GHz: readout2/readout1 = 0.8698

The median normalized ratio outside +/-15 MHz of 3.880 GHz is 0.9602, so the central feature is an extra drop of about 11.4 percentage points relative to that local off-resonance scale. Directly against the readout 1 reference, the deepest point is a 15.4% reduction. This is smaller than the ideal 21.9% estimate, but it has the expected sign and a localized finite-pulse line shape.

I also fit the normalized ratios to the same square-pulse response with center frequency and effective contrast free. The best center was 3.8796 GHz, with baseline ratio 0.9827 and effective contrast amplitude 0.125. The residual SSE was 0.0348 versus 0.0597 for a flat normalized-ratio null model. A fixed 22% contrast model selected the same center but was too deep, with SSE 0.0504. The stored averages are not a strong independent repeatability test because they may reflect tracking cadence, but both averages have their minimum normalized ratio at 3.880 GHz or the adjacent 3.885 GHz point.

Decision:
The physical model predicts a large negative signal readout feature for this near-pi pulse, and the normalized data contain a centered negative feature near 3.88 GHz with the expected sign and approximate finite-pulse width. The reduced contrast prevents high certainty about the exact amplitude, but the evidence supports a present pODMR resonance.
