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

## 2026-11-25 #3 收錄 xometry-cost-2020（Xometry〈How to Reduce CNC Machining Costs〉）

- 讀：網頁全文文字；沒有看圖。
- 新增：[[xometry-cost-2020]]、[[tolerance]]、[[machine-setup]]、[[hole-thread]]、[[batch-size]]、[[surface-finish]]（各 2–3 份來源），圖 `tolerance-band`、`machine-setup`、`hole-thread`、`batch-size`。
- 更新：[[internal-corner-radius]]、[[cavity-depth]]、[[thin-wall]]、[[machinability]]、[[cnc-milling]]、[[cnc-cost-guide]]、[[todo]]。
- **找到矛盾**：凹槽深度的「4 倍」，Hubs 寫成深度 ≤ 4 × XY 尺寸，Xometry 寫成長度 ≤ 4 × 深度，方向相反 → 兩個都照原文寫進 [[cavity-depth]]，不自己選一個。
- **可信度**：Xometry 是 Protolabs 集團以外的公司，內角圓角的「只有同一家」問題解決，從待辦移除。三家的標準公差換算後幾乎一樣（±0.125、±0.13、±0.127 mm）。
- 分支判斷：EDM／線切割到 2 份，但這輪已新增 5 頁，留在待辦。
- 第 1 次檢查失敗 1 項：log.md 沒有 xometry-cost-2020 的收錄紀錄；3 個警告：batch-size、hole-thread、surface-finish 沒有頁面連到 → 補紀錄，從 cnc-milling 的「規格怎麼讀」和導覽頁連過去。
- 第 2 次檢查：
```
頁數：sources 3、parts 1、processes 1、concepts 9、cases 0
健檢通過
```

## 2026-11-25 #4–#6 收錄 hubs-design-2026、hubs-cnc-basics-2026、iso2768-1989

這三份大多是「更新既有頁」，所以一起寫完來源頁，再跑一次檢查。（反思：一次三份，檢查失敗時比較難看出是哪一份造成的；之後還是一份一份來。）

- 讀：
  - hubs-design-2026：網頁全文文字（含規則表），沒看圖。
  - hubs-cnc-basics-2026：網頁全文文字，沒看圖。
  - iso2768-1989：標準全文（IS 2102 Part 1:1993 PDF，與 ISO 2768-1:1989 相同）。PDF 是掃描轉文字，表 1 已和同一份 PDF 的原始文字對過；表 2 的 v 級欄位不清楚，**待核對**。
- 新增：[[hubs-design-2026]]、[[hubs-cnc-basics-2026]]、[[iso2768-1989]]、[[cnc-turning]]（加工頁，1 份來源直接談）、[[general-tolerance]]（3 份來源）。
- 更新：[[cnc-milling]]（補完「為什麼選它」：vs. 車削、3D 列印、板金、5 軸）、[[cavity-depth]]、[[internal-corner-radius]]、[[thin-wall]]、[[hole-thread]]、[[tolerance]]、[[machine-setup]]、[[surface-finish]]、[[cnc-cost-guide]]（加總表與「不一致的地方」）、[[todo]]。
- **找到矛盾**：
  - hubs-cnc-basics-2026 自己有三處數字前後不一致（銑床尺寸、最嚴公差、金屬牆厚）→ 全部寫進來源頁的「推論」，不採用其中一個。
  - 盲孔留多長不攻牙：Hubs 兩篇寫半個孔徑和 1.5 倍孔徑 → 兩個都寫，標出小螺紋照長的留比較保險是 Wiki 推論。
  - 「一般公差 ≈ ±0.125 mm」：ISO 2768 的公差隨尺寸改變，所以這只是近似 → 寫進 [[general-tolerance]]。
- 分支判斷：5 軸出現在 2 份，但兩份都是 Hubs → 照第 7 節先不拆，寫在 [[machine-setup]]。文字刻字到 3 份，但對省錢篇是小項目，先放總表。
- 第 1 次檢查失敗 8 項：
  - 3 項是「相關頁面」的原因太短（「銑削」「車削」「總表」不到 4 個字）→ 改成一句完整的原因。
  - 2 項是連到還沒建的頁（cnc-turning、general-tolerance）→ 建頁。
  - 3 項是 log 沒有紀錄 → 補這一筆。
  - 警告：hubs-cost-2026 被 16 頁連到 → 已經有導覽頁 cnc-cost-guide，在它開頭加 `hub: cnc-cost-guide`。
- 第 2 次檢查失敗 3 項（只剩 log）；補完這一筆後：
```
頁數：sources 6、parts 1、processes 2、concepts 10、cases 0
健檢通過
```

## 2026-11-25 #7 健檢（lint_report.py）

- check.py 通過。
- 單向連結 7 條 → 補了 6 條回連（surface-finish → machinability 那條原本就有了一半，一併補上）。
- 「可能相關、卻互不相連」35 條：大部分是誤報。這個主題的來源都是「一份清單談十幾條規則」，所以幾乎每兩個概念頁都共用 2–3 份來源。**這個規則在機械 Wiki 不太適用**，先記下來，之後考慮改成「共用的來源排除總表型來源」或提高門檻（反思用）。
- 待辦裡可拆的 3 項：都已寫明暫不拆的理由。
