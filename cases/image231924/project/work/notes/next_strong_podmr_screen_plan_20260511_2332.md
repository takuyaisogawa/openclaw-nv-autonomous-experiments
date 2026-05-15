# Next strong-pi pulsed ODMR screen plan (2026-05-11 23:32)

## Question
What should happen after `image231924_c01` TrackCenter terminal evidence is available?

## Inputs read
- Human advice: use strong pi pulsed ODMR to judge magnetic-field alignment; keep search-screen measurement points around 20-30.
- `NV_RESEARCH_MEMORY.md`: strong-pi pulsed ODMR is the default resonance-presence screen; accurate `mw_freq_hz` needs weak-pi later if required.
- `NV_RESEARCH_KNOWLEDGE.md` Experiment Defaults / Shot Budget / Drift sections.
- Live manifest: `claw/sequence_manifests/staging/pulsed_odmr_rabimodulated_v1.json`.
- Live XML: `SavedSequences/SavedSequences-AWG/Rabimodulated.xml`.

## Action taken
Bridge-free route review only; no pODMR job was submitted because TrackCenter is currently running and the candidate has not yet been confirmed trackable.

## Result
If `image231924_c01` TrackCenter succeeds with healthy counts, the next bridge-touching step should be a bounded strong-pi pulsed ODMR alignment screen using:
- manifest/catalog: `pulsed_odmr_rabimodulated_v1` / `Rabimodulated.xml`
- scan variable: `mw_freq`
- suggested screen grid: about 25 points over an approximately 100 MHz window around the current aligned-NV resonance region near 3.875 GHz, adjusted by any fresher resonance/drift evidence at submit time
- strong-pi settings to set explicitly: `mod_depth=1.0`, `length_rabi_pulse=52e-9` unless fresher Rabi evidence changes the current pi pulse, `mw_ampl=-5`, `ampIQ=5`, `freqIQ=50e6`, `switch_delay=100e-9`
- averages: even count by default, likely `averages=2` for a screening pODMR unless advisory/drift caps require changing repetitions/averages
- do not include automatic `analysis.fit_kind` in the bridge job; analyze terminal savedexperiment/raw readouts first

XML readout/protocol notes from `Rabimodulated.xml`:
- readout 1 is the `m_S=0` reference.
- with `full_expt=0` (manifest default), the `m_S=+1` reference block is skipped, and the final readout after the Rabi pulse is the signal.
- `do_adiabatic_inversion` is declared but the active adiabatic-inversion block is commented out in the current XML.

## Checks actually performed
- Verified the live pODMR staging manifest allows `mw_freq` 1D scans and points up to 201.
- Verified the live XML active path includes the Rabi pulse followed by signal detection and that relevant variables are present.

## Remaining uncertainty
- The exact pODMR center/range should be chosen at submit time from the latest field/resonance context and any just-completed TrackCenter evidence. A bright image candidate is not alignment evidence.

## Next pointer
After the running TrackCenter job reaches terminal state, review final counts/tracked position. If successful, queue/verify/execute the strong-pi pODMR screen; if failed, use `image231924_candidate_list.json` to TrackCenter the next candidate.
