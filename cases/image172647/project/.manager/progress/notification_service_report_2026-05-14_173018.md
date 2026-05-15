NVプロジェクト進捗報告（自動・詳細）
プロジェクト: nv23_aligned_nv_t2star_13c_image172647_20260514_1728
目的: image172647 の範囲から磁場整列したNVを見つけ、T2* と 13C について根拠ある結論まで進める。

実験状況:
- 実機ブリッジは現在 running 1 / queued 0 / staging 0。稼働中は Ramsey/T2star scout `nv23_ramsey_20260514_201034_auto_ramsey` です。
- ジョブ内容は `auto__ramsey` / `ramsey.xml`、`reimage1804_c02` に対して tau 0..8 us、43点、det=1.5 MHz、mw_freq=3.876461010 GHz、8 averages x 50000 reps。T2* と 13C FFT確認のための scout です。
- 最新の直接確認では status は running、phase は `run_experiment_average_start`、表示は `(2/8) averages completed`、更新時刻はログ上 20:36:36、final count は 44.698 kcps。queued/staging は空で、stop request や monitor error はありません。
- first-average autosave は raw-export 済みです。構造は見えますが、低周波成分が強く、平均間の再現性がまだないため、T2* も 13C も未結論です。

ここまでの直接証拠:
- 初期候補 `image172647_c01` は一度 TrackCenter 41.984 kcps で成功しましたが、その後 pODMR 実行前アラインで 3.420 kcps、即時retrackでも 3.278 kcps と低カウントになりました。これは「共鳴なし」ではなく、位置/鮮度/トラッキングの証拠として扱われています。
- 元領域を再imageし、`reimage1804_c01` は TrackCenter 39.331 kcps で成功。ただし terminal strong-pi pODMR は健康なカウントにもかかわらず raw/fitted-reference の落ち込みが約4-5%で、期待される約22%強πコントラストに届かず、整列候補から reject されています。
- 次候補 `reimage1804_c02` は TrackCenter 39.690 kcps で成功。terminal strong-pi pODMR 4 averages x 50000 reps では、reference に対応するdipがなく、signal-only resonance が 3.875 GHz 近傍に出ました。Gaussian center は 3.876461 GHz、共分散由来不確かさは約0.69 MHz、FWHM 約11.2 MHz、深さは raw/fitted-reference で約13.8-14.0%。期待22%より低い caveat はありますが、`c01` より明確で、aligned NV branch として accept 済みです。

実験以外の研究/プロジェクト作業:
- bridge-free の terminal review protocol は準備済みです。内容は、raw/readout-aware review を先に行うこと、Ramsey信号が見えるまでT2* fitをしないこと、FFTでは det=1.5 MHz carrier と 13C Larmor由来の sideband 近傍（約1.115 MHz / 1.885 MHz）を見ること、孤立した低SNRピークだけで13Cを主張しないことです。
- 最初の Ramsey案（51点、4x100000 reps、det=2 MHz）は advisory の per-average window 742 s が昼間cap 600 sを超えたため、実行前に supersede されています。現在の43点・8x50000 reps案は advisory上 581.8 sでcap内でした。
- 明示的な bridge-free pending task は現時点ではありません。bridge occupancy により新しい bridge-touching work はブロック中です。opportunity-review が走る場合は、science-objective work first として terminal review準備、evidence gap整理、モデル/FFT判定基準の補強などから必要分を切り出す想定です。

最新の判断:
- aligned NV は `reimage1804_c02` として一旦確立。ただしpODMRコントラストが期待より低いため、T2*/13C interpretation では慎重に扱う。
- T2* と 13C はまだ未確定。first-average Ramsey snapshot は参考情報であり、claim-grade evidence ではありません。
- 実行中ジョブは健康に見えるので、止めずに terminal result またはより進んだ autosave を待つのが次の安全な一手です。

次の期待ステップ:
Ramsey scout が terminal になったら savedexperiment を raw export し、raw readouts / fitted-reference normalization / pointwise normalization を比較します。そのうえで、実信号が見える場合のみ T2* fit を行い、FFTで 13C sideband 候補を確認します。失敗前終了なら、T2*/13C証拠とは解釈せず、route・tracking・count freshness を分けて診断します。