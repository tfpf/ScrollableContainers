#! /usr/bin/python3 -B

import itertools
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QVBoxLayout

from ScrollableContainers.Qt5 import ScrollableAreaQt5

###############################################################################

def grid_of_widgets():
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle('`ScrollableAreaQt5` demo')

    # Create a scrollable area.
    scrollable_area = ScrollableAreaQt5()

    # Add widgets to the `area` attribute of the scrollable area, not to the
    # scrollable area itself.
    dim = 10
    grid_layout = QGridLayout(scrollable_area.area)
    for (i, j) in itertools.product(range(dim), repeat=2):
        grid_layout.addWidget(QLabel(text=f'Label\n({i}, {j})'), i, j)

    window.setCentralWidget(scrollable_area)
    window.show()
    app.exec()

###############################################################################

def single_widget():
    app = QApplication([])
    window = QMainWindow(size=QSize(600, 200))
    window.setWindowTitle('`ScrollableAreaQt5` demo')

    scrollable_area = ScrollableAreaQt5()

    vbox = QVBoxLayout(scrollable_area.area)
    vbox.addWidget(QLabel(text='big window, small label'))

    window.setCentralWidget(scrollable_area)
    window.show()
    app.exec()

###############################################################################

if __name__ == '__main__':
    grid_of_widgets()
    single_widget()
