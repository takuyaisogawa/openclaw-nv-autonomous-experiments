NVプロジェクト進捗報告（自動・詳細）
プロジェクト: nv23_aligned_nv_t2star_13c_image145844_20260513_1507
目的: image145844 から磁場整列したNVを見つけ、T2star と 13C について根拠ある結論を出す。

実験状況:
- r03 は、strong-pi pODMR と weak/fine pODMR の raw/readout-aware evidence により、現時点の磁場整列候補として採用済みです。周波数入力は fine weak-pi pODMR のグリッド根拠から mw_freq = 3.8759 GHz を使っています。
- 直近で完了した short-tau/high-SNR Ramsey（job: nv23_ramsey_20260513_230331_auto_ramsey）は、12 averages x 90000 repetitions、tau = 48 ns..1.968 us / 41 points、det = 1.0 MHz で安全に完了しました。最終 counts は 35.122 kcps、scan-order-aware drift は Scan.ScanOrderEachAvg / snake mode で no flagged averages でした。
- ただし terminal review では、最強の経験的 ratio-screen component が約 1.192 MHz、記述的な damped-sinusoid fit が約 1.198 MHz / T2star 約 6.33 us という結果に留まりました。これは「見えている成分の記述」であって、programmed carrier 1.0 MHz や期待 13C sideband（約 0.615 / 1.385 MHz）が十分優勢な物理モデルとして支持されたわけではありません。したがって、この run から T2star または 13C はまだ claim していません。
- その後、非ブラインドな det-shift Ramsey diagnostic が開始されました。現在の running job は nv23_ramsey_20260514_015423_auto_ramsey、batch は nv23_ramsey_20260514_015303 です。初期 status は 1/12 averages、final-count text 42.878 kcps、monitor last_error 空、stop_requested=false で健康です。running 中なので、bridge-touching の追加 submission は occupancy によりブロックされています。

実験以外の研究・プロジェクト作業:
- pending backlog / 明示的な research_task は 0 件です。
- 明示的な bridge-free task も現時点ではありません。進行中 run に対しては、autosave は anomaly/progress review 用に限定し、nonterminal data から T2star/13C claim はしない方針です。
- ただし backlog が空であることは「科学的作業がない」という意味ではありません。opportunity-review が走る場合は、objective と evidence gap から、解析・モデル比較・alternate protocol 検討などの science-objective work を必要に応じて切り出す想定です。

直近の agent 判断:
- short-tau det=1.0 MHz run は hard anomaly なしで完了したが、carrier/13C sideband model はまだ支持されない、と判断しました。
- 同じ条件の単純な blind repeat は避け、det だけを 1.0 MHz から 1.5 MHz に変える targeted follow-up を選択しました。物理的な Ramsey carrier 仮説なら、前回の約 1.192 MHz 成分は約 1.692 MHz へ追従するはずです。artifact/baseline 的な固定成分なら、単純には det に追従しないはずです。

証拠と caveat:
- 直接証拠: terminal raw export、scan-order-aware drift、review JSON/figure、lab log、intent verifier/advisory、running job initial status。
- 推論: 1.192 MHz 成分が physical carrier か artifact かは未決です。今回の det-shift run はその識別のためのテストです。
- r03 の整列候補としての採用は pODMR evidence に基づき支持されていますが、T2star と 13C はまだ未確定です。

次の expected step:
- det-shift Ramsey の完了を待ち、terminal artifacts を project にコピーしてから、raw export、scan-order-aware drift、1.5 MHz carrier、予測 det-tracking 約 1.692 MHz、13C sideband 約 1.307 / 2.076 MHz、前回 artifact-control 約 1.192 MHz を比較します。det-tracking signal と data shape が raw/readout-aware に支持される場合のみ、T2star fit や 13C 解釈へ進みます。