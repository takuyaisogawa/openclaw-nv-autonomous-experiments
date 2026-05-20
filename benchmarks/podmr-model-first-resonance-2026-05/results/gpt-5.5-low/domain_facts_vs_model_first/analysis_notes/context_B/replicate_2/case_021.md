Sequence inspection:

- Active sequence file/name: Rabimodulated.xml.
- The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- readout 1 is the true m_S = 0 reference after optical polarization and detection.
- readout 2 is the pODMR signal after a microwave Rabi pulse and detection.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this remains exactly 52 ns after rounding.

Expected signal model:

Use the given setup facts: contrast between m_S = 0 and m_S = +1 is about 22%, and the Rabi frequency is about 10 MHz at mod_depth = 1. For a square microwave pulse scanned through resonance, the driven population transfer is modeled as

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * tau)

where Omega = 10 MHz, tau = 52 ns, and delta is the frequency detuning in Hz. The expected normalized fluorescence ratio for readout 2 divided by readout 1 is then

R(delta) = 1 - 0.22 * P(delta).

On resonance, Omega * tau = 0.52 cycles, so P(0) = sin^2(pi * 0.52) = 0.996. The expected on-resonance ratio is therefore 1 - 0.22 * 0.996 = 0.781, i.e. an about 21.9% dip from the m_S = 0 reference. With 5 MHz scan spacing, the same model gives ratios around 0.835 at +/-5 MHz and about 0.94 at +/-10 MHz from resonance, so a real resonance should appear as a narrow, strong dip over a few scan points.

Observed data:

The combined readout 2 / readout 1 ratios around the dip are:

- 3.865 GHz: 37.923 / 37.673 = 1.0066
- 3.870 GHz: 35.808 / 38.808 = 0.9227
- 3.875 GHz: 31.865 / 41.808 = 0.7622
- 3.880 GHz: 30.788 / 40.192 = 0.7660
- 3.885 GHz: 34.288 / 38.577 = 0.8888
- 3.890 GHz: 38.019 / 38.673 = 0.9831

The off-dip mean ratio, excluding 3.865 to 3.885 GHz, is 0.9797 with standard deviation 0.0308. The central dip reaches about 0.762 to 0.766, equivalent to 23.4% to 23.8% contrast relative to the local reference. This is very close to the expected near-pi-pulse pODMR contrast scale of about 22%.

The two stored averages both show the same central readout-2 suppression near 3.875 to 3.880 GHz, but I treat this only as consistency with the tracking cadence caveat, not as a strong independent repeatability test.

Decision:

A pODMR resonance is present. The sign, amplitude, and width of the normalized readout-2 dip match the explicit Rabi-driven fluorescence model for a 52 ns pulse at mod_depth = 1.
