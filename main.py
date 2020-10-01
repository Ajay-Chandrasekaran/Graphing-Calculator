#!/usr/bin/env python3

import sys

from random import randint
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer


class AnotherWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self):
        self.wind = AnotherWindow()
        self.wind.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)
    sys.exit(app.exec_())
