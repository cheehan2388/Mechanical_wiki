# 開心的機械 Wiki

用白話整理機械知識：零件、加工（CNC、車床、板金⋯⋯）、設計規則。核心問題：

> **它在解決什麼問題？為什麼選它，不選別的？**

- 第一個主題：**CNC 省錢篇**（`wiki/cnc-cost-guide.md`），附 20 頁教學簡報（`slides/cnc-cost/`）。
- 規則：`AGENTS.md`（給 AI 看的，人也可以看）。

## 常用指令

```bash
pip install markdown latex2mathml
python3 tools/find.py 關鍵字        # 收錄前先找相關頁
python3 tools/check.py              # 檢查 Wiki
python3 tools/check_slides.py slides/cnc-cost/deck.md   # 檢查簡報
python3 tools/lint_report.py        # 健檢報告（只回報）
python3 tools/build_site.py         # 先檢查，通過才產生整個網站到 docs/
```

## 發布到 GitHub Pages

1. 在 GitHub 開一個 repo（例如 `Mechanical_wiki`），把這個資料夾推上去。
2. Settings → Pages → 選 main 分支的 `/docs`。
3. 網址如果不是 `https://cheehan2388.github.io/Mechanical_wiki/`，改 `tools/build_site.py` 開頭的 `SITE_URL`。
