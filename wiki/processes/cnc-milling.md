---
title: CNC 銑削
type: process
aliases: [銑削, 銑床, CNC milling, milling, 加工中心, MC, CNC]
sources: [hubs-cost-2026, protolabs-cost-2026, xometry-cost-2020, hubs-design-2026, hubs-cnc-basics-2026]
updated: 2026-11-25
---

# CNC 銑削

## 一句話

刀子轉、工件不動，用圓柱形的刀把一塊方料一層層挖成想要的形狀。

## 解決什麼問題

要做一個有平面、凹槽、孔的金屬或塑膠零件，數量又不多。手工做不準，開模又太貴，銑削可以直接從一塊料切出來。

**CNC** 是「電腦數值控制」：刀子怎麼走，由電腦照程式控制，不是人手搖。

## 怎麼做

{{figure:milling-vs-turning}}

1. 把一塊比成品大一點的方料（叫**毛胚**）夾在機台上。
2. 刀子高速旋轉，沿著電腦算好的路徑移動，一層層切掉不要的材料。
3. 一面做完，如果另一面也有形狀，就要把工件拆下來翻面再夾一次（[[machine-setup]]）。

電腦怎麼知道刀要怎麼走？設計好的 3D 模型（CAD）會轉成機器看得懂的指令 G-code（[[hubs-cnc-basics-2026]]）。

## 為什麼選它

- 銑削的成本從哪裡來：加工時間、開機成本、難做的形狀、材料（[[hubs-cost-2026]]）。加工時間常常是最大的一項（[[xometry-cost-2020]]）。
- **銑削 vs. 車削**：圓的、旋轉對稱的零件用車削比較順；其他形狀用銑削（[[hubs-cnc-basics-2026]]，見 [[cnc-turning]]）。
- **銑削 vs. 3D 列印**：銑削精度高、零件保有原料的強度；但開機成本比較高，一般交期約 10 天，3D 列印約 2–5 天（[[hubs-cnc-basics-2026]]）。
- **適合的量**：從 1 件打樣到約 1,000 件都很有效率（[[hubs-cnc-basics-2026]]）；Xometry 說 10,000 件以內最划算（[[xometry-cost-2020]]）。
- **銑削 vs. 板金**：牆很薄的零件，改用板金通常比較划算（[[xometry-cost-2020]]）。
- **3 軸 vs. 5 軸**：3 軸的刀只能從上面垂直下來；5 軸多了兩個旋轉方向，能少翻面、做複雜形狀，但比較貴（[[hubs-cnc-basics-2026]]、[[hubs-design-2026]]）。

## 規格怎麼讀

圖面上跟銑削成本最有關的幾個數字，每一項都有自己的頁：

- 內角的圓角半徑：[[internal-corner-radius]]
- 凹槽深度：[[cavity-depth]]
- 牆厚：[[thin-wall]]
- 材料：[[machinability]]
- 孔徑與螺紋長度：[[hole-thread]]
- 公差：[[tolerance]]
- 要翻面幾次：[[machine-setup]]
- 表面處理：[[surface-finish]]
- 訂幾件：[[batch-size]]

## 出問題怎麼認

- 牆太薄：切的時候變形或斷掉（[[hubs-cost-2026]] 第 3 招）。
- 細高的特徵：切的時候會振動，尺寸做不準（第 8 招）。
- 深槽、深牆：原料的殘留應力釋放，零件切完會走樣（[[protolabs-cost-2026]]）。
- 圖面畫尖的內角：收到的零件角落是圓的，這是刀的形狀，不是做錯（[[internal-corner-radius]]）。

## 證據

- [[hubs-cost-2026]]：14 招的成本規則，幾乎都是針對銑削。
- [[protolabs-cost-2026]]：加工廠自己寫的六招，重點在清角、薄牆、材料替代。
- [[xometry-cost-2020]]：另一家公司的十招，和前兩份大致一致，多談了孔與攻牙。
- [[hubs-design-2026]]：每條規則的建議值與勉強可做的值。
- [[hubs-cnc-basics-2026]]：銑削、車削、3 軸、5 軸的入門說明。

## 相關頁面

- [[hubs-cost-2026]]：銑削為什麼貴、怎麼省
- [[cnc-turning]]：另一種 CNC，差在誰在轉
- [[end-mill]]：銑削用的刀
- [[cnc-cost-guide]]：CNC 省錢篇的閱讀順序
