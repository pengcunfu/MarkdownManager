from PySide6 import QtWidgets
from PySide6.QtGui import QIcon


class OptionDialog(QtWidgets.QDialog):
    """
    选项窗口
    """

    def __init__(self, parent=None):
        super(OptionDialog, self).__init__(parent)
        self.resize(600, 400)
        self.setWindowTitle("选项")
        self.setWindowIcon(QIcon("./resources/icon.png"))
