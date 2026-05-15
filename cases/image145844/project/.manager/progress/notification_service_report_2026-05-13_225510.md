NVプロジェクト進捗報告（自動・詳細）
プロジェクト: nv23_aligned_nv_t2star_13c_image145844_20260513_1507
状態: active

実験状況:
- 実機は現在 running です。queued は空で、実行中は短tau・高SNR Ramsey診断 `nv23_ramsey_20260513_230331_auto_ramsey` 1件のみです。
- 直近コピー済みstatusの直接証拠では、state=running、phase=run_experiment_scan_point、平均 1/12、final count text は `42.367 kcps`、runtime monitor の last_error は空、stop_requested=false です。
- この実行は r03 の `mw_freq=3.8759 GHz`, `det=1.0 MHz`, `tau=48 ns..1.968 us`（41点）, `12 averages x 90000 repetitions`、合計 `1.08e6 shots/tau point` の設計です。tau=0を避け、短いT2star/初期時間キャリアが見えていない可能性を検査するための非ブラインドな条件変更です。
- runtime estimate は約 `7853 s` total、per-average/tracking window は `652 s` 程度で、夜間上限 `900 s` 内です。現時点ではautosaveがまだterminal evidenceではないため、T2star/13Cの判断には使いません。

これまでの科学的結論:
- r03 は aligned candidate として成立しています。直接証拠は strong-pi pODMR の 3.875 GHz grid dip、weak-pi pODMR の 3.876 GHz grid dip、fine weak-pi pODMR の 3.8759 GHz grid-supported center です。
- 一方で、T2star と nearby 13C はまだ未確定です。最初の det=1.5 MHz Ramsey scout と、2回目の det=1.0 MHz / 0..8 us / 8 avg Ramsey は、どちらも解析可能ではありましたが claim-grade ではありません。
- 2回目Ramseyのterminal reviewでは、実験は安全に完了（8 x 50000 shots/tau point、final counts `44.184 kcps`、monitor errorなし、stopなし、scan-order-aware drift flagなし）。ただし programmed carrier 1.0 MHz は弱く、LS amplitude は ratioで `0.00916`、raw signalで `0.277 kcps` と、期待していた 2..6 kcps 程度のraw oscillation scaleやSEMに対して小さい/近い値でした。最大成分は約 `1.178 MHz` で、carrierや期待13C sideband（約 `0.615/1.385 MHz`）と一致しません。したがってT2star/13C claimはしていません。

実験以外の研究・プロジェクト作業:
- backlog は空で、pending research_task は 0 件です。
- 明示的な bridge-free task は現時点ではありません。running job があるため、次のopportunity-reviewでは、必要ならautosaveの進捗/異常確認に限定し、science-objective work は主に evidence gap 整理・解析方針整理・次プロトコル候補の切り出しとして派生する見込みです。
- duplicate relaunch job `nv23_ramsey_20260513_230511_image145844_reimage_r03_ramsey_shorttau_48ns_1968ns_12x90k` は実行前にcanceledへ移され、重複取得は避けられています。これはbridge queueを増やさないための安全処理として記録済みです。

直近のagent判断:
- 2回目の8 us Ramseyを「単純に積み増す」のではなく、短tau・高SNR条件で「非常に短いT2star/早時間キャリアが見えていない」という具体的な失敗モードを検査する方針に変更しました。
- もし今回の短tau診断でも carrier/decay が支持されなければ、r03でのblind Ramsey repeatは避け、alternate protocol か「現在条件ではr03 Ramsey/13C unsupported」とする判断に進む予定です。

添付:
- 最新の完了済み解析として、2回目 det=1.0 MHz / 8 us Ramsey のterminal review図を1枚添付候補にします。これは「なぜT2star/13C未確定なのか」を見るための図で、現在running中の短tau診断の結果ではありません。

次の expected step:
- short-tau/high-SNR Ramsey の完了待ちです。terminal後に job/result/status/control と batch state をコピーし、final savedexperiment をraw export、scan-order-aware drift、raw/readout-aware carrier/decay review、target LS/FFT screen（1.0, 0.615, 1.385 MHz）を行います。支持が出た場合だけT2star fitへ進み、支持がなければblind repeatを止めて次プロトコル判断に進みます。
