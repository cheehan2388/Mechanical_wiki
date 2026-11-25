# 簡報稿：CNC 零件到底貴在哪裡？
#
# 格式：每頁用一行 `=== id | 版型 | 引用的 Wiki 頁 | 選項 ===` 開頭。
# - 引用：用逗號分隔的 Wiki 檔名。這頁出現的每個數字，都必須能在引用頁裡找到。
# - 選項：illustrative（示意頁，數字不檢查）、define:名詞（這頁負責解釋這個名詞）。
# - 版型：cover、statement、bullets、figure、table、quiz、sources
# 檢查：python3 tools/check_slides.py slides/cnc-cost/deck.md

=== cover | cover | cnc-cost-guide | ===
# CNC 零件到底貴在哪裡？

它在解決什麼問題？為什麼選它，不選別的？

開心的機械 Wiki・CNC 省錢篇

=== question | statement | cnc-cost-guide, hubs-cost-2026 | define:CNC ===
## 先問一個問題
同一個零件，換個畫法，報價可以差很多。

報價最大的一塊，通常是**機器要切多久**。這份簡報一條一條看：每條規則在解決什麼問題？

> **CNC**：電腦數值控制。刀怎麼走由電腦照程式控制，不是人手搖。

=== what | figure | cnc-milling, cnc-turning | define:銑削, define:車削 ===
## CNC 主要有兩種：差在誰在轉
{{figure:milling-vs-turning}}
> **銑削**：刀轉、工件不動，把方料挖出形狀。**車削**：工件轉、刀不轉，車出圓的零件。

=== four | bullets | hubs-cost-2026, cnc-cost-guide | ===
## 錢花在哪裡：四個來源
- **加工時間**：切越久越貴，通常是最大的一項。
- **開機成本**：準備檔案、規劃流程，做幾件都要花。
- **難做的形狀**：很薄的牆、要求很精準的尺寸，要放慢、多檢查。
- **材料**：價格，加上好不好切。

所以省錢規則都在做四件事：**少切、快切、少換刀、少翻面。**

=== tool | bullets | end-mill | define:端銑刀 ===
## 一切從刀的形狀開始
- 刀是**圓柱形**的 → 挖出來的內角一定是圓的。
- 刀越大，每圈削越多 → 切得越快。
- 刀伸越長越會晃 → 最舒服的深度約是刀徑的 2–3 倍。
> **端銑刀**：銑床最常用的刀，像一根有刃的圓棒，側面和底部都能切。

=== corner | figure | internal-corner-radius | define:內角圓角, define:清角 ===
## 規則 1：內角畫圓角
{{figure:corner-radius}}
> **內角圓角**：凹槽角落被刀切出的圓弧，至少畫到槽深的 1/3。**清角**：真要尖角時，在角落多挖的 U 形缺口。

=== corner2 | bullets | internal-corner-radius | ===
## 圓角畫多大？
- 12 mm 深的槽，圓角畫 5 mm 以上，工廠就能用 8 mm 的刀切。
- 所有內角用**同一個半徑**，就不用換刀。
- 真的要塞方形零件：加 6.35 mm 寬的清角，可以做到約 32 mm 深。

=== depth | figure | cavity-depth | ===
## 規則 2：凹槽別挖太深
{{figure:cavity-depth}}
就像握筷子的尾端攪碗底：伸越長越晃。建議深度不超過凹槽寬度的 4 倍；更深就考慮拆成兩個零件。

=== wall | bullets | thin-wall | define:顫振 ===
## 規則 3：牆別太薄
- 建議最小牆厚：金屬 **0.8 mm**、塑膠 **1.5 mm**。
- 太薄會顫振，只能分很多次、每次削一點；切完還可能翹。
- 牆真的要很薄？改用**板金**折出來通常比較便宜。
> **顫振**：刀和工件一起抖，表面留下波紋、尺寸不準。

=== hole | figure | hole-thread | define:盲孔, define:攻牙 ===
## 規則 4：孔用標準尺寸，螺紋別攻太深
{{figure:hole-thread}}
> **盲孔**：有底、沒穿透的孔。**攻牙**：用絲攻在孔壁切出螺紋，讓螺絲鎖得進去。螺紋長度 3 倍孔徑就夠。

=== tol | figure | tolerance | define:公差 ===
## 規則 5：只在需要的地方標公差
{{figure:tolerance-band}}
> **公差**：尺寸可以差多少。沒標的尺寸，三家工廠的標準都約 ±0.13 mm。

