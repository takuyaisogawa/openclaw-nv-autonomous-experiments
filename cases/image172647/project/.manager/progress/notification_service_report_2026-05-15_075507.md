NVプロジェクト進捗報告（自動）

プロジェクト: nv23_aligned_nv_t2star_13c_image172647_20260514_1728
目的: image172647 由来の磁場整列NVを見つけ、T2* と 13C について根拠のある結論まで進める。

実験状況:
- 実機は現在 CPMG N=8 の weak-13C discriminator を実行中です。
- bridge job: nv23_cpmg_20260515_072306_auto_cpmg
- sequence: CPMG.xml / tau scan 0.45..1.60 us / 37 points / 12 averages x 50000 reps
- 直近の直接status: 2026-05-15 08:00:56 EDT、phase は run_experiment_scan_point、表示は 3/12 averages completed。Final = 42.547 kcps、monitor active、last_error なし、stop_requested=false。
- runtime estimate は約 7359 s total、約 611 s/average。07:23開始なので、08:00時点では約38分経過です。
- autosave: C:\Users\<LAB_DOCUMENTS>\MATLAB\23-C\savedexperiments\NV1\1DExp-seq-CPMG-vary-tau-2026-05-15-072537

直近の研究判断:
- det=1.5/1.0/1.25 MHz のRamsey系列では、reimage1804_c02 は短い/few-us程度のT2*を支持しますが、精密な単一値まではまだ堅くありません。
- 13Cについては、det変更に合わせて高側band候補が動くように見える弱い物理候補は残っています。ただし振幅は約percent/sub-percentで、low-sideband/direct-Larmor/carrierの支持が不完全なので、Ramsey単独ではclaim-gradeではありません。
- そのため、盲目的にRamseyを積むのではなく、別プロトコルのCPMG tau scanで 13C DD resonance を確認する方針に切り替えました。target tau は f13≈384.6 kHz から 0.650 us（1/(4f)）と、慣例差を吸収する 1.300 us（1/(2f)）の両方をカバーしています。

直近の直接エビデンス:
- CPMG intent/verifier/advisory は通過済みで、queue idle確認後に materialize されました。advisoryは blockersなし、夜間cap内でした。
- 1-average autosave review: readout3 final echo では target tau に明瞭なdipなし。readout2 reference が 1.312 us 近傍で高く、terminal reviewでは raw/reference/self-baseline を必ず比較する必要があります。
- 2-average autosave review（bridge-free）: raw export は CPMG.xml、2 averages x 50000 reps、snake scan order、do_adiabatic_inversion=0 を確認。drift diagnostic は flagged averagesなし。readout3/self-baseline は 0.642 us近傍で 1.0197、1.312 us近傍で 0.9822。ただし2 averages同士の局所的な食い違いがあり、これは13C支持でも棄却でもありません。

非実験タスク状況:
- backlog上の pending research_task は 0、明示的なbridge-free taskも現在はありません。
- ただし bridge実行中に安全にできる作業としては、状態監視、必要なら後続の偶数average autosaveの暫定review、terminal時のreadout role/metadata確認準備があります。
- 次のopportunity-reviewが走る場合は、解析・モデル計算・文献/既存知識・evidence gap整理から、science-objective work firstで追加のbridge-free作業を切り出す想定です。

 caveat:
- ここでのCPMG autosave解釈はすべて非terminalです。現時点の直接証拠は「jobは健康に進行中」「autosaveは読める」「hard anomalyなし」までです。13C claim/rejection は terminalまたは十分な後続subsetの比較まで保留です。

次の期待ステップ:
- 実行は継続。hard anomalyがなければ terminal完了を待ちます。
- terminal後に raw export、readout role再確認、scan-order-aware drift、target tau 0.650/1.300 us と off-target/reference挙動を比較して、13C/T2*結論を保守的に更新します。