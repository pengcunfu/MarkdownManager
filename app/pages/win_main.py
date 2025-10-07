from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from pubsub import pub
from app.widgets.menubar import MenuBar
from app.widgets.toolbar import ToolBar
from app.widgets.markdown import MarkdownPreviewTree, FileBrowseTree
from app.widgets.statusbar import StatusBar
from app.config import ICON_PATH, APP_NAME
from app.utils.config_file import config_load


class MainWindow(QMainWindow):
    WINDOW_CLOSE = "WINDOW_CLOSE"

    def __init__(self):
        super().__init__()
        self.resize(1200, 700)
        self.setWindowTitle(APP_NAME)
        self.setMenuBar(MenuBar())
        self.addToolBar(ToolBar())
        self.setCentralWidget(MarkdownPreviewTree())
        self.setStatusBar(StatusBar())
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setWindowIconText("Markdown管理工具")

        pub.subscribe(self.on_close, self.WINDOW_CLOSE)

        data = config_load()
        file_list = data.get("file_list")

        if file_list:
            for file in file_list:
                pub.sendMessage(FileBrowseTree.TOPIC_ADD_FILE, file_path=file)

    def on_close(self):
        self.close()
