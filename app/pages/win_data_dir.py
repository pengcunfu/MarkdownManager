from PySide6.QtWidgets import QDialog, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QApplication

from app.utils.gen_path_file import list_dir_md_and_out_put


class DataDirApp(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Path Handle")
        self.textEdit_Path = QTextEdit()
        self.textEdit_Path.setMaximumHeight(32)
        self.textEdit_Prefix = QTextEdit()
        self.textEdit_Prefix.setMaximumHeight(32)
        self.button = QPushButton("生成", self)
        self.button.clicked.connect(self.on_button_click)
        self.textEdit_Result = QTextEdit()
        self.textEdit_Result.setReadOnly(True)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.textEdit_Path)
        vbox1.addWidget(self.textEdit_Prefix)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addWidget(self.button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.textEdit_Result)
        self.setLayout(vbox)

    def on_button_click(self):
        text1 = self.textEdit_Path.toPlainText()
        text2 = self.textEdit_Prefix.toPlainText()
        all_str = list_dir_md_and_out_put(text1, text2)
        self.textEdit_Result.setText(all_str)


def main():
    app = QApplication([])
    window = DataDirApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
