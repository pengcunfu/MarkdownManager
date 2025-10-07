import os.path

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QPushButton, QTextEdit, QVBoxLayout, \
    QWidget, QLabel, QHBoxLayout

from app.utils.post import handle_md_file, handle_md_dir


class UploadWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markdown Manager")
        self.resize(800, 600)

        # Layout and widgets
        self.layout = QVBoxLayout()

        self.hbox = QHBoxLayout()

        self.file_button = QPushButton("选择 Markdown 文件")
        self.file_button.clicked.connect(self.select_file)
        self.hbox.addWidget(self.file_button)

        self.dir_button = QPushButton("选择 Markdown 文件夹")
        self.dir_button.clicked.connect(self.select_directory)
        self.hbox.addWidget(self.dir_button)

        # 添加一个弹簧
        self.hbox.addStretch()

        self.layout.addLayout(self.hbox)

        # File and directory selection
        self.file_path_label = QLabel("选择文件或文件夹:")
        self.layout.addWidget(self.file_path_label)

        self.file_path_edit = QTextEdit()
        self.file_path_edit.setMaximumHeight(32)
        self.layout.addWidget(self.file_path_edit)

        self.file_path_label2 = QLabel("选择别名文件或文件夹:")
        self.layout.addWidget(self.file_path_label2)

        self.file_path_edit2 = QTextEdit()
        self.file_path_edit2.setMaximumHeight(32)
        self.layout.addWidget(self.file_path_edit2)

        # Start button
        self.start_button = QPushButton("开始")
        self.start_button.clicked.connect(self.start_processing)
        self.layout.addWidget(self.start_button)

        # Log display
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.layout.addWidget(self.log_text)

        # Set central widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def log(self, message: str):
        self.log_text.append(message)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择 Markdown 文件", "", "Markdown Files (*.md)")
        if file_path:
            self.file_path_edit.setText(f"{file_path}")

    def select_directory(self):
        dir_path = QFileDialog.getExistingDirectory(self, "选择 Markdown 文件夹")
        if dir_path:
            self.file_path_edit.setText(f"{dir_path}")

    def start_processing(self):
        in_path = self.file_path_edit.toPlainText()
        out_put = self.file_path_edit2.toPlainText()

        if not in_path:
            QMessageBox.warning(self, "警告", "请先选择文件或文件夹！")
            return

        if not out_put:
            QMessageBox.warning(self, "警告", "请先选择别名文件或文件夹！")
            return

        # 判断path_text是文件还是文件夹
        if os.path.isfile(in_path):
            self.log(f"开始处理文件: {in_path}")
            try:
                handle_md_file(in_path, log_callback=self.log)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"处理文件时出错: {e}")
        elif os.path.isdir(in_path):
            self.log(f"开始处理文件夹: {in_path} -> 输出到: {out_put}")
            try:
                handle_md_dir(in_path, out_put, log_callback=self.log)
            except Exception as e:
                QMessageBox.critical(self, "错误", f"处理文件夹时出错: {e}")
        else:
            QMessageBox.warning(self, "警告", "请先选择文件或文件夹！")


def main():
    app = QApplication([])
    window = UploadWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
