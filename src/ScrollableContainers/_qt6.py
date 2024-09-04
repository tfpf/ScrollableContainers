__all__ = ["ScrollableAreaQt6"]

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea, QVBoxLayout, QWidget


class ScrollableAreaQt6(QScrollArea):
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
        vbox.addWidget(self._area, alignment=Qt.AlignmentFlag.AlignHCenter)
        vbox.addStretch()
        self.setWidgetResizable(True)

    @property
    def area(self):
        return self._area
