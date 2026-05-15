NVプロジェクト進捗報告（自動・詳細）
プロジェクト: nv23_aligned_nv_t2star_13c_image145844_20260513_1507
状態: active

実験状況:
- 実機ブリッジは現在 running です。queued は 0、running は 1 件。
- 実行中ジョブ: nv23_pulsed_odmr_rabimodulated_v1_20260513_180419_pulsed_odmr_rabimodulated_v1
- 内容は、受理した r03 候補に対する weak-pi pODMR 周波数較正です。スキャン範囲は 3.865..3.885 GHz、21 点、4 averages x 50000 repetitions、mod_depth=0.1、length_rabi_pulse=0.57 us。
- 直接確認した live status では state=running、phase=run_experiment_scan_point、表示は「1/4 averages completed」、updated_at=18:15:53、elapsed=682 s、final_counts_text は Final = 41.918 kcps です。実行時見積もりは total 約 1447 s、per-average 約 356 s なので、まだ異常な長時間化とは見ていません。

直近の科学的進捗:
- r01 は最初に 38.629 kcps で track できましたが、最初の strong-pi pODMR は zero averages + 6.584 kcps count gate で失敗し、retrack も 4.224 kcps で失敗しました。これは「共鳴なし」ではなく、drift/focus/image-frame shift の証拠として扱われています。
- その後、元の image145844 範囲を fresh re-image し、候補を再選定しました。
- fresh r01 は track 38.971 kcps、fresh r02 は track 39.367 kcps でしたが、どちらも raw/readout-aware strong-pi pODMR review で clear usable resonance なしと判断され、T2star には使わない方針です。
- fresh r03 は TrackCenter が 43.535 kcps で成功し、strong-pi pODMR の raw/readout-aware review で 3.875 GHz grid point に明確な dip が出ました。raw signal、point-wise ratio、reference-line normalization のすべてで最深点が 3.875 GHz に一致し、raw signal drop は edge median 比で約 16.6%。4 averages 全てが center-point drop を支持し、drift analysis は flagged averages なしでした。
- 以上を直接証拠として、r03 は最初の磁場整列候補として受理されました。これは「aligned candidate established」までで、まだ T2star / 13C の結論ではありません。

実験以外の研究・project work:
- backlog は空で、明示的な pending research_task は 0 件です。
- 実行中の bridge job があるため、次の bridge-touching submission は terminal までブロックされています。
- 明示的な bridge-free task は現在 pending ではありません。ただし、次の opportunity-review / terminal 後 review では science-objective work first として、weak-pi 結果の raw/readout-aware 解析、model comparison、Ramsey/T2star 設計、13C Larmor 予測の更新などが派生する見込みです。

最新 agent 判断:
- 最新 completion は 18:12:59-04:00 の handoff_bridge_running。
- 判断内容: r03 strong-pi pODMR を、3.875 GHz の明確な resonance、約 16.6% raw drop、4 averages の一貫性、drift flag なし、という根拠で aligned candidate として受理。次に coarse strong-pi fit を直接 Ramsey 周波数に使わず、weak-pi pODMR で mw_freq を絞る方針にしました。
- weak-pi pODMR は model/advisory-backed intent として作成・検証され、bridge idle と safety gate を確認してから投入されています。advisory は high recent drift risk を示しましたが、per-average window は suggested cap 未満で blocker / recommended action はありませんでした。

証拠上の注意:
- r03 の strong-pi 結果は alignment screen としては強いですが、grid は粗いので Lorentzian fit は記述的扱いです。Ramsey/T2star 用の中心周波数としては、現在走っている weak-pi pODMR の terminal result と raw/readout-aware review を待つ必要があります。
- 直接証拠は project state、evidence ledger、live bridge status、最新 agent marker です。weak-pi の共鳴中心・T2star・13C はまだ inference もしくは未確定で、claim にはしていません。

次の expected step:
- weak-pi pODMR の terminal を待つ。
- terminal 後に job/result/status/control と batch state を project 側へコピーし、intent image145844_reimage_r03_weak_podmr_20260513_1753 を完了処理。
- savedexperiment を raw-export し、raw readouts、point-wise normalization、reference-line normalization、per-average behavior、drift analysis を確認してから、Ramsey/T2star 設計へ進みます。
