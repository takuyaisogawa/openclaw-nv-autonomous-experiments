NVプロジェクト進捗報告（自動・詳細）
プロジェクト: `nv23_aligned_nv_t2star_13c_image172647_20260514_1728`
目的: image172647 の範囲から磁場に沿ったNVを見つけ、T2* と近傍 13C の有無/結論を十分な根拠で決める。

**実験状況**
- 直接確認した最新の bridge 状態では、`reimage1804_c02` の strong-pi pulsed ODMR が `running/` に残っています。ジョブIDは `nv23_pulsed_odmr_rabimodulated_v1_20260514_191847_reimage1804_c02_strong_podmr`。
- `queued/` は 0 件でした。
- ただし注意点として、`status.json` の最終更新は `2026-05-14T19:25:53`、phase は `run_experiment_scan_point`、進捗は `average_index=1/4` のままです。現在時刻との比較では更新が古く、予定実行時間（約1978 s）より長く見えるため、次の監視では「完了済みなのに移動されていない」のか「実際に stuck running なのか」を確認する必要があります。今回は reporting-only のため、queue の停止・移動・再投入はしていません。

**ここまでの実験結果**
- 最初の `image172647_c01` は一度 TrackCenter が 41.984 kcps で通りましたが、その後の pODMR 実行前 AlignNV で 3.420 kcps、直後の単独 retrack でも 3.278 kcps となり、データ取得前に失敗しました。これは「共鳴なし」ではなく、count/freshness/tracking 由来の証拠です。
- そのため元の image172647 範囲を fresh re-image し、明示的な `ImageData_YXZ` / kcps 軸で候補を再ランキングしました。
- `reimage1804_c01` は TrackCenter 39.331 kcps で通り、4-average strong-pi pODMR は健康なカウントで完了しましたが、raw signal / fitted-reference の depression が約4–5%に留まり、期待される strong-pi contrast 約22%に対して小さすぎました。弱い normalization-only feature は採用せず、この branch では `reimage1804_c01` を reject 済みです。
- 次候補 `reimage1804_c02` は TrackCenter 39.690 kcps で通り、tracked position は `[117.4211443249154, 117.27496844942901, 115.55260043233898] um`。この候補について現在の strong-pi pODMR が terminal review 待ちです。

**研究・プロジェクト作業状況**
- T2* / 13C へ進む条件付き計画は作成済みです。ただしこれは「pODMR terminal review で明確に使える共鳴が見つかった場合のみ」の計画です。
- その計画では、現在の ms=+1 遷移近傍 3.875 GHz から B ≈ 35.86 mT、13C Larmor ≈ 384 kHz を見積もっています。Ramsey scout は 0..8 us / 51点なら 5 MHz detuning では FFT alias の恐れがあるため、2 MHz detuning を初期案にする、という判断が記録されています。
- 明示的に pending の bridge-free task は現在ありません。次の opportunity-review では、bridge が idle/terminal になった時点で、science-objective work first として terminal pODMR の raw/readout-aware review、evidence gap 整理、または Ramsey/T2*/13C 条件の具体化を切り出す想定です。

**最新の判断**
- 直接証拠: `reimage1804_c01` は terminal strong-pi pODMR の実データレビューにより reject。
- 直接証拠: `reimage1804_c02` は tracking 済みで、pODMR job は `running/` に存在。
- 推論/注意: status 更新が古く、予定時間より長く見えるため、次は terminal result の有無と stuck-running 状態を慎重に分けて確認する必要があります。

**次の期待ステップ**
1. `reimage1804_c02` pODMR の bridge 状態を確認し、done/failed/running-stale を判定。
2. 完了データがあれば savedexperiment を export し、raw signal/reference と安全な normalization を比較して、明確に使える共鳴か判断。
3. 共鳴が明確なら同じNVに集中して Ramsey/T2* と 13C FFT へ進む。明確でなければ `reimage1804_c02` を reject し、fallback の `reimage1804_c03` へ進む。
