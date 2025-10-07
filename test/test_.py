from PySide6.QtWidgets import QTextBrowser, QMainWindow, QApplication
import markdown
import sys
import os
import test

test.cwd()

interpreter_path = os.path.realpath(sys.executable)
QT_PLUGIN_PATH = os.path.normpath(
    os.path.join(os.path.dirname(interpreter_path), "./Lib/site-packages/PySide6/plugins"))
os.environ["QT_PLUGIN_PATH"] = QT_PLUGIN_PATH

# CSS 样式
css = """
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-family: Arial, sans-serif;
}
th, td {
    padding: 12px;
    border: 1px solid #ddd;
    text-align: center;
}
th {
    background-color: #f2f2f2;
    font-weight: bold;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}
tr:hover {
    background-color: #f1f1f1;
}
"""

# Markdown 表格内容
markdown_content = """
| 列1       | 列2       | 列3       |
| --------- | --------- | --------- |
| 单元格1   | 单元格2   | 单元格3   |
| 单元格4   | 单元格5   | 单元格6   |
| 单元格7   | 单元格8   | 单元格9   |
"""

app = QApplication(sys.argv)
win = QMainWindow()

# 渲染 Markdown 并应用 CSS
html = markdown.markdown(markdown_content, extensions=["tables"])
styled_html = f"<style>{css}</style>{html}"

# 在 QTextBrowser 中显示
preview_browser = QTextBrowser()
preview_browser.setHtml(styled_html)
win.setCentralWidget(preview_browser)

win.show()
sys.exit(app.exec())
