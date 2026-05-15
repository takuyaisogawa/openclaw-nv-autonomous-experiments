NVプロジェクト進捗報告（自動）

プロジェクト: `nv23_aligned_nv_t2star_13c_image145844_20260513_1507`
目的: image145844 由来の磁場整列NVを見つけ、T2* と近傍 13C について根拠のある結論を出すこと。
状態: active

実験状況（直接確認）
- 実機では r03 の det-shift Ramsey 診断が実行中です。
- job: `nv23_ramsey_20260514_015423_auto_ramsey`
- sequence: `ramsey.xml` / `auto__ramsey`
- 条件: `tau = 48 ns..1.968 us`, 41 points, `mw_freq = 3.8759 GHz`, `det = 1.5 MHz`, `12 averages x 90000 repetitions`
- bridge status は 2026-05-14 04:10:55 EDT 時点で `running`、phase は `run_experiment_scan_point`。
- 進捗は status 表示で `(11/12) averages completed`。残りはおおむね 1 average です。
- Final counts 表示は `44.796 kcps`。monitor `last_error` は空、`stop_requested=false`、runtime monitor は動作中で、実験停止や監視エラーは見えていません。
- 見積もり実行時間は全体で約7853秒、1 average あたり約652秒。現在の経過時間は約8179秒で、ほぼ終盤です。

科学的な進捗（直接証拠 + 解釈）
- この r03 は、強pi pODMR と弱pi/fine pODMR で明確な共鳴が確認済みの、現在の第一候補NVです。中心周波数は次段Ramsey用に `3.8759 GHz` を使っています。
- これまでの r03 Ramsey は解析可能でしたが、まだ T2* または 13C の主張には届いていません。特に det=1.0 MHz の short-tau/high-SNR run では経験的に約 `1.19 MHz` 成分が見えましたが、programmed carrier / 13C sideband モデルとしては未支持でした。
- 現在の det=1.5 MHz run は、その約 `1.19 MHz` 成分が物理的なRamseyキャリアなら det 変更に追従するか、固定的なartifactなら追従しないかを調べる targeted diagnostic です。

直近の agent/project 判断
- 最新の bridge-free opportunity review は 10-average autosave を対象に完了しています。
- その時点の直接証拠: analysis snapshot は 10/12 averages、Final `39.347 kcps`、その後の live status は 11/12 averages / Final `44.796 kcps`。monitor error なし、stop request なし。
- autosave raw export は 10 averages × 41 tau points × 90000 repetitions。scan-order-aware drift は `Scan.ScanOrderEachAvg` / snake order を使い、flagged averages は 0 でした。
- 非終端データでの探索的 ratio LS screen は、8-average 時点では carrier-like な `~1.58 MHz` 付近が目立っていましたが、10-average では top が `~0.847 MHz` に移動しました。一方で programmed `1.5 MHz` と det-tracking 予測 `~1.692 MHz` の振幅は同程度に残り、旧 `1.192 MHz` artifact-control target は弱いままです。
- したがって現時点の解釈は「旧 1.192 MHz をそのまま物理成分として昇格する根拠は弱いが、det追従キャリアとしてもまだ claim-grade ではない」です。T2* / 13C の結論はまだ出していません。

実験以外の project work
- backlog は空で、明示的に pending の bridge-free research_task はありません。
- 実験中なので新しい bridge-touching submission は queue/running occupancy によりブロックされています。
- 次の opportunity-review では、終端結果を待つだけでなく、science-objective work first の方針で、解析・モデル比較・evidence gap 整理などから安全に進められる項目があれば agent 側で切り出す想定です。

次の見込み
- この job が terminal になったら、job/result/status/control と batch state を project 側へコピーし、verified intent を完了扱いにします。
- その後、final savedexperiment を raw export し、scan-order-aware drift、raw signal、reference-line normalization、full/skip-transient view、LS/FFT screen を確認します。
- 判定対象は programmed `1.5 MHz`、det-tracking 予測 `~1.692 MHz`、13C sidebands `~1.307/~2.076 MHz`、旧 artifact-control `~1.192 MHz` です。raw/readout-aware に信号形状が支持される場合だけ T2* fit を扱います。支持されなければ、さらに盲目的なRamsey反復は避け、alternate protocol か「現条件では未支持」という結論へ進みます。

添付予定: 10-average autosave review plot（非終端・進捗確認用）。