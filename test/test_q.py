from PySide6.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QTimer


class MyTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()

        # 创建 Web 组件
        self.web_view = QWebEngineView()
        self.web_view.load("https://www.example.com")

        # 创建 Web 选项卡
        web_tab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.web_view)
        web_tab.setLayout(layout)

        # 添加 Tab
        self.addTab(QWidget(), "普通 Tab")
        self.addTab(web_tab, "Web 页")

        # 监听 tab 切换
        self.currentChanged.connect(self.handle_tab_change)

    def handle_tab_change(self, index):
        if self.widget(index) is self.web_view.parentWidget():
            self.web_view.hide()
            QTimer.singleShot(50, self.web_view.show)  # 延迟 50ms 后再显示，减少闪烁


app = QApplication([])
window = MyTabWidget()
window.show()
app.exec()
