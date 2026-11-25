---
title: 收錄紀錄
type: overview
sources: []
updated: 2026-11-25
---

# 收錄紀錄

每次收錄、產出、健檢都記一筆（AGENTS.md 第 6 節）。檢查器的輸出原樣保留。

## 2026-11-25 #0 建立 Wiki

- 核心問題：**它在解決什麼問題？為什麼選它，不選別的？**（使用者確認）
- 四問題：解決什麼問題、為什麼選它、規格怎麼讀、出問題怎麼認。
- 頁面類型：來源、零件、加工、概念、案例；工具沿用開心的 Quant Wiki，改成機械版的段落與禁用字。
- 第一個主題原本提案「螺絲與緊固件」，使用者改成「CNC 加工怎麼省錢」，並指定第一份資料。螺絲的資料先記進 [[todo]]。

## 2026-11-25 #1 收錄 hubs-cost-2026（Hubs〈14 招省 CNC 成本〉）

- 讀：網頁全文文字；圖片只有圖說，第 14 招的單價圖沒有數值。
- 新增：[[hubs-cost-2026]]、[[cnc-milling]]（文章直接談銑削，符合加工頁「1 份來源」的規則）、[[cnc-cost-guide]]（主題導覽，先只放閱讀順序）、圖 `milling-vs-turning`。
- 分支判斷：12 個概念（內角圓角、凹槽深度、薄牆、公差⋯⋯）都只出現在 1 份來源，先記進 [[todo]]，不建頁。
- 第 1 次檢查失敗 1 項：log.md 沒有 hubs-cost-2026 的收錄紀錄 → 補這一筆。
- 第 2 次檢查：見下一行輸出。
```
頁數：sources 1、parts 0、processes 1、concepts 0、cases 0
健檢通過
```

## 2026-11-25 #2 收錄 protolabs-cost-2026（Protolabs〈How to Reduce CNC Machining Costs〉）

- 讀：網頁全文文字；圖只讀到圖說。
- 新增：[[protolabs-cost-2026]]、[[end-mill]]（零件頁，兩份來源都直接談刀）、[[internal-corner-radius]]、[[cavity-depth]]、[[thin-wall]]、[[machinability]]，圖 `corner-radius`、`cavity-depth`。
- 更新：[[cnc-milling]]（加第二份來源、連到新概念頁）、[[cnc-cost-guide]]、[[todo]]。
- 分支判斷：4 個概念出現在 2 份來源，拆頁；「細高特徵」併進 [[thin-wall]]（兩者是同一個原因：會晃）。「文字與刻字」也到 2 份，但這輪已新增 5 個非來源頁（AGENTS.md 第 6 節的上限），先留在待辦。
- **可信度**：Hubs 現在屬於 Protolabs 集團，兩份來源不算完全獨立 → 在概念頁註明，並記進待辦要找別家的資料。
- 第 1 次檢查失敗 1 項：log.md 沒有 protolabs-cost-2026 的收錄紀錄；另有 1 個警告：沒有頁面連到 machinability → 補這一筆紀錄，並從 cnc-milling、導覽頁連過去。
- 第 2 次檢查：
```
頁數：sources 2、parts 1、processes 1、concepts 4、cases 0
健檢通過
```
