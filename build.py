"""把 src/app.html 和 fonts/ 里的字体打包成一个自包含的 index.html（可离线、可直接发送）。"""
import base64, os
ROOT = os.path.dirname(os.path.abspath(__file__))
DEVA = "U+0900-097F, U+1CD0-1CF4, U+1CF7-1CF9, U+200C-200D, U+20A8, U+20B9, U+20F0, U+25CC, U+A830-A839, U+A8E0-A8FF"
LATIN = "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD"
FACES = [("Noto Serif Devanagari", "NotoSerifDevanagari-deva.woff2", DEVA),
         ("Noto Serif Devanagari", "NotoSerifDevanagari-latin.woff2", LATIN),
         ("Special Elite", "SpecialElite-latin.woff2", LATIN)]
css = ""
for fam, f, rng in FACES:
    b64 = base64.b64encode(open(os.path.join(ROOT, "fonts", f), "rb").read()).decode()
    css += f'@font-face{{font-family:"{fam}";font-style:normal;font-weight:400;font-display:block;src:url(data:font/woff2;base64,{b64}) format("woff2");unicode-range:{rng};}}\n'
html = open(os.path.join(ROOT, "src", "app.html"), encoding="utf-8").read().replace("/*@@FONTS@@*/", css)
sample = "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(ROOT, "assets", "sample.jpg"), "rb").read()).decode()
html = html.replace("@@SAMPLE@@", sample)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
print("index.html", round(len(html.encode()) / 1024), "KB")
