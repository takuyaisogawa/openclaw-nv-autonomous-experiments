NVプロジェクト進捗報告（自動・詳細）
プロジェクト: nv23_aligned_nv_t2star_13c_image172647_20260514_1728
目的: image172647 由来の候補から磁場整列NVを見つけ、T2star と 13C について根拠ある結論まで進める。

実験状況:
- 直近の状態では、bridge は reimage1804_c02 の Ramsey/T2star scout を実行中です。ジョブIDは `nv23_ramsey_20260514_201034_auto_ramsey`。queued/staging は空で、新しいbridge-touching実験はこのジョブが終わるまで待ちです。
- このRamseyは、受理済み候補 `reimage1804_c02` に対する改訂版 scout です。条件は `auto__ramsey` / `ramsey.xml`, tau 0..8 us, 43 points, det=1.5 MHz, mw_freq=3.876461010 GHz, 8 averages x 50000 reps。初期案の 51 points / 4x100000 reps は、advisory が per-average 742 s と見積もり、昼間の 600 s cap を超えたため実行前に破棄されています。改訂案は advisory 上 581.8 s で blockers なしでした。
- 実行後のsnapshotでは、pre-run align counts は 43.710 kcps、実行中countもおおむね健康です。ランタイム見積もりは起動後に約 656.8 s/average と出ており、これはcap超過気味ですが、実行前advisoryはOKで、すでに健康に走っているため、停止理由ではなく terminal review 時の provenance として扱われています。

ここまでの直接証拠:
- `reimage1804_c02` は TrackCenter 成功: final_counts_kcps = 39.690、位置は [117.421, 117.275, 115.553] um。
- strong-pi pODMR terminal 4 averages は完了済み。raw/readout-aware review で signal-only の明瞭な共鳴が 3.875 GHz 近傍に見え、Gaussian center は 3.876461 GHz、共分散由来不確かさは約 0.69 MHz、FWHM は約 11.2 MHz。raw/fitted-reference depth は約 13.8-14.0%。期待していた ~22% より浅いですが、reject 済み c01 の 4-5% より十分大きく、reference側に同じdipはありません。したがって c02 を aligned-NV branch として受理しています。
- Ramsey first-average autosave は raw export/plot 済みです。ただし1 averageだけなので provisional です。raw signal/reference には構造が見えますが、FFTでは低周波成分も強く、average-to-average support がまだありません。現時点では T2star も 13C も claim していません。

推論・判断:
- alignment については「c02を進める」判断は妥当です。ただし pODMR contrast が期待値より低いので、後続のRamsey/T2star解析では SNR・drift・normalization artifact に慎重に扱います。
- 13C については、3.875 GHz付近の ms=+1 resonance から期待Larmorを約384 kHzと見積もり、det=1.5 MHz の carrier に対して sideband target はおおよそ 1.115 / 1.885 MHz です。このtargetは terminal review protocol に固定済みです。ただし、孤立した低SNRピークだけでは 13C claim しない方針です。

実験以外の研究/project work:
- 明示的に pending な bridge-free task は現在ありません。bridge-freeでは terminal review protocol 作成と first-average autosave の暫定レビューがすでに完了しています。
- opportunity-review が入る場合は、science-objective work first として、解析・モデル確認・evidence gap整理などから追加作業を切り出す想定です。ただし今は running Ramsey の terminal data 待ちが主線です。
- 古い image172647_c01 の stale recovery hook は停止方針で再確認済みです。旧c01の再試行は、現在の c02 branch と競合するので進めません。

次の期待ステップ:
- Ramsey/T2star scout の terminal 完了、または次の有用な autosave を待ちます。
- terminal success なら savedexperiment を raw export し、raw readouts、fitted-reference normalization、pointwise normalization を比較して、まず信号の有無を判定します。その後、信号が十分なら T2star fit、さらに det +/- ~384 kHz 近傍のFFT/13C sidebandを慎重に確認します。
- terminal failure の場合は、T2star/13C evidence として解釈せず、route/hardware/code failure なのか tracking/count freshness なのかを分けて判断します。

添付候補: 最新のRamsey first-average autosave plot（provisional）。1 averageだけなので結論用ではなく、途中経過の視覚確認用です。
