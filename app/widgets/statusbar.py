from PySide6.QtWidgets import QStatusBar, QLabel
from PySide6.QtCore import QTimer


class StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()
        # 添加永久状态信息
        self.memory_label = QLabel("内存: 0MB")
        self.addPermanentWidget(self.memory_label)

        self.cpu_label = QLabel("CPU: 0%")
        self.addPermanentWidget(self.cpu_label)

        # 显示临时消息
        self.showMessage("状态栏已初始化", 3000)  # 显示 3 秒

        # 模拟动态更新状态
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)  # 每 1 秒更新一次

    def update_status(self):
        """模拟更新状态信息"""
        import psutil  # 需要安装 psutil 库

        # 获取内存使用情况
        memory_info = psutil.virtual_memory()
        self.memory_label.setText(f"内存: {memory_info.used // 1024 // 1024}MB")

        # 获取 CPU 使用情况
        cpu_percent = psutil.cpu_percent(interval=0.1)
        self.cpu_label.setText(f"CPU: {cpu_percent}%")

        # 显示临时消息（模拟）
        if cpu_percent > 80:
            self.showMessage("CPU 使用率过高！", 1000)
