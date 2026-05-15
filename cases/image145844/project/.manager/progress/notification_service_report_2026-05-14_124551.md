NVプロジェクト進捗報告（自動・詳細）
プロジェクト: nv23_aligned_nv_t2star_13c_image145844_20260513_1507
時刻: 2026-05-14 12:46 EDT

実験状況:
現在、実機側のNV bridgeは idle です。running 0件、queued 0件で、直近のRamseyジョブ `nv23_ramsey_20260514_055148_auto_ramsey` は正常完了済みです。直接証拠として、最終レビューでは 20/20 averages、1.0e6 shots/tau、final_counts_kcps=43.433、monitor last_error 空、stop_requested=false、scan-order-aware drift は `Scan.ScanOrderEachAvg` / snake 由来で flagged averages 0 と記録されています。

実験結果の要点:
候補探索では r01/r02 は強pi pODMRで明確な使える共鳴が出ず、r03 が磁場整列候補として採択されています。r03 は TrackCenter で `[117.314436,117.761644,115.141679] um`、強pi pODMRで 3.875 GHz grid、弱pi/refresh pODMRで最終的に `mw_freq=3.8765 GHz` がグリッド支持の中心として使われました。

直近の refreshed-center 長スパンRamsey（det=1.5 MHz, tau 48 ns..8.048 us, 41点, 20x50000）は、データ品質としては解析可能でした。ただし結論は慎重です。直接証拠では、programmed 1.5 MHz carrier-like 成分は見えるものの modest で、ratio LS amplitude は full-span 0.01575、skip-first-4 で 0.01231、raw signal LS amplitude は 0.705 kcps でした。これは median per-point SEM 0.850 kcps より小さく、claim-grade のT2star値には不足です。Full/skip-transient のLS screenは 2.266-2.276 MHz 付近の high-edge 成分に支配され、固定carrierモデルより high-edge モデルがBICで有利でした。固定carrier T2star候補は order 1-3 us と推定されますが、モデル依存なので数値としては引用不可、という判断です。

13Cについても、期待される sideband 位置 1.115/1.885 MHz の振幅は 0.00278/0.00962 ratio 程度で、coherent symmetric sideband pair とは言えません。したがって現条件のRamsey/FFT/LS branchからは「近傍13C sideband/coupling の支持証拠なし」という負の結論が現在の直接結論です。

実験以外の研究・プロジェクト作業:
10:12にLaTeX/PDFの closeout/decision report が生成・検証されました。記録上は PDF header と build verification が通っており、r03 branch は「aligned NVは見つかった / claim-grade numeric T2starなし / 現条件で近傍13C支持なし」として line-complete 扱いになりました。10:14のagent完了マーカーでも、bridge queue は触っておらず、追加の自動bridge-touching workは新しい明示的protocol-development要求なしには正当化しない、とされています。

ただし、12:45に新しいinbox adviceが入り、projectは自動的に active に戻っています。直接内容は「bridge-free analysis only。追加測定はしない。最終refreshed-center Ramseyを、残留resonance-frequency calibration errorによるcarrier shiftと、そのshifted carrier周りの13C sidebandsを許して再解析し、解釈が変わればcloseout reportを書き直す」というものです。これは新しい測定要求ではなく、解析・モデル再評価の依頼です。

現在のpending backlogは0件で、明示的な bridge-free task はbacklog上まだ登録されていません。一方で推論として、次のopportunity-review / project wakeでは、この新しいadviceから bridge-free のscience-objective work（shifted-carrier + shifted-sideband model comparison、既存terminal Ramsey artifactの再評価、closeout report差分判定）が切り出される見込みです。実機は触らず、既存データだけで判断する流れです。

次の期待ステップ:
実行agentがinbox adviceを処理し、final refreshed-center Ramseyの既存raw/export・model comparisonを再読込して、carrier shiftを許したモデルが現在の結論を変えるかを確認します。結論が変わらなければcloseout維持、変わる場合はcloseout report更新、という分岐になります。添付候補として、現時点のmodel comparison図を1枚付けます。これは現closeout判断の根拠図であり、次の再解析で比較対象になります。