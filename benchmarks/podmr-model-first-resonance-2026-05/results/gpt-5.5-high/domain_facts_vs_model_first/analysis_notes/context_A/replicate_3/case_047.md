The active sequence is Rabimodulated.xml / Rabimodulated varying mw_freq. With full_expt = 0, the sequence first polarizes and detects the true mS = 0 reference, then applies one rabi_pulse_mod_wait_time pulse and detects the signal. Therefore readout 1 is the mS = 0 reference and readout 2 is the microwave-pulsed signal; there is no active mS = +1 reference branch in this run.

The provided sequence XML gives mod_depth = 1 and length_rabi_pulse = 52 ns. With the setup fact of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is approximately a pi pulse. If the swept mw_freq crosses a real pODMR resonance, the second readout should drop strongly relative to the first readout, on the order of the known 22% mS = 0 to mS = +1 contrast scale.

The combined raw data do not show that behavior. The second/first readout ratio stays close to unity, with the deepest apparent reduction around 0.973 and several neighboring or other points above 1. The small sign-changing differences are only a few percent, much smaller than the expected near-pi resonance response, and the per-average traces show large baseline/tracking shifts that can explain small point-to-point structure. Stored averages are only two and are not a strong independent repeatability check here.

Decision: resonance absent.
