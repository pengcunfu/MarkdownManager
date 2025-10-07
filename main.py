from PySide6.QtWidgets import QApplication
import sys
from app.pages.win_main import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
