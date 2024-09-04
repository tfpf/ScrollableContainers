__all__ = ["ScrollableAreaQt5"]

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QWidget


class ScrollableAreaQt5(QScrollArea):
    """
    Container with horizontal and vertical scrolling capabilities. Widgets must
    be added to its ``area`` attribute. Constructor arguments are passed to the
    parent constructor.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # This object only allows a container to be placed in it.
        container = QWidget()
        self.setWidget(container)
        vbox = QVBoxLayout(container)
        self._area = QWidget()
        vbox.addWidget(self._area, alignment=Qt.AlignHCenter)
        vbox.addStretch()
        self.setWidgetResizable(True)

    @property
    def area(self):
        return self._area
