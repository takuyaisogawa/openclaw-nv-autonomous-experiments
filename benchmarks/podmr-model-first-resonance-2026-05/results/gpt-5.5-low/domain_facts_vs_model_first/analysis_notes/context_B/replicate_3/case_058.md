Case podmr_044_2026-05-16-232730

Sequence and roles:
- The provided XML is Rabimodulated.xml, swept over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active pulse sequence: polarize, detect the bright m_S = 0 reference, wait, apply rabi_pulse_mod_wait_time, detect the post-pulse readout, then final wait.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The data are therefore not a full independent 0/1 reference experiment; the plotted readouts are raw detection channels/roles from the active bright reference and post-Rabi measurement structure.
- mod_depth = 1 in the provided XML and variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already on the 4 ns grid.

Quantitative physical model:
- Given setup Rabi frequency approximately 10 MHz at mod_depth = 1 and linear scaling with mod_depth, f_Rabi = 10 MHz.
- The pulse rotation angle is theta = 2*pi*f_Rabi*t = 2*pi*10e6*52e-9 = 3.267 rad = 187.2 deg.
- The resonant transition probability for a square pulse is sin^2(theta/2) = 0.996, essentially a pi pulse.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a true pODMR resonance should reduce the post-pulse fluorescence by about 0.22 * 0.996 = 21.9% relative to the local bright baseline.
- The observed combined baseline is about 48.62 raw counts, so the expected on-resonance drop is about 10.65 counts, giving an expected resonant readout near 37.97 counts if the drive is on resonance and the contrast scale applies.

Observed data:
- readout 1: mean 48.56, standard deviation 1.15, min 46.63, max 50.69, range 4.06 counts.
- readout 2: mean 48.69, standard deviation 1.20, min 46.77, max 51.54, range 4.77 counts.
- Average of both readouts: mean 48.62, standard deviation 1.04, min 46.88, max 50.78.
- The largest observed downward excursion in the combined trace is only about 1.75 counts below the mean, far smaller than the approximately 10.65-count drop expected for a resonant pi pulse.
- The per-average traces differ by a broad vertical offset consistent with tracking cadence or drift; they do not provide a strong independent repeatability test.

Decision:
No pODMR resonance is present. The active sequence should have produced a large negative fluorescence feature near resonance, but the data show only small scatter/drift and no localized dip of the expected magnitude.
