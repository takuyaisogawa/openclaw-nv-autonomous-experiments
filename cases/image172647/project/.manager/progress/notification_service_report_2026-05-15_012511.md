NVプロジェクト進捗報告（自動）
project: nv23_aligned_nv_t2star_13c_image172647_20260514_1728

現在の主目的は、image172647 周辺から磁場に沿った NV を見つけ、その NV で T2* と 13C について根拠のある結論を出すことです。

【実験状況】
実機では det=1.0 MHz の Ramsey / T2* / 13C 判別用ジョブ `nv23_ramsey_20260514_230820_auto_ramsey` がまだ running です。直近の直接証拠では、2026-05-15 01:25:03 EDT 更新時点で 10/16 averages 完了、残り 6 averages、進捗は約 62.5% です。条件は `ramsey.xml`、tau 0..10 us、51 points、16 averages x 50000 repetitions、mw_freq = 3.876501337 GHz、det = 1.0 MHz。現在のショット量は 500k shots/point 相当で、計画 800k shots/point の途中です。Final counts は 44.971 kcps、monitor は active、last_error なし、stop_requested=false、queued/staging も空です。現時点で硬い異常や停止理由は見えていません。

【ここまでの科学的状況】
直接証拠として、reimage1804_c02 は strong-pi pODMR で信号側だけの明瞭な共鳴を示し、磁場整列候補として採用済みです。ただしコントラストは期待 ~22% より低く、terminal strong-pi では約 13.8-14.0%、terminal weak-pi refinement では中心 3.876501337 GHz、深さ約 11.4%、FWHM 約 0.94 MHz でした。以前の det=1.5 MHz Ramsey terminal は、約 1.9 MHz 付近の弱い経験的 Ramsey 振動と数 us 程度の短い T2* を示唆しましたが、早い tau 点の扱いに fit が敏感で、最終的な単一 T2* 値や 13C 結論にはしていません。

今回の det=1.0 MHz Ramsey は、その曖昧な 1.9 MHz 成分と 13C sideband を切り分けるための follow-up です。期待する比較点は direct 13C Larmor 約 0.385 MHz、det-13C 約 0.615 MHz、det carrier 1.0 MHz、det+13C 約 1.385 MHz、そして以前の曖昧な ~1.9 MHz です。

【直近の autosave 解析】
最新の bridge-free 10-average autosave review では、scan-order-aware drift 診断が `Scan.ScanOrderEachAvg` / snake order を使い、flagged average はありませんでした。readout2 / self-baseline FFT の target bins は、direct 13C 0.20%、det-13C 0.64%、carrier 0.36%、det+13C 0.82%、以前の 1.9 MHz ambiguity 0.46% です。これは直接証拠ですが、まだ running autosave かつ 10/16 averages の中間データなので、T2* も 13C も主張していません。解釈としては「異常なしで蓄積中、ただし信号はまだ弱く provisional」です。

【実験以外の project work】
pending research_task は 0 件で、実験中に明示的に進める bridge-free task も現在はありません。次の opportunity-review では、science-objective work first の方針で、解析・モデル計算・evidence gap 整理などから実験を触らず進められる作業が派生する見込みです。ただし現状の最重要待ちは、この running Ramsey の terminal/anomaly evidence です。

【直近の agent / project 判断】
最新 agent completion は 2026-05-15 01:24:20 EDT で、terminal evidence 記録フローを manager 経由で処理し、cron が pending review を継続できるよう completion marker を自動作成した、という運用上の完了です。科学的な最新判断は、det=1.0 MHz Ramsey を止めずに terminal 16-average データを待つことです。

【次の期待ステップ】
次はジョブ完了後に savedexperiment を raw export し、raw readouts、reference-aware view、signal-self-baseline view、scan-order-aware drift を確認します。そのうえで信号が十分見える場合だけ T2* fit を行い、13C については det-shift に整合する sideband 支持があるかを確認します。孤立した低 SNR peak だけでは 13C claim にしません。

添付候補として、最新 10-average autosave の途中経過プロットを 1 枚付けます。これは理解補助用で、結論用の terminal figure ではありません。