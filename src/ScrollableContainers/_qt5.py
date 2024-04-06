__all__ = ["ScrollableAreaQt5"]

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QVBoxLayout, QWidget


class ScrollableAreaQt5(QScrollArea):
    """
    Container with horizontal and vertical scrolling capabilities. Widgets must
    be added to its `area` attribute.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # This object only allows a container to be placed in it.
        container = QWidget()
        self.setWidget(container)
        vbox = QVBoxLayout(container)
        self.area = QWidget()
        vbox.addWidget(self.area, alignment=Qt.AlignHCenter)
        vbox.addStretch()
        self.setWidgetResizable(True)
