Sequence interpretation:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to
3.925 GHz in 5 MHz steps. The provided sequence XML has full_expt = 0, so the
optional +1 reference block is skipped. The two active detections are therefore:

1. readout 1: polarized m_S = 0 reference after adj_polarize and before the
   scanned microwave pulse.
2. readout 2: signal after a modulated Rabi microwave pulse and then detection.

The active pulse is length_rabi_pulse = 52 ns with mod_depth = 1. With the stated
setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is close
to a pi pulse. If a resonance were present, the post-pulse signal should show a
large fluorescence reduction relative to the m_S = 0 reference, potentially on
the order of the 22% setup contrast for a strong transition.

Data assessment:

The combined readout 2 / readout 1 ratio ranges only from about 0.958 to 1.053,
with mean about 0.997. The deepest negative points are isolated and not a
coherent resonance-shaped dip across the scan. The raw readouts both show
point-to-point scatter and slow variation, and the two stored averages mainly
show offset/tracking changes rather than a repeatable resonance feature. There
is no centered, robust post-pulse fluorescence loss comparable to what the
near-pi pulse should produce on resonance.

Decision: resonance absent.
