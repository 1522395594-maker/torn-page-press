# 撕页印刷 · Torn Page Press

把照片「撕开」，露出底下印满经文的旧纸。

**在线使用：** https://1522395594-maker.github.io/torn-page-press/

## 玩法

1. 选一张照片（或者先用示例照片试试）
2. 选撕法：
   - **泪痕**：画一笔，撕出细长的口子，字竖着排在里面
   - **破洞**：点一下或抹一片，撕出不规则的洞
   - **撕角**：拖一条线，撕掉靠边的一整块
3. 换经文、纸和墨：默认是尼泊尔寺庙里常见的梵文经文（天城体），也可以写自己的字
4. 导出，存进相册

## 离线使用

`index.html` 是一个自包含的单文件，字体和示例照片都已内嵌，下载后用浏览器打开就能用，不需要联网。

## 开发

- 源码：`src/app.html`
- 字体：`fonts/`（Noto Serif Devanagari、Special Elite，SIL Open Font License）
- 打包：`python3 build.py`，生成根目录的 `index.html`

中文字体使用系统自带的宋体（苹果设备上是 Songti SC）。
