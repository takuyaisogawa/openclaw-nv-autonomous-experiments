NVプロジェクト進捗報告（自動）
project: nv23_aligned_nv_t2star_13c_image172647_20260514_1728

ファイル上の最新状態では、プロジェクトは active、実機は det=1.0 MHz の Ramsey/T2star/13C フォローアップを実行中です。bridge queue はこのジョブで占有されているため、次の bridge-touching work は terminal または anomaly evidence が出るまで待ちです。

実験ステータス:
- 現在 running: `nv23_ramsey_20260514_230820_auto_ramsey`
- sequence: `auto__ramsey` / `ramsey.xml`
- 条件: `mw_freq=3.876501337 GHz`, `det=1.0 MHz`, tau 0..10 us, 51 points, 16 averages x 50000 reps, length_pi_pulse=52 ns, mod_depth=1
- 最新 status copy では average 1/16、`Final = 40.049 kcps`、monitor active、last_error なし、stop_requested=false。autosave は有効ですが、この時点ではまだ completed average の raw export 対象はできていません。
- 予測時間は advisory で total 約11106 s、per-average tracking window 約692.6 s。夜間 cap 900 s 内なので実行判断は妥当です。

直近の直接証拠:
- terminal weak-pi pODMR refinement は完了済み。pre-run TrackCenter 41.608 kcps、post-run final 43.649 kcps、stop/error なし、snake scan-order drift flags なし。
- raw/readout-aware terminal review では、signal-only の narrow dip が strong-pi center 近傍に出ています。fit center は 3.876501337 GHz、depth 約11.4%、FWHM 約0.94 MHz。nearest sampled point 3.876461010 GHz では signal depression 約9.0%、reference depression 約0.5% で、normalization-only ではなさそうです。
- 以前の terminal det=1.5 MHz Ramsey は、約1.9 MHz の弱い empirical oscillation と short/few-us T2* order を支持しましたが、early tau の扱いで fitted T2* が変わるため final scalar T2* ではありません。nominal 1.5 MHz carrier は弱く、13C は未確立です。

推論・判断:
- weak-pi center は strong-pi center から約+40 kHz しかずれていないため、以前の ~1.9 MHz 成分を「電子共鳴中心が約+0.4 MHz ずれていた」と説明する線は弱くなりました。
- そのため最新 agent decision は、det を 1.5 MHz から 1.0 MHz に変える discriminator Ramsey を走らせる、というものです。期待される 13C Larmor は約0.385 MHz、sideband は約0.615 MHz と 1.385 MHz。今回の 10 us span では FFT bin 約100 kHz なので、古い ~1.9 MHz ambiguity から分離して見られる設計です。

実験以外の研究/project work:
- pending research_task は 0。
- 実験中に明示的に残っている bridge-free task は現時点ではありません。
- ただし autosave が十分に進んだら、bridge-free で raw export / drift check / provisional review は可能です。特に odd snake-order subset は provisional と明記する必要があります。
- opportunity-review が走る場合は、science-objective work first として、解析・モデル比較・evidence gap 整理から次の bridge-free 作業を切り出す想定です。

 caveat:
- c02 は magnetic-field-aligned branch として採用済みですが、strong-pi contrast は期待 ~22% より低め（terminal strong-pi で約13.8-14.0%）です。
- weak-pi pODMR は mw_freq refinement の根拠であり、それ自体は 13C 証拠ではありません。
- 13C claim は、今回の det-shift Ramsey の terminal data で det / det±13C / direct 13C-Larmor / 旧~1.9 MHz 成分を比較し、det-shift に整合する支持が出て初めて検討できます。孤立した低SNRピークだけでは claim しません。

次の期待ステップ:
この Ramsey job の terminal/anomaly evidence を待ちます。terminal success なら savedexperiment を raw export し、raw readouts、reference-aware normalization、signal self-baseline、per-average traces、FFT、drift diagnostic を確認してから、T2* fit と 13C 判定に進みます。