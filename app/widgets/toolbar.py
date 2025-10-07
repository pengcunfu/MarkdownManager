from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction, QIcon
from pubsub import pub


class ToolBar(QToolBar):
    TOOLBAR_OPEN_FILE = "TOOLBAR_OPEN_FILE"
    TOOLBAR_SAVE_FILE = "TOOLBAR_SAVE_FILE"
    TOOLBAR_WINDOW_CLOSE = "TOOLBAR_WINDOW_CLOSE"

    def __init__(self):
        super().__init__()

        open_action = QAction(QIcon("./resources/icons/open.png"), "打开", self)
        open_action.triggered.connect(self.on_open)
        self.addAction(open_action)

        save_action = QAction(QIcon("./resources/icons/save.png"), "保存", self)
        save_action.triggered.connect(self.on_save)
        self.addAction(save_action)

        # 添加分隔符
        self.addSeparator()

        exit_action = QAction(QIcon("./resources/icons/exit.png"), "退出", self)
        exit_action.triggered.connect(self.on_close)
        self.addAction(exit_action)

    def on_open(self):
        pub.sendMessage(self.TOOLBAR_OPEN_FILE)

    def on_save(self):
        pub.sendMessage(self.TOOLBAR_SAVE_FILE)

    def on_close(self):
        pub.sendMessage(self.TOOLBAR_WINDOW_CLOSE)
