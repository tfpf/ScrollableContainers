__all__ = ['ScrollableAreaQt5']

import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets


class ScrollableAreaQt5(QtWidgets.QScrollArea):
    """
Container with horizontal and vertical scrolling capabilities. Widgets must be
added to its `area` attribute.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # This object only allows a container to be placed in it.
        container = QtWidgets.QWidget()
        self.setWidget(container)
        vbox = QtWidgets.QVBoxLayout(container)
        self.area = QtWidgets.QWidget()
        vbox.addWidget(self.area, alignment=QtCore.Qt.AlignHCenter)
        vbox.addStretch()
        self.setWidgetResizable(True)
