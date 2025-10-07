from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication


class FeishuUploadDialog(QtWidgets.QDialog):
    """
    飞书对话框
    """
    pass


def main():
    app = QApplication([])
    window = FeishuUploadDialog()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
