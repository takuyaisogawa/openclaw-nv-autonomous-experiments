NVプロジェクト進捗報告（自動・詳細）
プロジェクト: `nv23_aligned_nv_t2star_13c_image145844_20260513_1507`
目的: image145844の範囲から磁場に整列したNVを見つけ、十分根拠のあるT2starと13C結論まで進める。

実験状況:
- 直近のproject state / log上では、候補r02のstrong-pi pulsed ODMRが実行中です。ジョブ名は `nv23_pulsed_odmr_rabimodulated_v1_20260513_162710_image145844_reimage_r02_strong_podmr`。
- r02はfresh re-image後の第2候補で、TrackCenterは `39.367 kcps`、追跡位置は `[115.864332, 117.919934, 116.274661] um`。これは直接のbridge resultとして記録されています。
- r02 pODMR条件は `3.825..3.925 GHz`、21点、`4 averages x 20000 repetitions`、`mod_depth=1`、`length_rabi_pulse=52 ns`。r01で平均ごとの時間が長くdrift flagが出たため、同程度のショット数を保ちながら1平均あたりを短くする設計に変更されています。
- このreporter wakeではbridge queueのsubmit/stop/validate等はしていません。ライブqueueを操作せず、project fileの直接証拠だけで報告しています。

ここまでの直接証拠:
- 初期image145844は `ImageData_YXZ`、単位kcps、範囲 `Y=110..120 um`, `X=114..124 um`, `Z=115..116 um` と確認済み。
- 最初のr01は一度 `38.629 kcps` でtrackしましたが、最初のstrong-pi pODMRは0 averagesで終了し、post-run Finalが `6.584 kcps`、retrackも `4.224 kcps` で失敗しました。これは「no resonance」ではなく、count/focus/image-frame shiftの証拠として扱われています。
- その後、同じimage145844領域をfresh Imagingし直し、bridge resultに記録された permutation `[2 3 1]` を使ってY-X-Zに直して候補選定しました。
- fresh候補は r01 `[114.333333,117.333333,116.0] um` peak `40.0 kcps`、r02 `[115.833333,118.166667,116.5] um` peak `36.0 kcps`、r03 `[117.166667,118.166667,116.0] um` peak `36.0 kcps`。
- fresh r01は `38.971 kcps` でtrack後、strong-pi pODMR自体は完了しました。しかしraw/readout-aware reviewでは明確に使える共鳴が支持されませんでした。signal variationはbaseline/drift/average間変化と同程度で、両averageがdrift-flag、記述的Lorentzian dip fitも `R2 ~ 0.20` と弱いです。そのためr01は現時点でT2star候補から外されています。

推論・判断:
- TrackCenter countは「見えている/追跡できる」証拠ですが、磁場整列の証拠ではありません。整列判定はstrong-pi pODMRの明確なusable resonanceで行う方針です。
- r01の失敗は2段階あります。初回はcount collapseなので分光結論ではなく、fresh r01の完了pODMRはraw reviewでno-clear-resonanceと判断、という整理です。
- r02が明確な共鳴を示せば、次にRamsey/T2starへ進む候補になります。ただしcenterは自動fitだけで採らず、raw readout、point-wise normalization、reference-line normalization、平均ごとの挙動、drift解析を見てから決める必要があります。

実験以外の研究・project作業:
- backlogは空で、明示的にpendingなresearch_taskはありません。
- 実験中に進める明示的なbridge-free taskも現時点ではありません。
- ただしopportunity-reviewでは、science-objective work firstとして、解析・モデル計算・文献/既存知見確認・evidence gap整理から1〜3件を切り出すことが期待されています。特にr02 terminal後のraw/readout review設計は次の中心作業です。

次の見込み:
1. r02 pODMRがterminalになるのを待つ。
2. job/result/batch stateをproject側に取り込み、intent `image145844_reimage_r02_strong_podmr_20260513_1622` を完了扱いにする。
3. raw/readout-aware reviewでusable resonanceの有無を判定する。
4. r02に明確な共鳴があれば、そのcenterに基づいてRamsey/T2star計画へ進む。なければr02を棄却し、fresh r03へ進む。

現時点の最終claim: 磁場整列NV、T2star、13C結論はいずれもまだ確立していません。