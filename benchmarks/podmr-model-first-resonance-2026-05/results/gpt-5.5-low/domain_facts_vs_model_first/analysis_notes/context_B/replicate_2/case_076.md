Case podmr_062_2026-05-17-063134

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels,
previous outputs, sibling cases, or external context.

Active pulse sequence and readout roles

The provided sequence is Rabimodulated.xml. The active instructions are:

- polarize with adj_polarize
- detection before the microwave pulse
- wait_for_awg
- the optional 1-level reference block is skipped because full_expt = 0
- rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth
- detection after the pulse

Therefore readout 1 is the polarized m_S = 0 reference. Readout 2 is the
post-Rabi-pulse readout. It is not an independent m_S = +1 reference because
the full_expt branch is inactive.

Sequence parameters from inputs/sequence.xml:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- swept variable = mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- sample_rate = 250 MHz, so 52 ns rounds to 52 ns exactly at the AWG grid

Explicit physical model calculation

Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1 and
scales linearly with mod_depth. For this sequence:

f_Rabi = 10 MHz
t_pulse = 52 ns
theta = 2*pi*f_Rabi*t_pulse = 3.267 rad = 187.2 deg
P_transfer = sin^2(theta/2) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22 percent, so a
resonant post-pulse readout should be lower than the pre-pulse m_S = 0
reference by:

expected fractional change = -0.22 * 0.996 = -0.219

The mean readout 1 level is 49.411 counts, giving an expected on-resonance
drop of:

49.411 * 0.219 = 10.83 counts

Observed quantitative comparison

Using readout 2 minus readout 1 across the 21 frequency points:

- mean difference = +0.033 counts
- standard deviation across scan points = 1.252 counts
- most negative point = -3.154 counts at 3.920 GHz
- most negative fractional point = -6.26 percent

The largest observed dip is much smaller than the approximately 10.8-count
drop expected for an on-resonance near-pi pulse in this setup. The data also do
not show a coherent resonance-shaped feature in which readout 2 is strongly
suppressed relative to readout 1. Stored averages are not treated as a strong
independent repeatability test because they can reflect tracking cadence.

Decision

The expected pODMR signal from the active pulse model is large, but the observed
post-pulse readout remains near the m_S = 0 reference with only small scan-scale
fluctuations. I decide resonance_absent.
