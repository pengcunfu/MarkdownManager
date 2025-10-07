import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("PySide6 状态条示例")

        # 创建状态条
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # 设置初始状态消息
        self.status_bar.showMessage("就绪", 3000)  # 显示 3 秒

        # 创建一个按钮用于更新状态条
        self.button = QPushButton("更新状态")
        self.button.clicked.connect(self.update_status)

        # 创建一个标签用于显示状态
        self.label = QLabel("点击按钮更新状态条")

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_status(self):
        # 更新状态条消息
        self.status_bar.showMessage("状态已更新！", 2000)  # 显示 2 秒
        self.label.setText("状态条已更新！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
