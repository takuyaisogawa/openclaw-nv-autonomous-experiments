NVプロジェクト進捗報告（自動）
project: nv23_aligned_nv_t2star_13c_image145844_20260513_1507
目的: image145844範囲から磁場整列NVを見つけ、T2star と 13C について根拠ある結論を出す。

実験状況:
実機は現在、2回目の Ramsey/T2star/13C follow-up を実行中です。running job は `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`。live status の直接読取では、2026-05-13 21:00:16 更新時点で state=running、phase=run_experiment_average_start、`(1/8) averages completed`、Final = 43.445 kcps、経過 640 s、stop requested なし、monitor error なしです。条件は validated `auto__ramsey` / `ramsey.xml`、tau 0..8 us を 41 points、mw_freq=3.8759 GHz、det=1.0 MHz、8 averages x 50000 repetitions。autosave は有効ですが、この status では autosave target exists=false なので、現時点では terminal 前の raw-export はまだ根拠として使っていません。

ここまでの直接 evidence:
r03 は strong-pi pODMR と weak-pi pODMR で usable resonance が確認済みです。さらに fine weak-pi pODMR terminal review で、combined raw signal、point-wise ratio、reference-line normalization がすべて 3.8759 GHz で最小になり、raw drop は edge median 比で約 11.9%、per-average raw minima は 3.8759/3.8760 GHz に分かれ、scan-order-aware drift flags は 0 でした。このため、次の Ramsey 入力周波数として `mw_freq_hz=3.8759e9` を採用しています。ただし、これは grid-supported center であり、sub-grid precision の主張ではありません。

直近の agent/project 判断:
20:59:30-04:00 の project agent completion では、fine pODMR の terminal result コピー、intent 完了、raw/readout-aware review、state/log/evidence 更新を終えたうえで、det-shifted Ramsey follow-up をモデル化・advisory確認・submit しました。bridge はこの Ramsey job で占有中なので、terminal まで追加の bridge-touching submission は止めています。

科学的な現状と caveat:
磁場整列候補としては `image145844_reimage_r03` を採用中です。一方で、T2star と 13C はまだ未確定です。前回の Ramsey scout は analyzable で drift flags もありませんでしたが、spectral content は弱く、最強の exploratory component が programmed det=1.5 MHz ではなく約 0.884 MHz 付近、かつ stored averages が一致しなかったため、claim-grade ではありませんでした。今回の det=1.0 MHz / 8 us / 8 averages は、carrier が 1.0 MHz に出るか、13C sideband が約 0.615/1.385 MHz 近傍に出るか、また前回の ~0.884 MHz 成分が固定artifact/noiseかを切り分ける目的です。ここは推論込みの設計意図で、結論は terminal raw/FFT review 後に限ります。

実験以外の研究/project work:
backlog は空で、明示的な pending bridge-free task は現在ありません。bridge-free に進められる解析は、terminal data または autosave raw-export が利用可能になってから意味が出ます。次回の opportunity-review では、science-objective work first の方針で、terminal 待ちの間にも解析・モデル計算・evidence gap 整理などに切り出せる仕事がないか確認する想定です。

次の expected step:
この Ramsey が terminal になったら、job/result/status/control と batch state を project 側へコピーし、intent を完了させ、savedexperiment を raw-export、scan-order-aware drift を実行します。その後、raw readout、point-wise ratio、reference-line normalization、per-average consistency、FFT/least-squares amplitudes を 1.0 MHz、1.0 MHz +/- f13C、前回の ~0.884 MHz で確認してから、T2star/13C を主張できるか判断します。現時点の推奨は wait for terminal review です。