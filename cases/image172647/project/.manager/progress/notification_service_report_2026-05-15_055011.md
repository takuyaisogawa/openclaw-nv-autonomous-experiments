NVプロジェクト進捗報告（自動）
project: nv23_aligned_nv_t2star_13c_image172647_20260514_1728
目的: image172647 由来の磁場アライン済みNVを見つけ、T2* と 13C の結論を十分な根拠で出すこと。

実験状況（直接確認）:
- 実機は実行中。job は `nv23_ramsey_20260515_030822_auto_ramsey`、sequence は `ramsey.xml`。
- status.json の最新更新は 2026-05-15 05:52:46 EDT。phase は `run_experiment_scan_point`、表示は 12/16 averages 完了。
- 設定は tau 0–10 us、51 points、50000 repetitions/average、16 averages 予定。現在は 75% 付近で、予定 800k shots/point のうち 600k shots/point 相当まで進んでいます。
- 実行開始は 03:08:31 EDT、経過は約2時間44分。見積もり総時間は約3時間25分なので、単純推定では残りは40分前後です。
- monitor は active、tick_count 1271、last_error は空、stop_requested=false。異常停止や手動停止要求は確認されていません。
- 注意: 05:48 のautosaveレビュー時点では Final=44.078 kcps でしたが、05:52 の live status runtime では Final=38.457 kcps と表示されています。どちらも直接ログ由来ですが、後者は最新の瞬間表示です。追跡不能や停止級の異常とはまだ扱っていません。

直近の解析・判断（直接証拠）:
- 05:47 の bridge-free autosave review では、保存済み11 averages のうち snake scan order のバランスを保つため最初の10 averagesを使用しました。bridge queue は触っていません。
- drift diagnostic は scan-order-aware で flagged averages なし。
- provisional FFT target bins（readout2 / signal self-baseline）は、direct 13C 0.58%、det-13C 1.08%、carrier 1.36%、det+13C 1.17%、old det=1 high/static 0.21%、static low 0.56%、previous 1.9 MHz 0.20%。
- これは 500k/800k shots per point の途中データなので、T2* や 13C の claim-grade 証拠ではありません。現在の結論は「det=1.25 MHz の追加Ramseyは順調に進行中、途中FFTでは carrier と det±13C 近傍に構造が見えるが、まだ最終判断不可」です。

研究・プロジェクト作業状況:
- pending research_task は 0。実験実行中に明示的に進める bridge-free task も現在はありません。
- 直前までに、det=1.0 MHz claim-grade Ramsey、det=1.5 MHz scout Ramsey、weak-pi pODMR refinement は完了済み。det=1.0 は短い/few-us程度のT2*順序を示した一方、13Cは弱い候補止まりでした。そのため今回の det=1.25 MHz run は、det-shift でアーティファクトと 13C 由来成分を切り分けるための追加判別実験です。
- 最新agent判断は「running jobを待つ。後続の有用な even-subset autosave か terminal 結果を bridge-free でレビューし、queue はmutateしない」。

根拠上の caveat:
- autosave解析は途中データで、scan-order balance のため全保存averageではなく even subset を使っています。
- FFT binの高さは低SNR・有限サンプリング・正規化方式に依存します。単一ピークだけで 13C claim にはしません。
- live counts は時点により揺れます。最新瞬間表示の低下は要注意ですが、monitor error / stop request / drift flag なしなので、現時点では経過観察です。

次の期待ステップ:
- まず実験の terminal completion または anomaly を待ちます。
- 完了後は raw export、raw/reference-aware/signal-self-baseline plot、scan-order-aware drift診断、T2* fit可否確認、direct 13C・det・det±13C・過去1.9 MHz領域の比較を行います。
- 明示的な bridge-free task は今は空ですが、次の opportunity-review で science-objective work first として解析・モデル計算・evidence gap整理などから必要な作業が切り出される見込みです。
