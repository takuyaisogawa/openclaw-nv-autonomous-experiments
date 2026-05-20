Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles from the instruction order:
- readout 1 is the detection immediately after adj_polarize, so it is the mS=0 fluorescence reference.
- full_expt is 0, so the optional mS=+1 reference block is skipped.
- readout 2 is the detection after the modulated Rabi microwave pulse, so it is the pODMR signal channel.

Pulse settings used for interpretation:
- mod_depth is 1 in the provided sequence values.
- length_rabi_pulse is 52 ns.
- With the stated 10 MHz Rabi frequency at mod_depth=1, this is close to a pi pulse.

Expected behavior:
- On resonance, the post-pulse signal readout should drop relative to the polarized mS=0 reference.
- The setup contrast scale is about 22%, so an ideal on-resonance pi pulse could be much deeper than the observed raw feature.

Observed data:
- The combined signal/reference ratio has its strongest depression near 3.850 GHz: readout 1 is 52.58, readout 2 is 48.71, ratio about 0.927.
- Neighboring points also show depressions around 3.835 and 3.865 GHz, and there is a weaker lower-signal region around 3.895 to 3.910 GHz.
- The two stored averages both show a signal/reference depression at 3.850 GHz, but stored averages are not a strong independent repeatability test because they can reflect tracking cadence.

Decision:
The data show a plausible pODMR dip near 3.85 GHz in the correct readout direction for the active near-pi Rabimodulated sequence. The feature is shallower and noisier than the full contrast scale would suggest, but it is structured enough relative to the reference channel to call resonance present.
