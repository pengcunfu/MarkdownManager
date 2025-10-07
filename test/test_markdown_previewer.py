from PySide6.QtWidgets import (QApplication, QMainWindow)
from app.widgets.markdown import MarkdownPreviewTree
from main import fix_bug

fix_bug()


class MarkdownPreviewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和大小
        self.setWindowTitle("Markdown 预览工具")
        self.setGeometry(100, 100, 800, 600)

        # 创建主窗口布局
        self.setCentralWidget(MarkdownPreviewTree())


if __name__ == "__main__":
    app = QApplication([])
    window = MarkdownPreviewApp()
    window.show()
    app.exec()
