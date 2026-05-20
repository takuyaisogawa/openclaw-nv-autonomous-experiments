# Analysis note

Case: podmr_073_2026-05-17-090948

The provided sequence XML is Rabimodulated.xml. The active instruction path is:

- `adj_polarize(...)`
- `detection(...)`
- `wait_for_awg(...)`
- optional "Acquire 1 level reference" block skipped because `full_expt = 0`
- `rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)`
- `detection(...)`
- final wait

Readout roles:

- readout 1 is the bright `m_S = 0` reference immediately after polarization
- readout 2 is the signal readout after the Rabi-modulated microwave pulse
- no separate `m_S = +1` reference is acquired, because the reference block is inactive

Active sequence parameters used for the physical model:

- `mod_depth = 1`
- `length_rabi_pulse = 52 ns`
- `sample_rate = 250 MHz`, so 52 ns is 13 samples and the rounding in the XML does not change the pulse duration
- scan range is 3.825 GHz to 3.925 GHz in 5 MHz steps

Quantitative model:

For a rectangular resonant Rabi pulse, I used

`P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))`

with `f_R = 10 MHz * mod_depth = 10 MHz`, `t = 52 ns`, and the setup contrast scale `C = 0.22`. The expected normalized signal readout is

`readout2 / readout1 = 1 - C * P(Delta)`.

Model values:

- Delta = 0 MHz: `P = 0.996`, expected drop = 21.9%, expected ratio = 0.781, about 10.96 raw-count units for a 50-count bright reference
- Delta = 2.5 MHz: `P = 0.929`, expected drop = 20.4%, expected ratio = 0.796
- Delta = 5 MHz: `P = 0.749`, expected drop = 16.5%, expected ratio = 0.835
- Delta = 10 MHz: `P = 0.273`, expected drop = 6.0%, expected ratio = 0.940
- Delta = 15 MHz: `P = 0.0117`, expected drop = 0.26%, expected ratio = 0.997

Therefore, if the scan crossed a pODMR resonance, this sequence should produce a large down-going feature in readout 2 relative to readout 1, typically one or two scan points with an order-10-count suppression near line center.

Data comparison:

- mean readout 1 = 50.167
- mean readout 2 = 50.045
- mean normalized contrast `(readout1 - readout2) / readout1` = 0.00222
- standard deviation of that contrast across scan points = 0.0217
- largest positive contrast point = 0.0496 at 3.855 GHz
- minimum observed `readout2 / readout1` ratio = 0.9504

I also checked the model fit against the normalized ratio. A free-amplitude Rabi-line fit within the scan prefers only a 0.0233 contrast amplitude, about one tenth of the expected 0.22 physical contrast. A fixed-contrast 22% Rabi line shape constrained to the scan window has RSS 0.0749, while a flat baseline has RSS 0.00943, so the physically expected resonance model is much worse than no resonance.

The stored averages are not treated as a strong independent repeatability test, since they can reflect tracking cadence. They also do not show the large readout-2 suppression predicted by the active pulse sequence.

Decision: pODMR resonance absent.
