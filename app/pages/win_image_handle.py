from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox, QApplication
from app.widgets.markdown import MarkdownPreviewWrapper


class ImageHandleDialog(QDialog):
    def __init__(self, md_file_path: str):
        """
        传入一个md文件的路径
        """
        super().__init__()
        self.md_file_path = md_file_path
        self.vbox = QVBoxLayout()

        self.setWindowTitle('Markdown图像处理')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        # self.setFixedSize(self.size())
        self.setWindowFlags(Qt.WindowType.Window)  # 允许最大化/最小化

        self.hbox1 = QHBoxLayout()
        self.button_handle = QPushButton()
        self.button_handle.setText("处理")
        self.button_handle.setMaximumWidth(120)
        self.button_handle.clicked.connect(self.on_handle)
        self.hbox1.addWidget(self.button_handle)

        self.button_apply = QPushButton()
        self.button_apply.setText("应用")
        self.button_apply.setMaximumWidth(120)
        self.button_apply.clicked.connect(self.on_apply)
        self.hbox1.addWidget(self.button_apply)

        self.hbox1.setDirection(QVBoxLayout.Direction.LeftToRight)
        self.hbox1.addStretch()

        self.hbox2 = QHBoxLayout()
        self.left = MarkdownPreviewWrapper()
        self.right = MarkdownPreviewWrapper()
        self.hbox2.addWidget(self.left)
        self.hbox2.addWidget(self.right)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)

        self.setLayout(self.vbox)
        self.__load_data()

        self.is_handle = False
        self.content = None

    def __load_data(self):
        self.left.set_markdown_file(self.md_file_path)

    def on_apply(self):
        if not self.is_handle or not self.content:
            QMessageBox.critical(self, "错误", "请先进行处理")
            return

        with open(file=self.md_file_path, mode="w", encoding="utf-8") as f:
            f.write(self.content)

        self.close()

    def on_handle(self):
        from app.utils.oss import MarkdownUpload, LocalFileUploader
        self.content = MarkdownUpload(self.md_file_path, LocalFileUploader()).handle()
        self.right.set_markdown_content(self.content)
        self.is_handle = True


def main():
    app = QApplication([])
    window = ImageHandleDialog()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
