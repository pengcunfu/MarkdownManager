import sys
import os
import markdown2  # 用于将 Markdown 转换为 HTML
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QLabel, QPushButton, QTextBrowser

class MarkdownViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Markdown 文件预览")
        self.setGeometry(200, 200, 600, 400)

        self.initUI()

    def initUI(self):
        # 创建一个 QWidget 作为中央窗口部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 布局
        layout = QVBoxLayout(central_widget)

        # 标签说明
        self.label = QLabel("欢迎使用 Markdown 文件预览！", self)
        layout.addWidget(self.label)

        # 创建一个按钮来打开文件
        self.open_button = QPushButton("打开文件", self)
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        # 创建一个 QTextBrowser 来显示渲染后的 Markdown 内容
        self.text_browser = QTextBrowser(self)
        layout.addWidget(self.text_browser)

    def open_file(self):
        # 打开文件对话框，选择 Markdown 文件
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "打开 Markdown 文件", "", "Markdown Files (*.md);;All Files (*)", options=options)
        
        if file_path:
            self.load_md(file_path)

    def load_md(self, file_path):
        # 将 Markdown 文件内容转换为 HTML 并显示
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # 使用 markdown2 将 Markdown 转换为 HTML
                html_content = markdown2.markdown(content)
                self.text_browser.setHtml(html_content)  # 设置 QTextBrowser 显示 HTML 内容
        except Exception as e:
            self.text_browser.setPlainText(f"加载文件失败: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarkdownViewer()
    window.show()
    sys.exit(app.exec_())
