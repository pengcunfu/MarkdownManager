import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar
from PySide6.QtGui import QIcon
from PySide6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("PySide6 工具条示例")

        # 创建工具条
        toolbar = QToolBar("主工具条")
        self.addToolBar(toolbar)

        # 创建打开动作
        open_action = QAction(QIcon("open.png"), "打开", self)
        open_action.triggered.connect(self.on_open)
        toolbar.addAction(open_action)

        # 创建保存动作
        save_action = QAction(QIcon("save.png"), "保存", self)
        save_action.triggered.connect(self.on_save)
        toolbar.addAction(save_action)

        # 添加分隔符
        toolbar.addSeparator()

        # 创建退出动作
        exit_action = QAction(QIcon("exit.png"), "退出", self)
        exit_action.triggered.connect(self.close)
        toolbar.addAction(exit_action)

    def on_open(self):
        print("打开文件")

    def on_save(self):
        print("保存文件")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
