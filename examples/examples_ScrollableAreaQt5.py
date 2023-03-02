#! /usr/bin/python3 -B

import itertools
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets

from ScrollableContainers.Qt5 import ScrollableAreaQt5

###############################################################################

def grid_of_widgets():
    app = QtWidgets.QApplication(['`ScrollableAreaQt5` demo'])
    window = QtWidgets.QMainWindow()

    # Create a scrollable area.
    scrollable_area = ScrollableAreaQt5()

    # Add widgets to the `area` attribute of the scrollable area, not to the
    # scrollable area itself.
    dim = 10
    grid_layout = QtWidgets.QGridLayout(scrollable_area.area)
    for (i, j) in itertools.product(range(dim), repeat=2):
        grid_layout.addWidget(QtWidgets.QLabel(text=f'Label\n({i}, {j})'), i, j)

    window.setCentralWidget(scrollable_area)
    window.show()
    app.exec_()

###############################################################################

def single_widget():
    app = QtWidgets.QApplication(['`ScrollableAreaQt5` demo'])
    window = QtWidgets.QMainWindow(size=QtCore.QSize(600, 200))

    scrollable_area = ScrollableAreaQt5()

    vbox = QtWidgets.QVBoxLayout(scrollable_area.area)
    vbox.addWidget(QtWidgets.QLabel(text='big window, small label'))

    window.setCentralWidget(scrollable_area)
    window.show()
    app.exec_()

###############################################################################

if __name__ == '__main__':
    grid_of_widgets()
    single_widget()
