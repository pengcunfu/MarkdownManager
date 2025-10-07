from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QDialog, QLabel, QApplication


class AboutDialog(QDialog):
    """
    关于对话框
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('关于')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setFixedSize(self.size())

        self.vbox = QtWidgets.QVBoxLayout()
        self.text = QLabel()
        self.text.setText("本程序由 Huaqiwill 开发")

        self.vbox.addWidget(self.text)

        self.setLayout(self.vbox)


def main():
    app = QApplication([])
    window = AboutDialog()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
