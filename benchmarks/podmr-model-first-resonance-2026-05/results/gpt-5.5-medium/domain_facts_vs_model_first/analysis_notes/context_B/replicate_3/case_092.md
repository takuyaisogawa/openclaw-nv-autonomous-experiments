<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_092

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence identification:

- Sequence: Rabimodulated.xml / Rabimodulated pODMR scan.
- Scanned parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz, so length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- mod_depth = 1 in the provided sequence XML and in the exported Variable_values.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. The adiabatic inversion flag is therefore not active for this measurement.
- Readout roles:
  - readout 1 is the initial laser-polarized mS = 0 reference, taken immediately after adj_polarize and before the Rabi pulse.
  - readout 2 is the post-Rabi-pulse measurement, taken after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth).

Physical model calculation:

The relevant pulse is a square Rabi pulse before readout 2. With the supplied setup facts, the resonant Rabi frequency is approximately

  f_R = 10 MHz * mod_depth = 10 MHz.

For a square pulse of duration tau = 52 ns, the resonant transfer probability is

  P_res = sin^2(pi * f_R * tau)
        = sin^2(pi * 10e6 * 52e-9)
        = 0.996.

Using the setup contrast scale C = 0.22 between mS = 0 and mS = +1, the expected resonant fractional PL change in readout 2 relative to readout 1 is

  Delta_PL / PL = -C * P_res = -0.219.

On the observed approximately 52-count baseline, this is an expected resonant dip of about

  52 * 0.219 = 11.4 counts.

For nonzero detuning, the explicit two-level square-pulse model is

  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) *
             sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).

At a 5 MHz detuning this gives about P = 0.75, still implying a roughly 16% PL dip, and at 10 MHz detuning it gives about P = 0.27, implying a roughly 6% PL dip. Therefore, if a resonance lay within the scan range, the 5 MHz sampled data should show a large negative feature over one or more neighboring points.

Observed normalized post-pulse contrast:

I evaluated (readout2 - readout1) / readout1 over the 21 scan points. The mean is -0.0012, the most negative value is -0.0310 at 3.905 GHz, and the most positive value is +0.0405. Thus the largest observed dip is only about 3.1%, far below the expected approximately 22% on-resonance response and below even the expected response for points several MHz away from resonance.

The per-average traces fluctuate at the count-scale level and stored averages are not a strong independent repeatability test here. The combined readouts also show no model-consistent broad Rabi-pulse dip: readout 2 is sometimes above readout 1, sometimes below, with no feature approaching the expected amplitude. This is inconsistent with a present pODMR resonance under the active pulse sequence and stated setup calibration.

Decision: resonance_absent.
