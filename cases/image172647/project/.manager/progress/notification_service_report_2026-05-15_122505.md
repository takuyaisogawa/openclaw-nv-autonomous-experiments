NVプロジェクト進捗報告（自動・詳細）
プロジェクト: nv23_aligned_nv_t2star_13c_image172647_20260514_1728

状態:
- 実験ブリッジは現在 idle。running 0 / queued 0 です。
- wake側のコンパクト状態には active とありますが、最新の project agent 完了マーカーと work/state.md の直接記録では「元の objective は満たされ、project lifecycle は completed / 次は idle」と整理されています。

実験・解析の到達点:
- 探索対象 image172647 から、最終的に `reimage1804_c02` を磁場整列NVブランチとして採用しました。直接証拠は、TrackCenter 成功（final_counts 約39.690 kcps）と、strong-pi pODMR の信号のみの明瞭な共鳴です。pODMRのコントラストは期待値より低め（約13.8-14.0%、期待は約22%）なので、ここは caveat 付きです。
- T2star については、det=1.5 / 1.0 / 1.25 MHz の Ramsey 系列がすべて short/few-us order を支持しました。代表的には約2-3 us 程度ですが、fit window・初期tau点の扱い・モデル選択でスカラーが動くため、「精密な単一値」ではなく「短い/few-us程度」という結論が直接証拠に合っています。
- 13C については、Ramsey単独では claim-grade ではありませんでした。高周波側 sideband らしい弱い成分が det を変えると概ね一緒に動く一方、振幅は約percent/sub-percentで、低周波側・direct Larmor・carrier の支持は不完全でした。
- その弱い候補を別プロトコルで確認するために行った CPMG N=8 tau scan は terminal 12 averages まで clean completion。直接証拠として、`CPMG.xml`, tau 0.45..1.60 us, 37 points, 12 x 50000 reps, snake scan order, stop_requested=false、pre/post counts 38.694/44.535 kcps、scan-order-aware drift flags なし、が確認されています。
- CPMGの最終 target-region review では、モデル上の `1/(4 f13)` 近傍（f13 ≈ 384.6 kHz、期待tau ≈0.650 us）の範囲内で、tau=0.6736 us に readout3/final echo のdipが出ました。readout3/self=0.9528、reference-normalizedでも約0.9518/0.9568です。これは det-shift Ramsey の弱い13C候補を独立に補強する直接証拠です。

結論（agent判断）:
- 最新agent判断（2026-05-15 09:48 EDT）では、目的は達成済みです。
- accepted aligned NV: `reimage1804_c02`
- T2star: short/few-us order（約2-3 us、method-sensitive）
- 13C: likely weak/moderate nearby-13C-like coupling signature。Ramsey + CPMG target-region dip で支持。ただし precise coupling extraction や publication-grade single-spin claim までは主張しません。
- このwakeでは bridge queue mutation は行われていません。今回のnotification_service reporterも報告のみで、queue/状態/backlogは変更していません。

実験以外の研究・プロジェクト作業:
- pending research_task は 0。backlog内訳は completed 11 / failed 2 で、現在の明示的な bridge-free pending task はありません。
- 実験中に進めるべき明示的 bridge-free task も現時点ではなし。
- ただし closeout report bundle は 12:25 EDT に作成済みです。LaTeX source と PDF が `work/reports/closeout_20260515_1225/` にあり、PDFは `%PDF-` header まで確認済みです。Tectonicはフォント取得のDNS失敗で完走できず、同じ内容を Matplotlib/PdfPages fallback でPDF化した、という caveat が記録されています。

次の期待ステップ:
- デフォルトでは追加の bridge 実験は不要です。
- Takuyaさんがより強い確度や精密化を希望する場合だけ、optional follow-up として 0.60..0.72 us 周辺の fine CPMG、または phase-readout XY8/DDRF 系の別ディスクリミネータが候補です。
- 明示的なbridge-free taskは今は pending なし。もしプロジェクトが再び active 扱いで opportunity-review に入るなら、science-objective work first の方針で、解析整理・モデル計算・文献/証拠gap整理から必要な1-3件を切り出すのが自然ですが、現状は closeout 済みのため新規実験を自動で増やす状態ではありません。

添付候補:
- CPMG terminal target-region plot を1枚添付します。tau=0.6736 us のdipと target-region の関係が一番わかりやすい図です。