=== general | table | general-tolerance, iso2768-1989 | define:一般公差, define:ISO 2768 ===
## 圖面角落的「ISO 2768-m」是什麼
| 尺寸範圍（mm） | m 級允許差多少 |
|---|---|
| 6–30 | ±0.2 mm |
| 30–120 | ±0.3 mm |
| 120–400 | ±0.5 mm |

尺寸越大，允許差越多。
> **一般公差**：沒寫公差的尺寸共用的規則。**ISO 2768**：最常用的一般公差國際標準，m 是中級。

=== setup | figure | machine-setup | define:裝夾, define:5 軸 ===
## 規則 6：少翻面
{{figure:machine-setup}}
> **裝夾**：把工件夾上機台並對好位置。兩面都有孔就要夾兩次。**5 軸**：機器自己會轉，少翻面，但比較貴。

=== material | table | machinability | define:可切削性 ===
## 規則 7：選好切、便宜的材料
| 材料（150×150×25 mm 板） | 價格（美元） |
|---|---|
| 6061 鋁 | 25 |
| 304 不鏽鋼 | 90 |
| PEEK 塑膠 | 300 |

不鏽鋼常要花鋁的 2 倍以上時間來切。
> **可切削性**：材料好不好切的分數，越高越好切。

=== finish | bullets | surface-finish, batch-size | define:表面處理, define:陽極處理 ===
## 規則 8、9：一種處理就好，一次多訂幾件
- 混用多種表面處理，要多做遮蔽，多一道工。
- 開機成本是固定的：1 件加到 5 件，單價約減半。
- 1,000 件以上，單價可降 5–10 倍。
> **表面處理**：切完後加的處理。**陽極處理**：鋁件常用，在表面長一層硬膜。

=== batch | figure | batch-size | illustrative ===
## 為什麼打樣一件那麼貴
{{figure:batch-size}}
像煮一鍋湯：洗菜、開火的時間跟煮幾碗無關。

=== answers | table | cnc-cost-guide | ===
## 回到核心問題
| 規則 | 解決什麼問題 | 為什麼選它 |
|---|---|---|
| 內角圓角 | 刀是圓的 | 大圓角能用大刀 |
| 淺槽 | 刀伸長會晃 | 穩、快；太深就拆件 |
| 厚一點的牆 | 薄牆會抖會翹 | 加厚最便宜 |
| 標準孔、短螺紋 | 特殊尺寸要換刀 | 一次到位、不斷絲攻 |
| 只標必要公差 | 越嚴越慢 | 其他交給一般公差 |
| 少翻面 | 每翻一次重新對位 | 一次夾完最省 |

=== quiz | quiz | internal-corner-radius, hole-thread, general-tolerance | ===
## 小測驗
?? 一個 15 mm 深的口袋，內角圓角至少要畫多大，才符合「1/3 深度」的規則？
- [ ] 1 mm
- [x] 5 mm
- [ ] 15 mm
!! 15 的 1/3 是 5（算術），畫 R5 以上，工廠就能用比較大的刀。
?? 要鎖 M6 螺絲，螺紋大概攻多深就夠？
- [ ] 6 mm
- [x] 18 mm 左右（孔徑的 3 倍）
- [ ] 越深越好
!! 3 倍孔徑就夠；攻太深強度不會變強，絲攻還容易斷。
?? 標題欄寫 ISO 2768-m，一個沒標公差的 80 mm 尺寸可以差多少？
- [ ] ±0.1 mm
- [x] ±0.3 mm
- [ ] ±1 mm
!! 80 落在 30–120 mm 那一格，m 級是 ±0.3 mm（查表的算術）。

=== takeaway | statement | cnc-cost-guide | ===
## 一句話帶走
**畫每一個形狀之前，先想：刀伸不伸得到、要切多久、要翻幾次面。**

真的需要的地方就付錢；不需要的地方，交給工廠最順手的做法。

=== sources | sources | hubs-cost-2026, protolabs-cost-2026, xometry-cost-2020, hubs-design-2026, hubs-cnc-basics-2026, iso2768-1989 | ===
## 參考資料
- Protolabs Network (Hubs). *14 proven design tips to reduce the cost of CNC machining*.（使用者指定）
- Protolabs Network (Hubs). *How to design parts for CNC machining*.
- Protolabs Network (Hubs). *What is CNC machining?*
- Protolabs. *How to Reduce CNC Machining Costs*.
- Lichtig, A. (2020). *How to Reduce CNC Machining Costs*. Xometry.
- ISO 2768-1:1989 *General tolerances*（以 IS 2102 Part 1:1993 閱讀）.

前四份都屬於 Protolabs 集團。所有數字都能在 Wiki 的來源頁查到。
