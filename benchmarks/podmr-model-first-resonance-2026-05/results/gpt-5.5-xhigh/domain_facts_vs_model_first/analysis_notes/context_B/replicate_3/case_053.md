Case: podmr_039_2026-05-16-221215

Input used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:

- Active sequence file: Rabimodulated.xml.
- Scanned variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz, so the requested 52 ns pulse is rounded as
  round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- mod_depth = 1.
- full_expt = 0, so the optional "1 level reference" branch is inactive.
- Readout 1 role: after adj_polarize and before any microwave pulse, therefore
  a true m_S = 0 fluorescence reference.
- Readout 2 role: after rabi_pulse_mod_wait_time(length_rabi_pulse,
  mod_depth), therefore the pODMR signal readout after the microwave pulse.

Physical model calculation:

For this setup, f_Rabi ~= 10 MHz * mod_depth. With mod_depth = 1 and pulse
duration t = 52 ns, f_Rabi = 10 MHz. The resonant transfer probability for a
square Rabi pulse is

  P(+1 | resonance) = sin^2(pi * f_Rabi * t)
                    = sin^2(pi * 10e6 * 52e-9)
                    = 0.996.

Using the setup contrast scale C ~= 0.22 between m_S = 0 and m_S = +1, the
expected signal/reference fractional change on resonance is

  Delta S / R0 ~= -C * P = -0.22 * 0.996 = -0.219.

The mean readout-1 reference is about 49.35 raw units, so the expected
on-resonance signal drop is about

  49.35 * 0.219 = 10.8 raw units.

For detuning, I used the square-pulse model

  P(df) = (Omega^2 / (Omega^2 + Delta^2))
          * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz and Delta = 2*pi*df. The measured normalized
contrast was y = readout2/readout1 - 1.

Measured comparison:

- The measured y range is -0.049 to +0.087.
- The largest observed negative raw signal-reference difference is -2.54 raw
  units, much smaller than the approximately -10.8 raw units expected for an
  in-window resonant pi pulse.
- A least-squares fit of y = b - A*P(df, center), allowing the resonance
  center to vary and requiring A >= 0, gives A ~= 0.0469 at about 3.915 GHz.
  This is only about 21% of the expected A ~= 0.219 depth.
- The unconstrained fit prefers the opposite sign around 3.885 GHz
  (A ~= -0.0516), which is not the physical pODMR dip expected for this
  readout ordering.
- If the full expected A = 0.22 contrast is enforced, any in-window resonance
  would predict much deeper dips than observed. The best fixed-depth fit moves
  the center outside the scan, near 3.936 GHz, and only describes a weak edge
  shoulder rather than a resolved pODMR resonance.
- The per-average signal-reference differences have standard deviations of
  about 2.33 and 1.42 raw units across frequency. Stored averages here are
  tracking-cadence snapshots rather than a strong independent repeatability
  test, so the small few-unit excursions are not enough to override the
  expected pi-pulse signal scale.

Decision:

The active sequence should produce a large negative signal-readout dip if a
pODMR resonance is present in the scan. The measured differential signal is
much too shallow and does not quantitatively match the expected detuned Rabi
response for a contained resonance. I therefore classify this case as
resonance_absent.
