Active sequence:
- Sequence file: Rabimodulated.xml.
- Active experiment path: full_expt = 0, so the optional mS=+1 reference block is disabled.
- The sequence first polarizes the NV and detects the bright mS=0 reference, waits, then applies a modulated Rabi microwave pulse and detects the signal readout.

Readout roles:
- Readout 1 is the true mS=0 / bright reference acquired immediately after optical polarization.
- Readout 2 is the post-microwave signal readout after the Rabi pulse.
- Because full_expt is zero, there is no separate active mS=+1 reference readout in this measurement.

Pulse settings:
- mod_depth = 1 in the provided sequence XML.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s.
- With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is approximately a pi pulse. On resonance it should produce near-maximal population transfer and a large fluorescence drop, up to the setup contrast scale of about 22%.

Data assessment:
- Readout 1 stays comparatively flat near 35-37 counts across the scan.
- Readout 2 has a broad, signal-specific dip centered around 3.875-3.880 GHz, falling to about 28.2 counts while nearby/off-resonance values are mostly around 35-37 counts.
- The minimum signal/reference ratio is about 0.764 at 3.880 GHz, a roughly 23.5% drop relative to the simultaneous bright reference. This is very close to the expected mS=0 to mS=+1 contrast for a pi-scale pulse in this setup.
- The feature appears in the combined signal readout and is visible across the stored averages, but I do not treat the two stored averages as a strong independent repeatability test because they may reflect tracking cadence.

Decision:
The scan contains a clear pODMR resonance: the post-pulse readout shows a large, localized contrast dip at the expected scale while the bright reference readout does not show a matching artifact.
