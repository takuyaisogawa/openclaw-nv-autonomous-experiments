<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_021

Files used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The active sequence is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction sequence first
polarizes and detects a true m_S = 0 bright reference, then waits, then applies
a modulated Rabi microwave pulse, and then detects again. The optional
"Acquire 1 level reference" block is inside "if abs(full_expt)>1e-12"; the
active full_expt value is 0, so that block is skipped. Therefore readout 1 is
the bright m_S = 0 reference and readout 2 is the post-pulse pODMR signal.

The active values are:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, which leaves 52 ns exactly on the sampled grid
- microwave pulse function: rabi_pulse_mod_wait_time(..., length_rabi_pulse,
  mod_depth, ...)

Physical model calculation

Given the stated setup facts, the Rabi frequency is about 10 MHz at
mod_depth = 1. For a resonant square pulse, the population transferred from
m_S = 0 to m_S = +1 is

P1(Delta = 0) = sin^2(pi * f_Rabi * t).

With f_Rabi = 10 MHz and t = 52 ns:

pi * f_Rabi * t = pi * 10e6 * 52e-9 = 1.6336 rad
P1 = sin^2(1.6336) = 0.9961.

The stated fluorescence contrast between m_S = 0 and m_S = +1 is about 22%.
Thus the expected on-resonance fractional signal loss in readout 2 relative to
the bright reference is

0.22 * 0.9961 = 0.2191, or 21.9%.

For a typical bright readout near 40 counts, the expected resonant readout-2
drop is about

40 * 0.2191 = 8.77 counts,

giving an expected readout-2 value near 31.2 counts.

I also evaluated the detuned square-pulse model

P1(Delta) = (Omega^2 / Omega_eff^2) * sin^2(Omega_eff * t / 2),
Omega_eff = sqrt(Omega^2 + Delta^2),

with Omega = 2*pi*10 MHz and Delta = 2*pi*(mw_freq - center). Fitting the
measured normalized deficit (readout1 - readout2) / readout1 against this
lineshape over a center-frequency grid gives a best center near 3.878 GHz, an
amplitude multiplier of 1.05 relative to the 22% contrast model, and a small
baseline deficit of about 0.5%.

Observed signal

The strongest feature is at 3.880 GHz:

- readout 1 = 40.1923
- readout 2 = 30.7885
- drop = 9.4038 counts
- normalized deficit = 9.4038 / 40.1923 = 0.2340, or 23.4%

This is close to the modeled expected resonant deficit of 21.9%. Away from the
feature, the fitted far-detuned residual scatter is about 3.3% in normalized
deficit, so the central deficit is roughly 7 sigma above that residual scale.
The per-average traces both show the same central readout-2 dip, but I do not
treat the stored averages as a strong independent repeatability test because
they may reflect tracking cadence.

Decision

A pODMR resonance is present. The readout roles and pulse parameters imply a
near-pi pulse on resonance, the expected fluorescence drop is about 8.8 counts
from a 40-count bright reference, and the measured central drop is about
9.4 counts with the correct readout polarity and frequency-localized shape.
