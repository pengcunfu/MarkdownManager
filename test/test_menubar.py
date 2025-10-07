import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PySide6.QtGui import QAction

import os
import test
# os.environ["QT_PLUGIN_PATH"] = r"D:\App\Software\miniconda3\envs\PySide6\Lib\site-packages\PySide6\plugins"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(800, 600)

        # 设置窗口标题
        self.setWindowTitle("PySide6 菜单示例")

        # 创建菜单栏
        menubar = self.menuBar()

        # 创建文件菜单
        file_menu = menubar.addMenu("文件")

        # 创建打开动作
        open_action = QAction("打开", self)
        open_action.triggered.connect(self.on_open)
        file_menu.addAction(open_action)

        # 创建保存动作
        save_action = QAction("保存", self)
        save_action.triggered.connect(self.on_save)
        file_menu.addAction(save_action)

        # 添加分隔符
        file_menu.addSeparator()

        # 创建退出动作
        exit_action = QAction("退出", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # 创建编辑菜单
        edit_menu = menubar.addMenu("编辑")

        # 创建剪切动作
        cut_action = QAction("剪切", self)
        cut_action.triggered.connect(self.on_cut)
        edit_menu.addAction(cut_action)

        # 创建复制动作
        copy_action = QAction("复制", self)
        copy_action.triggered.connect(self.on_copy)
        edit_menu.addAction(copy_action)

        # 创建粘贴动作
        paste_action = QAction("粘贴", self)
        paste_action.triggered.connect(self.on_paste)
        edit_menu.addAction(paste_action)

    def on_open(self):
        print("打开文件")

    def on_save(self):
        print("保存文件")

    def on_cut(self):
        print("剪切")

    def on_copy(self):
        print("复制")

    def on_paste(self):
        print("粘贴")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
