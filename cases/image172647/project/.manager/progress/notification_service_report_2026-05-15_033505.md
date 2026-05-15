NVプロジェクト進捗報告（自動）
project: nv23_aligned_nv_t2star_13c_image172647_20260514_1728

実験状況:
現在は reimage1804_c02 の det=1.25 MHz Ramsey 追試が実機で走行中です。job は `nv23_ramsey_20260515_030822_auto_ramsey`、sequence は `ramsey.xml`、tau 0..10 us / 51 points / 16 averages x 50000 reps です。読み取り時点の直接証拠では、bridge state は running、phase は `run_experiment_scan_point`、status 更新は 2026-05-15 03:44:40 EDT、2/16 averages 完了、elapsed 2169 s、monitor active、last_error なし、stop_requested=false、Final = 43.106 kcps です。開始時の TrackCenter も Final = 44.073 kcps で、現時点でアライメント崩れや停止要求の証拠はありません。

直近のデータ確認:
03:38-03:41 EDT に、この running job の autosave 2 averages だけを bridge-free に raw export / plot / drift review しました。これは 100k shots/point で、予定 terminal の 800k shots/point の 1/8 なので、進捗確認用の暫定証拠です。snake scan order の drift 診断では flagged averages は 0。readout2/self-baseline FFT の暫定 target bins は direct 13C 0.97%、det-13C 1.22%、carrier 1.29%、det+13C 0.71%、old det=1 high/static 0.71%、static low 1.33%、previous 1.9 MHz 1.13% でした。まだ T2star の最終値も 13C claim も出していません。

これまでの研究判断:
前段の terminal det=1.0 MHz Ramsey は clean に完了し、16 averages、pre/post counts 40.445/42.702 kcps、stopなし、safe shutdown ok、scan-order drift flagなしでした。直接証拠として T2star は short/few-us order を支持しますが、fit window や early tau に敏感で、単一の robust scalar にはしていません。13C は未確立です。ただし det=1.5 MHz と det=1.0 MHz の比較で、弱い high-sideband 互換成分が programmed detuning におおむね追随する可能性があり、単発ノイズだけとは断定せず、det=1.25 MHz の第三 det discriminator を実行する判断になりました。これは「実在 13C なら det+13C が約1.635 MHzへ動くはず、静的 artifact なら 0.7/1.4/1.9 MHz 付近に残るはず」という切り分けです。

実験以外の作業状況:
pending research_task は 0。実験中に進める明示的な bridge-free task も現時点ではありません。直近の bridge-free autosave review は完了済みで、bridge queue mutation はしていません。次の opportunity-review では、terminal を待つ間に science-objective work first として解析整理・モデル比較・evidence gap 整理などから安全な非実機作業が派生する可能性はありますが、今は優先すべき明示タスクはありません。

次の見込み:
基本方針は、この det=1.25 MHz job の terminal または hard anomaly を待つことです。途中でさらに有用な偶数 average autosave が出れば bridge-free に暫定確認できますが、bridge-touching work は terminal/anomaly evidence まで止めます。terminal 成功後は savedexperiment を raw export し、raw/reference-aware/self-baseline plot、scan-order-aware drift、FFT target comparison を行い、det=1.25 MHz model に従って弱い sideband が動いたかどうかで 13C の supported / absent / ambiguous を判断します。添付は今回の det=1.25 MHz 2-average autosave plot です（暫定・claim用ではありません）。