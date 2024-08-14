#! /usr/bin/env python3

import itertools

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QVBoxLayout
from ScrollableContainers import ScrollableAreaQt6


class ExamplesScrollableAreaQt6:
    def __init__(self):
        self.grid_of_widgets(QMainWindow())
        self.single_widget(QMainWindow())

    def grid_of_widgets(self, window):
        self.win1 = window
        window.setWindowTitle("`ScrollableAreaQt6` demo")

        # Create a scrollable area.
        scrollable_area = ScrollableAreaQt6()

        # Add widgets to the ``area`` attribute of the scrollable area, not to
        # the scrollable area itself.
        dim = 10
        grid_layout = QGridLayout(scrollable_area.area)
        for i, j in itertools.product(range(dim), repeat=2):
            label = QLabel(text=f"Label\n({i}, {j})")
            grid_layout.addWidget(label, i, j)

        window.setCentralWidget(scrollable_area)
        window.show()

    def single_widget(self, window):
        self.win2 = window
        window.setWindowTitle("`ScrollableAreaQt6` demo")
        window.resize(QSize(600, 200))

        scrollable_area = ScrollableAreaQt6()

        vbox = QVBoxLayout(scrollable_area.area)
        label = QLabel(text="big window, small label")
        vbox.addWidget(label)

        window.setCentralWidget(scrollable_area)
        window.show()


if __name__ == "__main__":
    app = QApplication([])
    examples = ExamplesScrollableAreaQt6()
    app.exec()
