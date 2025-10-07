import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QLabel, QPushButton, QPlainTextEdit

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

        # 创建一个文本框来显示 Markdown 内容
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setReadOnly(True)  # 设置为只读
        layout.addWidget(self.text_edit)

        # 设置接受拖放
        self.setAcceptDrops(True)

    def open_file(self):
        # 打开文件对话框，选择 Markdown 文件
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "打开 Markdown 文件", "", "Markdown Files (*.md);;All Files (*)", options=options)
        
        if file_path:
            self.load_md(file_path)

    def dragEnterEvent(self, event):
        # 允许拖拽进入
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # 处理拖拽的文件
        file_path = event.mimeData().urls()[0].toLocalFile()
        if file_path.endswith(".md"):
            self.load_md(file_path)

    def load_md(self, file_path):
        # 加载 Markdown 文件并显示其内容
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.text_edit.setPlainText(content)  # 设置文本框内容
        except Exception as e:
            self.text_edit.setPlainText(f"加载文件失败: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarkdownViewer()
    window.show()
    sys.exit(app.exec_())
