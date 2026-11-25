"""數字比對：check.py 和 check_slides.py 共用。

舊做法只問「這個數字有沒有出現在來源裡」，結果 0.9、12、60 這種常見數字，
在來源的別處剛好出現就會通過（2026-11-25 故意塞錯數字時發現，見 log.md）。
現在要同時符合三件事：
1. 數值相同（整數允許四捨五入，例如 −36 對得上 −36.2）。
2. 單位相同（12 倍對不上 12 mm；60 對不上 60%）。主張沒有單位時，只能對上來源裡同樣沒單位、或單位是「美元」的數字。
   來源表格裡沒寫單位的數字（單位常寫在表頭或表名），可以對上任何單位。
3. 來源那一行和主張那一行，至少共用一個「內容詞」（兩個中文字的詞，去掉常見虛詞），
   或共用一個 3 個字母以上的英文字／材料編號。
限制：還是只比對文字，不保證語意正確（例如來源裡另一句剛好也有「金屬 0.90 mm」）。
"""
import re

NUM_RE = re.compile(r"(?<![A-Za-z\d.])[−-]?\d[\d,]*(?:\.\d+)?")
UNIT_RE = re.compile(r"\s*(%|％|倍|mm|µm|μm|cm|in|英吋|吋|°|度|美元|\$|N·m|N|MPa|件|個|天|HRB|牙|號)")
STOP = set("""以上 以下 可以 這個 一個 就是 如果 因為 所以 還是 或是 而且 但是 不是 沒有 就能 就要 通常 比較 這種 那種
一般 大約 約是 之後 之前 時候 什麼 怎麼 多少 一樣 一定 不用 不要 需要 要用 用來 來說 說的 的話 也是 都是 只是 還有
原文 來源 這篇 這份 兩份 三份 見表 例如 例子 示意 寫的 寫成 至少 最多 最好 建議 超過 不超 的刀""".split())


def unit_after(text, end):
    m = UNIT_RE.match(text[end:])
    return m.group(1).replace("％", "%").replace("μm", "µm").replace("吋", "英吋").replace("英英吋", "英吋") if m else ""


def value(tok):
    return abs(float(tok.replace(",", "").replace("−", "-")))


def numbers_with_units(text):
    out = []
    for m in NUM_RE.finditer(text):
        try:
            out.append((value(m.group(0)), unit_after(text, m.end())))
        except ValueError:
            pass
    return out


def anchors(line):
    words = set()
    for run in re.findall(r"[一-鿿]+", line):
        for i in range(len(run) - 1):
            w = run[i:i + 2]
            if w not in STOP:
                words.add(w)
    words |= {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\d\-]{2,}", line)}
    words |= set(re.findall(r"(?<![\d.])\d{3,4}(?![\d.])", line))   # 材料編號：6061、304
    return words


def index_lines(text):
    """把來源全文切成行，每行記下 (數值, 單位) 和內容詞。表格的每一列也算一行，並帶上表頭的字。"""
    rows, header = [], ""
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"^\|[\s\-|:]+\|$", line):
            if not header:
                header = line
            ctx = line + " " + header
        else:
            if not line.startswith("|"):
                header = ""
            ctx = line
        rows.append((numbers_with_units(line), anchors(ctx), line.startswith("|")))
    return rows


def same_value(a, b):
    return abs(a - b) < 1e-9 or (a == int(a) and abs(a - b) < 0.5)


def found(n, unit, claim_line, source_rows):
    claim_words = anchors(claim_line)
    for nums, words, is_table in source_rows:
        for v, u in nums:
            if not same_value(n, v):
                continue
            if unit and u != unit and not (is_table and u == ""):
                continue
            if not unit and u not in ("", "美元"):
                continue
            if claim_words & words:
                return True
    return False
