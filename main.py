# -*- coding: utf-8 -*-
"""
CATIA CAA 源码框架快速生成器
主入口文件
"""
import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.styles import get_stylesheet


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(get_stylesheet())
    
    window = MainWindow()
    window.show()
    
    # 居中显示
    screen = app.primaryScreen().geometry()
    window.move(
        (screen.width() - window.width()) // 2,
        (screen.height() - window.height()) // 2
    )
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
