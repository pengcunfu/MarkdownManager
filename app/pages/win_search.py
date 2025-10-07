from PySide6.QtWidgets import QDialog


class SearchDialog(QDialog):
    """
    搜索窗口
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("搜索")
