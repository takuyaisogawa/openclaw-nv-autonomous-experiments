NVプロジェクト進捗報告（自動・詳細）
Project: nv23_aligned_nv_t2star_13c_image231924_20260511_2319
状態: active

実験状況（直接確認）:
現在、corrected-center Ramsey/T2star repeat が実機で running です。
job は `nv23_image231924_c01_corrected_center_ramsey_repeat_20260512_032137_image231924_c01_corrected_center_ramsey_repeat_20260512_0320_execute`、sequence は `ramsey.xml`、phase は `run_experiment_scan_point`。status.json の最終更新は 2026-05-12 03:46:21 EDT でした。

進捗は `(1/6) averages completed`、つまり 6 averages 中 1 average 完了です。条件は tau = 0..8 us、51 points、100000 repetitions/average、合計 600000 shots 予定。経過時間は 1468 s（約24.5分）で、runtime estimator は総計 4929 s（約82.2分）、1 average あたり約817 s と見積もっています。単純計算では残りは約57-58分です。runtime final counts は `Final = 27.690 kcps`、monitor は active、tick_count 147、last_error は空、stop_requested は false です。現時点で監視上の異常や停止要求は見えていません。

補足として、開始時の auto-align は `23.416 kcps` で通過し、pre-enqueue advisory も blocker なしでした。status には autosave target `...savedexperiments\NV1\1DExp-seq-ramsey-vary-tau-2026-05-12-032449` が記録されていますが、この snapshot では `autosave_target_exists=false` と表示されています。したがって、途中 raw export ではなく、ここで述べている進捗・counts は status.json 由来の直接 evidence です。

直近の研究判断（直接 evidence + agent review）:
前回の terminal Ramsey scout では、raw と fitted-reference normalization の両方で約 1.593 MHz の強い Ramsey oscillation が見えていました。ただし、このピークは「13C sideband らしい候補」ではあっても、前の弱π pODMR center の不確かさ内にある residual detuning でも説明可能でした。そのため T2star は 3.6-4.4 us 程度の candidate fit only、13C は candidate-only/unresolved と分類されていました。

その後の narrow weak-pi pODMR center refresh は成功し、raw signal と fitted-reference-normalized minimum が `3.8761166667 GHz` で一致しました。これは以前の weak-pi center より +0.250 MHz（pointwise ratio では +0.500 MHz も許す）ずれており、古い 1.593 MHz Ramsey peak は 13C ではなく、programmed det=2 MHz に対する残留 detuning 由来だった可能性がかなり高くなりました。この判断に基づいて、現在の corrected-center Ramsey は `mw_freq=3.8761166667 GHz` で走っています。

現時点の claim 状態:
- aligned/resonant NV: c01 は strong-pi + weak-pi/narrow weak-pi pODMR により、対象候補として継続する根拠あり。
- microwave center: `3.8761166667 GHz +/- 約0.25 MHz` grid-scale calibration。sub-grid 精度の主張ではありません。
- T2star: まだ最終値なし。前回の 3.6-4.4 us は candidate-fit-only。
- 13C: positive claim なし。古い 1.593 MHz peak は residual detuning artifact の可能性が上がっています。negative/no-13C conclusion も、今回の corrected-center terminal data を見てからです。

実験以外の project work:
現在 backlog.json は空で、pending research_task は 0 です。実験中に明示的に進める bridge-free task もありません。bridge は running なので、新規 submission や queue mutation は行っていません。この状態では、次の opportunity-review が来たときに science-objective work first として、解析、モデル計算、文献/過去 evidence gap 整理などから必要な bridge-free work が切り出される想定です。

次の expected step:
まず corrected-center Ramsey/T2star repeat の terminal result を待ちます。完了後は savedexperiment を raw export し、raw/readout-aware Ramsey signal、実 tau grid での FFT、drift/SNR を確認します。特に carrier が intended 2 MHz bin 付近へ戻るか、13C sideband window（概算で ~1.616 / ~2.384 MHz）に残る構造があるかを分けて評価します。その結果で T2star、13C、次の det-shift diagnostic または higher-shot repeat の要否を決めます。