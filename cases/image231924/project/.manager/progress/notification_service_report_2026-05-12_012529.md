NVプロジェクト進捗報告（自動）

プロジェクト: nv23_aligned_nv_t2star_13c_image231924_20260511_2319
目的: image231924 の範囲から磁場にアラインしたNVを見つけ、T2* と 13C 結合について根拠のある結論を出す。

実験状況（直接証拠）:
- 現在、c01候補で最初の Ramsey/T2star scout が実行中です。
- running job: nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute
- sequence: ramsey.xml / auto__ramsey
- status更新: 2026-05-12 01:41:31 EDT
- phase: run_experiment_scan_point
- 進捗表示: 1/4 averages completed（51 tau points, 100000 repetitions/average）
- 経過時間: 約21分。見積もり総時間は約55分、残りは粗く約34分です。
- counts: 実行前auto-alignは Final = 26.171 kcps、最新status上のFinalは 24.290 kcps。現時点でcount collapseやstop request、monitor errorは見えていません。
- autosave: 1DExp-seq-ramsey-vary-tau-2026-05-12-012318。1 average時点のMATはraw export済みで、in-progress reviewが作られています。

ここまでの科学的状態:
- image231924_c01 はTrackCenterで追跡可能で、strong-pi pODMR retryにより ms=+1 側の可視共鳴が確認されました。
- その後の weak-pi pODMR review では、Ramsey計画用の中心として mw_freq = 3.8758666667 GHz、grid/noise limitedで約 +/- 1 MHz が使える、という判断です。これはサブMHz精密校正ではありません。
- 現在のRamsey設計は tau 0..8 us、51点、det = 2 MHz、4 averages x 100000 reps。弱pi中心からの事前計算では Bz 約359 G、13C Larmor 約384 kHzなので、FFT上では2.000 MHz carrier近傍と、可能なら約1.616 / 2.384 MHzの13C sideband窓を確認する方針です。

途中解析（直接証拠＋推論の区別）:
- 直接証拠: 1 average autosaveのraw exportは成功し、51点のtau gridとsnake scan orderが確認されています。readout 1はmS=0 reference、readout 2はpost-Ramsey signalとして扱っています。
- 直接証拠: readout 1にはscan内のゆっくりした下向き傾向があるため、点ごとの単純normalizationだけでなく、reference fitで補正した表示/FFTを確認しています。
- 推論: 1 averageのnormalized traceは振動的に見え、FFTにも期待していたlower-sideband/carrier領域（例: 1.59 MHz, 1.96 MHz付近）にpowerがあります。ただし、これは「続行する価値がある」程度の途中証拠です。
- caveat: 1 averageだけではT2*値も13C結論もまだ支持されません。average間の安定性、最終SNR、driftの影響はterminal dataで再評価が必要です。

実験以外の研究・プロジェクト作業:
- backlog.json は現在空で、明示的なpending research_taskはありません。
- 実験中に今すぐ進める明示的なbridge-free taskもありません。直近では、Ramsey FFT expectationの記録と1-average autosave reviewが完了しています。
- 次のopportunity-reviewでは、terminal結果を待つだけでなく、必要ならscience-objective work firstとして、解析、モデル計算、文献/過去結果比較、evidence gap整理から1-3件を切り出す想定です。

直近のagent判断:
- image231924_c01を現在のaligned NV候補として採用し、strong-pi pODMRはalignment pass、weak-pi pODMRはRamsey用中心のrefinementとして扱う判断です。
- 最新の実行判断は、FFT-aware Ramsey/T2star scoutをsubmitし、実機jobを走らせたことです。その後のbridge-free reviewでは、1 average途中データは継続に値するが結論には不十分、と整理しています。

次の期待ステップ:
- まずrunning Ramsey/T2star scoutのterminal resultを待ちます。
- 完了後、final savedexperimentをraw exportし、raw/readout-awareなRamsey信号確認、actual tau gridでのFFT、T2*と13Cの独立評価を行います。
- terminal結果が非claim-gradeでもcounts/trackingが健全なら、c01をすぐ捨てず、観測されたSNR・drift・FFT分解能に基づいてRamsey repeat条件を再設計します。